"""Generated from Smithy shape ``com.amazonaws.vpclattice#BatchUpdateRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.rule_update_failure_list
    import capo_vpc_lattice.types.rule_update_success_list


class BatchUpdateRuleResponse(TypedDict, closed=True):
    successful: NotRequired[
        "capo_vpc_lattice.types.rule_update_success_list.RuleUpdateSuccessList"
    ]
    """<p>The rules that were successfully updated.</p>"""
    unsuccessful: NotRequired[
        "capo_vpc_lattice.types.rule_update_failure_list.RuleUpdateFailureList"
    ]
    """<p>The rules that the operation couldn't update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRuleResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import capo_vpc_lattice.types.rule_update_success_list

        out["successful"] = (
            capo_vpc_lattice.types.rule_update_success_list.serialize_json(
                value["successful"]
            )
        )
    if "unsuccessful" in value:
        import capo_vpc_lattice.types.rule_update_failure_list

        out["unsuccessful"] = (
            capo_vpc_lattice.types.rule_update_failure_list.serialize_json(
                value["unsuccessful"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateRuleResponse:
    out: BatchUpdateRuleResponse = {}  # type: ignore[typeddict-item]
    if "successful" in data:
        import capo_vpc_lattice.types.rule_update_success_list

        out["successful"] = (
            capo_vpc_lattice.types.rule_update_success_list.deserialize_json(
                data["successful"]
            )
        )
    if "unsuccessful" in data:
        import capo_vpc_lattice.types.rule_update_failure_list

        out["unsuccessful"] = (
            capo_vpc_lattice.types.rule_update_failure_list.deserialize_json(
                data["unsuccessful"]
            )
        )
    return out
