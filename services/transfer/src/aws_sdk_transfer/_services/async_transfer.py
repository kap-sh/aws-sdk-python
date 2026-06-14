"""Generated from Smithy shape ``com.amazonaws.transfer#TransferService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_transfer._auth._signers
import aws_sdk_transfer._auth._sigv4
from aws_sdk_transfer._auth._identity import Credentials
from aws_sdk_transfer._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_transfer._auth._zapros_handler import AuthMiddleware
from aws_sdk_transfer._pagination import resolve_path as _resolve_path
from aws_sdk_transfer._resources.transfer_service.agreement_resource import (
    AsyncAgreementResource,
)
from aws_sdk_transfer._resources.transfer_service.certificate_resource import (
    AsyncCertificateResource,
)
from aws_sdk_transfer._resources.transfer_service.connector_resource import (
    AsyncConnectorResource,
)
from aws_sdk_transfer._resources.transfer_service.profile_resource import (
    AsyncProfileResource,
)
from aws_sdk_transfer._resources.transfer_service.server_resource import (
    AsyncServerResource,
)
from aws_sdk_transfer._resources.transfer_service.user_resource import AsyncUserResource
from aws_sdk_transfer._resources.transfer_service.web_app_customization_resource import (
    AsyncWebAppCustomizationResource,
)
from aws_sdk_transfer._resources.transfer_service.web_app_resource import (
    AsyncWebAppResource,
)
from aws_sdk_transfer._resources.transfer_service.workflow_resource import (
    AsyncWorkflowResource,
)
from aws_sdk_transfer._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.callback_token
    import aws_sdk_transfer.types.connector_file_transfer_result
    import aws_sdk_transfer.types.connector_id
    import aws_sdk_transfer.types.create_access_request
    import aws_sdk_transfer.types.create_access_response
    import aws_sdk_transfer.types.custom_http_headers
    import aws_sdk_transfer.types.custom_step_status
    import aws_sdk_transfer.types.delete_access_request
    import aws_sdk_transfer.types.delete_host_key_request
    import aws_sdk_transfer.types.delete_ssh_public_key_request
    import aws_sdk_transfer.types.describe_access_request
    import aws_sdk_transfer.types.describe_access_response
    import aws_sdk_transfer.types.describe_execution_request
    import aws_sdk_transfer.types.describe_execution_response
    import aws_sdk_transfer.types.describe_host_key_request
    import aws_sdk_transfer.types.describe_host_key_response
    import aws_sdk_transfer.types.describe_security_policy_request
    import aws_sdk_transfer.types.describe_security_policy_response
    import aws_sdk_transfer.types.execution_id
    import aws_sdk_transfer.types.external_id
    import aws_sdk_transfer.types.file_path
    import aws_sdk_transfer.types.file_paths
    import aws_sdk_transfer.types.home_directory
    import aws_sdk_transfer.types.home_directory_mappings
    import aws_sdk_transfer.types.home_directory_type
    import aws_sdk_transfer.types.host_key
    import aws_sdk_transfer.types.host_key_description
    import aws_sdk_transfer.types.host_key_id
    import aws_sdk_transfer.types.import_host_key_request
    import aws_sdk_transfer.types.import_host_key_response
    import aws_sdk_transfer.types.import_ssh_public_key_request
    import aws_sdk_transfer.types.import_ssh_public_key_response
    import aws_sdk_transfer.types.list_accesses_request
    import aws_sdk_transfer.types.list_accesses_response
    import aws_sdk_transfer.types.list_executions_request
    import aws_sdk_transfer.types.list_executions_response
    import aws_sdk_transfer.types.list_file_transfer_results_request
    import aws_sdk_transfer.types.list_file_transfer_results_response
    import aws_sdk_transfer.types.list_host_keys_request
    import aws_sdk_transfer.types.list_host_keys_response
    import aws_sdk_transfer.types.list_security_policies_request
    import aws_sdk_transfer.types.list_security_policies_response
    import aws_sdk_transfer.types.list_tags_for_resource_request
    import aws_sdk_transfer.types.list_tags_for_resource_response
    import aws_sdk_transfer.types.listed_access
    import aws_sdk_transfer.types.listed_execution
    import aws_sdk_transfer.types.max_items
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.policy
    import aws_sdk_transfer.types.posix_profile
    import aws_sdk_transfer.types.protocol
    import aws_sdk_transfer.types.role
    import aws_sdk_transfer.types.security_policy_name
    import aws_sdk_transfer.types.send_workflow_step_state_request
    import aws_sdk_transfer.types.send_workflow_step_state_response
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.source_ip
    import aws_sdk_transfer.types.ssh_public_key_body
    import aws_sdk_transfer.types.ssh_public_key_id
    import aws_sdk_transfer.types.start_directory_listing_request
    import aws_sdk_transfer.types.start_directory_listing_response
    import aws_sdk_transfer.types.start_file_transfer_request
    import aws_sdk_transfer.types.start_file_transfer_response
    import aws_sdk_transfer.types.start_remote_delete_request
    import aws_sdk_transfer.types.start_remote_delete_response
    import aws_sdk_transfer.types.start_remote_move_request
    import aws_sdk_transfer.types.start_remote_move_response
    import aws_sdk_transfer.types.start_server_request
    import aws_sdk_transfer.types.stop_server_request
    import aws_sdk_transfer.types.tag
    import aws_sdk_transfer.types.tag_keys
    import aws_sdk_transfer.types.tag_resource_request
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.test_connection_request
    import aws_sdk_transfer.types.test_connection_response
    import aws_sdk_transfer.types.test_identity_provider_request
    import aws_sdk_transfer.types.test_identity_provider_response
    import aws_sdk_transfer.types.transfer_id
    import aws_sdk_transfer.types.untag_resource_request
    import aws_sdk_transfer.types.update_access_request
    import aws_sdk_transfer.types.update_access_response
    import aws_sdk_transfer.types.update_host_key_request
    import aws_sdk_transfer.types.update_host_key_response
    import aws_sdk_transfer.types.user_name
    import aws_sdk_transfer.types.user_password
    import aws_sdk_transfer.types.workflow_id


class AsyncTransferClientConfig(TypedDict, total=False):
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


class AsyncTransferClient:
    """A client for the ``Transfer`` service.

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
        self.config = AsyncTransferClientConfig(
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
        # resources
        self.agreement_resource = AsyncAgreementResource(self)
        self.certificate_resource = AsyncCertificateResource(self)
        self.connector_resource = AsyncConnectorResource(self)
        self.profile_resource = AsyncProfileResource(self)
        self.server_resource = AsyncServerResource(self)
        self.user_resource = AsyncUserResource(self)
        self.web_app_customization_resource = AsyncWebAppCustomizationResource(self)
        self.web_app_resource = AsyncWebAppResource(self)
        self.workflow_resource = AsyncWorkflowResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncTransferClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTransferClientConfig = config_overrides or {}
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

    async def create_access(
        self,
        role: "aws_sdk_transfer.types.role.Role",
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        external_id: "aws_sdk_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        home_directory: Optional[
            "aws_sdk_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "aws_sdk_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "aws_sdk_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["aws_sdk_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "aws_sdk_transfer.types.posix_profile.PosixProfile"
        ] = None,
    ) -> "aws_sdk_transfer.types.create_access_response.CreateAccessResponse":
        """<p>Used by administrators to choose which groups in the directory should have access to upload and download files over the enabled protocols using Transfer Family. For example, a Microsoft Active Directory might contain 50,000 users, but only a small fraction might need the ability to transfer files to the server. An administrator can use <code>CreateAccess</code> to limit the access to the correct set of users who need this ability.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { \"Entry\": \"/directory1\", \"Target\": \"/bucket_name/home/mydirectory\" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory (\"<code>chroot</code>\"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the <code>HomeDirectory</code> parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { \"Entry\": \"/\", \"Target\": \"/bucket_name/home/mydirectory\" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html\">Example session policy</a>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html\">AssumeRole</a> in the <i>Security Token Service API Reference</i>.</p> </note>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like \"<i>YourGroupName</i>*\"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.create_access_request.CreateAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.create_access_response.CreateAccessResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_access

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.create_access.async_create_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.create_access_request.CreateAccessRequest = {}  # type: ignore[typeddict-item]
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        input_["role"] = role
        input_["server_id"] = server_id
        input_["external_id"] = external_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_access(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        external_id: "aws_sdk_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Allows you to delete the access specified in the <code>ServerID</code> and <code>ExternalID</code> parameters.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this user assigned.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like \"<i>YourGroupName</i>*\"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_access_request.DeleteAccessRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_access

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_access.async_delete_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_access_request.DeleteAccessRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["external_id"] = external_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_host_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        host_key_id: "aws_sdk_transfer.types.host_key_id.HostKeyId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the host key that's specified in the <code>HostKeyId</code> parameter.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are deleting.</p>
            host_key_id: <p>The identifier of the host key that you are deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_host_key_request.DeleteHostKeyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_host_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_host_key.async_delete_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_host_key_request.DeleteHostKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["host_key_id"] = host_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ssh_public_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        ssh_public_key_id: "aws_sdk_transfer.types.ssh_public_key_id.SshPublicKeyId",
        user_name: "aws_sdk_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes a user's Secure Shell (SSH) public key.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a file transfer protocol-enabled server instance that has the user assigned to it.</p>
            ssh_public_key_id: <p>A unique identifier used to reference your user's specific SSH key.</p>
            user_name: <p>A unique string that identifies a user whose public key is being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_ssh_public_key_request.DeleteSshPublicKeyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_ssh_public_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_ssh_public_key.async_delete_ssh_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_ssh_public_key_request.DeleteSshPublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["ssh_public_key_id"] = ssh_public_key_id
        input_["user_name"] = user_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_access(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        external_id: "aws_sdk_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_access_response.DescribeAccessResponse":
        """<p>Describes the access that is assigned to the specific file transfer protocol-enabled server, as identified by its <code>ServerId</code> property and its <code>ExternalId</code>.</p> <p>The response from this call returns the properties of the access that is associated with the <code>ServerId</code> value that was specified.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that has this access assigned.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like \"<i>YourGroupName</i>*\"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_access_request.DescribeAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_access_response.DescribeAccessResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_access

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_access.async_describe_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_access_request.DescribeAccessRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["external_id"] = external_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_execution(
        self,
        execution_id: "aws_sdk_transfer.types.execution_id.ExecutionId",
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_execution_response.DescribeExecutionResponse":
        """<p>You can use <code>DescribeExecution</code> to check the details of the execution of the specified workflow.</p> <note> <p>This API call only returns details for in-progress workflows.</p> <p> If you provide an ID for an execution that is not in progress, or if the execution doesn't match the specified workflow ID, you receive a <code>ResourceNotFound</code> exception.</p> </note>

        Args:
            execution_id: <p>A unique identifier for the execution of a workflow.</p>
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_execution_request.DescribeExecutionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_execution_response.DescribeExecutionResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_execution

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_execution.async_describe_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_execution_request.DescribeExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["execution_id"] = execution_id
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_host_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        host_key_id: "aws_sdk_transfer.types.host_key_id.HostKeyId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_host_key_response.DescribeHostKeyResponse":
        """<p>Returns the details of the host key that's specified by the <code>HostKeyId</code> and <code>ServerId</code>.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you want described.</p>
            host_key_id: <p>The identifier of the host key that you want described.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_host_key_request.DescribeHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_host_key_response.DescribeHostKeyResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_host_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_host_key.async_describe_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_host_key_request.DescribeHostKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["host_key_id"] = host_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_security_policy(
        self,
        security_policy_name: "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_security_policy_response.DescribeSecurityPolicyResponse":
        """<p>Describes the security policy that is attached to your server or SFTP connector. The response contains a description of the security policy's properties. For more information about security policies, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html\">Working with security policies for servers</a> or <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html\">Working with security policies for SFTP connectors</a>.</p>

        Args:
            security_policy_name: <p>Specify the text name of the security policy for which you want the details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_security_policy_request.DescribeSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_security_policy_response.DescribeSecurityPolicyResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_security_policy

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_security_policy.async_describe_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_security_policy_request.DescribeSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["security_policy_name"] = security_policy_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_host_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        host_key_body: "aws_sdk_transfer.types.host_key.HostKey",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional[
            "aws_sdk_transfer.types.host_key_description.HostKeyDescription"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
    ) -> "aws_sdk_transfer.types.import_host_key_response.ImportHostKeyResponse":
        """<p>Adds a host key to the server that's specified by the <code>ServerId</code> parameter.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are importing.</p>
            host_key_body: <p>The private key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>
            description: <p>The text description that identifies this host key.</p>
            tags: <p>Key-value pairs that can be used to group and search for host keys.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.import_host_key_request.ImportHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.import_host_key_response.ImportHostKeyResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.import_host_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.import_host_key.async_import_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.import_host_key_request.ImportHostKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["host_key_body"] = host_key_body
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_ssh_public_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        ssh_public_key_body: "aws_sdk_transfer.types.ssh_public_key_body.SshPublicKeyBody",
        user_name: "aws_sdk_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.import_ssh_public_key_response.ImportSshPublicKeyResponse":
        """<p>Adds a Secure Shell (SSH) public key to a Transfer Family user identified by a <code>UserName</code> value assigned to the specific file transfer protocol-enabled server, identified by <code>ServerId</code>.</p> <p>The response returns the <code>UserName</code> value, the <code>ServerId</code> value, and the name of the <code>SshPublicKeyId</code>.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server.</p>
            ssh_public_key_body: <p>The public key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>
            user_name: <p>The name of the Transfer Family user that is assigned to one or more servers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.import_ssh_public_key_request.ImportSshPublicKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.import_ssh_public_key_response.ImportSshPublicKeyResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.import_ssh_public_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.import_ssh_public_key.async_import_ssh_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.import_ssh_public_key_request.ImportSshPublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["ssh_public_key_body"] = ssh_public_key_body
        input_["user_name"] = user_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_accesses(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_accesses_response.ListAccessesResponse":
        """<p>Lists the details for all the accesses you have on your server.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListAccesses</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional accesses.</p>
            server_id: <p>A system-assigned unique identifier for a server that has users assigned to it.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_accesses_request.ListAccessesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_accesses_response.ListAccessesResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_accesses

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_accesses.async_list_accesses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_accesses_request.ListAccessesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_accesses(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_transfer.types.listed_access.ListedAccess]":
        _token = next_token
        while True:
            _response = await self.list_accesses(
                server_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accesses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_executions(
        self,
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_executions_response.ListExecutionsResponse":
        """<p>Lists all in-progress executions for the specified workflow.</p> <note> <p>If the specified workflow ID cannot be found, <code>ListExecutions</code> returns a <code>ResourceNotFound</code> exception.</p> </note>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p> <code>ListExecutions</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional executions.</p> <p> This is useful for pagination, for instance. If you have 100 executions for a workflow, you might only want to list first 10. If so, call the API by specifying the <code>max-results</code>: </p> <p> <code>aws transfer list-executions --max-results 10</code> </p> <p> This returns details for the first 10 executions, as well as the pointer (<code>NextToken</code>) to the eleventh execution. You can now call the API again, supplying the <code>NextToken</code> value you received: </p> <p> <code>aws transfer list-executions --max-results 10 --next-token $somePointerReturnedFromPreviousListResult</code> </p> <p> This call returns the next 10 executions, the 11th through the 20th. You can then repeat the call until the details for all 100 executions have been returned. </p>
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_executions_response.ListExecutionsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_executions

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_executions_request.ListExecutionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_executions(
        self,
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_transfer.types.listed_execution.ListedExecution]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                workflow_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_file_transfer_results(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        transfer_id: "aws_sdk_transfer.types.transfer_id.TransferId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_transfer.types.list_file_transfer_results_response.ListFileTransferResultsResponse":
        """<p> Returns real-time updates and detailed information on the status of each individual file being transferred in a specific file transfer operation. You specify the file transfer by providing its <code>ConnectorId</code> and its <code>TransferId</code>.</p> <note> <p>File transfer results are available up to 7 days after an operation has been requested.</p> </note>

        Args:
            connector_id: <p>A unique identifier for a connector. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>
            transfer_id: <p>A unique identifier for a file transfer. This value should match the value supplied to the corresponding <code>StartFileTransfer</code> call.</p>
            next_token: <p>If there are more file details than returned in this call, use this value for a subsequent call to <code>ListFileTransferResults</code> to retrieve them.</p>
            max_results: <p>The maximum number of files to return in a single page. Note that currently you can specify a maximum of 10 file paths in a single <a href=\"https://docs.aws.amazon.com/transfer/latest/APIReference/API_StartFileTransfer.html\">StartFileTransfer</a> operation. Thus, the maximum number of file transfer results that can be returned in a single page is 10. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_file_transfer_results_request.ListFileTransferResultsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_file_transfer_results_response.ListFileTransferResultsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_file_transfer_results

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_file_transfer_results.async_list_file_transfer_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_file_transfer_results_request.ListFileTransferResultsRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        input_["transfer_id"] = transfer_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_file_transfer_results(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        transfer_id: "aws_sdk_transfer.types.transfer_id.TransferId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_transfer.types.connector_file_transfer_result.ConnectorFileTransferResult]":
        _token = next_token
        while True:
            _response = await self.list_file_transfer_results(
                connector_id,
                transfer_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("file_transfer_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_host_keys(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_host_keys_response.ListHostKeysResponse":
        """<p>Returns a list of host keys for the server that's specified by the <code>ServerId</code> parameter.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListHostKeys</code> to continue listing results.</p>
            server_id: <p>The identifier of the server that contains the host keys that you want to view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_host_keys_request.ListHostKeysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_host_keys_response.ListHostKeysResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_host_keys

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_host_keys.async_list_host_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_host_keys_request.ListHostKeysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_security_policies(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Lists the security policies that are attached to your servers and SFTP connectors. For more information about security policies, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html\">Working with security policies for servers</a> or <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html\">Working with security policies for SFTP connectors</a>.</p>

        Args:
            max_results: <p>Specifies the number of security policies to return as a response to the <code>ListSecurityPolicies</code> query.</p>
            next_token: <p>When additional results are obtained from the <code>ListSecurityPolicies</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional security policies.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_security_policies

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_security_policies.async_list_security_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_security_policies_request.ListSecurityPoliciesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_security_policies(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_transfer.types.security_policy_name.SecurityPolicyName]"
    ):
        _token = next_token
        while True:
            _response = await self.list_security_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("security_policy_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "aws_sdk_transfer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            arn: <p>Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            max_results: <p>Specifies the number of tags to return as a response to the <code>ListTagsForResource</code> request.</p>
            next_token: <p>When you request additional results from the <code>ListTagsForResource</code> operation, a <code>NextToken</code> parameter is returned in the input. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tags_for_resource(
        self,
        arn: "aws_sdk_transfer.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_transfer.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def send_workflow_step_state(
        self,
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        execution_id: "aws_sdk_transfer.types.execution_id.ExecutionId",
        token: "aws_sdk_transfer.types.callback_token.CallbackToken",
        status: "aws_sdk_transfer.types.custom_step_status.CustomStepStatus",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.send_workflow_step_state_response.SendWorkflowStepStateResponse":
        """<p>Sends a callback for asynchronous custom steps.</p> <p> The <code>ExecutionId</code>, <code>WorkflowId</code>, and <code>Token</code> are passed to the target resource during execution of a custom step of a workflow. You must include those with their callback as well as providing a status. </p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
            execution_id: <p>A unique identifier for the execution of a workflow.</p>
            token: <p>Used to distinguish between multiple callbacks for multiple Lambda steps within the same execution.</p>
            status: <p>Indicates whether the specified step succeeded or failed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.send_workflow_step_state_request.SendWorkflowStepStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.send_workflow_step_state_response.SendWorkflowStepStateResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.send_workflow_step_state

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.send_workflow_step_state.async_send_workflow_step_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.send_workflow_step_state_request.SendWorkflowStepStateRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["execution_id"] = execution_id
        input_["token"] = token
        input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_directory_listing(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        remote_directory_path: "aws_sdk_transfer.types.file_path.FilePath",
        output_directory_path: "aws_sdk_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_items: Optional["aws_sdk_transfer.types.max_items.MaxItems"] = None,
    ) -> "aws_sdk_transfer.types.start_directory_listing_response.StartDirectoryListingResponse":
        """<p>Retrieves a list of the contents of a directory from a remote SFTP server. You specify the connector ID, the output path, and the remote directory path. You can also specify the optional <code>MaxItems</code> value to control the maximum number of items that are listed from the remote directory. This API returns a list of all files and directories in the remote directory (up to the maximum value), but does not return files or folders in sub-directories. That is, it only returns a list of files and directories one-level deep.</p> <p>After you receive the listing file, you can provide the files that you want to transfer to the <code>RetrieveFilePaths</code> parameter of the <code>StartFileTransfer</code> API call.</p> <p>The naming convention for the output file is <code> <i>connector-ID</i>-<i>listing-ID</i>.json</code>. The output file contains the following information:</p> <ul> <li> <p> <code>filePath</code>: the complete path of a remote file, relative to the directory of the listing request for your SFTP connector on the remote server.</p> </li> <li> <p> <code>modifiedTimestamp</code>: the last time the file was modified, in UTC time format. This field is optional. If the remote file attributes don't contain a timestamp, it is omitted from the file listing.</p> </li> <li> <p> <code>size</code>: the size of the file, in bytes. This field is optional. If the remote file attributes don't contain a file size, it is omitted from the file listing.</p> </li> <li> <p> <code>path</code>: the complete path of a remote directory, relative to the directory of the listing request for your SFTP connector on the remote server.</p> </li> <li> <p> <code>truncated</code>: a flag indicating whether the list output contains all of the items contained in the remote directory or not. If your <code>Truncated</code> output value is true, you can increase the value provided in the optional <code>max-items</code> input attribute to be able to list more items (up to the maximum allowed list size of 200,000 items).</p> </li> </ul>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            remote_directory_path: <p>Specifies the directory on the remote SFTP server for which you want to list its contents.</p>
            max_items: <p>An optional parameter where you can specify the maximum number of file/directory names to retrieve. The default value is 1,000.</p>
            output_directory_path: <p>Specifies the path (bucket and prefix) in Amazon S3 storage to store the results of the directory listing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.start_directory_listing_request.StartDirectoryListingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.start_directory_listing_response.StartDirectoryListingResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.start_directory_listing

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.start_directory_listing.async_start_directory_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.start_directory_listing_request.StartDirectoryListingRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        input_["remote_directory_path"] = remote_directory_path
        if max_items is not None:
            input_["max_items"] = max_items
        input_["output_directory_path"] = output_directory_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_file_transfer(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        send_file_paths: Optional["aws_sdk_transfer.types.file_paths.FilePaths"] = None,
        retrieve_file_paths: Optional[
            "aws_sdk_transfer.types.file_paths.FilePaths"
        ] = None,
        local_directory_path: Optional[
            "aws_sdk_transfer.types.file_path.FilePath"
        ] = None,
        remote_directory_path: Optional[
            "aws_sdk_transfer.types.file_path.FilePath"
        ] = None,
        custom_http_headers: Optional[
            "aws_sdk_transfer.types.custom_http_headers.CustomHttpHeaders"
        ] = None,
    ) -> (
        "aws_sdk_transfer.types.start_file_transfer_response.StartFileTransferResponse"
    ):
        """<p>Begins a file transfer between local Amazon Web Services storage and a remote AS2 or SFTP server.</p> <ul> <li> <p>For an AS2 connector, you specify the <code>ConnectorId</code> and one or more <code>SendFilePaths</code> to identify the files you want to transfer.</p> </li> <li> <p>For an SFTP connector, the file transfer can be either outbound or inbound. In both cases, you specify the <code>ConnectorId</code>. Depending on the direction of the transfer, you also specify the following items:</p> <ul> <li> <p>If you are transferring file from a partner's SFTP server to Amazon Web Services storage, you specify one or more <code>RetrieveFilePaths</code> to identify the files you want to transfer, and a <code>LocalDirectoryPath</code> to specify the destination folder.</p> </li> <li> <p>If you are transferring file to a partner's SFTP server from Amazon Web Services storage, you specify one or more <code>SendFilePaths</code> to identify the files you want to transfer, and a <code>RemoteDirectoryPath</code> to specify the destination folder.</p> </li> </ul> </li> </ul>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            send_file_paths: <p>One or more source paths for the Amazon S3 storage. Each string represents a source file path for one outbound file transfer. For example, <code> <i>amzn-s3-demo-bucket</i>/<i>myfile.txt</i> </code>.</p> <note> <p>Replace <code> <i>amzn-s3-demo-bucket</i> </code> with one of your actual buckets.</p> </note>
            retrieve_file_paths: <p>One or more source paths for the partner's SFTP server. Each string represents a source file path for one inbound file transfer.</p>
            local_directory_path: <p>For an inbound transfer, the <code>LocaDirectoryPath</code> specifies the destination for one or more files that are transferred from the partner's SFTP server.</p>
            remote_directory_path: <p>For an outbound transfer, the <code>RemoteDirectoryPath</code> specifies the destination for one or more files that are transferred to the partner's SFTP server. If you don't specify a <code>RemoteDirectoryPath</code>, the destination for transferred files is the SFTP user's home directory.</p>
            custom_http_headers: <p>An array of key-value pairs that represent custom HTTP headers to include in AS2 messages. These headers are added to the AS2 message when sending files to your trading partner.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.start_file_transfer_request.StartFileTransferRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.start_file_transfer_response.StartFileTransferResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.start_file_transfer

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.start_file_transfer.async_start_file_transfer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.start_file_transfer_request.StartFileTransferRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        if send_file_paths is not None:
            input_["send_file_paths"] = send_file_paths
        if retrieve_file_paths is not None:
            input_["retrieve_file_paths"] = retrieve_file_paths
        if local_directory_path is not None:
            input_["local_directory_path"] = local_directory_path
        if remote_directory_path is not None:
            input_["remote_directory_path"] = remote_directory_path
        if custom_http_headers is not None:
            input_["custom_http_headers"] = custom_http_headers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_remote_delete(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        delete_path: "aws_sdk_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> (
        "aws_sdk_transfer.types.start_remote_delete_response.StartRemoteDeleteResponse"
    ):
        """<p>Deletes a file or directory on the remote SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            delete_path: <p>The absolute path of the file or directory to delete. You can only specify one path per call to this operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.start_remote_delete_request.StartRemoteDeleteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.start_remote_delete_response.StartRemoteDeleteResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.start_remote_delete

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.start_remote_delete.async_start_remote_delete(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.start_remote_delete_request.StartRemoteDeleteRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        input_["delete_path"] = delete_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_remote_move(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        source_path: "aws_sdk_transfer.types.file_path.FilePath",
        target_path: "aws_sdk_transfer.types.file_path.FilePath",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.start_remote_move_response.StartRemoteMoveResponse":
        """<p>Moves or renames a file or directory on the remote SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            source_path: <p>The absolute path of the file or directory to move or rename. You can only specify one path per call to this operation.</p>
            target_path: <p>The absolute path for the target of the move/rename operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.start_remote_move_request.StartRemoteMoveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.start_remote_move_response.StartRemoteMoveResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.start_remote_move

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.start_remote_move.async_start_remote_move(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.start_remote_move_request.StartRemoteMoveRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        input_["source_path"] = source_path
        input_["target_path"] = target_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_server(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Changes the state of a file transfer protocol-enabled server from <code>OFFLINE</code> to <code>ONLINE</code>. It has no impact on a server that is already <code>ONLINE</code>. An <code>ONLINE</code> server can accept and process file transfer jobs.</p> <p>The state of <code>STARTING</code> indicates that the server is in an intermediate state, either not fully able to respond, or not fully online. The values of <code>START_FAILED</code> can indicate an error condition.</p> <p>No response is returned from this call.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that you start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.start_server_request.StartServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.start_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.start_server.async_start_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.start_server_request.StartServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_server(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Changes the state of a file transfer protocol-enabled server from <code>ONLINE</code> to <code>OFFLINE</code>. An <code>OFFLINE</code> server cannot accept and process file transfer jobs. Information tied to your server, such as server and user properties, are not affected by stopping your server.</p> <note> <p>Stopping the server does not reduce or impact your file transfer protocol endpoint billing; you must delete the server to stop being billed.</p> </note> <p>The state of <code>STOPPING</code> indicates that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of <code>STOP_FAILED</code> can indicate an error condition.</p> <p>No response is returned from this call.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server that you stopped.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.stop_server_request.StopServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.stop_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.stop_server.async_stop_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.stop_server_request.StopServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        arn: "aws_sdk_transfer.types.arn.Arn",
        tags: "aws_sdk_transfer.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p> <p>There is no response returned from this call.</p>

        Args:
            arn: <p>An Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            tags: <p>Key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (servers, users, workflows, and so on) for any purpose.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_connection(
        self,
        connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.test_connection_response.TestConnectionResponse":
        """<p>Tests whether your SFTP connector is set up successfully. We highly recommend that you call this operation to test your ability to transfer files between local Amazon Web Services storage and a trading partner's SFTP server.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.test_connection_request.TestConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.test_connection_response.TestConnectionResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.test_connection

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.test_connection.async_test_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.test_connection_request.TestConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_identity_provider(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        user_name: "aws_sdk_transfer.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        server_protocol: Optional["aws_sdk_transfer.types.protocol.Protocol"] = None,
        source_ip: Optional["aws_sdk_transfer.types.source_ip.SourceIp"] = None,
        user_password: Optional[
            "aws_sdk_transfer.types.user_password.UserPassword"
        ] = None,
    ) -> "aws_sdk_transfer.types.test_identity_provider_response.TestIdentityProviderResponse":
        """<p>If the <code>IdentityProviderType</code> of a file transfer protocol-enabled server is <code>AWS_DIRECTORY_SERVICE</code> or <code>API_Gateway</code>, tests whether your identity provider is set up successfully. We highly recommend that you call this operation to test your authentication method as soon as you create your server. By doing so, you can troubleshoot issues with the identity provider integration to ensure that your users can successfully use the service.</p> <p> The <code>ServerId</code> and <code>UserName</code> parameters are required. The <code>ServerProtocol</code>, <code>SourceIp</code>, and <code>UserPassword</code> are all optional. </p> <p>Note the following:</p> <ul> <li> <p> You cannot use <code>TestIdentityProvider</code> if the <code>IdentityProviderType</code> of your server is <code>SERVICE_MANAGED</code>.</p> </li> <li> <p> <code>TestIdentityProvider</code> does not work with keys: it only accepts passwords.</p> </li> <li> <p> <code>TestIdentityProvider</code> can test the password operation for a custom Identity Provider that handles keys and passwords.</p> </li> <li> <p> If you provide any incorrect values for any parameters, the <code>Response</code> field is empty. </p> </li> <li> <p> If you provide a server ID for a server that uses service-managed users, you get an error: </p> <p> <code> An error occurred (InvalidRequestException) when calling the TestIdentityProvider operation: s-<i>server-ID</i> not configured for external auth </code> </p> </li> <li> <p> If you enter a Server ID for the <code>--server-id</code> parameter that does not identify an actual Transfer server, you receive the following error: </p> <p> <code>An error occurred (ResourceNotFoundException) when calling the TestIdentityProvider operation: Unknown server</code>. </p> <p>It is possible your sever is in a different region. You can specify a region by adding the following: <code>--region region-code</code>, such as <code>--region us-east-2</code> to specify a server in <b>US East (Ohio)</b>.</p> </li> </ul>

        Args:
            server_id: <p>A system-assigned identifier for a specific server. That server's user authentication method is tested with a user name and password.</p>
            server_protocol: <p>The type of file transfer protocol to be tested.</p> <p>The available protocols are:</p> <ul> <li> <p>Secure Shell (SSH) File Transfer Protocol (SFTP)</p> </li> <li> <p>File Transfer Protocol Secure (FTPS)</p> </li> <li> <p>File Transfer Protocol (FTP)</p> </li> <li> <p>Applicability Statement 2 (AS2)</p> </li> </ul>
            source_ip: <p>The source IP address of the account to be tested.</p>
            user_name: <p>The name of the account to be tested.</p>
            user_password: <p>The password of the account to be tested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.test_identity_provider_request.TestIdentityProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.test_identity_provider_response.TestIdentityProviderResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.test_identity_provider

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.test_identity_provider.async_test_identity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.test_identity_provider_request.TestIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        if server_protocol is not None:
            input_["server_protocol"] = server_protocol
        if source_ip is not None:
            input_["source_ip"] = source_ip
        input_["user_name"] = user_name
        if user_password is not None:
            input_["user_password"] = user_password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        arn: "aws_sdk_transfer.types.arn.Arn",
        tag_keys: "aws_sdk_transfer.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p> <p>No response is returned from this call.</p>

        Args:
            arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>
            tag_keys: <p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_access(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        external_id: "aws_sdk_transfer.types.external_id.ExternalId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        home_directory: Optional[
            "aws_sdk_transfer.types.home_directory.HomeDirectory"
        ] = None,
        home_directory_type: Optional[
            "aws_sdk_transfer.types.home_directory_type.HomeDirectoryType"
        ] = None,
        home_directory_mappings: Optional[
            "aws_sdk_transfer.types.home_directory_mappings.HomeDirectoryMappings"
        ] = None,
        policy: Optional["aws_sdk_transfer.types.policy.Policy"] = None,
        posix_profile: Optional[
            "aws_sdk_transfer.types.posix_profile.PosixProfile"
        ] = None,
        role: Optional["aws_sdk_transfer.types.role.Role"] = None,
    ) -> "aws_sdk_transfer.types.update_access_response.UpdateAccessResponse":
        """<p>Allows you to update parameters for the access specified in the <code>ServerID</code> and <code>ExternalID</code> parameters.</p>

        Args:
            home_directory: <p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>
            home_directory_type: <p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>
            home_directory_mappings: <p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { \"Entry\": \"/directory1\", \"Target\": \"/bucket_name/home/mydirectory\" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory (\"<code>chroot</code>\"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the <code>HomeDirectory</code> parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { \"Entry\": \"/\", \"Target\": \"/bucket_name/home/mydirectory\" } ]</code> </p>
            policy: <p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html\">Example session policy</a>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html\">AssumeRole</a> in the <i>Amazon Web ServicesSecurity Token Service API Reference</i>.</p> </note>
            role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>
            server_id: <p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>
            external_id: <p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like \"<i>YourGroupName</i>*\"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.update_access_request.UpdateAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.update_access_response.UpdateAccessResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_access

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.update_access.async_update_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.update_access_request.UpdateAccessRequest = {}  # type: ignore[typeddict-item]
        if home_directory is not None:
            input_["home_directory"] = home_directory
        if home_directory_type is not None:
            input_["home_directory_type"] = home_directory_type
        if home_directory_mappings is not None:
            input_["home_directory_mappings"] = home_directory_mappings
        if policy is not None:
            input_["policy"] = policy
        if posix_profile is not None:
            input_["posix_profile"] = posix_profile
        if role is not None:
            input_["role"] = role
        input_["server_id"] = server_id
        input_["external_id"] = external_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_host_key(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        host_key_id: "aws_sdk_transfer.types.host_key_id.HostKeyId",
        description: "aws_sdk_transfer.types.host_key_description.HostKeyDescription",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.update_host_key_response.UpdateHostKeyResponse":
        """<p>Updates the description for the host key that's specified by the <code>ServerId</code> and <code>HostKeyId</code> parameters.</p>

        Args:
            server_id: <p>The identifier of the server that contains the host key that you are updating.</p>
            host_key_id: <p>The identifier of the host key that you are updating.</p>
            description: <p>An updated description for the host key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.update_host_key_request.UpdateHostKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.update_host_key_response.UpdateHostKeyResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_host_key

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.update_host_key.async_update_host_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.update_host_key_request.UpdateHostKeyRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id
        input_["host_key_id"] = host_key_id
        input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
