"""Generated from Smithy shape ``com.amazonaws.location#JobErrorMessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.job_error_message

JobErrorMessagesList: TypeAlias = list[
    "aws_sdk_location.types.job_error_message.JobErrorMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobErrorMessagesList) -> list:
    return list(value)


def deserialize_json(data: list) -> JobErrorMessagesList:
    return list(data)
