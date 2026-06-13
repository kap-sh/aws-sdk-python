"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_codeguru_security.types.tag_map.TagMap"]
    """<p>An array of key-value pairs used to tag an existing scan. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A tag key. For example, <code>CostCenter</code>, <code>Environment</code>, or <code>Secret</code>. Tag keys are case sensitive.</p> </li> <li> <p>An optional tag value field. For example, <code>111122223333</code>, <code>Production</code>, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codeguru_security.types.tag_map

        out["tags"] = aws_sdk_codeguru_security.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codeguru_security.types.tag_map

        out["tags"] = aws_sdk_codeguru_security.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
