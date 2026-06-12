"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CodeStar_connections_20191201``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_codestar_connections._auth._identity import Credentials
from aws_sdk_codestar_connections._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_codestar_connections._auth._zapros_handler import AuthMiddleware
from aws_sdk_codestar_connections._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.amazon_resource_name
    import aws_sdk_codestar_connections.types.branch_name
    import aws_sdk_codestar_connections.types.connection_arn
    import aws_sdk_codestar_connections.types.connection_name
    import aws_sdk_codestar_connections.types.create_connection_input
    import aws_sdk_codestar_connections.types.create_connection_output
    import aws_sdk_codestar_connections.types.create_host_input
    import aws_sdk_codestar_connections.types.create_host_output
    import aws_sdk_codestar_connections.types.create_repository_link_input
    import aws_sdk_codestar_connections.types.create_repository_link_output
    import aws_sdk_codestar_connections.types.create_sync_configuration_input
    import aws_sdk_codestar_connections.types.create_sync_configuration_output
    import aws_sdk_codestar_connections.types.delete_connection_input
    import aws_sdk_codestar_connections.types.delete_connection_output
    import aws_sdk_codestar_connections.types.delete_host_input
    import aws_sdk_codestar_connections.types.delete_host_output
    import aws_sdk_codestar_connections.types.delete_repository_link_input
    import aws_sdk_codestar_connections.types.delete_repository_link_output
    import aws_sdk_codestar_connections.types.delete_sync_configuration_input
    import aws_sdk_codestar_connections.types.delete_sync_configuration_output
    import aws_sdk_codestar_connections.types.deployment_file_path
    import aws_sdk_codestar_connections.types.get_connection_input
    import aws_sdk_codestar_connections.types.get_connection_output
    import aws_sdk_codestar_connections.types.get_host_input
    import aws_sdk_codestar_connections.types.get_host_output
    import aws_sdk_codestar_connections.types.get_repository_link_input
    import aws_sdk_codestar_connections.types.get_repository_link_output
    import aws_sdk_codestar_connections.types.get_repository_sync_status_input
    import aws_sdk_codestar_connections.types.get_repository_sync_status_output
    import aws_sdk_codestar_connections.types.get_resource_sync_status_input
    import aws_sdk_codestar_connections.types.get_resource_sync_status_output
    import aws_sdk_codestar_connections.types.get_sync_blocker_summary_input
    import aws_sdk_codestar_connections.types.get_sync_blocker_summary_output
    import aws_sdk_codestar_connections.types.get_sync_configuration_input
    import aws_sdk_codestar_connections.types.get_sync_configuration_output
    import aws_sdk_codestar_connections.types.host_arn
    import aws_sdk_codestar_connections.types.host_name
    import aws_sdk_codestar_connections.types.iam_role_arn
    import aws_sdk_codestar_connections.types.id
    import aws_sdk_codestar_connections.types.kms_key_arn
    import aws_sdk_codestar_connections.types.list_connections_input
    import aws_sdk_codestar_connections.types.list_connections_output
    import aws_sdk_codestar_connections.types.list_hosts_input
    import aws_sdk_codestar_connections.types.list_hosts_output
    import aws_sdk_codestar_connections.types.list_repository_links_input
    import aws_sdk_codestar_connections.types.list_repository_links_output
    import aws_sdk_codestar_connections.types.list_repository_sync_definitions_input
    import aws_sdk_codestar_connections.types.list_repository_sync_definitions_output
    import aws_sdk_codestar_connections.types.list_sync_configurations_input
    import aws_sdk_codestar_connections.types.list_sync_configurations_output
    import aws_sdk_codestar_connections.types.list_tags_for_resource_input
    import aws_sdk_codestar_connections.types.list_tags_for_resource_output
    import aws_sdk_codestar_connections.types.max_results
    import aws_sdk_codestar_connections.types.next_token
    import aws_sdk_codestar_connections.types.owner_id
    import aws_sdk_codestar_connections.types.provider_type
    import aws_sdk_codestar_connections.types.publish_deployment_status
    import aws_sdk_codestar_connections.types.repository_link_id
    import aws_sdk_codestar_connections.types.repository_name
    import aws_sdk_codestar_connections.types.resolved_reason
    import aws_sdk_codestar_connections.types.resource_name
    import aws_sdk_codestar_connections.types.sharp_next_token
    import aws_sdk_codestar_connections.types.sync_configuration_type
    import aws_sdk_codestar_connections.types.tag_key_list
    import aws_sdk_codestar_connections.types.tag_list
    import aws_sdk_codestar_connections.types.tag_resource_input
    import aws_sdk_codestar_connections.types.tag_resource_output
    import aws_sdk_codestar_connections.types.trigger_resource_update_on
    import aws_sdk_codestar_connections.types.untag_resource_input
    import aws_sdk_codestar_connections.types.untag_resource_output
    import aws_sdk_codestar_connections.types.update_host_input
    import aws_sdk_codestar_connections.types.update_host_output
    import aws_sdk_codestar_connections.types.update_repository_link_input
    import aws_sdk_codestar_connections.types.update_repository_link_output
    import aws_sdk_codestar_connections.types.update_sync_blocker_input
    import aws_sdk_codestar_connections.types.update_sync_blocker_output
    import aws_sdk_codestar_connections.types.update_sync_configuration_input
    import aws_sdk_codestar_connections.types.update_sync_configuration_output
    import aws_sdk_codestar_connections.types.url
    import aws_sdk_codestar_connections.types.vpc_configuration


class CodeStarconnectionsClientConfig(TypedDict, total=False):
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


class CodeStarconnectionsClient:
    """A client for the ``CodeStarconnections`` service.

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
        self.config = CodeStarconnectionsClientConfig(
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
        self, config_overrides: Optional[CodeStarconnectionsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CodeStarconnectionsClientConfig = config_overrides or {}
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

    def create_connection(
        self,
        connection_name: "aws_sdk_codestar_connections.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        provider_type: Optional[
            "aws_sdk_codestar_connections.types.provider_type.ProviderType"
        ] = None,
        tags: Optional["aws_sdk_codestar_connections.types.tag_list.TagList"] = None,
        host_arn: Optional[
            "aws_sdk_codestar_connections.types.host_arn.HostArn"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.create_connection_output.CreateConnectionOutput":
        """<p>Creates a connection that can then be given to other Amazon Web Services services like CodePipeline so that it can access third-party code repositories. The connection is in pending status until the third-party connection handshake is completed from the console.</p>

        Args:
            provider_type: <p>The name of the external provider where your third-party code repository is configured.</p>
            connection_name: <p>The name of the connection to be created.</p>
            tags: <p>The key-value pair to use when tagging the resource.</p>
            host_arn: <p>The Amazon Resource Name (ARN) of the host associated with the connection to be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.create_connection_input.CreateConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.create_connection_output.CreateConnectionOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_connection

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_connection.create_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.create_connection_input.CreateConnectionInput = {}  # type: ignore[typeddict-item]
        if provider_type is not None:
            input["provider_type"] = provider_type
        input["connection_name"] = connection_name
        if tags is not None:
            input["tags"] = tags
        if host_arn is not None:
            input["host_arn"] = host_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_host(
        self,
        name: "aws_sdk_codestar_connections.types.host_name.HostName",
        provider_type: "aws_sdk_codestar_connections.types.provider_type.ProviderType",
        provider_endpoint: "aws_sdk_codestar_connections.types.url.Url",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        vpc_configuration: Optional[
            "aws_sdk_codestar_connections.types.vpc_configuration.VpcConfiguration"
        ] = None,
        tags: Optional["aws_sdk_codestar_connections.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_codestar_connections.types.create_host_output.CreateHostOutput":
        """<p>Creates a resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.</p> <note> <p>A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.</p> </note>

        Args:
            name: <p>The name of the host to be created.</p>
            provider_type: <p>The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.</p>
            provider_endpoint: <p>The endpoint of the infrastructure to be represented by the host after it is created.</p>
            vpc_configuration: <p>The VPC configuration to be provisioned for the host. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>
            tags: <p>Tags for the host to be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.create_host_input.CreateHostInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.create_host_output.CreateHostOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_host

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_host.create_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.create_host_input.CreateHostInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["provider_type"] = provider_type
        input["provider_endpoint"] = provider_endpoint
        if vpc_configuration is not None:
            input["vpc_configuration"] = vpc_configuration
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_repository_link(
        self,
        connection_arn: "aws_sdk_codestar_connections.types.connection_arn.ConnectionArn",
        owner_id: "aws_sdk_codestar_connections.types.owner_id.OwnerId",
        repository_name: "aws_sdk_codestar_connections.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        encryption_key_arn: Optional[
            "aws_sdk_codestar_connections.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_codestar_connections.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_codestar_connections.types.create_repository_link_output.CreateRepositoryLinkOutput":
        """<p>Creates a link to a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection to be associated with the repository link.</p>
            owner_id: <p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>
            repository_name: <p>The name of the repository to be associated with the repository link.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) encryption key for the repository to be associated with the repository link.</p>
            tags: <p>The tags for the repository to be associated with the repository link.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.create_repository_link_input.CreateRepositoryLinkInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.create_repository_link_output.CreateRepositoryLinkOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_repository_link

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_repository_link.create_repository_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.create_repository_link_input.CreateRepositoryLinkInput = {}  # type: ignore[typeddict-item]
        input["connection_arn"] = connection_arn
        input["owner_id"] = owner_id
        input["repository_name"] = repository_name
        if encryption_key_arn is not None:
            input["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_sync_configuration(
        self,
        branch: "aws_sdk_codestar_connections.types.branch_name.BranchName",
        config_file: "aws_sdk_codestar_connections.types.deployment_file_path.DeploymentFilePath",
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        role_arn: "aws_sdk_codestar_connections.types.iam_role_arn.IamRoleArn",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        publish_deployment_status: Optional[
            "aws_sdk_codestar_connections.types.publish_deployment_status.PublishDeploymentStatus"
        ] = None,
        trigger_resource_update_on: Optional[
            "aws_sdk_codestar_connections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.create_sync_configuration_output.CreateSyncConfigurationOutput":
        """<p>Creates a sync configuration which allows Amazon Web Services to sync content from a Git repository to update a specified Amazon Web Services resource. Parameters for the sync configuration are determined by the sync type.</p>

        Args:
            branch: <p>The branch in the repository from which changes will be synced.</p>
            config_file: <p>The file name of the configuration file that manages syncing between the connection and the repository. This configuration file is stored in the repository.</p>
            repository_link_id: <p>The ID of the repository link created for the connection. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>
            resource_name: <p>The name of the Amazon Web Services resource (for example, a CloudFormation stack in the case of CFN_STACK_SYNC) that will be synchronized from the linked repository.</p>
            role_arn: <p>The ARN of the IAM role that grants permission for Amazon Web Services to use Git sync to update a given Amazon Web Services resource on your behalf.</p>
            sync_type: <p>The type of sync configuration.</p>
            publish_deployment_status: <p>Whether to enable or disable publishing of deployment status to source providers.</p>
            trigger_resource_update_on: <p>When to trigger Git sync to begin the stack update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.create_sync_configuration_input.CreateSyncConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.create_sync_configuration_output.CreateSyncConfigurationOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_sync_configuration

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.create_sync_configuration.create_sync_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.create_sync_configuration_input.CreateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
        input["branch"] = branch
        input["config_file"] = config_file
        input["repository_link_id"] = repository_link_id
        input["resource_name"] = resource_name
        input["role_arn"] = role_arn
        input["sync_type"] = sync_type
        if publish_deployment_status is not None:
            input["publish_deployment_status"] = publish_deployment_status
        if trigger_resource_update_on is not None:
            input["trigger_resource_update_on"] = trigger_resource_update_on

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connection(
        self,
        connection_arn: "aws_sdk_codestar_connections.types.connection_arn.ConnectionArn",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.delete_connection_output.DeleteConnectionOutput":
        """<p>The connection to be deleted.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection to be deleted.</p> <note> <p>The ARN is never reused if the connection is deleted.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.delete_connection_input.DeleteConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.delete_connection_output.DeleteConnectionOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_connection

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.delete_connection_input.DeleteConnectionInput = {}  # type: ignore[typeddict-item]
        input["connection_arn"] = connection_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_host(
        self,
        host_arn: "aws_sdk_codestar_connections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.delete_host_output.DeleteHostOutput":
        """<p>The host to be deleted. Before you delete a host, all connections associated to the host must be deleted.</p> <note> <p>A host cannot be deleted if it is in the VPC_CONFIG_INITIALIZING or VPC_CONFIG_DELETING state.</p> </note>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the host to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.delete_host_input.DeleteHostInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.delete_host_output.DeleteHostOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_host

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_host.delete_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.delete_host_input.DeleteHostInput = {}  # type: ignore[typeddict-item]
        input["host_arn"] = host_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_repository_link(
        self,
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.delete_repository_link_output.DeleteRepositoryLinkOutput":
        """<p>Deletes the association between your connection and a specified external Git repository.</p>

        Args:
            repository_link_id: <p>The ID of the repository link to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.delete_repository_link_input.DeleteRepositoryLinkInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.delete_repository_link_output.DeleteRepositoryLinkOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_repository_link

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_repository_link.delete_repository_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.delete_repository_link_input.DeleteRepositoryLinkInput = {}  # type: ignore[typeddict-item]
        input["repository_link_id"] = repository_link_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_sync_configuration(
        self,
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.delete_sync_configuration_output.DeleteSyncConfigurationOutput":
        """<p>Deletes the sync configuration for a specified repository and connection.</p>

        Args:
            sync_type: <p>The type of sync configuration to be deleted.</p>
            resource_name: <p>The name of the Amazon Web Services resource associated with the sync configuration to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.delete_sync_configuration_input.DeleteSyncConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.delete_sync_configuration_output.DeleteSyncConfigurationOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_sync_configuration

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.delete_sync_configuration.delete_sync_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.delete_sync_configuration_input.DeleteSyncConfigurationInput = {}  # type: ignore[typeddict-item]
        input["sync_type"] = sync_type
        input["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connection(
        self,
        connection_arn: "aws_sdk_codestar_connections.types.connection_arn.ConnectionArn",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_connection_output.GetConnectionOutput":
        """<p>Returns the connection ARN and details such as status, owner, and provider type.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of a connection.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_connection_input.GetConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_connection_output.GetConnectionOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_connection

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_connection_input.GetConnectionInput = {}  # type: ignore[typeddict-item]
        input["connection_arn"] = connection_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_host(
        self,
        host_arn: "aws_sdk_codestar_connections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_host_output.GetHostOutput":
        """<p>Returns the host ARN and details such as status, provider type, endpoint, and, if applicable, the VPC configuration.</p>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the requested host.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_host_input.GetHostInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_host_output.GetHostOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_host

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_host.get_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_host_input.GetHostInput = {}  # type: ignore[typeddict-item]
        input["host_arn"] = host_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_repository_link(
        self,
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_repository_link_output.GetRepositoryLinkOutput":
        """<p>Returns details about a repository link. A repository link allows Git sync to monitor and sync changes from files in a specified Git repository.</p>

        Args:
            repository_link_id: <p>The ID of the repository link to get.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_repository_link_input.GetRepositoryLinkInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_repository_link_output.GetRepositoryLinkOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_repository_link

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_repository_link.get_repository_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_repository_link_input.GetRepositoryLinkInput = {}  # type: ignore[typeddict-item]
        input["repository_link_id"] = repository_link_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_repository_sync_status(
        self,
        branch: "aws_sdk_codestar_connections.types.branch_name.BranchName",
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput":
        """<p>Returns details about the sync status for a repository. A repository sync uses Git sync to push and pull changes from your remote repository.</p>

        Args:
            branch: <p>The branch of the repository link for the requested repository sync status.</p>
            repository_link_id: <p>The repository link ID for the requested repository sync status.</p>
            sync_type: <p>The sync type of the requested sync status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_repository_sync_status_input.GetRepositorySyncStatusInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_repository_sync_status

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_repository_sync_status.get_repository_sync_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_repository_sync_status_input.GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
        input["branch"] = branch
        input["repository_link_id"] = repository_link_id
        input["sync_type"] = sync_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_sync_status(
        self,
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_resource_sync_status_output.GetResourceSyncStatusOutput":
        """<p>Returns the status of the sync with the Git repository for a specific Amazon Web Services resource.</p>

        Args:
            resource_name: <p>The name of the Amazon Web Services resource for the sync status with the Git repository.</p>
            sync_type: <p>The sync type for the sync status with the Git repository.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_resource_sync_status_input.GetResourceSyncStatusInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_resource_sync_status_output.GetResourceSyncStatusOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_resource_sync_status

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_resource_sync_status.get_resource_sync_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_resource_sync_status_input.GetResourceSyncStatusInput = {}  # type: ignore[typeddict-item]
        input["resource_name"] = resource_name
        input["sync_type"] = sync_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_sync_blocker_summary(
        self,
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput":
        """<p>Returns a list of the most recent sync blockers.</p>

        Args:
            sync_type: <p>The sync type for the sync blocker summary.</p>
            resource_name: <p>The name of the Amazon Web Services resource currently blocked from automatically being synced from a Git repository.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_sync_blocker_summary

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_sync_blocker_summary.get_sync_blocker_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput = {}  # type: ignore[typeddict-item]
        input["sync_type"] = sync_type
        input["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_sync_configuration(
        self,
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.get_sync_configuration_output.GetSyncConfigurationOutput":
        """<p>Returns details about a sync configuration, including the sync type and resource name. A sync configuration allows the configuration to sync (push and pull) changes from the remote repository for a specified branch in a Git repository.</p>

        Args:
            sync_type: <p>The sync type for the sync configuration for which you want to retrieve information.</p>
            resource_name: <p>The name of the Amazon Web Services resource for the sync configuration for which you want to retrieve information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.get_sync_configuration_input.GetSyncConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.get_sync_configuration_output.GetSyncConfigurationOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_sync_configuration

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.get_sync_configuration.get_sync_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.get_sync_configuration_input.GetSyncConfigurationInput = {}  # type: ignore[typeddict-item]
        input["sync_type"] = sync_type
        input["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_connections(
        self,
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        provider_type_filter: Optional[
            "aws_sdk_codestar_connections.types.provider_type.ProviderType"
        ] = None,
        host_arn_filter: Optional[
            "aws_sdk_codestar_connections.types.host_arn.HostArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_codestar_connections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_codestar_connections.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.list_connections_output.ListConnectionsOutput":
        """<p>Lists the connections associated with your account.</p>

        Args:
            provider_type_filter: <p>Filters the list of connections to those associated with a specified provider, such as Bitbucket.</p>
            host_arn_filter: <p>Filters the list of connections to those associated with a specified host.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token that was returned from the previous <code>ListConnections</code> call, which can be used to return the next set of connections in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_connections_input.ListConnectionsInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_connections_output.ListConnectionsOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_connections

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_connections.list_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_connections_input.ListConnectionsInput = {}  # type: ignore[typeddict-item]
        if provider_type_filter is not None:
            input["provider_type_filter"] = provider_type_filter
        if host_arn_filter is not None:
            input["host_arn_filter"] = host_arn_filter
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

    def list_hosts(
        self,
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_codestar_connections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_codestar_connections.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.list_hosts_output.ListHostsOutput":
        """<p>Lists the hosts associated with your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token that was returned from the previous <code>ListHosts</code> call, which can be used to return the next set of hosts in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_hosts_input.ListHostsInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_hosts_output.ListHostsOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_hosts

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_hosts.list_hosts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_hosts_input.ListHostsInput = {}  # type: ignore[typeddict-item]
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

    def list_repository_links(
        self,
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_codestar_connections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_codestar_connections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.list_repository_links_output.ListRepositoryLinksOutput":
        """<p>Lists the repository links created for connections in your account.</p>

        Args:
            max_results: <p> A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p> An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_repository_links_input.ListRepositoryLinksInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_repository_links_output.ListRepositoryLinksOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_repository_links

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_repository_links.list_repository_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_repository_links_input.ListRepositoryLinksInput = {}  # type: ignore[typeddict-item]
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

    def list_repository_sync_definitions(
        self,
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput":
        """<p>Lists the repository sync definitions for repository links in your account.</p>

        Args:
            repository_link_id: <p>The ID of the repository link for the sync definition for which you want to retrieve information.</p>
            sync_type: <p>The sync type of the repository link for the the sync definition for which you want to retrieve information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_repository_sync_definitions

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_repository_sync_definitions.list_repository_sync_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput = {}  # type: ignore[typeddict-item]
        input["repository_link_id"] = repository_link_id
        input["sync_type"] = sync_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_sync_configurations(
        self,
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_codestar_connections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_codestar_connections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.list_sync_configurations_output.ListSyncConfigurationsOutput":
        """<p>Returns a list of sync configurations for a specified repository.</p>

        Args:
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p>An enumeration token that allows the operation to batch the results of the operation.</p>
            repository_link_id: <p>The ID of the repository link for the requested list of sync configurations.</p>
            sync_type: <p>The sync type for the requested list of sync configurations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_sync_configurations_input.ListSyncConfigurationsInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_sync_configurations_output.ListSyncConfigurationsOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_sync_configurations

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_sync_configurations.list_sync_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_sync_configurations_input.ListSyncConfigurationsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["repository_link_id"] = repository_link_id
        input["sync_type"] = sync_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_codestar_connections.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Gets the set of key-value pairs (metadata) that are used to manage the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_tags_for_resource

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_codestar_connections.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_codestar_connections.types.tag_list.TagList",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.tag_resource_output.TagResourceOutput":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>
            tags: <p>The tags you want to modify or add to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.tag_resource

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_codestar_connections.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_codestar_connections.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The list of keys for the tags to be removed from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.untag_resource

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_host(
        self,
        host_arn: "aws_sdk_codestar_connections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        provider_endpoint: Optional[
            "aws_sdk_codestar_connections.types.url.Url"
        ] = None,
        vpc_configuration: Optional[
            "aws_sdk_codestar_connections.types.vpc_configuration.VpcConfiguration"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.update_host_output.UpdateHostOutput":
        """<p>Updates a specified host with the provided configurations.</p>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the host to be updated.</p>
            provider_endpoint: <p>The URL or endpoint of the host to be updated.</p>
            vpc_configuration: <p>The VPC configuration of the host to be updated. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.update_host_input.UpdateHostInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.update_host_output.UpdateHostOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_host

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_host.update_host(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.update_host_input.UpdateHostInput = {}  # type: ignore[typeddict-item]
        input["host_arn"] = host_arn
        if provider_endpoint is not None:
            input["provider_endpoint"] = provider_endpoint
        if vpc_configuration is not None:
            input["vpc_configuration"] = vpc_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_repository_link(
        self,
        repository_link_id: "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        connection_arn: Optional[
            "aws_sdk_codestar_connections.types.connection_arn.ConnectionArn"
        ] = None,
        encryption_key_arn: Optional[
            "aws_sdk_codestar_connections.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.update_repository_link_output.UpdateRepositoryLinkOutput":
        """<p>Updates the association between your connection and a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection for the repository link to be updated. The updated connection ARN must have the same providerType (such as GitHub) as the original connection ARN for the repo link.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the encryption key for the repository link to be updated.</p>
            repository_link_id: <p>The ID of the repository link to be updated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.update_repository_link_input.UpdateRepositoryLinkInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.update_repository_link_output.UpdateRepositoryLinkOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_repository_link

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_repository_link.update_repository_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.update_repository_link_input.UpdateRepositoryLinkInput = {}  # type: ignore[typeddict-item]
        if connection_arn is not None:
            input["connection_arn"] = connection_arn
        if encryption_key_arn is not None:
            input["encryption_key_arn"] = encryption_key_arn
        input["repository_link_id"] = repository_link_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_sync_blocker(
        self,
        id: "aws_sdk_codestar_connections.types.id.Id",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        resolved_reason: "aws_sdk_codestar_connections.types.resolved_reason.ResolvedReason",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
    ) -> "aws_sdk_codestar_connections.types.update_sync_blocker_output.UpdateSyncBlockerOutput":
        """<p>Allows you to update the status of a sync blocker, resolving the blocker and allowing syncing to continue.</p>

        Args:
            id: <p>The ID of the sync blocker to be updated.</p>
            sync_type: <p>The sync type of the sync blocker to be updated.</p>
            resource_name: <p>The name of the resource for the sync blocker to be updated.</p>
            resolved_reason: <p>The reason for resolving the sync blocker.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.update_sync_blocker_input.UpdateSyncBlockerInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.update_sync_blocker_output.UpdateSyncBlockerOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_sync_blocker

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_sync_blocker.update_sync_blocker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.update_sync_blocker_input.UpdateSyncBlockerInput = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["sync_type"] = sync_type
        input["resource_name"] = resource_name
        input["resolved_reason"] = resolved_reason

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_sync_configuration(
        self,
        resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName",
        sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[CodeStarconnectionsClientConfig] = None,
        branch: Optional[
            "aws_sdk_codestar_connections.types.branch_name.BranchName"
        ] = None,
        config_file: Optional[
            "aws_sdk_codestar_connections.types.deployment_file_path.DeploymentFilePath"
        ] = None,
        repository_link_id: Optional[
            "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId"
        ] = None,
        role_arn: Optional[
            "aws_sdk_codestar_connections.types.iam_role_arn.IamRoleArn"
        ] = None,
        publish_deployment_status: Optional[
            "aws_sdk_codestar_connections.types.publish_deployment_status.PublishDeploymentStatus"
        ] = None,
        trigger_resource_update_on: Optional[
            "aws_sdk_codestar_connections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
        ] = None,
    ) -> "aws_sdk_codestar_connections.types.update_sync_configuration_output.UpdateSyncConfigurationOutput":
        """<p>Updates the sync configuration for your connection and a specified external Git repository.</p>

        Args:
            branch: <p>The branch for the sync configuration to be updated.</p>
            config_file: <p>The configuration file for the sync configuration to be updated.</p>
            repository_link_id: <p>The ID of the repository link for the sync configuration to be updated.</p>
            resource_name: <p>The name of the Amazon Web Services resource for the sync configuration to be updated.</p>
            role_arn: <p>The ARN of the IAM role for the sync configuration to be updated.</p>
            sync_type: <p>The sync type for the sync configuration to be updated.</p>
            publish_deployment_status: <p>Whether to enable or disable publishing of deployment status to source providers.</p>
            trigger_resource_update_on: <p>When to trigger Git sync to begin the stack update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codestar_connections.types.update_sync_configuration_input.UpdateSyncConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_codestar_connections.types.update_sync_configuration_output.UpdateSyncConfigurationOutput"
        ]:
            import aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_sync_configuration

            output, http_response = (
                aws_sdk_codestar_connections._operations.code_star_connections_20191201.update_sync_configuration.update_sync_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_codestar_connections.types.update_sync_configuration_input.UpdateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
        if branch is not None:
            input["branch"] = branch
        if config_file is not None:
            input["config_file"] = config_file
        if repository_link_id is not None:
            input["repository_link_id"] = repository_link_id
        input["resource_name"] = resource_name
        if role_arn is not None:
            input["role_arn"] = role_arn
        input["sync_type"] = sync_type
        if publish_deployment_status is not None:
            input["publish_deployment_status"] = publish_deployment_status
        if trigger_resource_update_on is not None:
            input["trigger_resource_update_on"] = trigger_resource_update_on

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
