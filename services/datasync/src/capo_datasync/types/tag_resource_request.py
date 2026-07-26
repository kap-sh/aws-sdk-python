"""Generated from Smithy shape ``com.amazonaws.datasync#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the resource to apply the tag to.</p>"""
    tags: "capo_datasync.types.input_tag_list.InputTagList"
    """<p>Specifies the tags that you want to apply to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_datasync.types.input_tag_list

    out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
