"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectIdentifierAndLinkNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier_and_link_name_tuple

ObjectIdentifierAndLinkNameList: TypeAlias = list[
    "capo_clouddirectory.types.object_identifier_and_link_name_tuple.ObjectIdentifierAndLinkNameTuple"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectIdentifierAndLinkNameList) -> list:
    import capo_clouddirectory.types.object_identifier_and_link_name_tuple

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.object_identifier_and_link_name_tuple.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ObjectIdentifierAndLinkNameList:
    import capo_clouddirectory.types.object_identifier_and_link_name_tuple

    out: ObjectIdentifierAndLinkNameList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.object_identifier_and_link_name_tuple.deserialize_json(
                item
            )
        )
    return out
