"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationConfigurationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_record_expiration_settings
    import aws_sdk_s3tables.types.table_record_expiration_status


class TableRecordExpirationConfigurationValue(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_s3tables.types.table_record_expiration_status.TableRecordExpirationStatus"
    ]
    """<p>The status of the expiration settings for records in the table.</p>"""
    settings: NotRequired[
        "aws_sdk_s3tables.types.table_record_expiration_settings.TableRecordExpirationSettings"
    ]
    """<p>The expiration settings for records in the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableRecordExpirationConfigurationValue) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_s3tables.types.table_record_expiration_status

        out["status"] = (
            aws_sdk_s3tables.types.table_record_expiration_status.serialize_json(
                value["status"]
            )
        )
    if "settings" in value:
        import aws_sdk_s3tables.types.table_record_expiration_settings

        out["settings"] = (
            aws_sdk_s3tables.types.table_record_expiration_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableRecordExpirationConfigurationValue:
    out: TableRecordExpirationConfigurationValue = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_s3tables.types.table_record_expiration_status

        out["status"] = (
            aws_sdk_s3tables.types.table_record_expiration_status.deserialize_json(
                data["status"]
            )
        )
    if "settings" in data:
        import aws_sdk_s3tables.types.table_record_expiration_settings

        out["settings"] = (
            aws_sdk_s3tables.types.table_record_expiration_settings.deserialize_json(
                data["settings"]
            )
        )
    return out
