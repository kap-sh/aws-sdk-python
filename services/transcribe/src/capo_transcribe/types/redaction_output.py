"""Generated from Smithy shape ``com.amazonaws.transcribe#RedactionOutput``."""

from typing import Literal, TypeAlias, cast

RedactionOutput: TypeAlias = Literal[
    "redacted",
    "redacted_and_unredacted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedactionOutput) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedactionOutput:
    return cast(RedactionOutput, data)
