"""Generated from Smithy shape ``com.amazonaws.shield#AttackLayer``."""

from typing import Literal, TypeAlias, cast

AttackLayer: TypeAlias = Literal[
    "NETWORK",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackLayer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttackLayer:
    return cast(AttackLayer, data)
