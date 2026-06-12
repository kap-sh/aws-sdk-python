"""Generated from Smithy shape ``com.amazonaws.connect#ContactStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_state

ContactStates: TypeAlias = list["aws_sdk_connect.types.contact_state.ContactState"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactStates) -> list:
    import aws_sdk_connect.types.contact_state

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactStates:
    import aws_sdk_connect.types.contact_state

    out: ContactStates = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_state.deserialize_json(item))
    return out
