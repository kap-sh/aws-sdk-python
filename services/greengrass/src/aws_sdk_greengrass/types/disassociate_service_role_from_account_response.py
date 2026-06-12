"""Generated from Smithy shape ``com.amazonaws.greengrass#DisassociateServiceRoleFromAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DisassociateServiceRoleFromAccountResponse(TypedDict):
    disassociated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time when the service role was disassociated from the account."""


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
