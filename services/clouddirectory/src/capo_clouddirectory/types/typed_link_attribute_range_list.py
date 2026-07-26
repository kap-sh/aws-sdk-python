"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_attribute_range

TypedLinkAttributeRangeList: TypeAlias = list[
    "capo_clouddirectory.types.typed_link_attribute_range.TypedLinkAttributeRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeRangeList) -> list:
    import capo_clouddirectory.types.typed_link_attribute_range

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.typed_link_attribute_range.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TypedLinkAttributeRangeList:
    import capo_clouddirectory.types.typed_link_attribute_range

    out: TypedLinkAttributeRangeList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.typed_link_attribute_range.deserialize_json(item)
        )
    return out
