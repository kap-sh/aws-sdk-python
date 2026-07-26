"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectivityResourceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.connectivity_resource_configuration_arn


class ConnectivityResourceParameters(TypedDict, closed=True):
    resource_parameters: "capo_eventbridge.types.connectivity_resource_configuration_arn.ConnectivityResourceConfigurationArn"
    """<p>The parameters for EventBridge to use when invoking the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectivityResourceParameters) -> dict:
    out: dict = {}
    import capo_eventbridge.types.connectivity_resource_configuration_arn

    out["ResourceParameters"] = (
        capo_eventbridge.types.connectivity_resource_configuration_arn.serialize_aws_json_1_1(
            value["resource_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectivityResourceParameters:
    out: ConnectivityResourceParameters = {}  # type: ignore[typeddict-item]
    if "ResourceParameters" in data:
        import capo_eventbridge.types.connectivity_resource_configuration_arn

        out["resource_parameters"] = (
            capo_eventbridge.types.connectivity_resource_configuration_arn.deserialize_aws_json_1_1(
                data["ResourceParameters"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectivityResourceParameters.resource_parameters required"
        )
    return out
