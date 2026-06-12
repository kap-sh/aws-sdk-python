"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#SendEmailVerificationCodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.email


class SendEmailVerificationCodeRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address to send the verification code to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendEmailVerificationCodeRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendEmailVerificationCodeRequest:
    out: SendEmailVerificationCodeRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("SendEmailVerificationCodeRequest.catalog required")
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("SendEmailVerificationCodeRequest.email required")
    return out
