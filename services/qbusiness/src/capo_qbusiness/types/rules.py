"""Generated from Smithy shape ``com.amazonaws.qbusiness#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.rule

Rules: TypeAlias = list["capo_qbusiness.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: Rules) -> list:
    import capo_qbusiness.types.rule

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rules:
    import capo_qbusiness.types.rule

    out: Rules = []
    for item in data:
        out.append(capo_qbusiness.types.rule.deserialize_json(item))
    return out
