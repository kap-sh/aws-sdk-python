"""Generated from Smithy shape ``com.amazonaws.appsync#RelationalDatabaseDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.rds_http_endpoint_config
    import capo_appsync.types.relational_database_source_type


class RelationalDatabaseDataSourceConfig(TypedDict, closed=True):
    relational_database_source_type: NotRequired[
        "capo_appsync.types.relational_database_source_type.RelationalDatabaseSourceType"
    ]
    """<p>Source type for the relational database.</p> <ul> <li> <p> <b>RDS_HTTP_ENDPOINT</b>: The relational database source type is an Amazon Relational Database Service (Amazon RDS) HTTP endpoint.</p> </li> </ul>"""
    rds_http_endpoint_config: NotRequired[
        "capo_appsync.types.rds_http_endpoint_config.RdsHttpEndpointConfig"
    ]
    """<p>Amazon RDS HTTP endpoint settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationalDatabaseDataSourceConfig) -> dict:
    out: dict = {}
    if "relational_database_source_type" in value:
        import capo_appsync.types.relational_database_source_type

        out["relationalDatabaseSourceType"] = (
            capo_appsync.types.relational_database_source_type.serialize_json(
                value["relational_database_source_type"]
            )
        )
    if "rds_http_endpoint_config" in value:
        import capo_appsync.types.rds_http_endpoint_config

        out["rdsHttpEndpointConfig"] = (
            capo_appsync.types.rds_http_endpoint_config.serialize_json(
                value["rds_http_endpoint_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RelationalDatabaseDataSourceConfig:
    out: RelationalDatabaseDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseSourceType" in data:
        import capo_appsync.types.relational_database_source_type

        out["relational_database_source_type"] = (
            capo_appsync.types.relational_database_source_type.deserialize_json(
                data["relationalDatabaseSourceType"]
            )
        )
    if "rdsHttpEndpointConfig" in data:
        import capo_appsync.types.rds_http_endpoint_config

        out["rds_http_endpoint_config"] = (
            capo_appsync.types.rds_http_endpoint_config.deserialize_json(
                data["rdsHttpEndpointConfig"]
            )
        )
    return out
