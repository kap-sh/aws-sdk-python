"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubstituteStringEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.substitute_string_entry

SubstituteStringEntries: TypeAlias = list[
    "capo_cloudwatch_logs.types.substitute_string_entry.SubstituteStringEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubstituteStringEntries) -> list:
    import capo_cloudwatch_logs.types.substitute_string_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.substitute_string_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubstituteStringEntries:
    import capo_cloudwatch_logs.types.substitute_string_entry

    out: SubstituteStringEntries = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.substitute_string_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
