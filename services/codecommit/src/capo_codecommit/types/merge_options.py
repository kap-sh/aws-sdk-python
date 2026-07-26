"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.merge_option_type_enum

MergeOptions: TypeAlias = list[
    "capo_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeOptions) -> list:
    import capo_codecommit.types.merge_option_type_enum

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.merge_option_type_enum.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MergeOptions:
    import capo_codecommit.types.merge_option_type_enum

    out: MergeOptions = []
    for item in data:
        out.append(
            capo_codecommit.types.merge_option_type_enum.deserialize_aws_json_1_1(item)
        )
    return out
