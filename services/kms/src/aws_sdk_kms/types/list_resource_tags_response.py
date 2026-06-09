"""Generated from Smithy shape ``com.amazonaws.kms#ListResourceTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.marker_type
    import aws_sdk_kms.types.tag_list


class ListResourceTagsResponse(TypedDict):
    tags: NotRequired["aws_sdk_kms.types.tag_list.TagList"]
    """<p>A list of tags. Each tag consists of a tag key and a tag value.</p> <note> <p>Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/abac.html\">ABAC for KMS</a> in the <i>Key Management Service Developer Guide</i>.</p> </note>"""
    next_marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p> <p>Do not assume or infer any information from this value.</p>"""
    truncated: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_kms.types.tag_list

        out["Tags"] = aws_sdk_kms.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceTagsResponse:
    out: ListResourceTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_kms.types.tag_list

        out["tags"] = aws_sdk_kms.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
