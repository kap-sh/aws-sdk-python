"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.database_connection_method
    import aws_sdk_ssm_sap.types.ssm_sap_arn


class DatabaseConnection(TypedDict, closed=True):
    database_connection_method: NotRequired[
        "aws_sdk_ssm_sap.types.database_connection_method.DatabaseConnectionMethod"
    ]
    """<p>The method of connection.</p>"""
    database_arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name of the connected SAP HANA database.</p>"""
    connection_ip: NotRequired["str"]
    """<p>The IP address for connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseConnection) -> dict:
    out: dict = {}
    if "database_connection_method" in value:
        import aws_sdk_ssm_sap.types.database_connection_method

        out["DatabaseConnectionMethod"] = (
            aws_sdk_ssm_sap.types.database_connection_method.serialize_json(
                value["database_connection_method"]
            )
        )
    if "database_arn" in value:
        out["DatabaseArn"] = value["database_arn"]
    if "connection_ip" in value:
        out["ConnectionIp"] = value["connection_ip"]
    return out


def deserialize_json(data: dict) -> DatabaseConnection:
    out: DatabaseConnection = {}  # type: ignore[typeddict-item]
    if "DatabaseConnectionMethod" in data:
        import aws_sdk_ssm_sap.types.database_connection_method

        out["database_connection_method"] = (
            aws_sdk_ssm_sap.types.database_connection_method.deserialize_json(
                data["DatabaseConnectionMethod"]
            )
        )
    if "DatabaseArn" in data:
        out["database_arn"] = data["DatabaseArn"]
    if "ConnectionIp" in data:
        out["connection_ip"] = data["ConnectionIp"]
    return out
