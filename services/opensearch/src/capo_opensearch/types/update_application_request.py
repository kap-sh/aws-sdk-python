"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.id


class UpdateApplicationRequest(TypedDict, closed=True):
    id: "capo_opensearch.types.id.Id"
    """<p>The unique identifier for the OpenSearch application to be updated.</p>"""
    data_sources: NotRequired["capo_opensearch.types.data_sources.DataSources"]
    """<p>The data sources to associate with the OpenSearch application.</p>"""
    app_configs: NotRequired["capo_opensearch.types.app_configs.AppConfigs"]
    """<p>The configuration settings to modify for the OpenSearch application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import capo_opensearch.types.data_sources

        out["dataSources"] = capo_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "app_configs" in value:
        import capo_opensearch.types.app_configs

        out["appConfigs"] = capo_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "dataSources" in data:
        import capo_opensearch.types.data_sources

        out["data_sources"] = capo_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "appConfigs" in data:
        import capo_opensearch.types.app_configs

        out["app_configs"] = capo_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    return out
