"""Generated from Smithy shape ``com.amazonaws.ecr#GetRegistryScanningConfigurationRequest``."""

from typing_extensions import TypedDict


class GetRegistryScanningConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegistryScanningConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegistryScanningConfigurationRequest:
    out: GetRegistryScanningConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
