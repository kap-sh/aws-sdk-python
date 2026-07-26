"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_verifiedpermissions.types.tag_map.TagMap"]
    """<p>The list of tags associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_verifiedpermissions.types.tag_map

        out["tags"] = capo_verifiedpermissions.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_verifiedpermissions.types.tag_map

        out["tags"] = capo_verifiedpermissions.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
