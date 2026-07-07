"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableRecordExpirationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_record_expiration_configuration_value


class GetTableRecordExpirationConfigurationResponse(TypedDict, closed=True):
    configuration: "aws_sdk_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue"
    """<p>The record expiration configuration for the table, including the status and retention settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableRecordExpirationConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.table_record_expiration_configuration_value

    out["configuration"] = (
        aws_sdk_s3tables.types.table_record_expiration_configuration_value.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableRecordExpirationConfigurationResponse:
    out: GetTableRecordExpirationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_s3tables.types.table_record_expiration_configuration_value

        out["configuration"] = (
            aws_sdk_s3tables.types.table_record_expiration_configuration_value.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableRecordExpirationConfigurationResponse.configuration required"
        )
    return out
