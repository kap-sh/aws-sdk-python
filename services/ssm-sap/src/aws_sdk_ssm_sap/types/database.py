"""Generated from Smithy shape ``com.amazonaws.ssmsap#Database``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_sap.types.application_credential_list
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.component_arn_list
    import aws_sdk_ssm_sap.types.component_id
    import aws_sdk_ssm_sap.types.database_id
    import aws_sdk_ssm_sap.types.database_status
    import aws_sdk_ssm_sap.types.database_type
    import aws_sdk_ssm_sap.types.ssm_sap_arn


class Database(TypedDict):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_id: NotRequired["aws_sdk_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    credentials: NotRequired[
        "aws_sdk_ssm_sap.types.application_credential_list.ApplicationCredentialList"
    ]
    """<p>The credentials of the database.</p>"""
    database_id: NotRequired["aws_sdk_ssm_sap.types.database_id.DatabaseId"]
    """<p>The ID of the SAP HANA database.</p>"""
    database_name: NotRequired["str"]
    """<p>The name of the database.</p>"""
    database_type: NotRequired["aws_sdk_ssm_sap.types.database_type.DatabaseType"]
    """<p>The type of the database.</p>"""
    arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""
    status: NotRequired["aws_sdk_ssm_sap.types.database_status.DatabaseStatus"]
    """<p>The status of the database.</p>"""
    primary_host: NotRequired["str"]
    """<p>The primary host of the database.</p>"""
    sql_port: NotRequired["int"]
    """<p>The SQL port of the database.</p>"""
    last_updated: NotRequired["datetime.datetime"]
    """<p>The time at which the database was last updated.</p>"""
    connected_component_arns: NotRequired[
        "aws_sdk_ssm_sap.types.component_arn_list.ComponentArnList"
    ]
    """<p>The Amazon Resource Names of the connected AWS Systems Manager for SAP components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Database) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "credentials" in value:
        import aws_sdk_ssm_sap.types.application_credential_list

        out["Credentials"] = (
            aws_sdk_ssm_sap.types.application_credential_list.serialize_json(
                value["credentials"]
            )
        )
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "database_type" in value:
        import aws_sdk_ssm_sap.types.database_type

        out["DatabaseType"] = aws_sdk_ssm_sap.types.database_type.serialize_json(
            value["database_type"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_ssm_sap.types.database_status

        out["Status"] = aws_sdk_ssm_sap.types.database_status.serialize_json(
            value["status"]
        )
    if "primary_host" in value:
        out["PrimaryHost"] = value["primary_host"]
    if "sql_port" in value:
        out["SQLPort"] = value["sql_port"]
    if "last_updated" in value:
        import aws_sdk_ssm_sap.types._prelude.timestamp

        out["LastUpdated"] = aws_sdk_ssm_sap.types._prelude.timestamp.serialize_json(
            value["last_updated"]
        )
    if "connected_component_arns" in value:
        import aws_sdk_ssm_sap.types.component_arn_list

        out["ConnectedComponentArns"] = (
            aws_sdk_ssm_sap.types.component_arn_list.serialize_json(
                value["connected_component_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    if "Credentials" in data:
        import aws_sdk_ssm_sap.types.application_credential_list

        out["credentials"] = (
            aws_sdk_ssm_sap.types.application_credential_list.deserialize_json(
                data["Credentials"]
            )
        )
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "DatabaseType" in data:
        import aws_sdk_ssm_sap.types.database_type

        out["database_type"] = aws_sdk_ssm_sap.types.database_type.deserialize_json(
            data["DatabaseType"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Status" in data:
        import aws_sdk_ssm_sap.types.database_status

        out["status"] = aws_sdk_ssm_sap.types.database_status.deserialize_json(
            data["Status"]
        )
    if "PrimaryHost" in data:
        out["primary_host"] = data["PrimaryHost"]
    if "SQLPort" in data:
        out["sql_port"] = data["SQLPort"]
    if "LastUpdated" in data:
        import aws_sdk_ssm_sap.types._prelude.timestamp

        out["last_updated"] = aws_sdk_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["LastUpdated"]
        )
    if "ConnectedComponentArns" in data:
        import aws_sdk_ssm_sap.types.component_arn_list

        out["connected_component_arns"] = (
            aws_sdk_ssm_sap.types.component_arn_list.deserialize_json(
                data["ConnectedComponentArns"]
            )
        )
    return out
