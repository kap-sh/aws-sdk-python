"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkSpecifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_specifier

TypedLinkSpecifierList: TypeAlias = list[
    "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkSpecifierList) -> list:
    import capo_clouddirectory.types.typed_link_specifier

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.typed_link_specifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> TypedLinkSpecifierList:
    import capo_clouddirectory.types.typed_link_specifier

    out: TypedLinkSpecifierList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(item)
        )
    return out
