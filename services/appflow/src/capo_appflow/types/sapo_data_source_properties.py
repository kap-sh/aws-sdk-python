"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.object
    import capo_appflow.types.sapo_data_pagination_config
    import capo_appflow.types.sapo_data_parallelism_config


class SAPODataSourceProperties(TypedDict, closed=True):
    object_path: NotRequired["capo_appflow.types.object.Object"]
    """<p> The object path specified in the SAPOData flow source. </p>"""
    parallelism_config: NotRequired[
        "capo_appflow.types.sapo_data_parallelism_config.SAPODataParallelismConfig"
    ]
    """<p>Sets the number of concurrent processes that transfers OData records from your SAP instance.</p>"""
    pagination_config: NotRequired[
        "capo_appflow.types.sapo_data_pagination_config.SAPODataPaginationConfig"
    ]
    """<p>Sets the page size for each concurrent process that transfers OData records from your SAP instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataSourceProperties) -> dict:
    out: dict = {}
    if "object_path" in value:
        out["objectPath"] = value["object_path"]
    if "parallelism_config" in value:
        import capo_appflow.types.sapo_data_parallelism_config

        out["parallelismConfig"] = (
            capo_appflow.types.sapo_data_parallelism_config.serialize_json(
                value["parallelism_config"]
            )
        )
    if "pagination_config" in value:
        import capo_appflow.types.sapo_data_pagination_config

        out["paginationConfig"] = (
            capo_appflow.types.sapo_data_pagination_config.serialize_json(
                value["pagination_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SAPODataSourceProperties:
    out: SAPODataSourceProperties = {}  # type: ignore[typeddict-item]
    if "objectPath" in data:
        out["object_path"] = data["objectPath"]
    if "parallelismConfig" in data:
        import capo_appflow.types.sapo_data_parallelism_config

        out["parallelism_config"] = (
            capo_appflow.types.sapo_data_parallelism_config.deserialize_json(
                data["parallelismConfig"]
            )
        )
    if "paginationConfig" in data:
        import capo_appflow.types.sapo_data_pagination_config

        out["pagination_config"] = (
            capo_appflow.types.sapo_data_pagination_config.deserialize_json(
                data["paginationConfig"]
            )
        )
    return out
