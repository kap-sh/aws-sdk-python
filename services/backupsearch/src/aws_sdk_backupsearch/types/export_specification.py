"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportSpecification``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_backupsearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.s3_export_specification


class _ExportSpecification_s3ExportSpecification(TypedDict):
    s3ExportSpecification: (
        "aws_sdk_backupsearch.types.s3_export_specification.S3ExportSpecification"
    )


ExportSpecification: TypeAlias = _ExportSpecification_s3ExportSpecification


# --- restJson1 ser/de ---
def serialize_json(value: ExportSpecification) -> dict:
    if "s3ExportSpecification" in value:
        import aws_sdk_backupsearch.types.s3_export_specification

        return {
            "s3ExportSpecification": aws_sdk_backupsearch.types.s3_export_specification.serialize_json(
                value["s3ExportSpecification"]
            )
        }
    else:
        raise SerializationError("ExportSpecification: no variant present")


def deserialize_json(data: dict) -> ExportSpecification:
    if "s3ExportSpecification" in data:
        import aws_sdk_backupsearch.types.s3_export_specification

        return {
            "s3ExportSpecification": aws_sdk_backupsearch.types.s3_export_specification.deserialize_json(
                data["s3ExportSpecification"]
            )
        }
    else:
        raise DeserializationError("ExportSpecification: no recognized variant key")
