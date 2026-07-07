"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminUserGlobalSignOutResponse``."""

from typing_extensions import TypedDict


class AdminUserGlobalSignOutResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminUserGlobalSignOutResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminUserGlobalSignOutResponse:
    out: AdminUserGlobalSignOutResponse = {}  # type: ignore[typeddict-item]
    return out
