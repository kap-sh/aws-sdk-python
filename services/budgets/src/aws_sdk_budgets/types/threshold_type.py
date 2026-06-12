"""Generated from Smithy shape ``com.amazonaws.budgets#ThresholdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The type of threshold for a notification.</p>"""
ThresholdType: TypeAlias = Literal[
    "PERCENTAGE",
    "ABSOLUTE_VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERCENTAGE",
        "ABSOLUTE_VALUE",
    )
)


def serialize_aws_json_1_1(value: ThresholdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThresholdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThresholdType value: {data!r}")
    return cast(ThresholdType, data)
