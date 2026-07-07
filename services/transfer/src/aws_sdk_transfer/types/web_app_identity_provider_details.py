"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppIdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.identity_center_config


class _WebAppIdentityProviderDetails_IdentityCenterConfig(TypedDict, closed=True):
    IdentityCenterConfig: (
        "aws_sdk_transfer.types.identity_center_config.IdentityCenterConfig"
    )


WebAppIdentityProviderDetails: TypeAlias = (
    _WebAppIdentityProviderDetails_IdentityCenterConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppIdentityProviderDetails) -> dict:
    if "IdentityCenterConfig" in value:
        import aws_sdk_transfer.types.identity_center_config

        return {
            "IdentityCenterConfig": aws_sdk_transfer.types.identity_center_config.serialize_aws_json_1_1(
                value["IdentityCenterConfig"]
            )
        }
    else:
        raise SerializationError("WebAppIdentityProviderDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WebAppIdentityProviderDetails:
    if "IdentityCenterConfig" in data:
        import aws_sdk_transfer.types.identity_center_config

        return {
            "IdentityCenterConfig": aws_sdk_transfer.types.identity_center_config.deserialize_aws_json_1_1(
                data["IdentityCenterConfig"]
            )
        }
    else:
        raise DeserializationError(
            "WebAppIdentityProviderDetails: no recognized variant key"
        )
