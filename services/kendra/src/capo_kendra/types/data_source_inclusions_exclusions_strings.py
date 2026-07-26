"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceInclusionsExclusionsStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.data_source_inclusions_exclusions_strings_member

DataSourceInclusionsExclusionsStrings: TypeAlias = list[
    "capo_kendra.types.data_source_inclusions_exclusions_strings_member.DataSourceInclusionsExclusionsStringsMember"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceInclusionsExclusionsStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataSourceInclusionsExclusionsStrings:
    return list(data)
