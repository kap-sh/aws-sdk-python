"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.endpoint_properties


class DescribeEndpointResponse(TypedDict, closed=True):
    endpoint_properties: NotRequired[
        "aws_sdk_comprehend.types.endpoint_properties.EndpointProperties"
    ]
    """<p>Describes information associated with the specific endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_properties" in value:
        import aws_sdk_comprehend.types.endpoint_properties

        out["EndpointProperties"] = (
            aws_sdk_comprehend.types.endpoint_properties.serialize_aws_json_1_1(
                value["endpoint_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointResponse:
    out: DescribeEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointProperties" in data:
        import aws_sdk_comprehend.types.endpoint_properties

        out["endpoint_properties"] = (
            aws_sdk_comprehend.types.endpoint_properties.deserialize_aws_json_1_1(
                data["EndpointProperties"]
            )
        )
    return out
