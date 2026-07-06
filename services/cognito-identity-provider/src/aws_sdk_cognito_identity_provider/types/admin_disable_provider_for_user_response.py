"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDisableProviderForUserResponse``."""

from typing_extensions import TypedDict


class AdminDisableProviderForUserResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDisableProviderForUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDisableProviderForUserResponse:
    out: AdminDisableProviderForUserResponse = {}  # type: ignore[typeddict-item]
    return out
