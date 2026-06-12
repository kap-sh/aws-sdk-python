"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListImportAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The type of action to perform on the address. The following are possible values:</p> <ul> <li> <p>PUT: add the addresses to the suppression list.</p> </li> <li> <p>DELETE: remove the address from the suppression list.</p> </li> </ul>"""
SuppressionListImportAction: TypeAlias = Literal[
    "DELETE",
    "PUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "PUT",
    )
)


def serialize_json(value: SuppressionListImportAction) -> str:
    return value


def deserialize_json(data: str) -> SuppressionListImportAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SuppressionListImportAction value: {data!r}"
        )
    return cast(SuppressionListImportAction, data)
