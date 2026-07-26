"""Generated from Smithy shape ``com.amazonaws.lightsail#TreatMissingData``."""

from typing import Literal, TypeAlias, cast

TreatMissingData: TypeAlias = Literal[
    "breaching",
    "notBreaching",
    "ignore",
    "missing",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TreatMissingData) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TreatMissingData:
    return cast(TreatMissingData, data)
