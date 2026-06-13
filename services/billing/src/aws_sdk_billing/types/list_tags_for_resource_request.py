"""Generated from Smithy shape ``com.amazonaws.billing#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.resource_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_billing.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
