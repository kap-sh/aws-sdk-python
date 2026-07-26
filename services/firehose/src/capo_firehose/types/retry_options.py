"""Generated from Smithy shape ``com.amazonaws.firehose#RetryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.retry_duration_in_seconds


class RetryOptions(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "capo_firehose.types.retry_duration_in_seconds.RetryDurationInSeconds"
    ]
    """<p>The period of time during which Firehose retries to deliver data to the specified destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryOptions:
    out: RetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
