"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeNameAndValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name_and_value

AttributeNameAndValueList: TypeAlias = list[
    "capo_clouddirectory.types.attribute_name_and_value.AttributeNameAndValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameAndValueList) -> list:
    import capo_clouddirectory.types.attribute_name_and_value

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.attribute_name_and_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttributeNameAndValueList:
    import capo_clouddirectory.types.attribute_name_and_value

    out: AttributeNameAndValueList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.attribute_name_and_value.deserialize_json(item)
        )
    return out
