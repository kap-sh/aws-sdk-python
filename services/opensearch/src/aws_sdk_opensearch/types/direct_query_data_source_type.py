"""Generated from Smithy shape ``com.amazonaws.opensearch#DirectQueryDataSourceType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.cloud_watch_direct_query_data_source
    import aws_sdk_opensearch.types.prometheus_direct_query_data_source
    import aws_sdk_opensearch.types.security_lake_direct_query_data_source


class _DirectQueryDataSourceType_CloudWatchLog(TypedDict, closed=True):
    CloudWatchLog: "aws_sdk_opensearch.types.cloud_watch_direct_query_data_source.CloudWatchDirectQueryDataSource"


class _DirectQueryDataSourceType_SecurityLake(TypedDict, closed=True):
    SecurityLake: "aws_sdk_opensearch.types.security_lake_direct_query_data_source.SecurityLakeDirectQueryDataSource"


class _DirectQueryDataSourceType_Prometheus(TypedDict, closed=True):
    Prometheus: "aws_sdk_opensearch.types.prometheus_direct_query_data_source.PrometheusDirectQueryDataSource"


DirectQueryDataSourceType: TypeAlias = (
    _DirectQueryDataSourceType_CloudWatchLog
    | _DirectQueryDataSourceType_SecurityLake
    | _DirectQueryDataSourceType_Prometheus
)


# --- restJson1 ser/de ---
def serialize_json(value: DirectQueryDataSourceType) -> dict:
    if "CloudWatchLog" in value:
        import aws_sdk_opensearch.types.cloud_watch_direct_query_data_source

        return {
            "CloudWatchLog": aws_sdk_opensearch.types.cloud_watch_direct_query_data_source.serialize_json(
                value["CloudWatchLog"]
            )
        }
    elif "SecurityLake" in value:
        import aws_sdk_opensearch.types.security_lake_direct_query_data_source

        return {
            "SecurityLake": aws_sdk_opensearch.types.security_lake_direct_query_data_source.serialize_json(
                value["SecurityLake"]
            )
        }
    elif "Prometheus" in value:
        import aws_sdk_opensearch.types.prometheus_direct_query_data_source

        return {
            "Prometheus": aws_sdk_opensearch.types.prometheus_direct_query_data_source.serialize_json(
                value["Prometheus"]
            )
        }
    else:
        raise SerializationError("DirectQueryDataSourceType: no variant present")


def deserialize_json(data: dict) -> DirectQueryDataSourceType:
    if "CloudWatchLog" in data:
        import aws_sdk_opensearch.types.cloud_watch_direct_query_data_source

        return {
            "CloudWatchLog": aws_sdk_opensearch.types.cloud_watch_direct_query_data_source.deserialize_json(
                data["CloudWatchLog"]
            )
        }
    elif "SecurityLake" in data:
        import aws_sdk_opensearch.types.security_lake_direct_query_data_source

        return {
            "SecurityLake": aws_sdk_opensearch.types.security_lake_direct_query_data_source.deserialize_json(
                data["SecurityLake"]
            )
        }
    elif "Prometheus" in data:
        import aws_sdk_opensearch.types.prometheus_direct_query_data_source

        return {
            "Prometheus": aws_sdk_opensearch.types.prometheus_direct_query_data_source.deserialize_json(
                data["Prometheus"]
            )
        }
    else:
        raise DeserializationError(
            "DirectQueryDataSourceType: no recognized variant key"
        )
