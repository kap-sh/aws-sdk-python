"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.amazon_resource_name


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_codeconnections.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    return out
