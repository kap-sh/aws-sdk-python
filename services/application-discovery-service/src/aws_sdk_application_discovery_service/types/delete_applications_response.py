"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteApplicationsResponse``."""

from typing_extensions import TypedDict


class DeleteApplicationsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationsResponse:
    out: DeleteApplicationsResponse = {}  # type: ignore[typeddict-item]
    return out
