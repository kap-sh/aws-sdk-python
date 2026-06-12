"""Generated from Smithy shape ``com.amazonaws.appfabric#AuditLogProcessingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.format
    import aws_sdk_appfabric.types.schema


class AuditLogProcessingConfiguration(TypedDict):
    schema: "aws_sdk_appfabric.types.schema.Schema"
    """<p>The event schema in which the audit logs need to be formatted.</p>"""
    format: "aws_sdk_appfabric.types.format.Format"
    """<p>The format in which the audit logs need to be formatted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditLogProcessingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.schema

    out["schema"] = aws_sdk_appfabric.types.schema.serialize_json(value["schema"])
    import aws_sdk_appfabric.types.format

    out["format"] = aws_sdk_appfabric.types.format.serialize_json(value["format"])
    return out


def deserialize_json(data: dict) -> AuditLogProcessingConfiguration:
    out: AuditLogProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_appfabric.types.schema

        out["schema"] = aws_sdk_appfabric.types.schema.deserialize_json(data["schema"])
    else:
        raise DeserializationError("AuditLogProcessingConfiguration.schema required")
    if "format" in data:
        import aws_sdk_appfabric.types.format

        out["format"] = aws_sdk_appfabric.types.format.deserialize_json(data["format"])
    else:
        raise DeserializationError("AuditLogProcessingConfiguration.format required")
    return out
