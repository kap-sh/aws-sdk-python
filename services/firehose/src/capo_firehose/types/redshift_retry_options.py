"""Generated from Smithy shape ``com.amazonaws.firehose#RedshiftRetryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.redshift_retry_duration_in_seconds


class RedshiftRetryOptions(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "capo_firehose.types.redshift_retry_duration_in_seconds.RedshiftRetryDurationInSeconds"
    ]
    """<p>The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of <code>DurationInSeconds</code> is 0 (zero) or if the first delivery attempt takes longer than the current value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftRetryOptions:
    out: RedshiftRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
