"""Generated from Smithy shape ``com.amazonaws.sesv2#GetSuppressedDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.tenant_name


class GetSuppressedDestinationRequest(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that's on the suppression list for your account or for the specified tenant.</p>"""
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant whose suppression list you want to query. If you omit this parameter, the operation targets the account-level suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuppressedDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSuppressedDestinationRequest:
    out: GetSuppressedDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
