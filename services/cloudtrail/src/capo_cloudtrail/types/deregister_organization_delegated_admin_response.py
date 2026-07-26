"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeregisterOrganizationDelegatedAdminResponse``."""

from typing_extensions import TypedDict


class DeregisterOrganizationDelegatedAdminResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterOrganizationDelegatedAdminResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeregisterOrganizationDelegatedAdminResponse:
    out: DeregisterOrganizationDelegatedAdminResponse = {}  # type: ignore[typeddict-item]
    return out
