"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionStatus``."""

from typing import Literal, TypeAlias, cast

TestGridSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
    "ERRORED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionStatus:
    return cast(TestGridSessionStatus, data)
