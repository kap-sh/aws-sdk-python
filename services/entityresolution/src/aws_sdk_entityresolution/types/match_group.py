"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.matched_records_list


class MatchGroup(TypedDict, closed=True):
    records: "aws_sdk_entityresolution.types.matched_records_list.MatchedRecordsList"
    """<p> The matched records.</p>"""
    match_id: "str"
    """<p> The match ID.</p>"""
    match_rule: "str"
    """<p> The match rule of the match group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchGroup) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.matched_records_list

    out["records"] = aws_sdk_entityresolution.types.matched_records_list.serialize_json(
        value["records"]
    )
    out["matchId"] = value["match_id"]
    out["matchRule"] = value["match_rule"]
    return out


def deserialize_json(data: dict) -> MatchGroup:
    out: MatchGroup = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_entityresolution.types.matched_records_list

        out["records"] = (
            aws_sdk_entityresolution.types.matched_records_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("MatchGroup.records required")
    if "matchId" in data:
        out["match_id"] = data["matchId"]
    else:
        raise DeserializationError("MatchGroup.match_id required")
    if "matchRule" in data:
        out["match_rule"] = data["matchRule"]
    else:
        raise DeserializationError("MatchGroup.match_rule required")
    return out
