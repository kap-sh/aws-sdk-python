"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSCopyStrategy``."""

from typing import Literal, TypeAlias, cast

OpenZFSCopyStrategy: TypeAlias = Literal[
    "CLONE",
    "FULL_COPY",
    "INCREMENTAL_COPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSCopyStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSCopyStrategy:
    return cast(OpenZFSCopyStrategy, data)
