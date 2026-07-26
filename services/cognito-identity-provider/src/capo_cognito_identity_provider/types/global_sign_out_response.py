"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GlobalSignOutResponse``."""

from typing_extensions import TypedDict


class GlobalSignOutResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlobalSignOutResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GlobalSignOutResponse:
    out: GlobalSignOutResponse = {}  # type: ignore[typeddict-item]
    return out
