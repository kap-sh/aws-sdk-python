"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.app_configs
    import aws_sdk_opensearch.types.data_sources
    import aws_sdk_opensearch.types.id


class UpdateApplicationRequest(TypedDict):
    id: "aws_sdk_opensearch.types.id.Id"
    """<p>The unique identifier for the OpenSearch application to be updated.</p>"""
    data_sources: NotRequired["aws_sdk_opensearch.types.data_sources.DataSources"]
    """<p>The data sources to associate with the OpenSearch application.</p>"""
    app_configs: NotRequired["aws_sdk_opensearch.types.app_configs.AppConfigs"]
    """<p>The configuration settings to modify for the OpenSearch application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import aws_sdk_opensearch.types.data_sources

        out["dataSources"] = aws_sdk_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "app_configs" in value:
        import aws_sdk_opensearch.types.app_configs

        out["appConfigs"] = aws_sdk_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "dataSources" in data:
        import aws_sdk_opensearch.types.data_sources

        out["data_sources"] = aws_sdk_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "appConfigs" in data:
        import aws_sdk_opensearch.types.app_configs

        out["app_configs"] = aws_sdk_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    return out
