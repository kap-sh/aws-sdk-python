"""Generated from Smithy shape ``com.amazonaws.macie2#Pages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.page

Pages: TypeAlias = list["capo_macie2.types.page.Page"]


# --- restJson1 ser/de ---
def serialize_json(value: Pages) -> list:
    import capo_macie2.types.page

    out: list = []
    for item in value:
        out.append(capo_macie2.types.page.serialize_json(item))
    return out


def deserialize_json(data: list) -> Pages:
    import capo_macie2.types.page

    out: Pages = []
    for item in data:
        out.append(capo_macie2.types.page.deserialize_json(item))
    return out
