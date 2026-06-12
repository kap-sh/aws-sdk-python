"""Generated from Smithy shape ``com.amazonaws.greengrass#AssociateServiceRoleToAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class AssociateServiceRoleToAccountResponse(TypedDict):
    associated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time when the service role was associated with the account."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateServiceRoleToAccountResponse) -> dict:
    out: dict = {}
    if "associated_at" in value:
        out["AssociatedAt"] = value["associated_at"]
    return out


def deserialize_json(data: dict) -> AssociateServiceRoleToAccountResponse:
    out: AssociateServiceRoleToAccountResponse = {}  # type: ignore[typeddict-item]
    if "AssociatedAt" in data:
        out["associated_at"] = data["AssociatedAt"]
    return out
