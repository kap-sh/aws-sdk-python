"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleIdentifier``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_id


class CaseRuleIdentifier(TypedDict):
    id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleIdentifier) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CaseRuleIdentifier:
    out: CaseRuleIdentifier = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CaseRuleIdentifier.id required")
    return out
