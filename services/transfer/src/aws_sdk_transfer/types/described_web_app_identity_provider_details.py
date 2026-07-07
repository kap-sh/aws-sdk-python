"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppIdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_identity_center_config


class _DescribedWebAppIdentityProviderDetails_IdentityCenterConfig(
    TypedDict, closed=True
):
    IdentityCenterConfig: "aws_sdk_transfer.types.described_identity_center_config.DescribedIdentityCenterConfig"


DescribedWebAppIdentityProviderDetails: TypeAlias = (
    _DescribedWebAppIdentityProviderDetails_IdentityCenterConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppIdentityProviderDetails) -> dict:
    if "IdentityCenterConfig" in value:
        import aws_sdk_transfer.types.described_identity_center_config

        return {
            "IdentityCenterConfig": aws_sdk_transfer.types.described_identity_center_config.serialize_aws_json_1_1(
                value["IdentityCenterConfig"]
            )
        }
    else:
        raise SerializationError(
            "DescribedWebAppIdentityProviderDetails: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppIdentityProviderDetails:
    if "IdentityCenterConfig" in data:
        import aws_sdk_transfer.types.described_identity_center_config

        return {
            "IdentityCenterConfig": aws_sdk_transfer.types.described_identity_center_config.deserialize_aws_json_1_1(
                data["IdentityCenterConfig"]
            )
        }
    else:
        raise DeserializationError(
            "DescribedWebAppIdentityProviderDetails: no recognized variant key"
        )
