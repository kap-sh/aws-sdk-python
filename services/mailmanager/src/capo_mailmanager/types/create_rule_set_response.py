"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateRuleSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_set_id


class CreateRuleSetResponse(TypedDict, closed=True):
    rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of the created rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRuleSetResponse) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRuleSetResponse:
    out: CreateRuleSetResponse = {}  # type: ignore[typeddict-item]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("CreateRuleSetResponse.rule_set_id required")
    return out
