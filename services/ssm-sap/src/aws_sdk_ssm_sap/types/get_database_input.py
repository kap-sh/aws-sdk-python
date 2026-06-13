"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetDatabaseInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.component_id
    import aws_sdk_ssm_sap.types.database_id
    import aws_sdk_ssm_sap.types.ssm_sap_arn


class GetDatabaseInput(TypedDict):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_id: NotRequired["aws_sdk_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    database_id: NotRequired["aws_sdk_ssm_sap.types.database_id.DatabaseId"]
    """<p>The ID of the database.</p>"""
    database_arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatabaseInput) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_arn" in value:
        out["DatabaseArn"] = value["database_arn"]
    return out


def deserialize_json(data: dict) -> GetDatabaseInput:
    out: GetDatabaseInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseArn" in data:
        out["database_arn"] = data["DatabaseArn"]
    return out
