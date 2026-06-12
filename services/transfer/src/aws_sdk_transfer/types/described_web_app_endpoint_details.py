"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_web_app_vpc_config


class _DescribedWebAppEndpointDetails_Vpc(TypedDict):
    Vpc: "aws_sdk_transfer.types.described_web_app_vpc_config.DescribedWebAppVpcConfig"


DescribedWebAppEndpointDetails: TypeAlias = _DescribedWebAppEndpointDetails_Vpc


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppEndpointDetails) -> dict:
    if "Vpc" in value:
        import aws_sdk_transfer.types.described_web_app_vpc_config

        return {
            "Vpc": aws_sdk_transfer.types.described_web_app_vpc_config.serialize_aws_json_1_1(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError("DescribedWebAppEndpointDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppEndpointDetails:
    if "Vpc" in data:
        import aws_sdk_transfer.types.described_web_app_vpc_config

        return {
            "Vpc": aws_sdk_transfer.types.described_web_app_vpc_config.deserialize_aws_json_1_1(
                data["Vpc"]
            )
        }
    else:
        raise DeserializationError(
            "DescribedWebAppEndpointDetails: no recognized variant key"
        )
