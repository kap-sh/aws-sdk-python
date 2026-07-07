"""Generated from Smithy shape ``com.amazonaws.dax#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.string
    import aws_sdk_dax.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the DAX resource to which tags should be added.</p>"""
    tags: "aws_sdk_dax.types.tag_list.TagList"
    """<p>The tags to be assigned to the DAX resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    import aws_sdk_dax.types.tag_list

    out["Tags"] = aws_sdk_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("TagResourceRequest.resource_name required")
    if "Tags" in data:
        import aws_sdk_dax.types.tag_list

        out["tags"] = aws_sdk_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
