"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#GranularityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The time granularity for aggregating the cost efficiency metrics.</p>"""
GranularityType: TypeAlias = Literal[
    "Daily",
    "Monthly",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GranularityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GranularityType:
    return cast(GranularityType, data)
