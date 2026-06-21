"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Priority``."""

from typing import Literal, TypeAlias, cast

"""<p>The priority level of a recommendation.</p> <p>Valid values include:</p> <ul> <li> <p> <code>High</code> </p> </li> <li> <p> <code>Medium</code> </p> </li> <li> <p> <code>Low</code> </p> </li> </ul>"""
Priority: TypeAlias = Literal[
    "High",
    "Medium",
    "Low",
]


# --- restJson1 ser/de ---
def serialize_json(value: Priority) -> str:
    return value


def deserialize_json(data: str) -> Priority:
    return cast(Priority, data)
