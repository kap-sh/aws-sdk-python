"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchClusterConfigStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config
    import aws_sdk_elasticsearch_service.types.option_status


class ElasticsearchClusterConfigStatus(TypedDict, closed=True):
    options: "aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
    """<p> Specifies the cluster configuration for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the configuration for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchClusterConfigStatus) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config

    out["Options"] = (
        aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.serialize_json(
            value["options"]
        )
    )
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ElasticsearchClusterConfigStatus:
    out: ElasticsearchClusterConfigStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config

        out["options"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("ElasticsearchClusterConfigStatus.options required")
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ElasticsearchClusterConfigStatus.status required")
    return out
