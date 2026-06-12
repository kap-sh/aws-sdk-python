"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectivityResourceParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connectivity_resource_configuration_arn


class ConnectivityResourceParameters(TypedDict):
    resource_parameters: "aws_sdk_eventbridge.types.connectivity_resource_configuration_arn.ConnectivityResourceConfigurationArn"
    """<p>The parameters for EventBridge to use when invoking the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectivityResourceParameters) -> dict:
    out: dict = {}
    import aws_sdk_eventbridge.types.connectivity_resource_configuration_arn

    out["ResourceParameters"] = (
        aws_sdk_eventbridge.types.connectivity_resource_configuration_arn.serialize_aws_json_1_1(
            value["resource_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectivityResourceParameters:
    out: ConnectivityResourceParameters = {}  # type: ignore[typeddict-item]
    if "ResourceParameters" in data:
        import aws_sdk_eventbridge.types.connectivity_resource_configuration_arn

        out["resource_parameters"] = (
            aws_sdk_eventbridge.types.connectivity_resource_configuration_arn.deserialize_aws_json_1_1(
                data["ResourceParameters"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectivityResourceParameters.resource_parameters required"
        )
    return out
