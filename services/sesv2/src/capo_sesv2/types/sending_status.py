"""Generated from Smithy shape ``com.amazonaws.sesv2#SendingStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The sending status for a reputation entity. This can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Sending is allowed for this entity.</p> </li> <li> <p> <code>DISABLED</code> – Sending is prevented for this entity.</p> </li> <li> <p> <code>REINSTATED</code> – Sending is allowed even if there are active reputation findings.</p> </li> </ul>"""
SendingStatus: TypeAlias = Literal[
    "ENABLED",
    "REINSTATED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SendingStatus) -> str:
    return value


def deserialize_json(data: str) -> SendingStatus:
    return cast(SendingStatus, data)
