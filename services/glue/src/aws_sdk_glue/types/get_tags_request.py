"""Generated from Smithy shape ``com.amazonaws.glue#GetTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn


class GetTagsRequest(TypedDict):
    resource_arn: "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to retrieve tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagsRequest:
    out: GetTagsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetTagsRequest.resource_arn required")
    return out
