"""Generated from Smithy shape ``com.amazonaws.comprehend#RelationshipsListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.relationship_type
    import aws_sdk_comprehend.types.string_list


class RelationshipsListItem(TypedDict):
    ids: NotRequired["aws_sdk_comprehend.types.string_list.StringList"]
    """<p>Identifers of the child blocks.</p>"""
    type: NotRequired["aws_sdk_comprehend.types.relationship_type.RelationshipType"]
    """<p>Only supported relationship is a child relationship.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipsListItem) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_comprehend.types.string_list

        out["Ids"] = aws_sdk_comprehend.types.string_list.serialize_aws_json_1_1(
            value["ids"]
        )
    if "type" in value:
        import aws_sdk_comprehend.types.relationship_type

        out["Type"] = aws_sdk_comprehend.types.relationship_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationshipsListItem:
    out: RelationshipsListItem = {}  # type: ignore[typeddict-item]
    if "Ids" in data:
        import aws_sdk_comprehend.types.string_list

        out["ids"] = aws_sdk_comprehend.types.string_list.deserialize_aws_json_1_1(
            data["Ids"]
        )
    if "Type" in data:
        import aws_sdk_comprehend.types.relationship_type

        out["type"] = (
            aws_sdk_comprehend.types.relationship_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
