"""Generated from Smithy shape ``com.amazonaws.swf#RecordMarkerFailedCause``."""

from typing import Literal, TypeAlias, cast

RecordMarkerFailedCause: TypeAlias = Literal["OPERATION_NOT_PERMITTED",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordMarkerFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecordMarkerFailedCause:
    return cast(RecordMarkerFailedCause, data)
