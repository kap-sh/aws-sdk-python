"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseCharacterSetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.character_set_type


class ListAutonomousDatabaseCharacterSetsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    character_set_type: NotRequired[
        "aws_sdk_odb.types.character_set_type.characterSetType"
    ]
    """<p>The type of character set to return results for, either the database character set or the national character set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseCharacterSetsInput) -> dict:
    out: dict = {}
    if "character_set_type" in value:
        import aws_sdk_odb.types.character_set_type

        out["characterSetType"] = (
            aws_sdk_odb.types.character_set_type.serialize_aws_json_1_0(
                value["character_set_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseCharacterSetsInput:
    out: ListAutonomousDatabaseCharacterSetsInput = {}  # type: ignore[typeddict-item]
    if "characterSetType" in data:
        import aws_sdk_odb.types.character_set_type

        out["character_set_type"] = (
            aws_sdk_odb.types.character_set_type.deserialize_aws_json_1_0(
                data["characterSetType"]
            )
        )
    return out
