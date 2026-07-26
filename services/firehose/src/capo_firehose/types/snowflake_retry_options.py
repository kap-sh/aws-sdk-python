"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeRetryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.snowflake_retry_duration_in_seconds


class SnowflakeRetryOptions(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "capo_firehose.types.snowflake_retry_duration_in_seconds.SnowflakeRetryDurationInSeconds"
    ]
    """<p>the time period where Firehose will retry sending data to the chosen HTTP endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeRetryOptions:
    out: SnowflakeRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
