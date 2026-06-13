"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateRootDomainUnitOwnerInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.user_identifier


class UpdateRootDomainUnitOwnerInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the root domain unit owner is to be updated.</p>"""
    current_owner: "aws_sdk_datazone.types.user_identifier.UserIdentifier"
    """<p>The current owner of the root domain unit.</p>"""
    new_owner: "str"
    """<p>The new owner of the root domain unit.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRootDomainUnitOwnerInput) -> dict:
    out: dict = {}
    out["currentOwner"] = value["current_owner"]
    out["newOwner"] = value["new_owner"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRootDomainUnitOwnerInput:
    out: UpdateRootDomainUnitOwnerInput = {}  # type: ignore[typeddict-item]
    if "currentOwner" in data:
        out["current_owner"] = data["currentOwner"]
    else:
        raise DeserializationError(
            "UpdateRootDomainUnitOwnerInput.current_owner required"
        )
    if "newOwner" in data:
        out["new_owner"] = data["newOwner"]
    else:
        raise DeserializationError("UpdateRootDomainUnitOwnerInput.new_owner required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
