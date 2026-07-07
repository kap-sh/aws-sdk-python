"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationAssignmentConfigurationResponse``."""

from typing_extensions import TypedDict


class PutApplicationAssignmentConfigurationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PutApplicationAssignmentConfigurationResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutApplicationAssignmentConfigurationResponse:
    out: PutApplicationAssignmentConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
