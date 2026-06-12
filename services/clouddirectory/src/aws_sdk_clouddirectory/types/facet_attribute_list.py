"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet_attribute

FacetAttributeList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.facet_attribute.FacetAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeList) -> list:
    import aws_sdk_clouddirectory.types.facet_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_clouddirectory.types.facet_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> FacetAttributeList:
    import aws_sdk_clouddirectory.types.facet_attribute

    out: FacetAttributeList = []
    for item in data:
        out.append(aws_sdk_clouddirectory.types.facet_attribute.deserialize_json(item))
    return out
