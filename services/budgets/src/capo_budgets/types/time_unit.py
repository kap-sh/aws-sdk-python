"""Generated from Smithy shape ``com.amazonaws.budgets#TimeUnit``."""

from typing import Literal, TypeAlias, cast

"""<p> The time unit of the budget, such as MONTHLY or QUARTERLY.</p>"""
TimeUnit: TypeAlias = Literal[
    "DAILY",
    "MONTHLY",
    "QUARTERLY",
    "ANNUALLY",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnit:
    return cast(TimeUnit, data)
