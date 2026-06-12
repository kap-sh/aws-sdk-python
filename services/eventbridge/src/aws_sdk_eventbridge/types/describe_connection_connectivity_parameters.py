"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeConnectionConnectivityParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.describe_connection_resource_parameters


class DescribeConnectionConnectivityParameters(TypedDict):
    resource_parameters: "aws_sdk_eventbridge.types.describe_connection_resource_parameters.DescribeConnectionResourceParameters"
    """<p>The parameters for EventBridge to use when invoking the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionConnectivityParameters) -> dict:
    out: dict = {}
    import aws_sdk_eventbridge.types.describe_connection_resource_parameters

    out["ResourceParameters"] = (
        aws_sdk_eventbridge.types.describe_connection_resource_parameters.serialize_aws_json_1_1(
            value["resource_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionConnectivityParameters:
    out: DescribeConnectionConnectivityParameters = {}  # type: ignore[typeddict-item]
    if "ResourceParameters" in data:
        import aws_sdk_eventbridge.types.describe_connection_resource_parameters

        out["resource_parameters"] = (
            aws_sdk_eventbridge.types.describe_connection_resource_parameters.deserialize_aws_json_1_1(
                data["ResourceParameters"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeConnectionConnectivityParameters.resource_parameters required"
        )
    return out
