"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeConnectionConnectivityParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.describe_connection_resource_parameters


class DescribeConnectionConnectivityParameters(TypedDict, closed=True):
    resource_parameters: "capo_eventbridge.types.describe_connection_resource_parameters.DescribeConnectionResourceParameters"
    """<p>The parameters for EventBridge to use when invoking the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionConnectivityParameters) -> dict:
    out: dict = {}
    import capo_eventbridge.types.describe_connection_resource_parameters

    out["ResourceParameters"] = (
        capo_eventbridge.types.describe_connection_resource_parameters.serialize_aws_json_1_1(
            value["resource_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionConnectivityParameters:
    out: DescribeConnectionConnectivityParameters = {}  # type: ignore[typeddict-item]
    if "ResourceParameters" in data:
        import capo_eventbridge.types.describe_connection_resource_parameters

        out["resource_parameters"] = (
            capo_eventbridge.types.describe_connection_resource_parameters.deserialize_aws_json_1_1(
                data["ResourceParameters"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeConnectionConnectivityParameters.resource_parameters required"
        )
    return out
