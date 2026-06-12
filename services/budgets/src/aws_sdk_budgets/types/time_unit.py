"""Generated from Smithy shape ``com.amazonaws.budgets#TimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The time unit of the budget, such as MONTHLY or QUARTERLY.</p>"""
TimeUnit: TypeAlias = Literal[
    "DAILY",
    "MONTHLY",
    "QUARTERLY",
    "ANNUALLY",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAILY",
        "MONTHLY",
        "QUARTERLY",
        "ANNUALLY",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnit value: {data!r}")
    return cast(TimeUnit, data)
