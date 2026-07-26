"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListScope``."""

from typing import Literal, TypeAlias, cast

"""<p>The suppression scope that determines which suppression list Amazon SES uses. Can be one of the following:</p> <ul> <li> <p> <code>TENANT</code> – Use the tenant's own suppression list.</p> </li> <li> <p> <code>ACCOUNT</code> – Use the account-level suppression list.</p> </li> </ul>"""
SuppressionListScope: TypeAlias = Literal[
    "ACCOUNT",
    "TENANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListScope) -> str:
    return value


def deserialize_json(data: str) -> SuppressionListScope:
    return cast(SuppressionListScope, data)
