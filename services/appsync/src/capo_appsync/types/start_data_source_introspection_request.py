"""Generated from Smithy shape ``com.amazonaws.appsync#StartDataSourceIntrospectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.rds_data_api_config


class StartDataSourceIntrospectionRequest(TypedDict, closed=True):
    rds_data_api_config: NotRequired[
        "capo_appsync.types.rds_data_api_config.RdsDataApiConfig"
    ]
    """<p>The <code>rdsDataApiConfig</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceIntrospectionRequest) -> dict:
    out: dict = {}
    if "rds_data_api_config" in value:
        import capo_appsync.types.rds_data_api_config

        out["rdsDataApiConfig"] = capo_appsync.types.rds_data_api_config.serialize_json(
            value["rds_data_api_config"]
        )
    return out


def deserialize_json(data: dict) -> StartDataSourceIntrospectionRequest:
    out: StartDataSourceIntrospectionRequest = {}  # type: ignore[typeddict-item]
    if "rdsDataApiConfig" in data:
        import capo_appsync.types.rds_data_api_config

        out["rds_data_api_config"] = (
            capo_appsync.types.rds_data_api_config.deserialize_json(
                data["rdsDataApiConfig"]
            )
        )
    return out
