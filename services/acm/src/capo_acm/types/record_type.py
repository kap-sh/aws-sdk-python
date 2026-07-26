"""Generated from Smithy shape ``com.amazonaws.acm#RecordType``."""

from typing import Literal, TypeAlias, cast

RecordType: TypeAlias = Literal["CNAME",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordType:
    return cast(RecordType, data)
