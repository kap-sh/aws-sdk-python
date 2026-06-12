"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.variable_entry

VariableEntryList: TypeAlias = list[
    "aws_sdk_frauddetector.types.variable_entry.VariableEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableEntryList) -> list:
    import aws_sdk_frauddetector.types.variable_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.variable_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VariableEntryList:
    import aws_sdk_frauddetector.types.variable_entry

    out: VariableEntryList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.variable_entry.deserialize_aws_json_1_1(item)
        )
    return out
