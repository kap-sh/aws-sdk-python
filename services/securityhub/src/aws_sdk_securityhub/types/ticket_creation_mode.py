"""Generated from Smithy shape ``com.amazonaws.securityhub#TicketCreationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

"""<p>The mode for creating a ticket.</p>"""
TicketCreationMode: TypeAlias = Literal["DRYRUN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DRYRUN",))


def serialize_json(value: TicketCreationMode) -> str:
    return value


def deserialize_json(data: str) -> TicketCreationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TicketCreationMode value: {data!r}")
    return cast(TicketCreationMode, data)
