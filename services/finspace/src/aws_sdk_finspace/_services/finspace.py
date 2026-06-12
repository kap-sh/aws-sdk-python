"""Generated from Smithy shape ``com.amazonaws.finspace#AWSHabaneroManagementService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_finspace._auth._signers
import aws_sdk_finspace._auth._sigv4
from aws_sdk_finspace._auth._identity import Credentials
from aws_sdk_finspace._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_finspace._auth._zapros_handler import AuthMiddleware
from aws_sdk_finspace._pagination import resolve_path as _resolve_path
from aws_sdk_finspace._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_finspace.types.auto_scaling_configuration
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.availability_zone_ids
    import aws_sdk_finspace.types.boolean_value
    import aws_sdk_finspace.types.boxed_integer
    import aws_sdk_finspace.types.capacity_configuration
    import aws_sdk_finspace.types.change_requests
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.code_configuration
    import aws_sdk_finspace.types.create_environment_request
    import aws_sdk_finspace.types.create_environment_response
    import aws_sdk_finspace.types.create_kx_changeset_request
    import aws_sdk_finspace.types.create_kx_changeset_response
    import aws_sdk_finspace.types.create_kx_cluster_request
    import aws_sdk_finspace.types.create_kx_cluster_response
    import aws_sdk_finspace.types.create_kx_database_request
    import aws_sdk_finspace.types.create_kx_database_response
    import aws_sdk_finspace.types.create_kx_dataview_request
    import aws_sdk_finspace.types.create_kx_dataview_response
    import aws_sdk_finspace.types.create_kx_environment_request
    import aws_sdk_finspace.types.create_kx_environment_response
    import aws_sdk_finspace.types.create_kx_scaling_group_request
    import aws_sdk_finspace.types.create_kx_scaling_group_response
    import aws_sdk_finspace.types.create_kx_user_request
    import aws_sdk_finspace.types.create_kx_user_response
    import aws_sdk_finspace.types.create_kx_volume_request
    import aws_sdk_finspace.types.create_kx_volume_response
    import aws_sdk_finspace.types.custom_dns_configuration
    import aws_sdk_finspace.types.data_bundle_arns
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.delete_environment_request
    import aws_sdk_finspace.types.delete_environment_response
    import aws_sdk_finspace.types.delete_kx_cluster_node_request
    import aws_sdk_finspace.types.delete_kx_cluster_node_response
    import aws_sdk_finspace.types.delete_kx_cluster_request
    import aws_sdk_finspace.types.delete_kx_cluster_response
    import aws_sdk_finspace.types.delete_kx_database_request
    import aws_sdk_finspace.types.delete_kx_database_response
    import aws_sdk_finspace.types.delete_kx_dataview_request
    import aws_sdk_finspace.types.delete_kx_dataview_response
    import aws_sdk_finspace.types.delete_kx_environment_request
    import aws_sdk_finspace.types.delete_kx_environment_response
    import aws_sdk_finspace.types.delete_kx_scaling_group_request
    import aws_sdk_finspace.types.delete_kx_scaling_group_response
    import aws_sdk_finspace.types.delete_kx_user_request
    import aws_sdk_finspace.types.delete_kx_user_response
    import aws_sdk_finspace.types.delete_kx_volume_request
    import aws_sdk_finspace.types.delete_kx_volume_response
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.environment_name
    import aws_sdk_finspace.types.execution_role_arn
    import aws_sdk_finspace.types.federation_mode
    import aws_sdk_finspace.types.federation_parameters
    import aws_sdk_finspace.types.fin_space_taggable_arn
    import aws_sdk_finspace.types.get_environment_request
    import aws_sdk_finspace.types.get_environment_response
    import aws_sdk_finspace.types.get_kx_changeset_request
    import aws_sdk_finspace.types.get_kx_changeset_response
    import aws_sdk_finspace.types.get_kx_cluster_request
    import aws_sdk_finspace.types.get_kx_cluster_response
    import aws_sdk_finspace.types.get_kx_connection_string_request
    import aws_sdk_finspace.types.get_kx_connection_string_response
    import aws_sdk_finspace.types.get_kx_database_request
    import aws_sdk_finspace.types.get_kx_database_response
    import aws_sdk_finspace.types.get_kx_dataview_request
    import aws_sdk_finspace.types.get_kx_dataview_response
    import aws_sdk_finspace.types.get_kx_environment_request
    import aws_sdk_finspace.types.get_kx_environment_response
    import aws_sdk_finspace.types.get_kx_scaling_group_request
    import aws_sdk_finspace.types.get_kx_scaling_group_response
    import aws_sdk_finspace.types.get_kx_user_request
    import aws_sdk_finspace.types.get_kx_user_response
    import aws_sdk_finspace.types.get_kx_volume_request
    import aws_sdk_finspace.types.get_kx_volume_response
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.initialization_script_file_path
    import aws_sdk_finspace.types.kms_key_arn
    import aws_sdk_finspace.types.kms_key_id
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_cache_storage_configurations
    import aws_sdk_finspace.types.kx_cluster_code_deployment_configuration
    import aws_sdk_finspace.types.kx_cluster_description
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_cluster_node_id_string
    import aws_sdk_finspace.types.kx_cluster_type
    import aws_sdk_finspace.types.kx_command_line_arguments
    import aws_sdk_finspace.types.kx_database_configurations
    import aws_sdk_finspace.types.kx_dataview_name
    import aws_sdk_finspace.types.kx_dataview_segment_configuration_list
    import aws_sdk_finspace.types.kx_deployment_configuration
    import aws_sdk_finspace.types.kx_environment
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_environment_name
    import aws_sdk_finspace.types.kx_host_type
    import aws_sdk_finspace.types.kx_nas1_configuration
    import aws_sdk_finspace.types.kx_savedown_storage_configuration
    import aws_sdk_finspace.types.kx_scaling_group_configuration
    import aws_sdk_finspace.types.kx_scaling_group_name
    import aws_sdk_finspace.types.kx_user_arn
    import aws_sdk_finspace.types.kx_user_name_string
    import aws_sdk_finspace.types.kx_volume_name
    import aws_sdk_finspace.types.kx_volume_type
    import aws_sdk_finspace.types.list_environments_request
    import aws_sdk_finspace.types.list_environments_response
    import aws_sdk_finspace.types.list_kx_changesets_request
    import aws_sdk_finspace.types.list_kx_changesets_response
    import aws_sdk_finspace.types.list_kx_cluster_nodes_request
    import aws_sdk_finspace.types.list_kx_cluster_nodes_response
    import aws_sdk_finspace.types.list_kx_clusters_request
    import aws_sdk_finspace.types.list_kx_clusters_response
    import aws_sdk_finspace.types.list_kx_databases_request
    import aws_sdk_finspace.types.list_kx_databases_response
    import aws_sdk_finspace.types.list_kx_dataviews_request
    import aws_sdk_finspace.types.list_kx_dataviews_response
    import aws_sdk_finspace.types.list_kx_environments_request
    import aws_sdk_finspace.types.list_kx_environments_response
    import aws_sdk_finspace.types.list_kx_scaling_groups_request
    import aws_sdk_finspace.types.list_kx_scaling_groups_response
    import aws_sdk_finspace.types.list_kx_users_request
    import aws_sdk_finspace.types.list_kx_users_response
    import aws_sdk_finspace.types.list_kx_volumes_request
    import aws_sdk_finspace.types.list_kx_volumes_response
    import aws_sdk_finspace.types.list_tags_for_resource_request
    import aws_sdk_finspace.types.list_tags_for_resource_response
    import aws_sdk_finspace.types.max_results
    import aws_sdk_finspace.types.pagination_token
    import aws_sdk_finspace.types.release_label
    import aws_sdk_finspace.types.result_limit
    import aws_sdk_finspace.types.role_arn
    import aws_sdk_finspace.types.superuser_parameters
    import aws_sdk_finspace.types.tag_key_list
    import aws_sdk_finspace.types.tag_map
    import aws_sdk_finspace.types.tag_resource_request
    import aws_sdk_finspace.types.tag_resource_response
    import aws_sdk_finspace.types.tickerplant_log_configuration
    import aws_sdk_finspace.types.transit_gateway_configuration
    import aws_sdk_finspace.types.untag_resource_request
    import aws_sdk_finspace.types.untag_resource_response
    import aws_sdk_finspace.types.update_environment_request
    import aws_sdk_finspace.types.update_environment_response
    import aws_sdk_finspace.types.update_kx_cluster_code_configuration_request
    import aws_sdk_finspace.types.update_kx_cluster_code_configuration_response
    import aws_sdk_finspace.types.update_kx_cluster_databases_request
    import aws_sdk_finspace.types.update_kx_cluster_databases_response
    import aws_sdk_finspace.types.update_kx_database_request
    import aws_sdk_finspace.types.update_kx_database_response
    import aws_sdk_finspace.types.update_kx_dataview_request
    import aws_sdk_finspace.types.update_kx_dataview_response
    import aws_sdk_finspace.types.update_kx_environment_network_request
    import aws_sdk_finspace.types.update_kx_environment_network_response
    import aws_sdk_finspace.types.update_kx_environment_request
    import aws_sdk_finspace.types.update_kx_environment_response
    import aws_sdk_finspace.types.update_kx_user_request
    import aws_sdk_finspace.types.update_kx_user_response
    import aws_sdk_finspace.types.update_kx_volume_request
    import aws_sdk_finspace.types.update_kx_volume_response
    import aws_sdk_finspace.types.vpc_configuration


class finspaceClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class finspaceClient:
    """A client for the ``finspace`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = finspaceClientConfig(
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
        self, config_overrides: Optional[finspaceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: finspaceClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def create_environment(
        self,
        name: "aws_sdk_finspace.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        kms_key_id: Optional["aws_sdk_finspace.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
        federation_mode: Optional[
            "aws_sdk_finspace.types.federation_mode.FederationMode"
        ] = None,
        federation_parameters: Optional[
            "aws_sdk_finspace.types.federation_parameters.FederationParameters"
        ] = None,
        superuser_parameters: Optional[
            "aws_sdk_finspace.types.superuser_parameters.SuperuserParameters"
        ] = None,
        data_bundles: Optional[
            "aws_sdk_finspace.types.data_bundle_arns.DataBundleArns"
        ] = None,
    ) -> "aws_sdk_finspace.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Create a new FinSpace environment.</p>

        Args:
            name: <p>The name of the FinSpace environment to be created.</p>
            description: <p>The description of the FinSpace environment to be created.</p>
            kms_key_id: <p>The KMS key id to encrypt your data in the FinSpace environment.</p>
            tags: <p>Add tags to your FinSpace environment.</p>
            federation_mode: <p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>
            federation_parameters: <p>Configuration information when authentication mode is FEDERATED.</p>
            superuser_parameters: <p>Configuration information for the superuser.</p>
            data_bundles: <p>The list of Amazon Resource Names (ARN) of the data bundles to install. Currently supported data bundle ARNs:</p> <ul> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/capital-markets-sample</code> - Contains sample Capital Markets datasets, categories and controlled vocabularies.</p> </li> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/taq</code> (default) - Contains trades and quotes data in addition to sample Capital Markets data.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_environment_request.CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if federation_mode is not None:
            input["federation_mode"] = federation_mode
        if federation_parameters is not None:
            input["federation_parameters"] = federation_parameters
        if superuser_parameters is not None:
            input["superuser_parameters"] = superuser_parameters
        if data_bundles is not None:
            input["data_bundles"] = data_bundles

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_changeset(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        change_requests: "aws_sdk_finspace.types.change_requests.ChangeRequests",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> (
        "aws_sdk_finspace.types.create_kx_changeset_response.CreateKxChangesetResponse"
    ):
        """<p> Creates a changeset for a kdb database. A changeset allows you to add and delete existing files by using an ordered list of change requests. </p>

        Args:
            environment_id: <p>A unique identifier of the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            change_requests: <p>A list of change request objects that are run in order. A change request object consists of <code>changeType</code> , <code>s3Path</code>, and <code>dbPath</code>. A changeType can have the following values: </p> <ul> <li> <p>PUT – Adds or updates files in a database.</p> </li> <li> <p>DELETE – Deletes files in a database.</p> </li> </ul> <p>All the change requests require a mandatory <code>dbPath</code> attribute that defines the path within the database directory. All database paths must start with a leading / and end with a trailing /. The <code>s3Path</code> attribute defines the s3 source file path and is required for a PUT change type. The <code>s3path</code> must end with a trailing / if it is a directory and must end without a trailing / if it is a file. </p> <p>Here are few examples of how you can use the change request object:</p> <ol> <li> <p>This request adds a single sym file at database root location. </p> <p> <code>{ \"changeType\": \"PUT\", \"s3Path\":\"s3://bucket/db/sym\", \"dbPath\":\"/\"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the 2020.01.02 partition of the database.</p> <p> <code>{ \"changeType\": \"PUT\", \"s3Path\":\"s3://bucket/db/2020.01.02/\", \"dbPath\":\"/2020.01.02/\"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the <i>taq</i> table partition of the database.</p> <p> <code>[ { \"changeType\": \"PUT\", \"s3Path\":\"s3://bucket/db/2020.01.02/taq/\", \"dbPath\":\"/2020.01.02/taq/\"}]</code> </p> </li> <li> <p>This request deletes the 2020.01.02 partition of the database.</p> <p> <code>[{ \"changeType\": \"DELETE\", \"dbPath\": \"/2020.01.02/\"} ]</code> </p> </li> <li> <p>The <i>DELETE</i> request allows you to delete the existing files under the 2020.01.02 partition of the database, and the <i>PUT</i> request adds a new taq table under it.</p> <p> <code>[ {\"changeType\": \"DELETE\", \"dbPath\":\"/2020.01.02/\"}, {\"changeType\": \"PUT\", \"s3Path\":\"s3://bucket/db/2020.01.02/taq/\", \"dbPath\":\"/2020.01.02/taq/\"}]</code> </p> </li> </ol>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_changeset_request.CreateKxChangesetRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_changeset_response.CreateKxChangesetResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_changeset

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_changeset.create_kx_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_changeset_request.CreateKxChangesetRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["change_requests"] = change_requests
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_cluster(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        cluster_type: "aws_sdk_finspace.types.kx_cluster_type.KxClusterType",
        release_label: "aws_sdk_finspace.types.release_label.ReleaseLabel",
        vpc_configuration: "aws_sdk_finspace.types.vpc_configuration.VpcConfiguration",
        az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
        tickerplant_log_configuration: Optional[
            "aws_sdk_finspace.types.tickerplant_log_configuration.TickerplantLogConfiguration"
        ] = None,
        databases: Optional[
            "aws_sdk_finspace.types.kx_database_configurations.KxDatabaseConfigurations"
        ] = None,
        cache_storage_configurations: Optional[
            "aws_sdk_finspace.types.kx_cache_storage_configurations.KxCacheStorageConfigurations"
        ] = None,
        auto_scaling_configuration: Optional[
            "aws_sdk_finspace.types.auto_scaling_configuration.AutoScalingConfiguration"
        ] = None,
        cluster_description: Optional[
            "aws_sdk_finspace.types.kx_cluster_description.KxClusterDescription"
        ] = None,
        capacity_configuration: Optional[
            "aws_sdk_finspace.types.capacity_configuration.CapacityConfiguration"
        ] = None,
        initialization_script: Optional[
            "aws_sdk_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
        ] = None,
        command_line_arguments: Optional[
            "aws_sdk_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
        ] = None,
        code: Optional[
            "aws_sdk_finspace.types.code_configuration.CodeConfiguration"
        ] = None,
        execution_role: Optional[
            "aws_sdk_finspace.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
        savedown_storage_configuration: Optional[
            "aws_sdk_finspace.types.kx_savedown_storage_configuration.KxSavedownStorageConfiguration"
        ] = None,
        availability_zone_id: Optional[
            "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
        scaling_group_configuration: Optional[
            "aws_sdk_finspace.types.kx_scaling_group_configuration.KxScalingGroupConfiguration"
        ] = None,
    ) -> "aws_sdk_finspace.types.create_kx_cluster_response.CreateKxClusterResponse":
        """<p>Creates a new kdb cluster.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A unique name for the cluster that you want to create.</p>
            cluster_type: <p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>
            tickerplant_log_configuration: <p> A configuration to store Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type <code>Tickerplant</code>, the location of the TP volume on the cluster will be available by using the global variable <code>.aws.tp_log_path</code>. </p>
            databases: <p>A list of databases that will be available for querying.</p>
            cache_storage_configurations: <p>The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store. </p>
            auto_scaling_configuration: <p>The configuration based on which FinSpace will scale in or scale out nodes in your cluster.</p>
            cluster_description: <p>A description of the cluster.</p>
            capacity_configuration: <p>A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.</p>
            release_label: <p>The version of FinSpace managed kdb to run.</p>
            vpc_configuration: <p>Configuration details about the network where the Privatelink endpoint of the cluster resides.</p>
            initialization_script: <p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p>
            command_line_arguments: <p>Defines the key-value pairs to make them available inside the cluster.</p>
            code: <p>The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster. </p>
            execution_role: <p>An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.</p>
            savedown_storage_configuration: <p>The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose <code>clusterType</code> as RDB. All the data written to this storage space is lost when the cluster node is restarted.</p>
            az_mode: <p>The number of availability zones you want to assign per cluster. This can be one of the following </p> <ul> <li> <p> <code>SINGLE</code> – Assigns one availability zone per cluster.</p> </li> <li> <p> <code>MULTI</code> – Assigns all the availability zones per cluster.</p> </li> </ul>
            availability_zone_id: <p>The availability zone identifiers for the requested regions.</p>
            tags: <p>A list of key-value pairs to label the cluster. You can add up to 50 tags to a cluster.</p>
            scaling_group_configuration: <p>The structure that stores the configuration details of a scaling group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_cluster_request.CreateKxClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_cluster_response.CreateKxClusterResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_cluster

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_cluster.create_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_cluster_request.CreateKxClusterRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        input["cluster_type"] = cluster_type
        if tickerplant_log_configuration is not None:
            input["tickerplant_log_configuration"] = tickerplant_log_configuration
        if databases is not None:
            input["databases"] = databases
        if cache_storage_configurations is not None:
            input["cache_storage_configurations"] = cache_storage_configurations
        if auto_scaling_configuration is not None:
            input["auto_scaling_configuration"] = auto_scaling_configuration
        if cluster_description is not None:
            input["cluster_description"] = cluster_description
        if capacity_configuration is not None:
            input["capacity_configuration"] = capacity_configuration
        input["release_label"] = release_label
        input["vpc_configuration"] = vpc_configuration
        if initialization_script is not None:
            input["initialization_script"] = initialization_script
        if command_line_arguments is not None:
            input["command_line_arguments"] = command_line_arguments
        if code is not None:
            input["code"] = code
        if execution_role is not None:
            input["execution_role"] = execution_role
        if savedown_storage_configuration is not None:
            input["savedown_storage_configuration"] = savedown_storage_configuration
        input["az_mode"] = az_mode
        if availability_zone_id is not None:
            input["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input["tags"] = tags
        if scaling_group_configuration is not None:
            input["scaling_group_configuration"] = scaling_group_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_database(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_finspace.types.create_kx_database_response.CreateKxDatabaseResponse":
        """<p>Creates a new kdb database in the environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            description: <p>A description of the database.</p>
            tags: <p>A list of key-value pairs to label the kdb database. You can add up to 50 tags to your kdb database</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_database_request.CreateKxDatabaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_database_response.CreateKxDatabaseResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_database

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_database.create_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_database_request.CreateKxDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_dataview(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName",
        az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        availability_zone_id: Optional[
            "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        changeset_id: Optional[
            "aws_sdk_finspace.types.changeset_id.ChangesetId"
        ] = None,
        segment_configurations: Optional[
            "aws_sdk_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
        ] = None,
        auto_update: Optional[
            "aws_sdk_finspace.types.boolean_value.booleanValue"
        ] = None,
        read_write: Optional[
            "aws_sdk_finspace.types.boolean_value.booleanValue"
        ] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_finspace.types.create_kx_dataview_response.CreateKxDataviewResponse":
        """<p> Creates a snapshot of kdb database with tiered storage capabilities and a pre-warmed cache, ready for mounting on kdb clusters. Dataviews are only available for clusters running on a scaling group. They are not supported on dedicated clusters. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, where you want to create the dataview. </p>
            database_name: <p> The name of the database where you want to create a dataview. </p>
            dataview_name: <p>A unique identifier for the dataview.</p>
            az_mode: <p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>
            availability_zone_id: <p> The identifier of the availability zones. </p>
            changeset_id: <p> A unique identifier of the changeset that you want to use to ingest data. </p>
            segment_configurations: <p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>
            auto_update: <p>The option to specify whether you want to apply all the future additions and corrections automatically to the dataview, when you ingest new changesets. The default value is false.</p>
            read_write: <p> The option to specify whether you want to make the dataview writable to perform database maintenance. The following are some considerations related to writable dataviews. </p> <ul> <li> <p>You cannot create partial writable dataviews. When you create writeable dataviews you must provide the entire database path.</p> </li> <li> <p>You cannot perform updates on a writeable dataview. Hence, <code>autoUpdate</code> must be set as <b>False</b> if <code>readWrite</code> is <b>True</b> for a dataview.</p> </li> <li> <p>You must also use a unique volume for creating a writeable dataview. So, if you choose a volume that is already in use by another dataview, the dataview creation fails.</p> </li> <li> <p>Once you create a dataview as writeable, you cannot change it to read-only. So, you cannot update the <code>readWrite</code> parameter later.</p> </li> </ul>
            description: <p>A description of the dataview.</p>
            tags: <p> A list of key-value pairs to label the dataview. You can add up to 50 tags to a dataview. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_dataview_request.CreateKxDataviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_dataview_response.CreateKxDataviewResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_dataview

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_dataview.create_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_dataview_request.CreateKxDataviewRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["dataview_name"] = dataview_name
        input["az_mode"] = az_mode
        if availability_zone_id is not None:
            input["availability_zone_id"] = availability_zone_id
        if changeset_id is not None:
            input["changeset_id"] = changeset_id
        if segment_configurations is not None:
            input["segment_configurations"] = segment_configurations
        if auto_update is not None:
            input["auto_update"] = auto_update
        if read_write is not None:
            input["read_write"] = read_write
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_environment(
        self,
        name: "aws_sdk_finspace.types.kx_environment_name.KxEnvironmentName",
        kms_key_id: "aws_sdk_finspace.types.kms_key_arn.KmsKeyARN",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.create_kx_environment_response.CreateKxEnvironmentResponse":
        """<p>Creates a managed kdb environment for the account.</p>

        Args:
            name: <p>The name of the kdb environment that you want to create.</p>
            description: <p>A description for the kdb environment.</p>
            kms_key_id: <p>The KMS key ID to encrypt your data in the FinSpace environment.</p>
            tags: <p>A list of key-value pairs to label the kdb environment. You can add up to 50 tags to your kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_environment_request.CreateKxEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_environment_response.CreateKxEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_environment.create_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_environment_request.CreateKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_scaling_group(
        self,
        client_token: "aws_sdk_finspace.types.client_token.ClientToken",
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        host_type: "aws_sdk_finspace.types.kx_host_type.KxHostType",
        availability_zone_id: "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_finspace.types.create_kx_scaling_group_response.CreateKxScalingGroupResponse":
        """<p>Creates a new scaling group. </p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment, where you want to create the scaling group. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>
            host_type: <p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.</p> <p>You can add one of the following values:</p> <ul> <li> <p> <code>kx.sg.large</code> – The host type with a configuration of 16 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.sg.xlarge</code> – The host type with a configuration of 32 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.sg.2xlarge</code> – The host type with a configuration of 64 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.sg.4xlarge</code> – The host type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.sg.8xlarge</code> – The host type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.sg.16xlarge</code> – The host type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg.32xlarge</code> – The host type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> <li> <p> <code>kx.sg1.16xlarge</code> – The host type with a configuration of 1949 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg1.24xlarge</code> – The host type with a configuration of 2948 GiB memory and 96 vCPUs.</p> </li> </ul>
            availability_zone_id: <p>The identifier of the availability zones.</p>
            tags: <p> A list of key-value pairs to label the scaling group. You can add up to 50 tags to a scaling group. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_scaling_group_request.CreateKxScalingGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_scaling_group_response.CreateKxScalingGroupResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_scaling_group

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_scaling_group.create_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_scaling_group_request.CreateKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["scaling_group_name"] = scaling_group_name
        input["host_type"] = host_type
        input["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_user(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString",
        iam_role: "aws_sdk_finspace.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.create_kx_user_response.CreateKxUserResponse":
        """<p>Creates a user in FinSpace kdb environment with an associated IAM role.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment where you want to create a user.</p>
            user_name: <p>A unique identifier for the user.</p>
            iam_role: <p>The IAM role ARN that will be associated with the user.</p>
            tags: <p>A list of key-value pairs to label the user. You can add up to 50 tags to a user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_user_request.CreateKxUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_user_response.CreateKxUserResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_user

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_user.create_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_user_request.CreateKxUserRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["user_name"] = user_name
        input["iam_role"] = iam_role
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_kx_volume(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_type: "aws_sdk_finspace.types.kx_volume_type.KxVolumeType",
        volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName",
        az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode",
        availability_zone_ids: "aws_sdk_finspace.types.availability_zone_ids.AvailabilityZoneIds",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        nas1_configuration: Optional[
            "aws_sdk_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
        ] = None,
        tags: Optional["aws_sdk_finspace.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_finspace.types.create_kx_volume_response.CreateKxVolumeResponse":
        """<p> Creates a new volume with a specific amount of throughput and storage capacity. </p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_type: <p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. When you select <code>NAS_1</code> volume type, you must also provide <code>nas1Configuration</code>. </p>
            volume_name: <p>A unique identifier for the volume.</p>
            description: <p> A description of the volume. </p>
            nas1_configuration: <p> Specifies the configuration for the Network attached storage (NAS_1) file system volume. This parameter is required when you choose <code>volumeType</code> as <i>NAS_1</i>.</p>
            az_mode: <p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>
            availability_zone_ids: <p>The identifier of the availability zones.</p>
            tags: <p> A list of key-value pairs to label the volume. You can add up to 50 tags to a volume. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.create_kx_volume_request.CreateKxVolumeRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.create_kx_volume_response.CreateKxVolumeResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_volume

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.create_kx_volume.create_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.create_kx_volume_request.CreateKxVolumeRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["environment_id"] = environment_id
        input["volume_type"] = volume_type
        input["volume_name"] = volume_name
        if description is not None:
            input["description"] = description
        if nas1_configuration is not None:
            input["nas1_configuration"] = nas1_configuration
        input["az_mode"] = az_mode
        input["availability_zone_ids"] = availability_zone_ids
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Delete an FinSpace environment.</p>

        Args:
            environment_id: <p>The identifier for the FinSpace environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_environment_request.DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_cluster(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_cluster_response.DeleteKxClusterResponse":
        """<p>Deletes a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_cluster_request.DeleteKxClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_cluster_response.DeleteKxClusterResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_cluster

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_cluster.delete_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_cluster_request.DeleteKxClusterRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_cluster_node(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        node_id: "aws_sdk_finspace.types.kx_cluster_node_id_string.KxClusterNodeIdString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_cluster_node_response.DeleteKxClusterNodeResponse":
        """<p>Deletes the specified nodes from a cluster. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster, for which you want to delete the nodes.</p>
            node_id: <p>A unique identifier for the node that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_cluster_node_request.DeleteKxClusterNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_cluster_node_response.DeleteKxClusterNodeResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_cluster_node

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_cluster_node.delete_kx_cluster_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_cluster_node_request.DeleteKxClusterNodeRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        input["node_id"] = node_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_database(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_database_response.DeleteKxDatabaseResponse":
        """<p>Deletes the specified database and all of its associated data. This action is irreversible. You must copy any data out of the database before deleting it if the data is to be retained.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_database_request.DeleteKxDatabaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_database_response.DeleteKxDatabaseResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_database

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_database.delete_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_database_request.DeleteKxDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_dataview(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_dataview_response.DeleteKxDataviewResponse":
        """<p> Deletes the specified dataview. Before deleting a dataview, make sure that it is not in use by any cluster. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>
            database_name: <p>The name of the database whose dataview you want to delete.</p>
            dataview_name: <p>The name of the dataview that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_dataview_request.DeleteKxDataviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_dataview_response.DeleteKxDataviewResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_dataview

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_dataview.delete_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_dataview_request.DeleteKxDataviewRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["dataview_name"] = dataview_name
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_environment_response.DeleteKxEnvironmentResponse":
        """<p>Deletes the kdb environment. This action is irreversible. Deleting a kdb environment will remove all the associated data and any services running in it. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_environment_request.DeleteKxEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_environment_response.DeleteKxEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_environment.delete_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_environment_request.DeleteKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_scaling_group(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_scaling_group_response.DeleteKxScalingGroupResponse":
        """<p> Deletes the specified scaling group. This action is irreversible. You cannot delete a scaling group until all the clusters running on it have been deleted.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_scaling_group_request.DeleteKxScalingGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_scaling_group_response.DeleteKxScalingGroupResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_scaling_group

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_scaling_group.delete_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_scaling_group_request.DeleteKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["scaling_group_name"] = scaling_group_name
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_user(
        self,
        user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString",
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_user_response.DeleteKxUserResponse":
        """<p>Deletes a user in the specified kdb environment.</p>

        Args:
            user_name: <p>A unique identifier for the user that you want to delete.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_user_request.DeleteKxUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_user_response.DeleteKxUserResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_user

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_user.delete_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_user_request.DeleteKxUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["environment_id"] = environment_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_kx_volume(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "aws_sdk_finspace.types.delete_kx_volume_response.DeleteKxVolumeResponse":
        """<p> Deletes a volume. You can only delete a volume if it's not attached to a cluster or a dataview. When a volume is deleted, any data on the volume is lost. This action is irreversible. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_name: <p> The name of the volume that you want to delete. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.delete_kx_volume_request.DeleteKxVolumeRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.delete_kx_volume_response.DeleteKxVolumeResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_volume

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.delete_kx_volume.delete_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.delete_kx_volume_request.DeleteKxVolumeRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["volume_name"] = volume_name
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns the FinSpace environment object.</p>

        Args:
            environment_id: <p>The identifier of the FinSpace environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_changeset(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        changeset_id: "aws_sdk_finspace.types.changeset_id.ChangesetId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_changeset_response.GetKxChangesetResponse":
        """<p>Returns information about a kdb changeset.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            changeset_id: <p>A unique identifier of the changeset for which you want to retrieve data.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_changeset_request.GetKxChangesetRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_changeset_response.GetKxChangesetResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_changeset

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_changeset.get_kx_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_changeset_request.GetKxChangesetRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["changeset_id"] = changeset_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_cluster(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_cluster_response.GetKxClusterResponse":
        """<p>Retrieves information about a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster that you want to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_cluster_request.GetKxClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_cluster_response.GetKxClusterResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_cluster

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_cluster.get_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_cluster_request.GetKxClusterRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_connection_string(
        self,
        user_arn: "aws_sdk_finspace.types.kx_user_arn.KxUserArn",
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_connection_string_response.GetKxConnectionStringResponse":
        """<p>Retrieves a connection string for a user to connect to a kdb cluster. You must call this API using the same role that you have defined while creating a user. </p>

        Args:
            user_arn: <p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A name of the kdb cluster.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_connection_string_request.GetKxConnectionStringRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_connection_string_response.GetKxConnectionStringResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_connection_string

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_connection_string.get_kx_connection_string(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_connection_string_request.GetKxConnectionStringRequest = {}  # type: ignore[typeddict-item]
        input["user_arn"] = user_arn
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_database(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_database_response.GetKxDatabaseResponse":
        """<p>Returns database information for the specified environment ID.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_database_request.GetKxDatabaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_database_response.GetKxDatabaseResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_database

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_database.get_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_database_request.GetKxDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_dataview(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_dataview_response.GetKxDataviewResponse":
        """<p> Retrieves details of the dataview. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to retrieve the dataview details.</p>
            database_name: <p> The name of the database where you created the dataview.</p>
            dataview_name: <p>A unique identifier for the dataview.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_dataview_request.GetKxDataviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_dataview_response.GetKxDataviewResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_dataview

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_dataview.get_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_dataview_request.GetKxDataviewRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["dataview_name"] = dataview_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_environment_response.GetKxEnvironmentResponse":
        """<p>Retrieves all the information for the specified kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_environment_request.GetKxEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_environment_response.GetKxEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_environment.get_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_environment_request.GetKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_scaling_group(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> (
        "aws_sdk_finspace.types.get_kx_scaling_group_response.GetKxScalingGroupResponse"
    ):
        """<p> Retrieves details of a scaling group.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_scaling_group_request.GetKxScalingGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_scaling_group_response.GetKxScalingGroupResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_scaling_group

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_scaling_group.get_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_scaling_group_request.GetKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["scaling_group_name"] = scaling_group_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_user(
        self,
        user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString",
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_user_response.GetKxUserResponse":
        """<p>Retrieves information about the specified kdb user.</p>

        Args:
            user_name: <p>A unique identifier for the user.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_user_request.GetKxUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_user_response.GetKxUserResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_user

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_user.get_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_user_request.GetKxUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_kx_volume(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.get_kx_volume_response.GetKxVolumeResponse":
        """<p> Retrieves the information about the volume. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_name: <p>A unique identifier for the volume.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.get_kx_volume_request.GetKxVolumeRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.get_kx_volume_response.GetKxVolumeResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_volume

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.get_kx_volume.get_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.get_kx_volume_request.GetKxVolumeRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["volume_name"] = volume_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "aws_sdk_finspace.types.list_environments_response.ListEnvironmentsResponse":
        """<p>A list of all of your FinSpace environments.</p>

        Args:
            next_token: <p>A token generated by FinSpace that specifies where to continue pagination if a previous request was truncated. To get the next set of pages, pass in the <code>nextToken</code>nextToken value from the response object of the previous page call.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_environments

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_changesets(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_finspace.types.list_kx_changesets_response.ListKxChangesetsResponse":
        """<p>Returns a list of all the changesets for a database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_changesets_request.ListKxChangesetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_changesets_response.ListKxChangesetsResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_changesets

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_changesets.list_kx_changesets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_changesets_request.ListKxChangesetsRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_cluster_nodes(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "aws_sdk_finspace.types.list_kx_cluster_nodes_response.ListKxClusterNodesResponse":
        """<p>Lists all the nodes in a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A unique name for the cluster.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_cluster_nodes_request.ListKxClusterNodesRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_cluster_nodes_response.ListKxClusterNodesResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_cluster_nodes

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_cluster_nodes.list_kx_cluster_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_cluster_nodes_request.ListKxClusterNodesRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_clusters(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        cluster_type: Optional[
            "aws_sdk_finspace.types.kx_cluster_type.KxClusterType"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.list_kx_clusters_response.ListKxClustersResponse":
        """<p>Returns a list of clusters.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_type: <p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_clusters_request.ListKxClustersRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_clusters_response.ListKxClustersResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_clusters

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_clusters.list_kx_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_clusters_request.ListKxClustersRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if cluster_type is not None:
            input["cluster_type"] = cluster_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_databases(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_finspace.types.list_kx_databases_response.ListKxDatabasesResponse":
        """<p>Returns a list of all the databases in the kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_databases_request.ListKxDatabasesRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_databases_response.ListKxDatabasesResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_databases

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_databases.list_kx_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_databases_request.ListKxDatabasesRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_dataviews(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_finspace.types.list_kx_dataviews_response.ListKxDataviewsResponse":
        """<p> Returns a list of all the dataviews in the database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, for which you want to retrieve a list of dataviews.</p>
            database_name: <p> The name of the database where the dataviews were created.</p>
            next_token: <p> A token that indicates where a results page should begin. </p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_dataviews_request.ListKxDataviewsRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_dataviews_response.ListKxDataviewsResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_dataviews

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_dataviews.list_kx_dataviews(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_dataviews_request.ListKxDataviewsRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace.types.boxed_integer.BoxedInteger"
        ] = None,
    ) -> "aws_sdk_finspace.types.list_kx_environments_response.ListKxEnvironmentsResponse":
        """<p>Returns a list of kdb environments created in an account.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_environments_request.ListKxEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_environments_response.ListKxEnvironmentsResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_environments

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_environments.list_kx_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_environments_request.ListKxEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_kx_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_finspace.types.boxed_integer.BoxedInteger"
        ] = None,
    ) -> "Iterator[aws_sdk_finspace.types.kx_environment.KxEnvironment]":
        _token = next_token
        while True:
            _response = self.list_kx_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_scaling_groups(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.list_kx_scaling_groups_response.ListKxScalingGroupsResponse":
        """<p> Returns a list of scaling groups in a kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, for which you want to retrieve a list of scaling groups.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p> A token that indicates where a results page should begin. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_scaling_groups_request.ListKxScalingGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_scaling_groups_response.ListKxScalingGroupsResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_scaling_groups

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_scaling_groups.list_kx_scaling_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_scaling_groups_request.ListKxScalingGroupsRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_users(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "aws_sdk_finspace.types.list_kx_users_response.ListKxUsersResponse":
        """<p>Lists all the users in a kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_users_request.ListKxUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_users_response.ListKxUsersResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_users

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_users.list_kx_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_users_request.ListKxUsersRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_kx_volumes(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        max_results: Optional["aws_sdk_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_finspace.types.pagination_token.PaginationToken"
        ] = None,
        volume_type: Optional[
            "aws_sdk_finspace.types.kx_volume_type.KxVolumeType"
        ] = None,
    ) -> "aws_sdk_finspace.types.list_kx_volumes_response.ListKxVolumesResponse":
        """<p> Lists all the volumes in a kdb environment. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            volume_type: <p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_kx_volumes_request.ListKxVolumesRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_kx_volumes_response.ListKxVolumesResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_volumes

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_kx_volumes.list_kx_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_kx_volumes_request.ListKxVolumesRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if volume_type is not None:
            input["volume_type"] = volume_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>A list of all tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        tags: "aws_sdk_finspace.types.tag_map.TagMap",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to a FinSpace resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource.</p>
            tags: <p>One or more tags to be assigned to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.tag_resource

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        tag_keys: "aws_sdk_finspace.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "aws_sdk_finspace.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from a FinSpace resource.</p>

        Args:
            resource_arn: <p>A FinSpace resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN).</p>
            tag_keys: <p>The tag keys (names) of one or more tags to be removed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.untag_resource

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        name: Optional[
            "aws_sdk_finspace.types.environment_name.EnvironmentName"
        ] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        federation_mode: Optional[
            "aws_sdk_finspace.types.federation_mode.FederationMode"
        ] = None,
        federation_parameters: Optional[
            "aws_sdk_finspace.types.federation_parameters.FederationParameters"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Update your FinSpace environment.</p>

        Args:
            environment_id: <p>The identifier of the FinSpace environment.</p>
            name: <p>The name of the environment.</p>
            description: <p>The description of the environment.</p>
            federation_mode: <p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_environment_request.UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if federation_mode is not None:
            input["federation_mode"] = federation_mode
        if federation_parameters is not None:
            input["federation_parameters"] = federation_parameters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_cluster_code_configuration(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        code: "aws_sdk_finspace.types.code_configuration.CodeConfiguration",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        initialization_script: Optional[
            "aws_sdk_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
        ] = None,
        command_line_arguments: Optional[
            "aws_sdk_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
        ] = None,
        deployment_configuration: Optional[
            "aws_sdk_finspace.types.kx_cluster_code_deployment_configuration.KxClusterCodeDeploymentConfiguration"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_cluster_code_configuration_response.UpdateKxClusterCodeConfigurationResponse":
        """<p> Allows you to update code configuration on a running cluster. By using this API you can update the code, the initialization script path, and the command line arguments for a specific cluster. The configuration that you want to update will override any existing configurations on the cluster. </p>

        Args:
            environment_id: <p> A unique identifier of the kdb environment. </p>
            cluster_name: <p>The name of the cluster.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            initialization_script: <p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>
            command_line_arguments: <p>Specifies the key-value pairs to make them available inside the cluster.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>
            deployment_configuration: <p> The configuration that allows you to choose how you want to update the code on a cluster. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_cluster_code_configuration_request.UpdateKxClusterCodeConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_cluster_code_configuration_response.UpdateKxClusterCodeConfigurationResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_cluster_code_configuration

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_cluster_code_configuration.update_kx_cluster_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_cluster_code_configuration_request.UpdateKxClusterCodeConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        if client_token is not None:
            input["client_token"] = client_token
        input["code"] = code
        if initialization_script is not None:
            input["initialization_script"] = initialization_script
        if command_line_arguments is not None:
            input["command_line_arguments"] = command_line_arguments
        if deployment_configuration is not None:
            input["deployment_configuration"] = deployment_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_cluster_databases(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName",
        databases: "aws_sdk_finspace.types.kx_database_configurations.KxDatabaseConfigurations",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        deployment_configuration: Optional[
            "aws_sdk_finspace.types.kx_deployment_configuration.KxDeploymentConfiguration"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_cluster_databases_response.UpdateKxClusterDatabasesResponse":
        """<p>Updates the databases mounted on a kdb cluster, which includes the <code>changesetId</code> and all the dbPaths to be cached. This API does not allow you to change a database name or add a database if you created a cluster without one. </p> <p>Using this API you can point a cluster to a different changeset and modify a list of partitions being cached.</p>

        Args:
            environment_id: <p>The unique identifier of a kdb environment.</p>
            cluster_name: <p>A unique name for the cluster that you want to modify.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            databases: <p> The structure of databases mounted on the cluster.</p>
            deployment_configuration: <p> The configuration that allows you to choose how you want to update the databases on a cluster. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_cluster_databases_request.UpdateKxClusterDatabasesRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_cluster_databases_response.UpdateKxClusterDatabasesResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_cluster_databases

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_cluster_databases.update_kx_cluster_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_cluster_databases_request.UpdateKxClusterDatabasesRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["cluster_name"] = cluster_name
        if client_token is not None:
            input["client_token"] = client_token
        input["databases"] = databases
        if deployment_configuration is not None:
            input["deployment_configuration"] = deployment_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_database(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
    ) -> "aws_sdk_finspace.types.update_kx_database_response.UpdateKxDatabaseResponse":
        """<p>Updates information for the given kdb database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            description: <p>A description of the database.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_database_request.UpdateKxDatabaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_database_response.UpdateKxDatabaseResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_database

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_database.update_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_database_request.UpdateKxDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        if description is not None:
            input["description"] = description
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_dataview(
        self,
        environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId",
        database_name: "aws_sdk_finspace.types.database_name.DatabaseName",
        dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName",
        client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        changeset_id: Optional[
            "aws_sdk_finspace.types.changeset_id.ChangesetId"
        ] = None,
        segment_configurations: Optional[
            "aws_sdk_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_dataview_response.UpdateKxDataviewResponse":
        """<p> Updates the specified dataview. The dataviews get automatically updated when any new changesets are ingested. Each update of the dataview creates a new version, including changeset details and cache configurations</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, where you want to update the dataview.</p>
            database_name: <p> The name of the database.</p>
            dataview_name: <p>The name of the dataview that you want to update.</p>
            description: <p> The description for a dataview. </p>
            changeset_id: <p>A unique identifier for the changeset.</p>
            segment_configurations: <p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_dataview_request.UpdateKxDataviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_dataview_response.UpdateKxDataviewResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_dataview

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_dataview.update_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_dataview_request.UpdateKxDataviewRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["database_name"] = database_name
        input["dataview_name"] = dataview_name
        if description is not None:
            input["description"] = description
        if changeset_id is not None:
            input["changeset_id"] = changeset_id
        if segment_configurations is not None:
            input["segment_configurations"] = segment_configurations
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_environment(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        name: Optional[
            "aws_sdk_finspace.types.kx_environment_name.KxEnvironmentName"
        ] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_environment_response.UpdateKxEnvironmentResponse":
        """<p>Updates information for the given kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            name: <p>The name of the kdb environment.</p>
            description: <p>A description of the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_environment_request.UpdateKxEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_environment_response.UpdateKxEnvironmentResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_environment

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_environment.update_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_environment_request.UpdateKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_environment_network(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        transit_gateway_configuration: Optional[
            "aws_sdk_finspace.types.transit_gateway_configuration.TransitGatewayConfiguration"
        ] = None,
        custom_dns_configuration: Optional[
            "aws_sdk_finspace.types.custom_dns_configuration.CustomDNSConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_environment_network_response.UpdateKxEnvironmentNetworkResponse":
        """<p>Updates environment network to connect to your internal network by using a transit gateway. This API supports request to create a transit gateway attachment from FinSpace VPC to your transit gateway ID and create a custom Route-53 outbound resolvers.</p> <p>Once you send a request to update a network, you cannot change it again. Network update might require termination of any clusters that are running in the existing network.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            transit_gateway_configuration: <p>Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.</p>
            custom_dns_configuration: <p>A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_environment_network_request.UpdateKxEnvironmentNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_environment_network_response.UpdateKxEnvironmentNetworkResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_environment_network

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_environment_network.update_kx_environment_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_environment_network_request.UpdateKxEnvironmentNetworkRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        if transit_gateway_configuration is not None:
            input["transit_gateway_configuration"] = transit_gateway_configuration
        if custom_dns_configuration is not None:
            input["custom_dns_configuration"] = custom_dns_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_user(
        self,
        environment_id: "aws_sdk_finspace.types.id_type.IdType",
        user_name: "aws_sdk_finspace.types.kx_user_name_string.KxUserNameString",
        iam_role: "aws_sdk_finspace.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_user_response.UpdateKxUserResponse":
        """<p>Updates the user details. You can only update the IAM role associated with a user.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            user_name: <p>A unique identifier for the user.</p>
            iam_role: <p>The IAM role ARN that is associated with the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_user_request.UpdateKxUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_user_response.UpdateKxUserResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_user

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_user.update_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_user_request.UpdateKxUserRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["user_name"] = user_name
        input["iam_role"] = iam_role
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_kx_volume(
        self,
        environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["aws_sdk_finspace.types.description.Description"] = None,
        client_token: Optional[
            "aws_sdk_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        nas1_configuration: Optional[
            "aws_sdk_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
        ] = None,
    ) -> "aws_sdk_finspace.types.update_kx_volume_response.UpdateKxVolumeResponse":
        """<p> Updates the throughput or capacity of a volume. During the update process, the filesystem might be unavailable for a few minutes. You can retry any operations after the update is complete. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment where you created the storage volume. </p>
            volume_name: <p> A unique identifier for the volume.</p>
            description: <p> A description of the volume. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            nas1_configuration: <p> Specifies the configuration for the Network attached storage (NAS_1) file system volume.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_finspace.types.update_kx_volume_request.UpdateKxVolumeRequest]",
        ) -> OperationResponse[
            "aws_sdk_finspace.types.update_kx_volume_response.UpdateKxVolumeResponse"
        ]:
            import aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_volume

            output, http_response = (
                aws_sdk_finspace._operations.aws_habanero_management_service.update_kx_volume.update_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_finspace.types.update_kx_volume_request.UpdateKxVolumeRequest = {}  # type: ignore[typeddict-item]
        input["environment_id"] = environment_id
        input["volume_name"] = volume_name
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token
        if nas1_configuration is not None:
            input["nas1_configuration"] = nas1_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
