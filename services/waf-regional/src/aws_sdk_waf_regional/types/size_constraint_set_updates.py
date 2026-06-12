"""Generated from Smithy shape ``com.amazonaws.wafregional#SizeConstraintSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.size_constraint_set_update

SizeConstraintSetUpdates: TypeAlias = list[
    "aws_sdk_waf_regional.types.size_constraint_set_update.SizeConstraintSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetUpdates) -> list:
    import aws_sdk_waf_regional.types.size_constraint_set_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.size_constraint_set_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SizeConstraintSetUpdates:
    import aws_sdk_waf_regional.types.size_constraint_set_update

    out: SizeConstraintSetUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.size_constraint_set_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
