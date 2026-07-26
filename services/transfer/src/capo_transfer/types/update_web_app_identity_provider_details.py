"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppIdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_transfer.types.update_web_app_identity_center_config


class _UpdateWebAppIdentityProviderDetails_IdentityCenterConfig(TypedDict, closed=True):
    IdentityCenterConfig: "capo_transfer.types.update_web_app_identity_center_config.UpdateWebAppIdentityCenterConfig"


UpdateWebAppIdentityProviderDetails: TypeAlias = (
    _UpdateWebAppIdentityProviderDetails_IdentityCenterConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppIdentityProviderDetails) -> dict:
    if "IdentityCenterConfig" in value:
        import capo_transfer.types.update_web_app_identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.update_web_app_identity_center_config.serialize_aws_json_1_1(
                value["IdentityCenterConfig"]
            )
        }
    else:
        raise SerializationError(
            "UpdateWebAppIdentityProviderDetails: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppIdentityProviderDetails:
    if "IdentityCenterConfig" in data:
        import capo_transfer.types.update_web_app_identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.update_web_app_identity_center_config.deserialize_aws_json_1_1(
                data["IdentityCenterConfig"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateWebAppIdentityProviderDetails: no recognized variant key"
        )
