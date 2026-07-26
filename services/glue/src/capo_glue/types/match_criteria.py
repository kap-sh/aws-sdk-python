"""Generated from Smithy shape ``com.amazonaws.glue#MatchCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

MatchCriteria: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchCriteria) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchCriteria:
    return list(data)
