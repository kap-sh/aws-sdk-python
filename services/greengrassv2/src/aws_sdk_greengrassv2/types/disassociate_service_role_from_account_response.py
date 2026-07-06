"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DisassociateServiceRoleFromAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class DisassociateServiceRoleFromAccountResponse(TypedDict, closed=True):
    disassociated_at: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The time when the service role was disassociated from IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateServiceRoleFromAccountResponse) -> dict:
    out: dict = {}
    if "disassociated_at" in value:
        out["DisassociatedAt"] = value["disassociated_at"]
    return out


def deserialize_json(data: dict) -> DisassociateServiceRoleFromAccountResponse:
    out: DisassociateServiceRoleFromAccountResponse = {}  # type: ignore[typeddict-item]
    if "DisassociatedAt" in data:
        out["disassociated_at"] = data["DisassociatedAt"]
    return out
