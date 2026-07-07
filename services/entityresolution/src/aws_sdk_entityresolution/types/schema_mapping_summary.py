"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaMappingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.schema_mapping_arn


class SchemaMappingSummary(TypedDict, closed=True):
    schema_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema.</p>"""
    schema_arn: "aws_sdk_entityresolution.types.schema_mapping_arn.SchemaMappingArn"
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>SchemaMapping</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was last updated.</p>"""
    has_workflows: "bool"
    """<p>Specifies whether the schema mapping has been applied to a workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaMappingSummary) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    out["schemaArn"] = value["schema_arn"]
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["createdAt"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    out["hasWorkflows"] = value["has_workflows"]
    return out


def deserialize_json(data: dict) -> SchemaMappingSummary:
    out: SchemaMappingSummary = {}  # type: ignore[typeddict-item]
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    else:
        raise DeserializationError("SchemaMappingSummary.schema_name required")
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    else:
        raise DeserializationError("SchemaMappingSummary.schema_arn required")
    if "createdAt" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SchemaMappingSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("SchemaMappingSummary.updated_at required")
    if "hasWorkflows" in data:
        out["has_workflows"] = data["hasWorkflows"]
    else:
        raise DeserializationError("SchemaMappingSummary.has_workflows required")
    return out
