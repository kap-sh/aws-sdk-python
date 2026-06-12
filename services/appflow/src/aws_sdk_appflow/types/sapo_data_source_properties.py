"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object
    import aws_sdk_appflow.types.sapo_data_pagination_config
    import aws_sdk_appflow.types.sapo_data_parallelism_config


class SAPODataSourceProperties(TypedDict):
    object_path: NotRequired["aws_sdk_appflow.types.object.Object"]
    """<p> The object path specified in the SAPOData flow source. </p>"""
    parallelism_config: NotRequired[
        "aws_sdk_appflow.types.sapo_data_parallelism_config.SAPODataParallelismConfig"
    ]
    """<p>Sets the number of concurrent processes that transfers OData records from your SAP instance.</p>"""
    pagination_config: NotRequired[
        "aws_sdk_appflow.types.sapo_data_pagination_config.SAPODataPaginationConfig"
    ]
    """<p>Sets the page size for each concurrent process that transfers OData records from your SAP instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataSourceProperties) -> dict:
    out: dict = {}
    if "object_path" in value:
        out["objectPath"] = value["object_path"]
    if "parallelism_config" in value:
        import aws_sdk_appflow.types.sapo_data_parallelism_config

        out["parallelismConfig"] = (
            aws_sdk_appflow.types.sapo_data_parallelism_config.serialize_json(
                value["parallelism_config"]
            )
        )
    if "pagination_config" in value:
        import aws_sdk_appflow.types.sapo_data_pagination_config

        out["paginationConfig"] = (
            aws_sdk_appflow.types.sapo_data_pagination_config.serialize_json(
                value["pagination_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SAPODataSourceProperties:
    out: SAPODataSourceProperties = {}  # type: ignore[typeddict-item]
    if "objectPath" in data:
        out["object_path"] = data["objectPath"]
    if "parallelismConfig" in data:
        import aws_sdk_appflow.types.sapo_data_parallelism_config

        out["parallelism_config"] = (
            aws_sdk_appflow.types.sapo_data_parallelism_config.deserialize_json(
                data["parallelismConfig"]
            )
        )
    if "paginationConfig" in data:
        import aws_sdk_appflow.types.sapo_data_pagination_config

        out["pagination_config"] = (
            aws_sdk_appflow.types.sapo_data_pagination_config.deserialize_json(
                data["paginationConfig"]
            )
        )
    return out
