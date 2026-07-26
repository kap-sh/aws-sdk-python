"""Generated from Smithy shape ``com.amazonaws.keyspaces#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.tag_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The Amazon Keyspaces resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>"""
    tags: "capo_keyspaces.types.tag_list.TagList"
    """<p>A list of existing tags to be removed from the Amazon Keyspaces resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_keyspaces.types.tag_list

    out["tags"] = capo_keyspaces.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tags required")
    return out
