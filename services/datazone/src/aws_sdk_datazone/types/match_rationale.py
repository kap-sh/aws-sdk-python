"""Generated from Smithy shape ``com.amazonaws.datazone#MatchRationale``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.match_rationale_item

MatchRationale: TypeAlias = list[
    "aws_sdk_datazone.types.match_rationale_item.MatchRationaleItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchRationale) -> list:
    import aws_sdk_datazone.types.match_rationale_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.match_rationale_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchRationale:
    import aws_sdk_datazone.types.match_rationale_item

    out: MatchRationale = []
    for item in data:
        out.append(aws_sdk_datazone.types.match_rationale_item.deserialize_json(item))
    return out
