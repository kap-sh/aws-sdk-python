"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTaskFilterName``."""

from typing import Literal, TypeAlias, cast

ImportTaskFilterName: TypeAlias = Literal[
    "IMPORT_TASK_ID",
    "STATUS",
    "NAME",
    "FILE_CLASSIFICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportTaskFilterName:
    return cast(ImportTaskFilterName, data)
