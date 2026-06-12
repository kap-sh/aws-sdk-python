"""Generated from Smithy shape ``com.amazonaws.athena#GetResourceDashboardRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.amazon_resource_name


class GetResourceDashboardRequest(TypedDict):
    resource_arn: "aws_sdk_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>The The Amazon Resource Name (ARN) for a session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceDashboardRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceDashboardRequest:
    out: GetResourceDashboardRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("GetResourceDashboardRequest.resource_arn required")
    return out
