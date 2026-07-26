"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.amazon_resource_name
    import capo_iotfleetwise.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotfleetwise.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tags: "capo_iotfleetwise.types.tag_list.TagList"
    """<p>The new or modified tags for the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.tag_list

    out["Tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
