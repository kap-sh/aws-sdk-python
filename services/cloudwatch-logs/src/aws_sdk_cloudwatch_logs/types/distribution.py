"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Distribution``."""

from typing import Literal, TypeAlias, cast

"""<p>The method used to distribute log data to the destination, which can be either random or grouped by log stream.</p>"""
Distribution: TypeAlias = Literal[
    "Random",
    "ByLogStream",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Distribution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Distribution:
    return cast(Distribution, data)
