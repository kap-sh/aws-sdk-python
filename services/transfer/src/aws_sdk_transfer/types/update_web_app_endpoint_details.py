"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.update_web_app_vpc_config


class _UpdateWebAppEndpointDetails_Vpc(TypedDict, closed=True):
    Vpc: "aws_sdk_transfer.types.update_web_app_vpc_config.UpdateWebAppVpcConfig"


UpdateWebAppEndpointDetails: TypeAlias = _UpdateWebAppEndpointDetails_Vpc


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppEndpointDetails) -> dict:
    if "Vpc" in value:
        import aws_sdk_transfer.types.update_web_app_vpc_config

        return {
            "Vpc": aws_sdk_transfer.types.update_web_app_vpc_config.serialize_aws_json_1_1(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError("UpdateWebAppEndpointDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppEndpointDetails:
    if "Vpc" in data:
        import aws_sdk_transfer.types.update_web_app_vpc_config

        return {
            "Vpc": aws_sdk_transfer.types.update_web_app_vpc_config.deserialize_aws_json_1_1(
                data["Vpc"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateWebAppEndpointDetails: no recognized variant key"
        )
