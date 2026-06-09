"""Generated from Smithy shape ``com.amazonaws.kms#DryRunModifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.dry_run_modifier_type

DryRunModifierList: TypeAlias = list[
    "aws_sdk_kms.types.dry_run_modifier_type.DryRunModifierType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunModifierList) -> list:
    import aws_sdk_kms.types.dry_run_modifier_type

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.dry_run_modifier_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DryRunModifierList:
    import aws_sdk_kms.types.dry_run_modifier_type

    out: DryRunModifierList = []
    for item in data:
        out.append(
            aws_sdk_kms.types.dry_run_modifier_type.deserialize_aws_json_1_1(item)
        )
    return out
