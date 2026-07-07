"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.component_id
    import aws_sdk_ssm_sap.types.database_id
    import aws_sdk_ssm_sap.types.database_type
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.tag_map


class DatabaseSummary(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_id: NotRequired["aws_sdk_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    database_id: NotRequired["aws_sdk_ssm_sap.types.database_id.DatabaseId"]
    """<p>The ID of the database.</p>"""
    database_type: NotRequired["aws_sdk_ssm_sap.types.database_type.DatabaseType"]
    """<p>The type of the database.</p>"""
    arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""
    tags: NotRequired["aws_sdk_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_type" in value:
        import aws_sdk_ssm_sap.types.database_type

        out["DatabaseType"] = aws_sdk_ssm_sap.types.database_type.serialize_json(
            value["database_type"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_ssm_sap.types.tag_map

        out["Tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DatabaseSummary:
    out: DatabaseSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseType" in data:
        import aws_sdk_ssm_sap.types.database_type

        out["database_type"] = aws_sdk_ssm_sap.types.database_type.deserialize_json(
            data["DatabaseType"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
