"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserAttributesResponse``."""

from typing_extensions import TypedDict


class DeleteUserAttributesResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserAttributesResponse:
    out: DeleteUserAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
