"""Generated from Smithy shape ``com.amazonaws.emr#OutputNotebookFormat``."""

from typing import Literal, TypeAlias, cast

OutputNotebookFormat: TypeAlias = Literal["HTML",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputNotebookFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputNotebookFormat:
    return cast(OutputNotebookFormat, data)
