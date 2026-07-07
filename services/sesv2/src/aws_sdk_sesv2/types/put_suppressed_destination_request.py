"""Generated from Smithy shape ``com.amazonaws.sesv2#PutSuppressedDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.suppression_list_reason
    import aws_sdk_sesv2.types.tenant_name


class PutSuppressedDestinationRequest(TypedDict, closed=True):
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The email address that should be added to the suppression list for your account or for the specified tenant.</p>"""
    reason: "aws_sdk_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The factors that should cause the email address to be added to the suppression list for your account or for the specified tenant.</p>"""
    tenant_name: NotRequired["aws_sdk_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant whose suppression list you want to add the address to. If you omit this parameter, the address is added to the account-level suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSuppressedDestinationRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import aws_sdk_sesv2.types.suppression_list_reason

    out["Reason"] = aws_sdk_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> PutSuppressedDestinationRequest:
    out: PutSuppressedDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError(
            "PutSuppressedDestinationRequest.email_address required"
        )
    if "Reason" in data:
        import aws_sdk_sesv2.types.suppression_list_reason

        out["reason"] = aws_sdk_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        raise DeserializationError("PutSuppressedDestinationRequest.reason required")
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    return out
