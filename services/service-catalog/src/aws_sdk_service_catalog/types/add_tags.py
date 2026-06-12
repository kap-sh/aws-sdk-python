"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AddTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag

AddTags: TypeAlias = list["aws_sdk_service_catalog.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTags) -> list:
    import aws_sdk_service_catalog.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_service_catalog.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddTags:
    import aws_sdk_service_catalog.types.tag

    out: AddTags = []
    for item in data:
        out.append(aws_sdk_service_catalog.types.tag.deserialize_aws_json_1_1(item))
    return out
