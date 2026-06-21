"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewStatus``."""

from typing import Literal, TypeAlias, cast

PreviewStatus: TypeAlias = Literal[
    "WORK_IN_PROGRESS",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreviewStatus:
    return cast(PreviewStatus, data)
