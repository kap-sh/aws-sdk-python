"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AddTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.tag

AddTags: TypeAlias = list["capo_service_catalog.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTags) -> list:
    import capo_service_catalog.types.tag

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddTags:
    import capo_service_catalog.types.tag

    out: AddTags = []
    for item in data:
        out.append(capo_service_catalog.types.tag.deserialize_aws_json_1_1(item))
    return out
