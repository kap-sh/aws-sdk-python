"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.record_detail

RecordDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.record_detail.RecordDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordDetails) -> list:
    import aws_sdk_service_catalog.types.record_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.record_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordDetails:
    import aws_sdk_service_catalog.types.record_detail

    out: RecordDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.record_detail.deserialize_aws_json_1_1(item)
        )
    return out
