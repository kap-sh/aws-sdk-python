"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointRetryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.http_endpoint_retry_duration_in_seconds


class HttpEndpointRetryOptions(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_retry_duration_in_seconds.HttpEndpointRetryDurationInSeconds"
    ]
    """<p>The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesn't include the periods during which Firehose waits for acknowledgment from the specified destination after each attempt. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointRetryOptions) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointRetryOptions:
    out: HttpEndpointRetryOptions = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
