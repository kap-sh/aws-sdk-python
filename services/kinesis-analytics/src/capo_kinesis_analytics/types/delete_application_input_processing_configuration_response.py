"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationInputProcessingConfigurationResponse``."""

from typing_extensions import TypedDict


class DeleteApplicationInputProcessingConfigurationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationInputProcessingConfigurationResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationInputProcessingConfigurationResponse:
    out: DeleteApplicationInputProcessingConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
