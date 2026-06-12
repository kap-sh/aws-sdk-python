"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#UtteranceData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.count
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.utterance_string


class UtteranceData(TypedDict):
    utterance_string: NotRequired[
        "aws_sdk_lex_model_building_service.types.utterance_string.UtteranceString"
    ]
    """<p>The text that was entered by the user or the text representation of an audio clip.</p>"""
    count: NotRequired["aws_sdk_lex_model_building_service.types.count.Count"]
    """<p>The number of times that the utterance was processed.</p>"""
    distinct_users: NotRequired["aws_sdk_lex_model_building_service.types.count.Count"]
    """<p>The total number of individuals that used the utterance.</p>"""
    first_uttered_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the utterance was first recorded.</p>"""
    last_uttered_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the utterance was last recorded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceData) -> dict:
    out: dict = {}
    if "utterance_string" in value:
        out["utteranceString"] = value["utterance_string"]
    if "count" in value:
        out["count"] = value["count"]
    if "distinct_users" in value:
        out["distinctUsers"] = value["distinct_users"]
    if "first_uttered_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["firstUtteredDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["first_uttered_date"]
            )
        )
    if "last_uttered_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUtteredDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_uttered_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceData:
    out: UtteranceData = {}  # type: ignore[typeddict-item]
    if "utteranceString" in data:
        out["utterance_string"] = data["utteranceString"]
    if "count" in data:
        out["count"] = data["count"]
    if "distinctUsers" in data:
        out["distinct_users"] = data["distinctUsers"]
    if "firstUtteredDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["first_uttered_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["firstUtteredDate"]
            )
        )
    if "lastUtteredDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_uttered_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUtteredDate"]
            )
        )
    return out
