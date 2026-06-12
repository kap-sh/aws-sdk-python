"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.rule_summary

RuleSummaryList: TypeAlias = list["aws_sdk_vpc_lattice.types.rule_summary.RuleSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummaryList) -> list:
    import aws_sdk_vpc_lattice.types.rule_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_vpc_lattice.types.rule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSummaryList:
    import aws_sdk_vpc_lattice.types.rule_summary

    out: RuleSummaryList = []
    for item in data:
        out.append(aws_sdk_vpc_lattice.types.rule_summary.deserialize_json(item))
    return out
