"""Generated from Smithy shape ``com.amazonaws.securityhub#TicketCreationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The mode for creating a ticket.</p>"""
TicketCreationMode: TypeAlias = Literal["DRYRUN",]


# --- restJson1 ser/de ---
def serialize_json(value: TicketCreationMode) -> str:
    return value


def deserialize_json(data: str) -> TicketCreationMode:
    return cast(TicketCreationMode, data)
