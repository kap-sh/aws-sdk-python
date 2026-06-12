"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet_attribute_update

FacetAttributeUpdateList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.facet_attribute_update.FacetAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeUpdateList) -> list:
    import aws_sdk_clouddirectory.types.facet_attribute_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.facet_attribute_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FacetAttributeUpdateList:
    import aws_sdk_clouddirectory.types.facet_attribute_update

    out: FacetAttributeUpdateList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.facet_attribute_update.deserialize_json(item)
        )
    return out
