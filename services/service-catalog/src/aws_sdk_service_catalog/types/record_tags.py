"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.record_tag

RecordTags: TypeAlias = list["aws_sdk_service_catalog.types.record_tag.RecordTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordTags) -> list:
    import aws_sdk_service_catalog.types.record_tag

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.record_tag.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordTags:
    import aws_sdk_service_catalog.types.record_tag

    out: RecordTags = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.record_tag.deserialize_aws_json_1_1(item)
        )
    return out
