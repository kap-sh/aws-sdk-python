"""Generated from Smithy shape ``com.amazonaws.glacier#SetVaultNotificationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.vault_notification_config


class SetVaultNotificationsInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    vault_notification_config: NotRequired[
        "aws_sdk_glacier.types.vault_notification_config.VaultNotificationConfig"
    ]
    """<p>Provides options for specifying notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetVaultNotificationsInput) -> dict:
    out: dict = {}
    if "vault_notification_config" in value:
        import aws_sdk_glacier.types.vault_notification_config

        out["vaultNotificationConfig"] = (
            aws_sdk_glacier.types.vault_notification_config.serialize_json(
                value["vault_notification_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetVaultNotificationsInput:
    out: SetVaultNotificationsInput = {}  # type: ignore[typeddict-item]
    if "vaultNotificationConfig" in data:
        import aws_sdk_glacier.types.vault_notification_config

        out["vault_notification_config"] = (
            aws_sdk_glacier.types.vault_notification_config.deserialize_json(
                data["vaultNotificationConfig"]
            )
        )
    return out
