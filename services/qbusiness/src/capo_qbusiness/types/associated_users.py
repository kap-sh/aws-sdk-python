"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.associated_user

AssociatedUsers: TypeAlias = list["capo_qbusiness.types.associated_user.AssociatedUser"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedUsers) -> list:
    import capo_qbusiness.types.associated_user

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.associated_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedUsers:
    import capo_qbusiness.types.associated_user

    out: AssociatedUsers = []
    for item in data:
        out.append(capo_qbusiness.types.associated_user.deserialize_json(item))
    return out
