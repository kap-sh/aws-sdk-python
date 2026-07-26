"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#OverwriteOption``."""

from typing import Literal, TypeAlias, cast

OverwriteOption: TypeAlias = Literal[
    "CREATE_NEW_REPORT",
    "OVERWRITE_REPORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverwriteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteOption:
    return cast(OverwriteOption, data)
