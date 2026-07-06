"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.endpoints


class DescribeEndpointsResponse(TypedDict, closed=True):
    endpoints: "aws_sdk_dynamodb.types.endpoints.Endpoints"
    """<p>List of endpoints.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.endpoints

    out["Endpoints"] = aws_sdk_dynamodb.types.endpoints.serialize_aws_json_1_0(
        value["endpoints"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_dynamodb.types.endpoints

        out["endpoints"] = aws_sdk_dynamodb.types.endpoints.deserialize_aws_json_1_0(
            data["Endpoints"]
        )
    else:
        raise DeserializationError("DescribeEndpointsResponse.endpoints required")
    return out
