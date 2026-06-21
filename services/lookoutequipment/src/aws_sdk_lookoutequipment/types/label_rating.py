"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelRating``."""

from typing import Literal, TypeAlias, cast

LabelRating: TypeAlias = Literal[
    "ANOMALY",
    "NO_ANOMALY",
    "NEUTRAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelRating) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LabelRating:
    return cast(LabelRating, data)
