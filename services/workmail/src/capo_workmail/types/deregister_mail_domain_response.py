"""Generated from Smithy shape ``com.amazonaws.workmail#DeregisterMailDomainResponse``."""

from typing_extensions import TypedDict


class DeregisterMailDomainResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterMailDomainResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterMailDomainResponse:
    out: DeregisterMailDomainResponse = {}  # type: ignore[typeddict-item]
    return out
