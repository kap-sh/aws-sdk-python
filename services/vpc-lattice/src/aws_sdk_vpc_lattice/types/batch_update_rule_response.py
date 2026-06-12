"""Generated from Smithy shape ``com.amazonaws.vpclattice#BatchUpdateRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.rule_update_failure_list
    import aws_sdk_vpc_lattice.types.rule_update_success_list


class BatchUpdateRuleResponse(TypedDict):
    successful: NotRequired[
        "aws_sdk_vpc_lattice.types.rule_update_success_list.RuleUpdateSuccessList"
    ]
    """<p>The rules that were successfully updated.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_vpc_lattice.types.rule_update_failure_list.RuleUpdateFailureList"
    ]
    """<p>The rules that the operation couldn't update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRuleResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import aws_sdk_vpc_lattice.types.rule_update_success_list

        out["successful"] = (
            aws_sdk_vpc_lattice.types.rule_update_success_list.serialize_json(
                value["successful"]
            )
        )
    if "unsuccessful" in value:
        import aws_sdk_vpc_lattice.types.rule_update_failure_list

        out["unsuccessful"] = (
            aws_sdk_vpc_lattice.types.rule_update_failure_list.serialize_json(
                value["unsuccessful"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateRuleResponse:
    out: BatchUpdateRuleResponse = {}  # type: ignore[typeddict-item]
    if "successful" in data:
        import aws_sdk_vpc_lattice.types.rule_update_success_list

        out["successful"] = (
            aws_sdk_vpc_lattice.types.rule_update_success_list.deserialize_json(
                data["successful"]
            )
        )
    if "unsuccessful" in data:
        import aws_sdk_vpc_lattice.types.rule_update_failure_list

        out["unsuccessful"] = (
            aws_sdk_vpc_lattice.types.rule_update_failure_list.deserialize_json(
                data["unsuccessful"]
            )
        )
    return out
