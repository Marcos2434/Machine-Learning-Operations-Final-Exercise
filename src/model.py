from pytorch_lightning import LightningModule
from torch import nn, optim

class MyAwesomeModel(LightningModule):
    def __init__(self):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(1, 64, 3), # [N, 64, 26]
            nn.LeakyReLU(),
            nn.Conv2d(64, 32, 3), # [N, 32, 24]
            nn.LeakyReLU(),
            nn.Conv2d(32, 16, 3), # [N, 16, 22]
            nn.LeakyReLU(),
            nn.Conv2d(16, 8, 3), # [N, 8, 20]
            nn.LeakyReLU()
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(8 * 20 * 20, 128),
            nn.Dropout(),
            nn.Linear(128, 10)
        )
        self.criterium = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.classifier(self.backbone(x))

    def training_step(self, batch, batch_idx):
        data, target = batch
        preds = self(data)
        loss = self.criterium(preds, target)
        return loss

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=1e-2)

# import torch
# from torch import nn


# class MyAwesomeModel(nn.Module):
#     """My awesome model."""

#     def __init__(self) -> None:
#         super().__init__()
#         self.conv1 = nn.Conv2d(1, 32, 3, 1)
#         self.conv2 = nn.Conv2d(32, 64, 3, 1)
#         self.conv3 = nn.Conv2d(64, 128, 3, 1)
#         self.dropout = nn.Dropout(0.5)
#         self.fc1 = nn.Linear(128, 10)

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         """Forward pass."""
#         x = torch.relu(self.conv1(x))
#         x = torch.max_pool2d(x, 2, 2)
#         x = torch.relu(self.conv2(x))
#         x = torch.max_pool2d(x, 2, 2)
#         x = torch.relu(self.conv3(x))
#         x = torch.max_pool2d(x, 2, 2)
#         x = torch.flatten(x, 1)
#         x = self.dropout(x)
#         return self.fc1(x)


# if __name__ == "__main__":
#     model = MyAwesomeModel()
#     print(f"Model architecture: {model}")
#     print(f"Number of parameters: {sum(p.numel() for p in model.parameters())}")

#     dummy_input = torch.randn(1, 1, 28, 28)
#     output = model(dummy_input)
#     print(f"Output shape: {output.shape}")
