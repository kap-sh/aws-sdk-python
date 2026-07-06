"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetSchemaVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.schema_id
    import aws_sdk_iot_managed_integrations.types.schema_version_description
    import aws_sdk_iot_managed_integrations.types.schema_version_namespace_name
    import aws_sdk_iot_managed_integrations.types.schema_version_schema
    import aws_sdk_iot_managed_integrations.types.schema_version_type
    import aws_sdk_iot_managed_integrations.types.schema_version_version
    import aws_sdk_iot_managed_integrations.types.schema_version_visibility


class GetSchemaVersionResponse(TypedDict, closed=True):
    schema_id: NotRequired["aws_sdk_iot_managed_integrations.types.schema_id.SchemaId"]
    """<p>The id of the schema version.</p>"""
    type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_type.SchemaVersionType"
    ]
    """<p>The type of schema version.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_description.SchemaVersionDescription"
    ]
    """<p>The description of the schema version.</p>"""
    namespace: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
    ]
    """<p>The name of the schema version.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
    ]
    """<p>The schema version. If this is left blank, it defaults to the latest version.</p>"""
    visibility: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
    ]
    """<p>The visibility of the schema version.</p>"""
    schema: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_schema.SchemaVersionSchema"
    ]
    """<p>The schema of the schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaVersionResponse) -> dict:
    out: dict = {}
    if "schema_id" in value:
        out["SchemaId"] = value["schema_id"]
    if "type" in value:
        import aws_sdk_iot_managed_integrations.types.schema_version_type

        out["Type"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_type.serialize_json(
                value["type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "semantic_version" in value:
        out["SemanticVersion"] = value["semantic_version"]
    if "visibility" in value:
        import aws_sdk_iot_managed_integrations.types.schema_version_visibility

        out["Visibility"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_visibility.serialize_json(
                value["visibility"]
            )
        )
    if "schema" in value:
        out["Schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> GetSchemaVersionResponse:
    out: GetSchemaVersionResponse = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        out["schema_id"] = data["SchemaId"]
    if "Type" in data:
        import aws_sdk_iot_managed_integrations.types.schema_version_type

        out["type"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_type.deserialize_json(
                data["Type"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "SemanticVersion" in data:
        out["semantic_version"] = data["SemanticVersion"]
    if "Visibility" in data:
        import aws_sdk_iot_managed_integrations.types.schema_version_visibility

        out["visibility"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_visibility.deserialize_json(
                data["Visibility"]
            )
        )
    if "Schema" in data:
        out["schema"] = data["Schema"]
    return out
