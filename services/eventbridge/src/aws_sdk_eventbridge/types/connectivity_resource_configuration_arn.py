"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectivityResourceConfigurationArn``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.resource_configuration_arn


class ConnectivityResourceConfigurationArn(TypedDict):
    resource_configuration_arn: (
        "aws_sdk_eventbridge.types.resource_configuration_arn.ResourceConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration for the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectivityResourceConfigurationArn) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectivityResourceConfigurationArn:
    out: ConnectivityResourceConfigurationArn = {}  # type: ignore[typeddict-item]
    if "ResourceConfigurationArn" in data:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        raise DeserializationError(
            "ConnectivityResourceConfigurationArn.resource_configuration_arn required"
        )
    return out
