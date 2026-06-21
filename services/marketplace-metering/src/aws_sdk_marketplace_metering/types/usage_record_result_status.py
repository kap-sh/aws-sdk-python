"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecordResultStatus``."""

from typing import Literal, TypeAlias, cast

UsageRecordResultStatus: TypeAlias = Literal[
    "Success",
    "CustomerNotSubscribed",
    "DuplicateRecord",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageRecordResultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageRecordResultStatus:
    return cast(UsageRecordResultStatus, data)
