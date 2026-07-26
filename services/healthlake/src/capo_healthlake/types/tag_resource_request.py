"""Generated from Smithy shape ``com.amazonaws.healthlake#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.amazon_resource_name
    import capo_healthlake.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_healthlake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that grants access to the data store tags are being added to.</p>"""
    tags: "capo_healthlake.types.tag_list.TagList"
    """<p>The user-specified key and value pair tags being added to a data store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_healthlake.types.tag_list

    out["Tags"] = capo_healthlake.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_healthlake.types.tag_list

        out["tags"] = capo_healthlake.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
