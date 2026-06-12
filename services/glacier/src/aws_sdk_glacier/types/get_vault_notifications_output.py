"""Generated from Smithy shape ``com.amazonaws.glacier#GetVaultNotificationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.vault_notification_config


class GetVaultNotificationsOutput(TypedDict):
    vault_notification_config: NotRequired[
        "aws_sdk_glacier.types.vault_notification_config.VaultNotificationConfig"
    ]
    """<p>Returns the notification configuration set on the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVaultNotificationsOutput) -> dict:
    out: dict = {}
    if "vault_notification_config" in value:
        import aws_sdk_glacier.types.vault_notification_config

        out["vaultNotificationConfig"] = (
            aws_sdk_glacier.types.vault_notification_config.serialize_json(
                value["vault_notification_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVaultNotificationsOutput:
    out: GetVaultNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "vaultNotificationConfig" in data:
        import aws_sdk_glacier.types.vault_notification_config

        out["vault_notification_config"] = (
            aws_sdk_glacier.types.vault_notification_config.deserialize_json(
                data["vaultNotificationConfig"]
            )
        )
    return out
