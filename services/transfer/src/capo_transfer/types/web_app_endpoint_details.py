"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_transfer.types.web_app_vpc_config


class _WebAppEndpointDetails_Vpc(TypedDict, closed=True):
    Vpc: "capo_transfer.types.web_app_vpc_config.WebAppVpcConfig"


WebAppEndpointDetails: TypeAlias = _WebAppEndpointDetails_Vpc


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppEndpointDetails) -> dict:
    if "Vpc" in value:
        import capo_transfer.types.web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.web_app_vpc_config.serialize_aws_json_1_1(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError("WebAppEndpointDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WebAppEndpointDetails:
    if "Vpc" in data:
        import capo_transfer.types.web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.web_app_vpc_config.deserialize_aws_json_1_1(
                data["Vpc"]
            )
        }
    else:
        raise DeserializationError("WebAppEndpointDetails: no recognized variant key")
