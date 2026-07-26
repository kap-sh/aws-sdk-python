"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceRetryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.amazonopensearchservice_retry_duration_in_seconds


class AmazonopensearchserviceRetryOptions(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "capo_firehose.types.amazonopensearchservice_retry_duration_in_seconds.AmazonopensearchserviceRetryDurationInSeconds"
    ]
    """<p>After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonopensearchserviceRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonopensearchserviceRetryOptions:
    out: AmazonopensearchserviceRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
