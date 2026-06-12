"""Generated from Smithy shape ``com.amazonaws.inspector#SetTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.tag_list


class SetTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that you want to set tags to.</p>"""
    tags: NotRequired["aws_sdk_inspector.types.tag_list.TagList"]
    """<p>A collection of key and value pairs that you want to set to the assessment template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_inspector.types.tag_list

        out["tags"] = aws_sdk_inspector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetTagsForResourceRequest:
    out: SetTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("SetTagsForResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_inspector.types.tag_list

        out["tags"] = aws_sdk_inspector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
