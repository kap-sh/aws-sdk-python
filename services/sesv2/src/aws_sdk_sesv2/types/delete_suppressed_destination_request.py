"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteSuppressedDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.tenant_name


class DeleteSuppressedDestinationRequest(TypedDict):
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The suppressed email destination to remove from the suppression list for your account or for the specified tenant.</p>"""
    tenant_name: NotRequired["aws_sdk_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant whose suppression list you want to remove the address from. If you omit this parameter, the address is removed from the account-level suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSuppressedDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSuppressedDestinationRequest:
    out: DeleteSuppressedDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
