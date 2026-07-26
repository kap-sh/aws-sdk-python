"""Generated from Smithy shape ``com.amazonaws.waf#SizeConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.size_constraint

SizeConstraints: TypeAlias = list["capo_waf.types.size_constraint.SizeConstraint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraints) -> list:
    import capo_waf.types.size_constraint

    out: list = []
    for item in value:
        out.append(capo_waf.types.size_constraint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SizeConstraints:
    import capo_waf.types.size_constraint

    out: SizeConstraints = []
    for item in data:
        out.append(capo_waf.types.size_constraint.deserialize_aws_json_1_1(item))
    return out
