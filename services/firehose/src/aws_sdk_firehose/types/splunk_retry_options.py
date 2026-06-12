"""Generated from Smithy shape ``com.amazonaws.firehose#SplunkRetryOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.splunk_retry_duration_in_seconds


class SplunkRetryOptions(TypedDict):
    duration_in_seconds: NotRequired[
        "aws_sdk_firehose.types.splunk_retry_duration_in_seconds.SplunkRetryDurationInSeconds"
    ]
    """<p>The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplunkRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplunkRetryOptions:
    out: SplunkRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
