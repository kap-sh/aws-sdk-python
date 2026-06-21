"""Generated from Smithy shape ``com.amazonaws.emr#IdcUserAssignment``."""

from typing import Literal, TypeAlias, cast

IdcUserAssignment: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdcUserAssignment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdcUserAssignment:
    return cast(IdcUserAssignment, data)
