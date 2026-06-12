"""Generated from Smithy shape ``com.amazonaws.macie2#FindingsFilterListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.findings_filter_action
    import aws_sdk_macie2.types.tag_map


class FindingsFilterListItem(TypedDict):
    action: NotRequired[
        "aws_sdk_macie2.types.findings_filter_action.FindingsFilterAction"
    ]
    """<p>The action that's performed on findings that match the filter criteria. Possible values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, don't perform any action on the findings.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the filter.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the filter.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom name of the filter.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingsFilterListItem) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_macie2.types.findings_filter_action

        out["action"] = aws_sdk_macie2.types.findings_filter_action.serialize_json(
            value["action"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> FindingsFilterListItem:
    out: FindingsFilterListItem = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_macie2.types.findings_filter_action

        out["action"] = aws_sdk_macie2.types.findings_filter_action.deserialize_json(
            data["action"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
