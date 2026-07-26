"""Generated from Smithy shape ``com.amazonaws.waf#SizeConstraintSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.size_constraint_set_update

SizeConstraintSetUpdates: TypeAlias = list[
    "capo_waf.types.size_constraint_set_update.SizeConstraintSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetUpdates) -> list:
    import capo_waf.types.size_constraint_set_update

    out: list = []
    for item in value:
        out.append(
            capo_waf.types.size_constraint_set_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SizeConstraintSetUpdates:
    import capo_waf.types.size_constraint_set_update

    out: SizeConstraintSetUpdates = []
    for item in data:
        out.append(
            capo_waf.types.size_constraint_set_update.deserialize_aws_json_1_1(item)
        )
    return out
