"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableRecordExpirationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_record_expiration_configuration_value


class PutTableRecordExpirationConfigurationRequest(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    value: "capo_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue"
    """<p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableRecordExpirationConfigurationRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_record_expiration_configuration_value

    out["value"] = (
        capo_s3tables.types.table_record_expiration_configuration_value.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableRecordExpirationConfigurationRequest:
    out: PutTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_s3tables.types.table_record_expiration_configuration_value

        out["value"] = (
            capo_s3tables.types.table_record_expiration_configuration_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableRecordExpirationConfigurationRequest.value required"
        )
    return out
