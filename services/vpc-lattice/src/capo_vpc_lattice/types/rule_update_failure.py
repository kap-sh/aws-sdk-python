"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdateFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.failure_code
    import capo_vpc_lattice.types.failure_message
    import capo_vpc_lattice.types.rule_identifier


class RuleUpdateFailure(TypedDict, closed=True):
    rule_identifier: NotRequired[
        "capo_vpc_lattice.types.rule_identifier.RuleIdentifier"
    ]
    """<p>The ID or ARN of the rule.</p>"""
    failure_code: NotRequired["capo_vpc_lattice.types.failure_code.FailureCode"]
    """<p>The failure code.</p>"""
    failure_message: NotRequired[
        "capo_vpc_lattice.types.failure_message.FailureMessage"
    ]
    """<p>The failure message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdateFailure) -> dict:
    out: dict = {}
    if "rule_identifier" in value:
        out["ruleIdentifier"] = value["rule_identifier"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> RuleUpdateFailure:
    out: RuleUpdateFailure = {}  # type: ignore[typeddict-item]
    if "ruleIdentifier" in data:
        out["rule_identifier"] = data["ruleIdentifier"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
