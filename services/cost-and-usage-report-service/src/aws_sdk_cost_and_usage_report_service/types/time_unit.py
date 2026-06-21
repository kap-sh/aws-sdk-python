"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#TimeUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The length of time covered by the report. </p>"""
TimeUnit: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "MONTHLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnit:
    return cast(TimeUnit, data)
