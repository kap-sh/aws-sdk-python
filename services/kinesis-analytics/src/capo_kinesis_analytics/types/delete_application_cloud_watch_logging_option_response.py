"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationCloudWatchLoggingOptionResponse``."""

from typing_extensions import TypedDict


class DeleteApplicationCloudWatchLoggingOptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationCloudWatchLoggingOptionResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationCloudWatchLoggingOptionResponse:
    out: DeleteApplicationCloudWatchLoggingOptionResponse = {}  # type: ignore[typeddict-item]
    return out
