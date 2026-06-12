"""Generated from Smithy shape ``com.amazonaws.appsync#StartDataSourceIntrospectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.rds_data_api_config


class StartDataSourceIntrospectionRequest(TypedDict):
    rds_data_api_config: NotRequired[
        "aws_sdk_appsync.types.rds_data_api_config.RdsDataApiConfig"
    ]
    """<p>The <code>rdsDataApiConfig</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceIntrospectionRequest) -> dict:
    out: dict = {}
    if "rds_data_api_config" in value:
        import aws_sdk_appsync.types.rds_data_api_config

        out["rdsDataApiConfig"] = (
            aws_sdk_appsync.types.rds_data_api_config.serialize_json(
                value["rds_data_api_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartDataSourceIntrospectionRequest:
    out: StartDataSourceIntrospectionRequest = {}  # type: ignore[typeddict-item]
    if "rdsDataApiConfig" in data:
        import aws_sdk_appsync.types.rds_data_api_config

        out["rds_data_api_config"] = (
            aws_sdk_appsync.types.rds_data_api_config.deserialize_json(
                data["rdsDataApiConfig"]
            )
        )
    return out
