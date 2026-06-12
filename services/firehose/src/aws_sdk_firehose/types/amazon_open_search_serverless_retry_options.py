"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessRetryOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.amazon_open_search_serverless_retry_duration_in_seconds


class AmazonOpenSearchServerlessRetryOptions(TypedDict):
    duration_in_seconds: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_retry_duration_in_seconds.AmazonOpenSearchServerlessRetryDurationInSeconds"
    ]
    """<p>After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonOpenSearchServerlessRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonOpenSearchServerlessRetryOptions:
    out: AmazonOpenSearchServerlessRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
