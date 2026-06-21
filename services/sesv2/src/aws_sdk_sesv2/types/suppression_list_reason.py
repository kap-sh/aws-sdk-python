"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason that the address was added to the suppression list for your account or for a specific tenant. The value can be one of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES added an email address to the suppression list for your account or for a specific tenant because a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES added an email address to the suppression list for your account or for a specific tenant because a message sent to that address results in a hard bounce.</p> </li> </ul>"""
SuppressionListReason: TypeAlias = Literal[
    "BOUNCE",
    "COMPLAINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListReason) -> str:
    return value


def deserialize_json(data: str) -> SuppressionListReason:
    return cast(SuppressionListReason, data)
