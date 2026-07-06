"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetSchemaVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.schema_version_format
    import aws_sdk_iot_managed_integrations.types.schema_version_type
    import aws_sdk_iot_managed_integrations.types.schema_versioned_id


class GetSchemaVersionRequest(TypedDict, closed=True):
    type: "aws_sdk_iot_managed_integrations.types.schema_version_type.SchemaVersionType"
    """<p>The type of schema version.</p>"""
    schema_versioned_id: (
        "aws_sdk_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId"
    )
    """<p>Schema id with a version specified. If the version is missing, it defaults to latest version.</p>"""
    format: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat"
    ]
    """<p>The format of the schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaVersionRequest:
    out: GetSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    return out
