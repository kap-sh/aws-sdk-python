"""Generated from Smithy shape ``com.amazonaws.glue#DQStopJobOnFailureTiming``."""

from typing import Literal, TypeAlias, cast

DQStopJobOnFailureTiming: TypeAlias = Literal[
    "Immediate",
    "AfterDataLoad",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DQStopJobOnFailureTiming) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQStopJobOnFailureTiming:
    return cast(DQStopJobOnFailureTiming, data)
