"""Generated from Smithy shape ``com.amazonaws.configservice#ChronologicalOrder``."""

from typing import Literal, TypeAlias, cast

ChronologicalOrder: TypeAlias = Literal[
    "Reverse",
    "Forward",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChronologicalOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChronologicalOrder:
    return cast(ChronologicalOrder, data)
