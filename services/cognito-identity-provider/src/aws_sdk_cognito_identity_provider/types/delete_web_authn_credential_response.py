"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteWebAuthnCredentialResponse``."""

from typing_extensions import TypedDict


class DeleteWebAuthnCredentialResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebAuthnCredentialResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebAuthnCredentialResponse:
    out: DeleteWebAuthnCredentialResponse = {}  # type: ignore[typeddict-item]
    return out
