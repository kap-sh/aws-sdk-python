"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListImportAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of action to perform on the address. The following are possible values:</p> <ul> <li> <p>PUT: add the addresses to the suppression list.</p> </li> <li> <p>DELETE: remove the address from the suppression list.</p> </li> </ul>"""
SuppressionListImportAction: TypeAlias = Literal[
    "DELETE",
    "PUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListImportAction) -> str:
    return value


def deserialize_json(data: str) -> SuppressionListImportAction:
    return cast(SuppressionListImportAction, data)
