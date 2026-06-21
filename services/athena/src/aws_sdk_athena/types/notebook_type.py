"""Generated from Smithy shape ``com.amazonaws.athena#NotebookType``."""

from typing import Literal, TypeAlias, cast

NotebookType: TypeAlias = Literal["IPYNB",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookType:
    return cast(NotebookType, data)
