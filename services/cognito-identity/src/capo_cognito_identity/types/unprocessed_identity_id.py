"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UnprocessedIdentityId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.error_code
    import capo_cognito_identity.types.identity_id


class UnprocessedIdentityId(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    error_code: NotRequired["capo_cognito_identity.types.error_code.ErrorCode"]
    """<p>The error code indicating the type of error that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedIdentityId) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "error_code" in value:
        import capo_cognito_identity.types.error_code

        out["ErrorCode"] = (
            capo_cognito_identity.types.error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedIdentityId:
    out: UnprocessedIdentityId = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "ErrorCode" in data:
        import capo_cognito_identity.types.error_code

        out["error_code"] = (
            capo_cognito_identity.types.error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    return out
