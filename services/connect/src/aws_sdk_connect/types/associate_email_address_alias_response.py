"""Generated from Smithy shape ``com.amazonaws.connect#AssociateEmailAddressAliasResponse``."""

from typing_extensions import TypedDict


class AssociateEmailAddressAliasResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEmailAddressAliasResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateEmailAddressAliasResponse:
    out: AssociateEmailAddressAliasResponse = {}  # type: ignore[typeddict-item]
    return out
