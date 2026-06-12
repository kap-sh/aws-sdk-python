"""Generated from Smithy shape ``com.amazonaws.memorydb#AmazonMemoryDB``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_memorydb._auth._identity import Credentials
from aws_sdk_memorydb._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_memorydb._auth._zapros_handler import AuthMiddleware
from aws_sdk_memorydb._pagination import resolve_path as _resolve_path
from aws_sdk_memorydb._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.access_string
    import aws_sdk_memorydb.types.acl
    import aws_sdk_memorydb.types.acl_name
    import aws_sdk_memorydb.types.authentication_mode
    import aws_sdk_memorydb.types.batch_update_cluster_request
    import aws_sdk_memorydb.types.batch_update_cluster_response
    import aws_sdk_memorydb.types.boolean
    import aws_sdk_memorydb.types.boolean_optional
    import aws_sdk_memorydb.types.cluster
    import aws_sdk_memorydb.types.cluster_name_list
    import aws_sdk_memorydb.types.copy_snapshot_request
    import aws_sdk_memorydb.types.copy_snapshot_response
    import aws_sdk_memorydb.types.create_acl_request
    import aws_sdk_memorydb.types.create_acl_response
    import aws_sdk_memorydb.types.create_cluster_request
    import aws_sdk_memorydb.types.create_cluster_response
    import aws_sdk_memorydb.types.create_multi_region_cluster_request
    import aws_sdk_memorydb.types.create_multi_region_cluster_response
    import aws_sdk_memorydb.types.create_parameter_group_request
    import aws_sdk_memorydb.types.create_parameter_group_response
    import aws_sdk_memorydb.types.create_snapshot_request
    import aws_sdk_memorydb.types.create_snapshot_response
    import aws_sdk_memorydb.types.create_subnet_group_request
    import aws_sdk_memorydb.types.create_subnet_group_response
    import aws_sdk_memorydb.types.create_user_request
    import aws_sdk_memorydb.types.create_user_response
    import aws_sdk_memorydb.types.delete_acl_request
    import aws_sdk_memorydb.types.delete_acl_response
    import aws_sdk_memorydb.types.delete_cluster_request
    import aws_sdk_memorydb.types.delete_cluster_response
    import aws_sdk_memorydb.types.delete_multi_region_cluster_request
    import aws_sdk_memorydb.types.delete_multi_region_cluster_response
    import aws_sdk_memorydb.types.delete_parameter_group_request
    import aws_sdk_memorydb.types.delete_parameter_group_response
    import aws_sdk_memorydb.types.delete_snapshot_request
    import aws_sdk_memorydb.types.delete_snapshot_response
    import aws_sdk_memorydb.types.delete_subnet_group_request
    import aws_sdk_memorydb.types.delete_subnet_group_response
    import aws_sdk_memorydb.types.delete_user_request
    import aws_sdk_memorydb.types.delete_user_response
    import aws_sdk_memorydb.types.describe_ac_ls_request
    import aws_sdk_memorydb.types.describe_ac_ls_response
    import aws_sdk_memorydb.types.describe_clusters_request
    import aws_sdk_memorydb.types.describe_clusters_response
    import aws_sdk_memorydb.types.describe_engine_versions_request
    import aws_sdk_memorydb.types.describe_engine_versions_response
    import aws_sdk_memorydb.types.describe_events_request
    import aws_sdk_memorydb.types.describe_events_response
    import aws_sdk_memorydb.types.describe_multi_region_clusters_request
    import aws_sdk_memorydb.types.describe_multi_region_clusters_response
    import aws_sdk_memorydb.types.describe_multi_region_parameter_groups_request
    import aws_sdk_memorydb.types.describe_multi_region_parameter_groups_response
    import aws_sdk_memorydb.types.describe_multi_region_parameters_request
    import aws_sdk_memorydb.types.describe_multi_region_parameters_response
    import aws_sdk_memorydb.types.describe_parameter_groups_request
    import aws_sdk_memorydb.types.describe_parameter_groups_response
    import aws_sdk_memorydb.types.describe_parameters_request
    import aws_sdk_memorydb.types.describe_parameters_response
    import aws_sdk_memorydb.types.describe_reserved_nodes_offerings_request
    import aws_sdk_memorydb.types.describe_reserved_nodes_offerings_response
    import aws_sdk_memorydb.types.describe_reserved_nodes_request
    import aws_sdk_memorydb.types.describe_reserved_nodes_response
    import aws_sdk_memorydb.types.describe_service_updates_request
    import aws_sdk_memorydb.types.describe_service_updates_response
    import aws_sdk_memorydb.types.describe_snapshots_request
    import aws_sdk_memorydb.types.describe_snapshots_response
    import aws_sdk_memorydb.types.describe_subnet_groups_request
    import aws_sdk_memorydb.types.describe_subnet_groups_response
    import aws_sdk_memorydb.types.describe_users_request
    import aws_sdk_memorydb.types.describe_users_response
    import aws_sdk_memorydb.types.engine_version_info
    import aws_sdk_memorydb.types.event
    import aws_sdk_memorydb.types.failover_shard_request
    import aws_sdk_memorydb.types.failover_shard_response
    import aws_sdk_memorydb.types.filter_list
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.ip_discovery
    import aws_sdk_memorydb.types.key_list
    import aws_sdk_memorydb.types.kms_key_id
    import aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_request
    import aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_response
    import aws_sdk_memorydb.types.list_allowed_node_type_updates_request
    import aws_sdk_memorydb.types.list_allowed_node_type_updates_response
    import aws_sdk_memorydb.types.list_tags_request
    import aws_sdk_memorydb.types.list_tags_response
    import aws_sdk_memorydb.types.multi_region_cluster
    import aws_sdk_memorydb.types.network_type
    import aws_sdk_memorydb.types.parameter
    import aws_sdk_memorydb.types.parameter_group
    import aws_sdk_memorydb.types.parameter_name_list
    import aws_sdk_memorydb.types.parameter_name_value_list
    import aws_sdk_memorydb.types.purchase_reserved_nodes_offering_request
    import aws_sdk_memorydb.types.purchase_reserved_nodes_offering_response
    import aws_sdk_memorydb.types.replica_configuration_request
    import aws_sdk_memorydb.types.reserved_node
    import aws_sdk_memorydb.types.reserved_nodes_offering
    import aws_sdk_memorydb.types.reset_parameter_group_request
    import aws_sdk_memorydb.types.reset_parameter_group_response
    import aws_sdk_memorydb.types.security_group_ids_list
    import aws_sdk_memorydb.types.service_update
    import aws_sdk_memorydb.types.service_update_request
    import aws_sdk_memorydb.types.service_update_status_list
    import aws_sdk_memorydb.types.shard_configuration_request
    import aws_sdk_memorydb.types.snapshot
    import aws_sdk_memorydb.types.snapshot_arns_list
    import aws_sdk_memorydb.types.source_type
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.subnet_group
    import aws_sdk_memorydb.types.subnet_identifier_list
    import aws_sdk_memorydb.types.t_stamp
    import aws_sdk_memorydb.types.tag_list
    import aws_sdk_memorydb.types.tag_resource_request
    import aws_sdk_memorydb.types.tag_resource_response
    import aws_sdk_memorydb.types.target_bucket
    import aws_sdk_memorydb.types.untag_resource_request
    import aws_sdk_memorydb.types.untag_resource_response
    import aws_sdk_memorydb.types.update_acl_request
    import aws_sdk_memorydb.types.update_acl_response
    import aws_sdk_memorydb.types.update_cluster_request
    import aws_sdk_memorydb.types.update_cluster_response
    import aws_sdk_memorydb.types.update_multi_region_cluster_request
    import aws_sdk_memorydb.types.update_multi_region_cluster_response
    import aws_sdk_memorydb.types.update_parameter_group_request
    import aws_sdk_memorydb.types.update_parameter_group_response
    import aws_sdk_memorydb.types.update_strategy
    import aws_sdk_memorydb.types.update_subnet_group_request
    import aws_sdk_memorydb.types.update_subnet_group_response
    import aws_sdk_memorydb.types.update_user_request
    import aws_sdk_memorydb.types.update_user_response
    import aws_sdk_memorydb.types.user
    import aws_sdk_memorydb.types.user_name
    import aws_sdk_memorydb.types.user_name_list_input


class AsyncMemoryDBClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncMemoryDBClient:
    """A client for the ``MemoryDB`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncMemoryDBClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncMemoryDBClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMemoryDBClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def batch_update_cluster(
        self,
        cluster_names: "aws_sdk_memorydb.types.cluster_name_list.ClusterNameList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update: Optional[
            "aws_sdk_memorydb.types.service_update_request.ServiceUpdateRequest"
        ] = None,
    ) -> "aws_sdk_memorydb.types.batch_update_cluster_response.BatchUpdateClusterResponse":
        """<p>Apply the service update to a list of clusters supplied. For more information on service updates and applying them, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/managing-updates.html#applying-updates\">Applying the service updates</a>.</p>

        Args:
            cluster_names: <p>The cluster names to apply the updates.</p>
            service_update: <p>The unique ID of the service update</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.batch_update_cluster_request.BatchUpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.batch_update_cluster_response.BatchUpdateClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.batch_update_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.batch_update_cluster.async_batch_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.batch_update_cluster_request.BatchUpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input["cluster_names"] = cluster_names
        if service_update is not None:
            input["service_update"] = service_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def copy_snapshot(
        self,
        source_snapshot_name: "aws_sdk_memorydb.types.string.String",
        target_snapshot_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        target_bucket: Optional[
            "aws_sdk_memorydb.types.target_bucket.TargetBucket"
        ] = None,
        kms_key_id: Optional["aws_sdk_memorydb.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.copy_snapshot_response.CopySnapshotResponse":
        """<p>Makes a copy of an existing snapshot.</p>

        Args:
            source_snapshot_name: <p>The name of an existing snapshot from which to make a copy.</p>
            target_snapshot_name: <p>A name for the snapshot copy. MemoryDB does not permit overwriting a snapshot, therefore this name must be unique within its context - MemoryDB or an Amazon S3 bucket if exporting.</p>
            target_bucket: <p>The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access. When using this parameter to export a snapshot, be sure MemoryDB has the needed permissions to this S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/snapshots-exporting.html\">Step 2: Grant MemoryDB Access to Your Amazon S3 Bucket</a>. </p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the target snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.copy_snapshot_request.CopySnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.copy_snapshot_response.CopySnapshotResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.copy_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.copy_snapshot.async_copy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.copy_snapshot_request.CopySnapshotRequest = {}  # type: ignore[typeddict-item]
        input["source_snapshot_name"] = source_snapshot_name
        input["target_snapshot_name"] = target_snapshot_name
        if target_bucket is not None:
            input["target_bucket"] = target_bucket
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_acl(
        self,
        acl_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_names: Optional[
            "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.create_acl_response.CreateACLResponse":
        """<p>Creates an Access Control List. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            acl_name: <p>The name of the Access Control List.</p>
            user_names: <p>The list of users that belong to the Access Control List.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_acl_request.CreateACLRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_acl_response.CreateACLResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_acl

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_acl.async_create_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_acl_request.CreateACLRequest = {}  # type: ignore[typeddict-item]
        input["acl_name"] = acl_name
        if user_names is not None:
            input["user_names"] = user_names
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_cluster(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        node_type: "aws_sdk_memorydb.types.string.String",
        acl_name: "aws_sdk_memorydb.types.acl_name.ACLName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        parameter_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        num_shards: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        num_replicas_per_shard: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        subnet_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        security_group_ids: Optional[
            "aws_sdk_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        maintenance_window: Optional["aws_sdk_memorydb.types.string.String"] = None,
        port: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        sns_topic_arn: Optional["aws_sdk_memorydb.types.string.String"] = None,
        tls_enabled: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_arns: Optional[
            "aws_sdk_memorydb.types.snapshot_arns_list.SnapshotArnsList"
        ] = None,
        snapshot_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_retention_limit: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
        snapshot_window: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        data_tiering: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional[
            "aws_sdk_memorydb.types.network_type.NetworkType"
        ] = None,
        ip_discovery: Optional[
            "aws_sdk_memorydb.types.ip_discovery.IpDiscovery"
        ] = None,
    ) -> "aws_sdk_memorydb.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a cluster. All nodes in the cluster run the same protocol-compliant engine software.</p>

        Args:
            cluster_name: <p>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</p>
            node_type: <p>The compute and memory capacity of the nodes in the cluster.</p>
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be created.</p>
            parameter_group_name: <p>The name of the parameter group associated with the cluster.</p>
            description: <p>An optional description of the cluster.</p>
            num_shards: <p>The number of shards the cluster will contain. The default value is 1. </p>
            num_replicas_per_shard: <p>The number of replicas to apply to each shard. The default value is 1. The maximum is 5. </p>
            subnet_group_name: <p>The name of the subnet group to be used for the cluster.</p>
            security_group_ids: <p>A list of security group names to associate with this cluster.</p>
            maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            port: <p>The port number on which each of the nodes accepts connections.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p>
            tls_enabled: <p>A flag to enable in-transit encryption on the cluster.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the cluster.</p>
            snapshot_arns: <p>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</p>
            snapshot_name: <p>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</p>
            snapshot_retention_limit: <p>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>
            tags: <p>A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValue Key=mySecondKey, Value=mySecondKeyValue.</p>
            snapshot_window: <p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.</p> <p> Example: 05:00-09:00</p> <p> If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.</p>
            acl_name: <p>The name of the Access Control List to associate with the cluster.</p>
            engine: <p>The name of the engine to be used for the cluster.</p>
            engine_version: <p>The version number of the Redis OSS engine to be used for the cluster.</p>
            auto_minor_version_upgrade: <p>When set to true, the cluster will automatically receive minor engine version upgrades after launch.</p>
            data_tiering: <p>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see <a href=\"https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html\">Data tiering</a>.</p>
            network_type: <p>Specifies the IP address type for the cluster. Valid values are 'ipv4', 'ipv6', or 'dual_stack'. When set to 'ipv4', the cluster will only be accessible via IPv4 addresses. When set to 'ipv6', the cluster will only be accessible via IPv6 addresses. When set to 'dual_stack', the cluster will be accessible via both IPv4 and IPv6 addresses. If not specified, the default is 'ipv4'.</p>
            ip_discovery: <p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_cluster_response.CreateClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_cluster_request.CreateClusterRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        input["node_type"] = node_type
        if multi_region_cluster_name is not None:
            input["multi_region_cluster_name"] = multi_region_cluster_name
        if parameter_group_name is not None:
            input["parameter_group_name"] = parameter_group_name
        if description is not None:
            input["description"] = description
        if num_shards is not None:
            input["num_shards"] = num_shards
        if num_replicas_per_shard is not None:
            input["num_replicas_per_shard"] = num_replicas_per_shard
        if subnet_group_name is not None:
            input["subnet_group_name"] = subnet_group_name
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids
        if maintenance_window is not None:
            input["maintenance_window"] = maintenance_window
        if port is not None:
            input["port"] = port
        if sns_topic_arn is not None:
            input["sns_topic_arn"] = sns_topic_arn
        if tls_enabled is not None:
            input["tls_enabled"] = tls_enabled
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if snapshot_arns is not None:
            input["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            input["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            input["snapshot_retention_limit"] = snapshot_retention_limit
        if tags is not None:
            input["tags"] = tags
        if snapshot_window is not None:
            input["snapshot_window"] = snapshot_window
        input["acl_name"] = acl_name
        if engine is not None:
            input["engine"] = engine
        if engine_version is not None:
            input["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if data_tiering is not None:
            input["data_tiering"] = data_tiering
        if network_type is not None:
            input["network_type"] = network_type
        if ip_discovery is not None:
            input["ip_discovery"] = ip_discovery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_multi_region_cluster(
        self,
        multi_region_cluster_name_suffix: "aws_sdk_memorydb.types.string.String",
        node_type: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        multi_region_parameter_group_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        num_shards: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tls_enabled: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.create_multi_region_cluster_response.CreateMultiRegionClusterResponse":
        """<p>Creates a new multi-Region cluster.</p>

        Args:
            multi_region_cluster_name_suffix: <p>A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with \"virxk\", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions.</p>
            description: <p>A description for the multi-Region cluster.</p>
            engine: <p>The name of the engine to be used for the multi-Region cluster.</p>
            engine_version: <p>The version of the engine to be used for the multi-Region cluster.</p>
            node_type: <p>The node type to be used for the multi-Region cluster.</p>
            multi_region_parameter_group_name: <p>The name of the multi-Region parameter group to be associated with the cluster.</p>
            num_shards: <p>The number of shards for the multi-Region cluster.</p>
            tls_enabled: <p>Whether to enable TLS encryption for the multi-Region cluster.</p>
            tags: <p>A list of tags to be applied to the multi-Region cluster.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_multi_region_cluster_request.CreateMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_multi_region_cluster_response.CreateMultiRegionClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_multi_region_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_multi_region_cluster.async_create_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_multi_region_cluster_request.CreateMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
        input["multi_region_cluster_name_suffix"] = multi_region_cluster_name_suffix
        if description is not None:
            input["description"] = description
        if engine is not None:
            input["engine"] = engine
        if engine_version is not None:
            input["engine_version"] = engine_version
        input["node_type"] = node_type
        if multi_region_parameter_group_name is not None:
            input["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
        if num_shards is not None:
            input["num_shards"] = num_shards
        if tls_enabled is not None:
            input["tls_enabled"] = tls_enabled
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_parameter_group(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        family: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.create_parameter_group_response.CreateParameterGroupResponse":
        """<p>Creates a new MemoryDB parameter group. A parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/parametergroups.html\">Configuring engine parameters using parameter groups</a>. </p>

        Args:
            parameter_group_name: <p>The name of the parameter group.</p>
            family: <p>The name of the parameter group family that the parameter group can be used with.</p>
            description: <p>An optional description of the parameter group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_parameter_group_request.CreateParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_parameter_group_response.CreateParameterGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_parameter_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_parameter_group.async_create_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_parameter_group_request.CreateParameterGroupRequest = {}  # type: ignore[typeddict-item]
        input["parameter_group_name"] = parameter_group_name
        input["family"] = family
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_snapshot(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        snapshot_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        kms_key_id: Optional["aws_sdk_memorydb.types.string.String"] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.create_snapshot_response.CreateSnapshotResponse":
        """<p>Creates a copy of an entire cluster at a specific moment in time.</p>

        Args:
            cluster_name: <p>The snapshot is created from this cluster.</p>
            snapshot_name: <p>A name for the snapshot being created.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_snapshot_request.CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        input["snapshot_name"] = snapshot_name
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subnet_group(
        self,
        subnet_group_name: "aws_sdk_memorydb.types.string.String",
        subnet_ids: "aws_sdk_memorydb.types.subnet_identifier_list.SubnetIdentifierList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_memorydb.types.create_subnet_group_response.CreateSubnetGroupResponse"
    ):
        """<p>Creates a subnet group. A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/subnetgroups.html\">Subnets and subnet groups</a>.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group.</p>
            description: <p>A description for the subnet group.</p>
            subnet_ids: <p>A list of VPC subnet IDs for the subnet group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_subnet_group_request.CreateSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_subnet_group_response.CreateSubnetGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_subnet_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_subnet_group.async_create_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_subnet_group_request.CreateSubnetGroupRequest = {}  # type: ignore[typeddict-item]
        input["subnet_group_name"] = subnet_group_name
        if description is not None:
            input["description"] = description
        input["subnet_ids"] = subnet_ids
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_user(
        self,
        user_name: "aws_sdk_memorydb.types.user_name.UserName",
        authentication_mode: "aws_sdk_memorydb.types.authentication_mode.AuthenticationMode",
        access_string: "aws_sdk_memorydb.types.access_string.AccessString",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.create_user_response.CreateUserResponse":
        """<p>Creates a MemoryDB user. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            user_name: <p>The name of the user. This value must be unique as it also serves as the user identifier.</p>
            authentication_mode: <p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>
            access_string: <p>Access permissions string used for this user.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.create_user

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["authentication_mode"] = authentication_mode
        input["access_string"] = access_string
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_acl(
        self,
        acl_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.delete_acl_response.DeleteACLResponse":
        """<p>Deletes an Access Control List. The ACL must first be disassociated from the cluster before it can be deleted. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html\">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            acl_name: <p>The name of the Access Control List to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_acl_request.DeleteACLRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_acl_response.DeleteACLResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_acl

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_acl.async_delete_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_acl_request.DeleteACLRequest = {}  # type: ignore[typeddict-item]
        input["acl_name"] = acl_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cluster(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        final_snapshot_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a cluster. It also deletes all associated nodes and node endpoints.</p> <note> <p> <code>CreateSnapshot</code> permission is required to create a final snapshot. Without this permission, the API call will fail with an <code>Access Denied</code> exception.</p> </note>

        Args:
            cluster_name: <p>The name of the cluster to be deleted</p>
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be deleted.</p>
            final_snapshot_name: <p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_cluster_request.DeleteClusterRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        if multi_region_cluster_name is not None:
            input["multi_region_cluster_name"] = multi_region_cluster_name
        if final_snapshot_name is not None:
            input["final_snapshot_name"] = final_snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_multi_region_cluster(
        self,
        multi_region_cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.delete_multi_region_cluster_response.DeleteMultiRegionClusterResponse":
        """<p>Deletes an existing multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_multi_region_cluster_request.DeleteMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_multi_region_cluster_response.DeleteMultiRegionClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_multi_region_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_multi_region_cluster.async_delete_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_multi_region_cluster_request.DeleteMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
        input["multi_region_cluster_name"] = multi_region_cluster_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_parameter_group(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.delete_parameter_group_response.DeleteParameterGroupResponse":
        """<p>Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any clusters. You cannot delete the default parameter groups in your account.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_parameter_group_request.DeleteParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_parameter_group_response.DeleteParameterGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_parameter_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_parameter_group.async_delete_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_parameter_group_request.DeleteParameterGroupRequest = {}  # type: ignore[typeddict-item]
        input["parameter_group_name"] = parameter_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_snapshot(
        self,
        snapshot_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.delete_snapshot_response.DeleteSnapshotResponse":
        """<p>Deletes an existing snapshot. When you receive a successful response from this operation, MemoryDB immediately begins deleting the snapshot; you cannot cancel or revert this operation.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_snapshot_request.DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
        input["snapshot_name"] = snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subnet_group(
        self,
        subnet_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> (
        "aws_sdk_memorydb.types.delete_subnet_group_response.DeleteSubnetGroupResponse"
    ):
        """<p>Deletes a subnet group. You cannot delete a default subnet group or one that is associated with any clusters.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_subnet_group_request.DeleteSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_subnet_group_response.DeleteSubnetGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_subnet_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_subnet_group.async_delete_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_subnet_group_request.DeleteSubnetGroupRequest = {}  # type: ignore[typeddict-item]
        input["subnet_group_name"] = subnet_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_user(
        self,
        user_name: "aws_sdk_memorydb.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user. The user will be removed from all ACLs and in turn removed from all clusters.</p>

        Args:
            user_name: <p>The name of the user to delete</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.delete_user_request.DeleteUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.delete_user

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_ac_ls(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        acl_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_ac_ls_response.DescribeACLsResponse":
        """<p>Returns a list of ACLs.</p>

        Args:
            acl_name: <p>The name of the ACL.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_ac_ls_request.DescribeACLsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_ac_ls_response.DescribeACLsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_ac_ls

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_ac_ls.async_describe_ac_ls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_ac_ls_request.DescribeACLsRequest = {}  # type: ignore[typeddict-item]
        if acl_name is not None:
            input["acl_name"] = acl_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_ac_ls(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        acl_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.acl.ACL]":
        _token = next_token
        while True:
            _response = await self.describe_ac_ls(
                config_overrides=config_overrides,
                acl_name=acl_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ac_ls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        show_shard_details: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "aws_sdk_memorydb.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.</p>

        Args:
            cluster_name: <p>The name of the cluster.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            show_shard_details: <p>An optional flag that can be included in the request to retrieve information about the individual shard(s).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_clusters

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_clusters_request.DescribeClustersRequest = {}  # type: ignore[typeddict-item]
        if cluster_name is not None:
            input["cluster_name"] = cluster_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if show_shard_details is not None:
            input["show_shard_details"] = show_shard_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        show_shard_details: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.cluster.Cluster]":
        _token = next_token
        while True:
            _response = await self.describe_clusters(
                config_overrides=config_overrides,
                cluster_name=cluster_name,
                max_results=max_results,
                next_token=_token,
                show_shard_details=show_shard_details,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        engine: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        parameter_group_family: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        default_only: Optional["aws_sdk_memorydb.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_memorydb.types.describe_engine_versions_response.DescribeEngineVersionsResponse":
        """<p>Returns a list of the available Redis OSS engine versions.</p>

        Args:
            engine: <p>The name of the engine for which to list available versions.</p>
            engine_version: <p>The Redis OSS engine version</p>
            parameter_group_family: <p>The name of a specific parameter group family to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            default_only: <p>If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_engine_versions_request.DescribeEngineVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_engine_versions_response.DescribeEngineVersionsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_engine_versions

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_engine_versions.async_describe_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_engine_versions_request.DescribeEngineVersionsRequest = {}  # type: ignore[typeddict-item]
        if engine is not None:
            input["engine"] = engine
        if engine_version is not None:
            input["engine_version"] = engine_version
        if parameter_group_family is not None:
            input["parameter_group_family"] = parameter_group_family
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if default_only is not None:
            input["default_only"] = default_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        engine: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        parameter_group_family: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        default_only: Optional["aws_sdk_memorydb.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.engine_version_info.EngineVersionInfo]":
        _token = next_token
        while True:
            _response = await self.describe_engine_versions(
                config_overrides=config_overrides,
                engine=engine,
                engine_version=engine_version,
                parameter_group_family=parameter_group_family,
                max_results=max_results,
                next_token=_token,
                default_only=default_only,
            )
            _page = _resolve_path(_response, ("engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        source_type: Optional["aws_sdk_memorydb.types.source_type.SourceType"] = None,
        start_time: Optional["aws_sdk_memorydb.types.t_stamp.TStamp"] = None,
        end_time: Optional["aws_sdk_memorydb.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_events_response.DescribeEventsResponse":
        """<p>Returns events related to clusters, security groups, and parameter groups. You can obtain events specific to a particular cluster, security group, or parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.</p>

        Args:
            source_name: <p>The identifier of the event source for which events are returned. If not specified, all sources are included in the response.</p>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z</p>
            end_time: <p>The end of the time interval for which to retrieve events, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z</p>
            duration: <p>The number of minutes worth of events to retrieve.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_events_request.DescribeEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_events_response.DescribeEventsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_events

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_events_request.DescribeEventsRequest = {}  # type: ignore[typeddict-item]
        if source_name is not None:
            input["source_name"] = source_name
        if source_type is not None:
            input["source_type"] = source_type
        if start_time is not None:
            input["start_time"] = start_time
        if end_time is not None:
            input["end_time"] = end_time
        if duration is not None:
            input["duration"] = duration
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        source_type: Optional["aws_sdk_memorydb.types.source_type.SourceType"] = None,
        start_time: Optional["aws_sdk_memorydb.types.t_stamp.TStamp"] = None,
        end_time: Optional["aws_sdk_memorydb.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.event.Event]":
        _token = next_token
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                source_name=source_name,
                source_type=source_type,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_multi_region_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        show_cluster_details: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "aws_sdk_memorydb.types.describe_multi_region_clusters_response.DescribeMultiRegionClustersResponse":
        """<p>Returns details about one or more multi-Region clusters.</p>

        Args:
            multi_region_cluster_name: <p>The name of a specific multi-Region cluster to describe.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A token to specify where to start paginating.</p>
            show_cluster_details: <p>Details about the multi-Region cluster.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_multi_region_clusters_request.DescribeMultiRegionClustersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_multi_region_clusters_response.DescribeMultiRegionClustersResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_clusters

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_clusters.async_describe_multi_region_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_multi_region_clusters_request.DescribeMultiRegionClustersRequest = {}  # type: ignore[typeddict-item]
        if multi_region_cluster_name is not None:
            input["multi_region_cluster_name"] = multi_region_cluster_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if show_cluster_details is not None:
            input["show_cluster_details"] = show_cluster_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_multi_region_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        show_cluster_details: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_memorydb.types.multi_region_cluster.MultiRegionCluster]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_multi_region_clusters(
                config_overrides=config_overrides,
                multi_region_cluster_name=multi_region_cluster_name,
                max_results=max_results,
                next_token=_token,
                show_cluster_details=show_cluster_details,
            )
            _page = _resolve_path(_response, ("multi_region_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_multi_region_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_parameter_group_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_multi_region_parameter_groups_response.DescribeMultiRegionParameterGroupsResponse":
        """<p>Returns a list of multi-region parameter groups.</p>

        Args:
            multi_region_parameter_group_name: <p>The request for information on a specific multi-region parameter group.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_multi_region_parameter_groups_request.DescribeMultiRegionParameterGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_multi_region_parameter_groups_response.DescribeMultiRegionParameterGroupsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_parameter_groups

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_parameter_groups.async_describe_multi_region_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_multi_region_parameter_groups_request.DescribeMultiRegionParameterGroupsRequest = {}  # type: ignore[typeddict-item]
        if multi_region_parameter_group_name is not None:
            input["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_multi_region_parameters(
        self,
        multi_region_parameter_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_multi_region_parameters_response.DescribeMultiRegionParametersResponse":
        """<p>Returns the detailed parameter list for a particular multi-region parameter group.</p>

        Args:
            multi_region_parameter_group_name: <p>The name of the multi-region parameter group to return details for.</p>
            source: <p>The parameter types to return. Valid values: user | system | engine-default</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_multi_region_parameters_request.DescribeMultiRegionParametersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_multi_region_parameters_response.DescribeMultiRegionParametersResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_parameters

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_multi_region_parameters.async_describe_multi_region_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_multi_region_parameters_request.DescribeMultiRegionParametersRequest = {}  # type: ignore[typeddict-item]
        input["multi_region_parameter_group_name"] = multi_region_parameter_group_name
        if source is not None:
            input["source"] = source
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        parameter_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_parameter_groups_response.DescribeParameterGroupsResponse":
        """<p>Returns a list of parameter group descriptions. If a parameter group name is specified, the list contains only the descriptions for that group.</p>

        Args:
            parameter_group_name: <p>The name of a specific parameter group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_parameter_groups_request.DescribeParameterGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_parameter_groups_response.DescribeParameterGroupsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_parameter_groups

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_parameter_groups.async_describe_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_parameter_groups_request.DescribeParameterGroupsRequest = {}  # type: ignore[typeddict-item]
        if parameter_group_name is not None:
            input["parameter_group_name"] = parameter_group_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        parameter_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.parameter_group.ParameterGroup]":
        _token = next_token
        while True:
            _response = await self.describe_parameter_groups(
                config_overrides=config_overrides,
                parameter_group_name=parameter_group_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_parameters(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> (
        "aws_sdk_memorydb.types.describe_parameters_response.DescribeParametersResponse"
    ):
        """<p>Returns the detailed parameter list for a particular parameter group.</p>

        Args:
            parameter_group_name: <p>he name of a specific parameter group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_parameters_request.DescribeParametersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_parameters_response.DescribeParametersResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_parameters

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_parameters.async_describe_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_parameters_request.DescribeParametersRequest = {}  # type: ignore[typeddict-item]
        input["parameter_group_name"] = parameter_group_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_parameters(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.parameter.Parameter]":
        _token = next_token
        while True:
            _response = await self.describe_parameters(
                parameter_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("parameters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["aws_sdk_memorydb.types.string.String"] = None,
        reserved_nodes_offering_id: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        duration: Optional["aws_sdk_memorydb.types.string.String"] = None,
        offering_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_reserved_nodes_response.DescribeReservedNodesResponse":
        """<p>Returns information about reserved nodes for this account, or about a specified reserved node.</p>

        Args:
            reservation_id: <p>The reserved node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.</p>
            reserved_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.</p>
            node_type: <p>The node type filter value. Use this parameter to show only those reservations matching the specified node type. For more information, see <a href=\"https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported\">Supported node types</a>.</p>
            duration: <p>The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: \"All Upfront\"|\"Partial Upfront\"| \"No Upfront\"</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_reserved_nodes_request.DescribeReservedNodesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_reserved_nodes_response.DescribeReservedNodesResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_reserved_nodes

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_reserved_nodes.async_describe_reserved_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_reserved_nodes_request.DescribeReservedNodesRequest = {}  # type: ignore[typeddict-item]
        if reservation_id is not None:
            input["reservation_id"] = reservation_id
        if reserved_nodes_offering_id is not None:
            input["reserved_nodes_offering_id"] = reserved_nodes_offering_id
        if node_type is not None:
            input["node_type"] = node_type
        if duration is not None:
            input["duration"] = duration
        if offering_type is not None:
            input["offering_type"] = offering_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["aws_sdk_memorydb.types.string.String"] = None,
        reserved_nodes_offering_id: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        duration: Optional["aws_sdk_memorydb.types.string.String"] = None,
        offering_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.reserved_node.ReservedNode]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_nodes(
                config_overrides=config_overrides,
                reservation_id=reservation_id,
                reserved_nodes_offering_id=reserved_nodes_offering_id,
                node_type=node_type,
                duration=duration,
                offering_type=offering_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reserved_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reserved_nodes_offering_id: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        duration: Optional["aws_sdk_memorydb.types.string.String"] = None,
        offering_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_reserved_nodes_offerings_response.DescribeReservedNodesOfferingsResponse":
        """<p>Lists available reserved node offerings.</p>

        Args:
            reserved_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>
            node_type: <p>The node type for the reserved nodes. For more information, see <a href=\"https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported\">Supported node types</a>.</p>
            duration: <p>Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: \"All Upfront\"|\"Partial Upfront\"| \"No Upfront\"</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_reserved_nodes_offerings_request.DescribeReservedNodesOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_reserved_nodes_offerings_response.DescribeReservedNodesOfferingsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_reserved_nodes_offerings

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_reserved_nodes_offerings.async_describe_reserved_nodes_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_reserved_nodes_offerings_request.DescribeReservedNodesOfferingsRequest = {}  # type: ignore[typeddict-item]
        if reserved_nodes_offering_id is not None:
            input["reserved_nodes_offering_id"] = reserved_nodes_offering_id
        if node_type is not None:
            input["node_type"] = node_type
        if duration is not None:
            input["duration"] = duration
        if offering_type is not None:
            input["offering_type"] = offering_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_reserved_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reserved_nodes_offering_id: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        duration: Optional["aws_sdk_memorydb.types.string.String"] = None,
        offering_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.reserved_nodes_offering.ReservedNodesOffering]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_nodes_offerings(
                config_overrides=config_overrides,
                reserved_nodes_offering_id=reserved_nodes_offering_id,
                node_type=node_type,
                duration=duration,
                offering_type=offering_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reserved_nodes_offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        cluster_names: Optional[
            "aws_sdk_memorydb.types.cluster_name_list.ClusterNameList"
        ] = None,
        status: Optional[
            "aws_sdk_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_service_updates_response.DescribeServiceUpdatesResponse":
        """<p>Returns details of the service updates.</p>

        Args:
            service_update_name: <p>The unique ID of the service update to describe.</p>
            cluster_names: <p>The list of cluster names to identify service updates to apply.</p>
            status: <p>The status(es) of the service updates to filter on.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_service_updates_request.DescribeServiceUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_service_updates_response.DescribeServiceUpdatesResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_service_updates

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_service_updates.async_describe_service_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_service_updates_request.DescribeServiceUpdatesRequest = {}  # type: ignore[typeddict-item]
        if service_update_name is not None:
            input["service_update_name"] = service_update_name
        if cluster_names is not None:
            input["cluster_names"] = cluster_names
        if status is not None:
            input["status"] = status
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        cluster_names: Optional[
            "aws_sdk_memorydb.types.cluster_name_list.ClusterNameList"
        ] = None,
        status: Optional[
            "aws_sdk_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.service_update.ServiceUpdate]":
        _token = next_token
        while True:
            _response = await self.describe_service_updates(
                config_overrides=config_overrides,
                service_update_name=service_update_name,
                cluster_names=cluster_names,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_updates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        source: Optional["aws_sdk_memorydb.types.string.String"] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        show_detail: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "aws_sdk_memorydb.types.describe_snapshots_response.DescribeSnapshotsResponse":
        """<p>Returns information about cluster snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cluster.</p>

        Args:
            cluster_name: <p>A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.</p>
            snapshot_name: <p>A user-supplied name of the snapshot. If this parameter is specified, only this named snapshot is described.</p>
            source: <p>If set to system, the output shows snapshots that were automatically created by MemoryDB. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            show_detail: <p>A Boolean value which if true, the shard configuration is included in the snapshot description.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_snapshots_request.DescribeSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_snapshots_response.DescribeSnapshotsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_snapshots

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_snapshots.async_describe_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_snapshots_request.DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
        if cluster_name is not None:
            input["cluster_name"] = cluster_name
        if snapshot_name is not None:
            input["snapshot_name"] = snapshot_name
        if source is not None:
            input["source"] = source
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if show_detail is not None:
            input["show_detail"] = show_detail

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        source: Optional["aws_sdk_memorydb.types.string.String"] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        show_detail: Optional[
            "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.snapshot.Snapshot]":
        _token = next_token
        while True:
            _response = await self.describe_snapshots(
                config_overrides=config_overrides,
                cluster_name=cluster_name,
                snapshot_name=snapshot_name,
                source=source,
                next_token=_token,
                max_results=max_results,
                show_detail=show_detail,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        subnet_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse":
        """<p>Returns a list of subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_subnet_groups

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_subnet_groups.async_describe_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest = {}  # type: ignore[typeddict-item]
        if subnet_group_name is not None:
            input["subnet_group_name"] = subnet_group_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        subnet_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.subnet_group.SubnetGroup]":
        _token = next_token
        while True:
            _response = await self.describe_subnet_groups(
                config_overrides=config_overrides,
                subnet_group_name=subnet_group_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subnet_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_users(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_name: Optional["aws_sdk_memorydb.types.user_name.UserName"] = None,
        filters: Optional["aws_sdk_memorydb.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "aws_sdk_memorydb.types.describe_users_response.DescribeUsersResponse":
        """<p>Returns a list of users.</p>

        Args:
            user_name: <p>The name of the user.</p>
            filters: <p>Filter to determine the list of users to return.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.describe_users_request.DescribeUsersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.describe_users_response.DescribeUsersResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.describe_users

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.describe_users.async_describe_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.describe_users_request.DescribeUsersRequest = {}  # type: ignore[typeddict-item]
        if user_name is not None:
            input["user_name"] = user_name
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_users(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_name: Optional["aws_sdk_memorydb.types.user_name.UserName"] = None,
        filters: Optional["aws_sdk_memorydb.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["aws_sdk_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_memorydb.types.user.User]":
        _token = next_token
        while True:
            _response = await self.describe_users(
                config_overrides=config_overrides,
                user_name=user_name,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def failover_shard(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        shard_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.failover_shard_response.FailoverShardResponse":
        """<p>Used to failover a shard. This API is designed for testing the behavior of your application in case of MemoryDB failover. It is not designed to be used as a production-level tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large scale operational events, Amazon may block this API. </p>

        Args:
            cluster_name: <p>The cluster being failed over.</p>
            shard_name: <p>The name of the shard.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.failover_shard_request.FailoverShardRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.failover_shard_response.FailoverShardResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.failover_shard

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.failover_shard.async_failover_shard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.failover_shard_request.FailoverShardRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        input["shard_name"] = shard_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_allowed_multi_region_cluster_updates(
        self,
        multi_region_cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_response.ListAllowedMultiRegionClusterUpdatesResponse":
        """<p>Lists the allowed updates for a multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_request.ListAllowedMultiRegionClusterUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_response.ListAllowedMultiRegionClusterUpdatesResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.list_allowed_multi_region_cluster_updates

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.list_allowed_multi_region_cluster_updates.async_list_allowed_multi_region_cluster_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.list_allowed_multi_region_cluster_updates_request.ListAllowedMultiRegionClusterUpdatesRequest = {}  # type: ignore[typeddict-item]
        input["multi_region_cluster_name"] = multi_region_cluster_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_allowed_node_type_updates(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.list_allowed_node_type_updates_response.ListAllowedNodeTypeUpdatesResponse":
        """<p>Lists all available node types that you can scale to from your cluster's current node type. When you use the UpdateCluster operation to scale your cluster, the value of the NodeType parameter must be one of the node types returned by this operation.</p>

        Args:
            cluster_name: <p>The name of the cluster you want to scale. MemoryDB uses the cluster name to identify the current node type being used by this cluster, and from that to create a list of node types you can scale up to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.list_allowed_node_type_updates_request.ListAllowedNodeTypeUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.list_allowed_node_type_updates_response.ListAllowedNodeTypeUpdatesResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.list_allowed_node_type_updates

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.list_allowed_node_type_updates.async_list_allowed_node_type_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.list_allowed_node_type_updates_request.ListAllowedNodeTypeUpdatesRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags(
        self,
        resource_arn: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.list_tags_response.ListTagsResponse":
        """<p>Lists all tags currently on a named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track your MemoryDB resources. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p>When you add or remove tags from multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p></p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want the list of tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.list_tags_response.ListTagsResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.list_tags

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def purchase_reserved_nodes_offering(
        self,
        reserved_nodes_offering_id: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["aws_sdk_memorydb.types.string.String"] = None,
        node_count: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["aws_sdk_memorydb.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_memorydb.types.purchase_reserved_nodes_offering_response.PurchaseReservedNodesOfferingResponse":
        """<p>Allows you to purchase a reserved node offering. Reserved nodes are not eligible for cancellation and are non-refundable.</p>

        Args:
            reserved_nodes_offering_id: <p>The ID of the reserved node offering to purchase.</p>
            reservation_id: <p>A customer-specified identifier to track this reservation.</p>
            node_count: <p>The number of node instances to reserve.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.purchase_reserved_nodes_offering_request.PurchaseReservedNodesOfferingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.purchase_reserved_nodes_offering_response.PurchaseReservedNodesOfferingResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.purchase_reserved_nodes_offering

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.purchase_reserved_nodes_offering.async_purchase_reserved_nodes_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.purchase_reserved_nodes_offering_request.PurchaseReservedNodesOfferingRequest = {}  # type: ignore[typeddict-item]
        input["reserved_nodes_offering_id"] = reserved_nodes_offering_id
        if reservation_id is not None:
            input["reservation_id"] = reservation_id
        if node_count is not None:
            input["node_count"] = node_count
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_parameter_group(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        all_parameters: Optional["aws_sdk_memorydb.types.boolean.Boolean"] = None,
        parameter_names: Optional[
            "aws_sdk_memorydb.types.parameter_name_list.ParameterNameList"
        ] = None,
    ) -> "aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse":
        """<p>Modifies the parameters of a parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire parameter group, specify the AllParameters and ParameterGroupName parameters.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to reset.</p>
            all_parameters: <p>If true, all parameters in the parameter group are reset to their default values. If false, only the parameters listed by ParameterNames are reset to their default values.</p>
            parameter_names: <p>An array of parameter names to reset to their default values. If AllParameters is true, do not use ParameterNames. If AllParameters is false, you must specify the name of at least one parameter to reset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.reset_parameter_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.reset_parameter_group.async_reset_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest = {}  # type: ignore[typeddict-item]
        input["parameter_group_name"] = parameter_group_name
        if all_parameters is not None:
            input["all_parameters"] = all_parameters
        if parameter_names is not None:
            input["parameter_names"] = parameter_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_memorydb.types.string.String",
        tags: "aws_sdk_memorydb.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.tag_resource_response.TagResourceResponse":
        """<p> Use this operation to add tags to a resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your MemoryDB resources. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p>When you add tags to multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p>You can specify cost-allocation tags for your MemoryDB resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html\">Using Cost Allocation Tags</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tags are to be added.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_memorydb.types.string.String",
        tag_keys: "aws_sdk_memorydb.types.key_list.KeyList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.untag_resource_response.UntagResourceResponse":
        """<p>Use this operation to remove tags on a resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your MemoryDB resources. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p>When you remove tags from multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html\">Tagging your MemoryDB resources</a>.</p> <p>You can specify cost-allocation tags for your MemoryDB resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html\">Using Cost Allocation Tags</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tags are to be removed.</p>
            tag_keys: <p>The list of keys of the tags that are to be removed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_acl(
        self,
        acl_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_names_to_add: Optional[
            "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
        user_names_to_remove: Optional[
            "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
    ) -> "aws_sdk_memorydb.types.update_acl_response.UpdateACLResponse":
        """<p>Changes the list of users that belong to the Access Control List.</p>

        Args:
            acl_name: <p>The name of the Access Control List.</p>
            user_names_to_add: <p>The list of users to add to the Access Control List.</p>
            user_names_to_remove: <p>The list of users to remove from the Access Control List.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_acl_request.UpdateACLRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_acl_response.UpdateACLResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_acl

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_acl.async_update_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_acl_request.UpdateACLRequest = {}  # type: ignore[typeddict-item]
        input["acl_name"] = acl_name
        if user_names_to_add is not None:
            input["user_names_to_add"] = user_names_to_add
        if user_names_to_remove is not None:
            input["user_names_to_remove"] = user_names_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_cluster(
        self,
        cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        security_group_ids: Optional[
            "aws_sdk_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        maintenance_window: Optional["aws_sdk_memorydb.types.string.String"] = None,
        sns_topic_arn: Optional["aws_sdk_memorydb.types.string.String"] = None,
        sns_topic_status: Optional["aws_sdk_memorydb.types.string.String"] = None,
        parameter_group_name: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_window: Optional["aws_sdk_memorydb.types.string.String"] = None,
        snapshot_retention_limit: Optional[
            "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        replica_configuration: Optional[
            "aws_sdk_memorydb.types.replica_configuration_request.ReplicaConfigurationRequest"
        ] = None,
        shard_configuration: Optional[
            "aws_sdk_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
        ] = None,
        acl_name: Optional["aws_sdk_memorydb.types.acl_name.ACLName"] = None,
        ip_discovery: Optional[
            "aws_sdk_memorydb.types.ip_discovery.IpDiscovery"
        ] = None,
    ) -> "aws_sdk_memorydb.types.update_cluster_response.UpdateClusterResponse":
        """<p>Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration settings by specifying the settings and the new values.</p>

        Args:
            cluster_name: <p>The name of the cluster to update.</p>
            description: <p>The description of the cluster to update.</p>
            security_group_ids: <p>The SecurityGroupIds to update.</p>
            maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            sns_topic_arn: <p>The SNS topic ARN to update.</p>
            sns_topic_status: <p>The status of the Amazon SNS notification topic. Notifications are sent only if the status is active.</p>
            parameter_group_name: <p>The name of the parameter group to update.</p>
            snapshot_window: <p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</p>
            snapshot_retention_limit: <p>The number of days for which MemoryDB retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>
            node_type: <p>A valid node type that you want to scale this cluster up or down to.</p>
            engine: <p>The name of the engine to be used for the cluster.</p>
            engine_version: <p>The upgraded version of the engine to be run on the nodes. You can upgrade to a newer engine version, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.</p>
            replica_configuration: <p>The number of replicas that will reside in each shard.</p>
            shard_configuration: <p>The number of shards in the cluster.</p>
            acl_name: <p>The Access Control List that is associated with the cluster.</p>
            ip_discovery: <p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes will return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_cluster_request.UpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        if description is not None:
            input["description"] = description
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids
        if maintenance_window is not None:
            input["maintenance_window"] = maintenance_window
        if sns_topic_arn is not None:
            input["sns_topic_arn"] = sns_topic_arn
        if sns_topic_status is not None:
            input["sns_topic_status"] = sns_topic_status
        if parameter_group_name is not None:
            input["parameter_group_name"] = parameter_group_name
        if snapshot_window is not None:
            input["snapshot_window"] = snapshot_window
        if snapshot_retention_limit is not None:
            input["snapshot_retention_limit"] = snapshot_retention_limit
        if node_type is not None:
            input["node_type"] = node_type
        if engine is not None:
            input["engine"] = engine
        if engine_version is not None:
            input["engine_version"] = engine_version
        if replica_configuration is not None:
            input["replica_configuration"] = replica_configuration
        if shard_configuration is not None:
            input["shard_configuration"] = shard_configuration
        if acl_name is not None:
            input["acl_name"] = acl_name
        if ip_discovery is not None:
            input["ip_discovery"] = ip_discovery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_multi_region_cluster(
        self,
        multi_region_cluster_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        node_type: Optional["aws_sdk_memorydb.types.string.String"] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        engine_version: Optional["aws_sdk_memorydb.types.string.String"] = None,
        shard_configuration: Optional[
            "aws_sdk_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
        ] = None,
        multi_region_parameter_group_name: Optional[
            "aws_sdk_memorydb.types.string.String"
        ] = None,
        update_strategy: Optional[
            "aws_sdk_memorydb.types.update_strategy.UpdateStrategy"
        ] = None,
    ) -> "aws_sdk_memorydb.types.update_multi_region_cluster_response.UpdateMultiRegionClusterResponse":
        """<p>Updates the configuration of an existing multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be updated.</p>
            node_type: <p>The new node type to be used for the multi-Region cluster.</p>
            description: <p>A new description for the multi-Region cluster.</p>
            engine_version: <p>The new engine version to be used for the multi-Region cluster.</p>
            multi_region_parameter_group_name: <p>The new multi-Region parameter group to be associated with the cluster.</p>
            update_strategy: <p>The strategy to use for the update operation. Supported values are \"coordinated\" or \"uncoordinated\".</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_multi_region_cluster_request.UpdateMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_multi_region_cluster_response.UpdateMultiRegionClusterResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_multi_region_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_multi_region_cluster.async_update_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_multi_region_cluster_request.UpdateMultiRegionClusterRequest = {}  # type: ignore[typeddict-item]
        input["multi_region_cluster_name"] = multi_region_cluster_name
        if node_type is not None:
            input["node_type"] = node_type
        if description is not None:
            input["description"] = description
        if engine_version is not None:
            input["engine_version"] = engine_version
        if shard_configuration is not None:
            input["shard_configuration"] = shard_configuration
        if multi_region_parameter_group_name is not None:
            input["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
        if update_strategy is not None:
            input["update_strategy"] = update_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_parameter_group(
        self,
        parameter_group_name: "aws_sdk_memorydb.types.string.String",
        parameter_name_values: "aws_sdk_memorydb.types.parameter_name_value_list.ParameterNameValueList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "aws_sdk_memorydb.types.update_parameter_group_response.UpdateParameterGroupResponse":
        """<p>Updates the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to update.</p>
            parameter_name_values: <p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be updated per request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_parameter_group_request.UpdateParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_parameter_group_response.UpdateParameterGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_parameter_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_parameter_group.async_update_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_parameter_group_request.UpdateParameterGroupRequest = {}  # type: ignore[typeddict-item]
        input["parameter_group_name"] = parameter_group_name
        input["parameter_name_values"] = parameter_name_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subnet_group(
        self,
        subnet_group_name: "aws_sdk_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["aws_sdk_memorydb.types.string.String"] = None,
        subnet_ids: Optional[
            "aws_sdk_memorydb.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> (
        "aws_sdk_memorydb.types.update_subnet_group_response.UpdateSubnetGroupResponse"
    ):
        """<p>Updates a subnet group. For more information, see <a href=\"https://docs.aws.amazon.com/MemoryDB/latest/devguide/ubnetGroups.Modifying.html\">Updating a subnet group</a> </p>

        Args:
            subnet_group_name: <p>The name of the subnet group</p>
            description: <p>A description of the subnet group</p>
            subnet_ids: <p>The EC2 subnet IDs for the subnet group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_subnet_group_request.UpdateSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_subnet_group_response.UpdateSubnetGroupResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_subnet_group

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_subnet_group.async_update_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_subnet_group_request.UpdateSubnetGroupRequest = {}  # type: ignore[typeddict-item]
        input["subnet_group_name"] = subnet_group_name
        if description is not None:
            input["description"] = description
        if subnet_ids is not None:
            input["subnet_ids"] = subnet_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_user(
        self,
        user_name: "aws_sdk_memorydb.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        authentication_mode: Optional[
            "aws_sdk_memorydb.types.authentication_mode.AuthenticationMode"
        ] = None,
        access_string: Optional[
            "aws_sdk_memorydb.types.access_string.AccessString"
        ] = None,
    ) -> "aws_sdk_memorydb.types.update_user_response.UpdateUserResponse":
        """<p>Changes user password(s) and/or access string.</p>

        Args:
            user_name: <p>The name of the user</p>
            authentication_mode: <p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>
            access_string: <p>Access permissions string used for this user.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_memorydb.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_memorydb.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_memorydb._operations.amazon_memory_db.update_user

            (
                output,
                http_response,
            ) = await aws_sdk_memorydb._operations.amazon_memory_db.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_memorydb.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        if authentication_mode is not None:
            input["authentication_mode"] = authentication_mode
        if access_string is not None:
            input["access_string"] = access_string

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
