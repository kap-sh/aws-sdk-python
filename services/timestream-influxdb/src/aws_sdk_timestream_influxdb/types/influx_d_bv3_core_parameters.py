"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InfluxDBv3CoreParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.data_fusion_runtime_type
    import aws_sdk_timestream_influxdb.types.duration
    import aws_sdk_timestream_influxdb.types.log_formats
    import aws_sdk_timestream_influxdb.types.percent_or_absolute_long


class InfluxDBv3CoreParameters(TypedDict, closed=True):
    query_file_limit: NotRequired["int"]
    """<p>Limits the number of Parquet files a query can access. If a query attempts to read more than this limit, InfluxDB 3 returns an error.</p> <p>Default: 432</p>"""
    query_log_size: NotRequired["int"]
    """<p>Defines the size of the query log. Up to this many queries remain in the log before older queries are evicted to make room for new ones.</p> <p>Default: 1000</p>"""
    log_filter: NotRequired["str"]
    """<p>Sets the filter directive for logs.</p>"""
    log_format: NotRequired["aws_sdk_timestream_influxdb.types.log_formats.LogFormats"]
    """<p>Defines the message format for logs.</p> <p>Default: full</p>"""
    data_fusion_num_threads: NotRequired["int"]
    """<p>Sets the maximum number of DataFusion runtime threads to use.</p>"""
    data_fusion_runtime_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.data_fusion_runtime_type.DataFusionRuntimeType"
    ]
    """<p>Specifies the DataFusion tokio runtime type.</p> <p>Default: multi-thread</p>"""
    data_fusion_runtime_disable_lifo_slot: NotRequired["bool"]
    """<p>Disables the LIFO slot of the DataFusion runtime.</p>"""
    data_fusion_runtime_event_interval: NotRequired["int"]
    """<p>Sets the number of scheduler ticks after which the scheduler of the DataFusion tokio runtime polls for external events–for example: timers, I/O.</p>"""
    data_fusion_runtime_global_queue_interval: NotRequired["int"]
    """<p>Sets the number of scheduler ticks after which the scheduler of the DataFusion runtime polls the global task queue.</p>"""
    data_fusion_runtime_max_blocking_threads: NotRequired["int"]
    """<p>Specifies the limit for additional threads spawned by the DataFusion runtime.</p>"""
    data_fusion_runtime_max_io_events_per_tick: NotRequired["int"]
    """<p>Configures the maximum number of events processed per tick by the tokio DataFusion runtime.</p>"""
    data_fusion_runtime_thread_keep_alive: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets a custom timeout for a thread in the blocking pool of the tokio DataFusion runtime.</p>"""
    data_fusion_runtime_thread_priority: NotRequired["int"]
    """<p>Sets the thread priority for tokio DataFusion runtime workers.</p> <p>Default: 10</p>"""
    data_fusion_max_parquet_fanout: NotRequired["int"]
    """<p>When multiple parquet files are required in a sorted way (deduplication for example), specifies the maximum fanout.</p> <p>Default: 1000</p>"""
    data_fusion_use_cached_parquet_loader: NotRequired["bool"]
    """<p>Uses a cached parquet loader when reading parquet files from the object store.</p>"""
    data_fusion_config: NotRequired["str"]
    """<p>Provides custom configuration to DataFusion as a comma-separated list of key:value pairs.</p>"""
    max_http_request_size: NotRequired["int"]
    """<p>Specifies the maximum size of HTTP requests.</p> <p>Default: 10485760</p>"""
    force_snapshot_mem_threshold: NotRequired[
        "aws_sdk_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the threshold for the internal memory buffer. Supports either a percentage (portion of available memory) or absolute value in MB–for example: 70% or 100</p> <p>Default: 70%</p>"""
    wal_snapshot_size: NotRequired["int"]
    """<p>Defines the number of WAL files to attempt to remove in a snapshot. This, multiplied by the interval, determines how often snapshots are taken.</p> <p>Default: 600</p>"""
    wal_max_write_buffer_size: NotRequired["int"]
    """<p>Specifies the maximum number of write requests that can be buffered before a flush must be executed and succeed.</p> <p>Default: 100000</p>"""
    snapshotted_wal_files_to_keep: NotRequired["int"]
    """<p>Specifies the number of snapshotted WAL files to retain in the object store. Flushing the WAL files does not clear the WAL files immediately; they are deleted when the number of snapshotted WAL files exceeds this number.</p> <p>Default: 300</p>"""
    preemptive_cache_age: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to prefetch into the Parquet cache during compaction.</p> <p>Default: 3d</p>"""
    parquet_mem_cache_prune_percentage: NotRequired["float"]
    """<p>Specifies the percentage of entries to prune during a prune operation on the in-memory Parquet cache.</p> <p>Default: 0.1</p>"""
    parquet_mem_cache_prune_interval: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets the interval to check if the in-memory Parquet cache needs to be pruned.</p> <p>Default: 1s</p>"""
    disable_parquet_mem_cache: NotRequired["bool"]
    """<p>Disables the in-memory Parquet cache. By default, the cache is enabled.</p>"""
    parquet_mem_cache_query_path_duration: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the time window for caching recent Parquet files in memory.</p> <p>Default: 5h</p>"""
    last_cache_eviction_interval: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to evict expired entries from the Last-N-Value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.</p> <p>Default: 10s</p>"""
    distinct_cache_eviction_interval: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to evict expired entries from the distinct value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.</p> <p>Default: 10s</p>"""
    gen1_duration: NotRequired["aws_sdk_timestream_influxdb.types.duration.Duration"]
    """<p>Specifies the duration that Parquet files are arranged into. Data timestamps land each row into a file of this duration. Supported durations are 1m, 5m, and 10m. These files are known as “generation 1” files that the compactor in InfluxDB 3 Enterprise can merge into larger generations.</p> <p>Default: 10m</p>"""
    exec_mem_pool_bytes: NotRequired[
        "aws_sdk_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the size of memory pool used during query execution. Can be given as absolute value in bytes or as a percentage of the total available memory–for example: 8000000000 or 10%.</p> <p>Default: 20%</p>"""
    parquet_mem_cache_size: NotRequired[
        "aws_sdk_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the size of the in-memory Parquet cache in megabytes or percentage of total available memory.</p> <p>Default: 20%</p>"""
    wal_replay_fail_on_error: NotRequired["bool"]
    """<p>Determines whether WAL replay should fail when encountering errors.</p> <p>Default: false</p>"""
    wal_replay_concurrency_limit: NotRequired["int"]
    """<p>Concurrency limit during WAL replay. Setting this number too high can lead to OOM. The default is dynamically determined.</p> <p>Default: max(num_cpus, 10)</p>"""
    table_index_cache_max_entries: NotRequired["int"]
    """<p>Specifies the maximum number of entries in the table index cache.</p> <p>Default: 1000</p>"""
    table_index_cache_concurrency_limit: NotRequired["int"]
    """<p>Limits the concurrency level for table index cache operations.</p> <p>Default: 8</p>"""
    gen1_lookback_duration: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies how far back to look when creating generation 1 Parquet files.</p> <p>Default: 24h</p>"""
    retention_check_interval: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>The interval at which retention policies are checked and enforced. Enter as a human-readable time–for example: 30m or 1h.</p> <p>Default: 30m</p>"""
    delete_grace_period: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the grace period before permanently deleting data.</p> <p>Default: 24h</p>"""
    hard_delete_default_duration: NotRequired[
        "aws_sdk_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets the default duration for hard deletion of data.</p> <p>Default: 90d</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InfluxDBv3CoreParameters) -> dict:
    out: dict = {}
    if "query_file_limit" in value:
        out["queryFileLimit"] = value["query_file_limit"]
    if "query_log_size" in value:
        out["queryLogSize"] = value["query_log_size"]
    if "log_filter" in value:
        out["logFilter"] = value["log_filter"]
    if "log_format" in value:
        import aws_sdk_timestream_influxdb.types.log_formats

        out["logFormat"] = (
            aws_sdk_timestream_influxdb.types.log_formats.serialize_aws_json_1_0(
                value["log_format"]
            )
        )
    if "data_fusion_num_threads" in value:
        out["dataFusionNumThreads"] = value["data_fusion_num_threads"]
    if "data_fusion_runtime_type" in value:
        import aws_sdk_timestream_influxdb.types.data_fusion_runtime_type

        out["dataFusionRuntimeType"] = (
            aws_sdk_timestream_influxdb.types.data_fusion_runtime_type.serialize_aws_json_1_0(
                value["data_fusion_runtime_type"]
            )
        )
    if "data_fusion_runtime_disable_lifo_slot" in value:
        out["dataFusionRuntimeDisableLifoSlot"] = value[
            "data_fusion_runtime_disable_lifo_slot"
        ]
    if "data_fusion_runtime_event_interval" in value:
        out["dataFusionRuntimeEventInterval"] = value[
            "data_fusion_runtime_event_interval"
        ]
    if "data_fusion_runtime_global_queue_interval" in value:
        out["dataFusionRuntimeGlobalQueueInterval"] = value[
            "data_fusion_runtime_global_queue_interval"
        ]
    if "data_fusion_runtime_max_blocking_threads" in value:
        out["dataFusionRuntimeMaxBlockingThreads"] = value[
            "data_fusion_runtime_max_blocking_threads"
        ]
    if "data_fusion_runtime_max_io_events_per_tick" in value:
        out["dataFusionRuntimeMaxIoEventsPerTick"] = value[
            "data_fusion_runtime_max_io_events_per_tick"
        ]
    if "data_fusion_runtime_thread_keep_alive" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["dataFusionRuntimeThreadKeepAlive"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["data_fusion_runtime_thread_keep_alive"]
            )
        )
    if "data_fusion_runtime_thread_priority" in value:
        out["dataFusionRuntimeThreadPriority"] = value[
            "data_fusion_runtime_thread_priority"
        ]
    if "data_fusion_max_parquet_fanout" in value:
        out["dataFusionMaxParquetFanout"] = value["data_fusion_max_parquet_fanout"]
    if "data_fusion_use_cached_parquet_loader" in value:
        out["dataFusionUseCachedParquetLoader"] = value[
            "data_fusion_use_cached_parquet_loader"
        ]
    if "data_fusion_config" in value:
        out["dataFusionConfig"] = value["data_fusion_config"]
    if "max_http_request_size" in value:
        out["maxHttpRequestSize"] = value["max_http_request_size"]
    if "force_snapshot_mem_threshold" in value:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["forceSnapshotMemThreshold"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["force_snapshot_mem_threshold"]
            )
        )
    if "wal_snapshot_size" in value:
        out["walSnapshotSize"] = value["wal_snapshot_size"]
    if "wal_max_write_buffer_size" in value:
        out["walMaxWriteBufferSize"] = value["wal_max_write_buffer_size"]
    if "snapshotted_wal_files_to_keep" in value:
        out["snapshottedWalFilesToKeep"] = value["snapshotted_wal_files_to_keep"]
    if "preemptive_cache_age" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["preemptiveCacheAge"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["preemptive_cache_age"]
            )
        )
    if "parquet_mem_cache_prune_percentage" in value:
        out["parquetMemCachePrunePercentage"] = value[
            "parquet_mem_cache_prune_percentage"
        ]
    if "parquet_mem_cache_prune_interval" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["parquetMemCachePruneInterval"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["parquet_mem_cache_prune_interval"]
            )
        )
    if "disable_parquet_mem_cache" in value:
        out["disableParquetMemCache"] = value["disable_parquet_mem_cache"]
    if "parquet_mem_cache_query_path_duration" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["parquetMemCacheQueryPathDuration"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["parquet_mem_cache_query_path_duration"]
            )
        )
    if "last_cache_eviction_interval" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["lastCacheEvictionInterval"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["last_cache_eviction_interval"]
            )
        )
    if "distinct_cache_eviction_interval" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["distinctCacheEvictionInterval"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["distinct_cache_eviction_interval"]
            )
        )
    if "gen1_duration" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["gen1Duration"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["gen1_duration"]
            )
        )
    if "exec_mem_pool_bytes" in value:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["execMemPoolBytes"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["exec_mem_pool_bytes"]
            )
        )
    if "parquet_mem_cache_size" in value:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["parquetMemCacheSize"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["parquet_mem_cache_size"]
            )
        )
    if "wal_replay_fail_on_error" in value:
        out["walReplayFailOnError"] = value["wal_replay_fail_on_error"]
    if "wal_replay_concurrency_limit" in value:
        out["walReplayConcurrencyLimit"] = value["wal_replay_concurrency_limit"]
    if "table_index_cache_max_entries" in value:
        out["tableIndexCacheMaxEntries"] = value["table_index_cache_max_entries"]
    if "table_index_cache_concurrency_limit" in value:
        out["tableIndexCacheConcurrencyLimit"] = value[
            "table_index_cache_concurrency_limit"
        ]
    if "gen1_lookback_duration" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["gen1LookbackDuration"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["gen1_lookback_duration"]
            )
        )
    if "retention_check_interval" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["retentionCheckInterval"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["retention_check_interval"]
            )
        )
    if "delete_grace_period" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["deleteGracePeriod"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["delete_grace_period"]
            )
        )
    if "hard_delete_default_duration" in value:
        import aws_sdk_timestream_influxdb.types.duration

        out["hardDeleteDefaultDuration"] = (
            aws_sdk_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["hard_delete_default_duration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InfluxDBv3CoreParameters:
    out: InfluxDBv3CoreParameters = {}  # type: ignore[typeddict-item]
    if "queryFileLimit" in data:
        out["query_file_limit"] = data["queryFileLimit"]
    if "queryLogSize" in data:
        out["query_log_size"] = data["queryLogSize"]
    if "logFilter" in data:
        out["log_filter"] = data["logFilter"]
    if "logFormat" in data:
        import aws_sdk_timestream_influxdb.types.log_formats

        out["log_format"] = (
            aws_sdk_timestream_influxdb.types.log_formats.deserialize_aws_json_1_0(
                data["logFormat"]
            )
        )
    if "dataFusionNumThreads" in data:
        out["data_fusion_num_threads"] = data["dataFusionNumThreads"]
    if "dataFusionRuntimeType" in data:
        import aws_sdk_timestream_influxdb.types.data_fusion_runtime_type

        out["data_fusion_runtime_type"] = (
            aws_sdk_timestream_influxdb.types.data_fusion_runtime_type.deserialize_aws_json_1_0(
                data["dataFusionRuntimeType"]
            )
        )
    if "dataFusionRuntimeDisableLifoSlot" in data:
        out["data_fusion_runtime_disable_lifo_slot"] = data[
            "dataFusionRuntimeDisableLifoSlot"
        ]
    if "dataFusionRuntimeEventInterval" in data:
        out["data_fusion_runtime_event_interval"] = data[
            "dataFusionRuntimeEventInterval"
        ]
    if "dataFusionRuntimeGlobalQueueInterval" in data:
        out["data_fusion_runtime_global_queue_interval"] = data[
            "dataFusionRuntimeGlobalQueueInterval"
        ]
    if "dataFusionRuntimeMaxBlockingThreads" in data:
        out["data_fusion_runtime_max_blocking_threads"] = data[
            "dataFusionRuntimeMaxBlockingThreads"
        ]
    if "dataFusionRuntimeMaxIoEventsPerTick" in data:
        out["data_fusion_runtime_max_io_events_per_tick"] = data[
            "dataFusionRuntimeMaxIoEventsPerTick"
        ]
    if "dataFusionRuntimeThreadKeepAlive" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["data_fusion_runtime_thread_keep_alive"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["dataFusionRuntimeThreadKeepAlive"]
            )
        )
    if "dataFusionRuntimeThreadPriority" in data:
        out["data_fusion_runtime_thread_priority"] = data[
            "dataFusionRuntimeThreadPriority"
        ]
    if "dataFusionMaxParquetFanout" in data:
        out["data_fusion_max_parquet_fanout"] = data["dataFusionMaxParquetFanout"]
    if "dataFusionUseCachedParquetLoader" in data:
        out["data_fusion_use_cached_parquet_loader"] = data[
            "dataFusionUseCachedParquetLoader"
        ]
    if "dataFusionConfig" in data:
        out["data_fusion_config"] = data["dataFusionConfig"]
    if "maxHttpRequestSize" in data:
        out["max_http_request_size"] = data["maxHttpRequestSize"]
    if "forceSnapshotMemThreshold" in data:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["force_snapshot_mem_threshold"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["forceSnapshotMemThreshold"]
            )
        )
    if "walSnapshotSize" in data:
        out["wal_snapshot_size"] = data["walSnapshotSize"]
    if "walMaxWriteBufferSize" in data:
        out["wal_max_write_buffer_size"] = data["walMaxWriteBufferSize"]
    if "snapshottedWalFilesToKeep" in data:
        out["snapshotted_wal_files_to_keep"] = data["snapshottedWalFilesToKeep"]
    if "preemptiveCacheAge" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["preemptive_cache_age"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["preemptiveCacheAge"]
            )
        )
    if "parquetMemCachePrunePercentage" in data:
        out["parquet_mem_cache_prune_percentage"] = data[
            "parquetMemCachePrunePercentage"
        ]
    if "parquetMemCachePruneInterval" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["parquet_mem_cache_prune_interval"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["parquetMemCachePruneInterval"]
            )
        )
    if "disableParquetMemCache" in data:
        out["disable_parquet_mem_cache"] = data["disableParquetMemCache"]
    if "parquetMemCacheQueryPathDuration" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["parquet_mem_cache_query_path_duration"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["parquetMemCacheQueryPathDuration"]
            )
        )
    if "lastCacheEvictionInterval" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["last_cache_eviction_interval"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["lastCacheEvictionInterval"]
            )
        )
    if "distinctCacheEvictionInterval" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["distinct_cache_eviction_interval"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["distinctCacheEvictionInterval"]
            )
        )
    if "gen1Duration" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["gen1_duration"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["gen1Duration"]
            )
        )
    if "execMemPoolBytes" in data:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["exec_mem_pool_bytes"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["execMemPoolBytes"]
            )
        )
    if "parquetMemCacheSize" in data:
        import aws_sdk_timestream_influxdb.types.percent_or_absolute_long

        out["parquet_mem_cache_size"] = (
            aws_sdk_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["parquetMemCacheSize"]
            )
        )
    if "walReplayFailOnError" in data:
        out["wal_replay_fail_on_error"] = data["walReplayFailOnError"]
    if "walReplayConcurrencyLimit" in data:
        out["wal_replay_concurrency_limit"] = data["walReplayConcurrencyLimit"]
    if "tableIndexCacheMaxEntries" in data:
        out["table_index_cache_max_entries"] = data["tableIndexCacheMaxEntries"]
    if "tableIndexCacheConcurrencyLimit" in data:
        out["table_index_cache_concurrency_limit"] = data[
            "tableIndexCacheConcurrencyLimit"
        ]
    if "gen1LookbackDuration" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["gen1_lookback_duration"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["gen1LookbackDuration"]
            )
        )
    if "retentionCheckInterval" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["retention_check_interval"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["retentionCheckInterval"]
            )
        )
    if "deleteGracePeriod" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["delete_grace_period"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["deleteGracePeriod"]
            )
        )
    if "hardDeleteDefaultDuration" in data:
        import aws_sdk_timestream_influxdb.types.duration

        out["hard_delete_default_duration"] = (
            aws_sdk_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["hardDeleteDefaultDuration"]
            )
        )
    return out
