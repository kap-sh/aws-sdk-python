"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDeleteUserAttributesResponse``."""

from typing_extensions import TypedDict


class AdminDeleteUserAttributesResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDeleteUserAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDeleteUserAttributesResponse:
    out: AdminDeleteUserAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
