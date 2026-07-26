"""Generated from Smithy shape ``com.amazonaws.eventbridge#PropagateTags``."""

from typing import Literal, TypeAlias, cast

PropagateTags: TypeAlias = Literal["TASK_DEFINITION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropagateTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateTags:
    return cast(PropagateTags, data)
