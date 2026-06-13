"""Generated from Smithy shape ``com.amazonaws.quicksight#SnowflakeParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authentication_type
    import aws_sdk_quicksight.types.database
    import aws_sdk_quicksight.types.database_access_control_role
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.o_auth_parameters
    import aws_sdk_quicksight.types.warehouse


class SnowflakeParameters(TypedDict):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>Host.</p>"""
    database: "aws_sdk_quicksight.types.database.Database"
    """<p>Database.</p>"""
    warehouse: "aws_sdk_quicksight.types.warehouse.Warehouse"
    """<p>Warehouse.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_quicksight.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.</p>"""
    database_access_control_role: NotRequired[
        "aws_sdk_quicksight.types.database_access_control_role.DatabaseAccessControlRole"
    ]
    """<p>The database access control role.</p>"""
    o_auth_parameters: NotRequired[
        "aws_sdk_quicksight.types.o_auth_parameters.OAuthParameters"
    ]
    """<p>An object that contains information needed to create a data source connection between an Quick Sight account and Snowflake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Database"] = value["database"]
    out["Warehouse"] = value["warehouse"]
    if "authentication_type" in value:
        import aws_sdk_quicksight.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_quicksight.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "database_access_control_role" in value:
        out["DatabaseAccessControlRole"] = value["database_access_control_role"]
    if "o_auth_parameters" in value:
        import aws_sdk_quicksight.types.o_auth_parameters

        out["OAuthParameters"] = (
            aws_sdk_quicksight.types.o_auth_parameters.serialize_json(
                value["o_auth_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnowflakeParameters:
    out: SnowflakeParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("SnowflakeParameters.host required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("SnowflakeParameters.database required")
    if "Warehouse" in data:
        out["warehouse"] = data["Warehouse"]
    else:
        raise DeserializationError("SnowflakeParameters.warehouse required")
    if "AuthenticationType" in data:
        import aws_sdk_quicksight.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_quicksight.types.authentication_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    if "DatabaseAccessControlRole" in data:
        out["database_access_control_role"] = data["DatabaseAccessControlRole"]
    if "OAuthParameters" in data:
        import aws_sdk_quicksight.types.o_auth_parameters

        out["o_auth_parameters"] = (
            aws_sdk_quicksight.types.o_auth_parameters.deserialize_json(
                data["OAuthParameters"]
            )
        )
    return out
