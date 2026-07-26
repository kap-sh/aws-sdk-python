"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSessionMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_session_message

CisSessionMessages: TypeAlias = list[
    "capo_inspector2.types.cis_session_message.CisSessionMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisSessionMessages) -> list:
    import capo_inspector2.types.cis_session_message

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_session_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisSessionMessages:
    import capo_inspector2.types.cis_session_message

    out: CisSessionMessages = []
    for item in data:
        out.append(capo_inspector2.types.cis_session_message.deserialize_json(item))
    return out
