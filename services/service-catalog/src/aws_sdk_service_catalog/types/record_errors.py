"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.record_error

RecordErrors: TypeAlias = list["aws_sdk_service_catalog.types.record_error.RecordError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordErrors) -> list:
    import aws_sdk_service_catalog.types.record_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.record_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordErrors:
    import aws_sdk_service_catalog.types.record_error

    out: RecordErrors = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.record_error.deserialize_aws_json_1_1(item)
        )
    return out
