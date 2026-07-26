"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteSigningConfigurationRequest``."""

from typing_extensions import TypedDict


class DeleteSigningConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSigningConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSigningConfigurationRequest:
    out: DeleteSigningConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
