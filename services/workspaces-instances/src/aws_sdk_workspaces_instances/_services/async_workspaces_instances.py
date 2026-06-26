"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EUCMIFrontendAPIService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_workspaces_instances._auth._signers
import aws_sdk_workspaces_instances._auth._sigv4
from aws_sdk_workspaces_instances._auth._identity import Credentials
from aws_sdk_workspaces_instances._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_workspaces_instances._auth._zapros_handler import AuthMiddleware
from aws_sdk_workspaces_instances._pagination import resolve_path as _resolve_path
from aws_sdk_workspaces_instances._services._aws_config import aaws_config
from aws_sdk_workspaces_instances._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.associate_volume_request
    import aws_sdk_workspaces_instances.types.associate_volume_response
    import aws_sdk_workspaces_instances.types.billing_configuration
    import aws_sdk_workspaces_instances.types.client_token
    import aws_sdk_workspaces_instances.types.create_volume_request
    import aws_sdk_workspaces_instances.types.create_volume_response
    import aws_sdk_workspaces_instances.types.create_workspace_instance_request
    import aws_sdk_workspaces_instances.types.create_workspace_instance_response
    import aws_sdk_workspaces_instances.types.delete_volume_request
    import aws_sdk_workspaces_instances.types.delete_volume_response
    import aws_sdk_workspaces_instances.types.delete_workspace_instance_request
    import aws_sdk_workspaces_instances.types.delete_workspace_instance_response
    import aws_sdk_workspaces_instances.types.device_name
    import aws_sdk_workspaces_instances.types.disassociate_mode_enum
    import aws_sdk_workspaces_instances.types.disassociate_volume_request
    import aws_sdk_workspaces_instances.types.disassociate_volume_response
    import aws_sdk_workspaces_instances.types.get_workspace_instance_request
    import aws_sdk_workspaces_instances.types.get_workspace_instance_response
    import aws_sdk_workspaces_instances.types.instance_configuration_filter
    import aws_sdk_workspaces_instances.types.instance_type_info
    import aws_sdk_workspaces_instances.types.kms_key_id
    import aws_sdk_workspaces_instances.types.list_instance_types_max_results
    import aws_sdk_workspaces_instances.types.list_instance_types_request
    import aws_sdk_workspaces_instances.types.list_instance_types_response
    import aws_sdk_workspaces_instances.types.list_regions_request
    import aws_sdk_workspaces_instances.types.list_regions_response
    import aws_sdk_workspaces_instances.types.list_tags_for_resource_request
    import aws_sdk_workspaces_instances.types.list_tags_for_resource_response
    import aws_sdk_workspaces_instances.types.list_workspace_instances_request
    import aws_sdk_workspaces_instances.types.list_workspace_instances_response
    import aws_sdk_workspaces_instances.types.managed_instance_request
    import aws_sdk_workspaces_instances.types.max_results
    import aws_sdk_workspaces_instances.types.next_token
    import aws_sdk_workspaces_instances.types.non_negative_integer
    import aws_sdk_workspaces_instances.types.provision_states
    import aws_sdk_workspaces_instances.types.region
    import aws_sdk_workspaces_instances.types.snapshot_id
    import aws_sdk_workspaces_instances.types.string64
    import aws_sdk_workspaces_instances.types.tag_key_list
    import aws_sdk_workspaces_instances.types.tag_list
    import aws_sdk_workspaces_instances.types.tag_resource_request
    import aws_sdk_workspaces_instances.types.tag_resource_response
    import aws_sdk_workspaces_instances.types.tag_specifications
    import aws_sdk_workspaces_instances.types.untag_resource_request
    import aws_sdk_workspaces_instances.types.untag_resource_response
    import aws_sdk_workspaces_instances.types.volume_id
    import aws_sdk_workspaces_instances.types.volume_type_enum
    import aws_sdk_workspaces_instances.types.workspace_instance
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class AsyncWorkspacesInstancesClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncWorkspacesInstancesClient:
    """A client for the ``WorkspacesInstances`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncWorkspacesInstancesClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWorkspacesInstancesClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_volume(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        volume_id: "aws_sdk_workspaces_instances.types.volume_id.VolumeId",
        device: "aws_sdk_workspaces_instances.types.device_name.DeviceName",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.associate_volume_response.AssociateVolumeResponse":
        """<p>Attaches a volume to a WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>WorkSpace Instance to attach volume to.</p>
            volume_id: <p>Volume to be attached.</p>
            device: <p>Device path for volume attachment.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.associate_volume_request.AssociateVolumeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.associate_volume_response.AssociateVolumeResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.associate_volume

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.associate_volume.async_associate_volume(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.associate_volume_request.AssociateVolumeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id
        input_["volume_id"] = volume_id
        input_["device"] = device

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_volume(
        self,
        availability_zone: "aws_sdk_workspaces_instances.types.string64.String64",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workspaces_instances.types.client_token.ClientToken"
        ] = None,
        encrypted: Optional[bool] = None,
        iops: Optional[
            "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
        ] = None,
        kms_key_id: Optional[
            "aws_sdk_workspaces_instances.types.kms_key_id.KmsKeyId"
        ] = None,
        size_in_gb: Optional[
            "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
        ] = None,
        snapshot_id: Optional[
            "aws_sdk_workspaces_instances.types.snapshot_id.SnapshotId"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_workspaces_instances.types.tag_specifications.TagSpecifications"
        ] = None,
        throughput: Optional[
            "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
        ] = None,
        volume_type: Optional[
            "aws_sdk_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
        ] = None,
    ) -> (
        "aws_sdk_workspaces_instances.types.create_volume_response.CreateVolumeResponse"
    ):
        """<p>Creates a new volume for WorkSpace Instances.</p>

        Args:
            availability_zone: <p>Availability zone for the volume.</p>
            client_token: <p>Unique token to prevent duplicate volume creation.</p>
            encrypted: <p>Indicates if the volume should be encrypted.</p>
            iops: <p>Input/output operations per second for the volume.</p>
            kms_key_id: <p>KMS key for volume encryption.</p>
            size_in_gb: <p>Volume size in gigabytes.</p>
            snapshot_id: <p>Source snapshot for volume creation.</p>
            tag_specifications: <p>Metadata tags for the volume.</p>
            throughput: <p>Volume throughput performance.</p>
            volume_type: <p>Type of EBS volume.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Indicates that a service quota has been exceeded.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.create_volume_request.CreateVolumeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.create_volume_response.CreateVolumeResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.create_volume

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.create_volume.async_create_volume(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.create_volume_request.CreateVolumeRequest = {}  # type: ignore[typeddict-item]
        input_["availability_zone"] = availability_zone
        if client_token is not None:
            input_["client_token"] = client_token
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if iops is not None:
            input_["iops"] = iops
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if size_in_gb is not None:
            input_["size_in_gb"] = size_in_gb
        if snapshot_id is not None:
            input_["snapshot_id"] = snapshot_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if throughput is not None:
            input_["throughput"] = throughput
        if volume_type is not None:
            input_["volume_type"] = volume_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_workspace_instance(
        self,
        managed_instance: "aws_sdk_workspaces_instances.types.managed_instance_request.ManagedInstanceRequest",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workspaces_instances.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_workspaces_instances.types.tag_list.TagList"] = None,
        billing_configuration: Optional[
            "aws_sdk_workspaces_instances.types.billing_configuration.BillingConfiguration"
        ] = None,
    ) -> "aws_sdk_workspaces_instances.types.create_workspace_instance_response.CreateWorkspaceInstanceResponse":
        """<p>Launches a new WorkSpace Instance with specified configuration parameters, enabling programmatic workspace deployment.</p>

        Args:
            client_token: <p>Unique token to ensure idempotent instance creation, preventing duplicate workspace launches.</p>
            tags: <p>Optional metadata tags for categorizing and managing WorkSpaces Instances.</p>
            managed_instance: <p>Comprehensive configuration settings for the WorkSpaces Instance, including network, compute, and storage parameters.</p>
            billing_configuration: <p>Optional billing configuration for the WorkSpace Instance. Allows customers to specify their preferred billing mode when creating a new instance. Defaults to hourly billing if not specified.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Indicates that a service quota has been exceeded.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.create_workspace_instance_request.CreateWorkspaceInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.create_workspace_instance_response.CreateWorkspaceInstanceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.create_workspace_instance

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.create_workspace_instance.async_create_workspace_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.create_workspace_instance_request.CreateWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        input_["managed_instance"] = managed_instance
        if billing_configuration is not None:
            input_["billing_configuration"] = billing_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_volume(
        self,
        volume_id: "aws_sdk_workspaces_instances.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> (
        "aws_sdk_workspaces_instances.types.delete_volume_response.DeleteVolumeResponse"
    ):
        """<p>Deletes a specified volume.</p>

        Args:
            volume_id: <p>Identifier of the volume to delete.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.delete_volume_request.DeleteVolumeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.delete_volume_response.DeleteVolumeResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.delete_volume

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.delete_volume.async_delete_volume(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.delete_volume_request.DeleteVolumeRequest = {}  # type: ignore[typeddict-item]
        input_["volume_id"] = volume_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_workspace_instance(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.delete_workspace_instance_response.DeleteWorkspaceInstanceResponse":
        """<p>Deletes the specified WorkSpace</p> <important> <p>Usage of this API will result in deletion of the resource in question.</p> </important>

        Args:
            workspace_instance_id: <p>Unique identifier of the WorkSpaces Instance targeted for deletion.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.delete_workspace_instance_request.DeleteWorkspaceInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.delete_workspace_instance_response.DeleteWorkspaceInstanceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.delete_workspace_instance

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.delete_workspace_instance.async_delete_workspace_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.delete_workspace_instance_request.DeleteWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_volume(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        volume_id: "aws_sdk_workspaces_instances.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        device: Optional[
            "aws_sdk_workspaces_instances.types.device_name.DeviceName"
        ] = None,
        disassociate_mode: Optional[
            "aws_sdk_workspaces_instances.types.disassociate_mode_enum.DisassociateModeEnum"
        ] = None,
    ) -> "aws_sdk_workspaces_instances.types.disassociate_volume_response.DisassociateVolumeResponse":
        """<p>Detaches a volume from a WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>WorkSpace Instance to detach volume from.</p>
            volume_id: <p>Volume to be detached.</p>
            device: <p>Device path of volume to detach.</p>
            disassociate_mode: <p>Mode for volume detachment.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.conflict_exception.ConflictException: <p>Signals a conflict with the current state of the resource.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.disassociate_volume_request.DisassociateVolumeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.disassociate_volume_response.DisassociateVolumeResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.disassociate_volume

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.disassociate_volume.async_disassociate_volume(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.disassociate_volume_request.DisassociateVolumeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id
        input_["volume_id"] = volume_id
        if device is not None:
            input_["device"] = device
        if disassociate_mode is not None:
            input_["disassociate_mode"] = disassociate_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workspace_instance(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.get_workspace_instance_response.GetWorkspaceInstanceResponse":
        """<p>Retrieves detailed information about a specific WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>Unique identifier of the WorkSpace Instance to retrieve.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.get_workspace_instance_request.GetWorkspaceInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.get_workspace_instance_response.GetWorkspaceInstanceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.get_workspace_instance

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.get_workspace_instance.async_get_workspace_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.get_workspace_instance_request.GetWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_instance_types(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.list_instance_types_max_results.ListInstanceTypesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
        instance_configuration_filter: Optional[
            "aws_sdk_workspaces_instances.types.instance_configuration_filter.InstanceConfigurationFilter"
        ] = None,
    ) -> "aws_sdk_workspaces_instances.types.list_instance_types_response.ListInstanceTypesResponse":
        """<p>Retrieves a list of instance types supported by Amazon WorkSpaces Instances, enabling precise workspace infrastructure configuration.</p>

        Args:
            max_results: <p>Maximum number of instance types to return in a single API call. Enables pagination of instance type results.</p>
            next_token: <p>Pagination token for retrieving subsequent pages of instance type results.</p>
            instance_configuration_filter: <p>Optional filter to narrow instance type results based on configuration requirements. Only returns instance types that support the specified combination of tenancy, platform type, and billing mode.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.list_instance_types_request.ListInstanceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.list_instance_types_response.ListInstanceTypesResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_instance_types

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_instance_types.async_list_instance_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.list_instance_types_request.ListInstanceTypesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if instance_configuration_filter is not None:
            input_["instance_configuration_filter"] = instance_configuration_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_instance_types(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.list_instance_types_max_results.ListInstanceTypesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
        instance_configuration_filter: Optional[
            "aws_sdk_workspaces_instances.types.instance_configuration_filter.InstanceConfigurationFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_workspaces_instances.types.instance_type_info.InstanceTypeInfo]":
        _token = next_token
        while True:
            _response = await self.list_instance_types(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                instance_configuration_filter=instance_configuration_filter,
            )
            _page = _resolve_path(_response, ("instance_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_regions(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_workspaces_instances.types.list_regions_response.ListRegionsResponse":
        """<p>Retrieves a list of AWS regions supported by Amazon WorkSpaces Instances, enabling region discovery for workspace deployments.</p>

        Args:
            max_results: <p>Maximum number of regions to return in a single API call. Enables pagination of region results.</p>
            next_token: <p>Pagination token for retrieving subsequent pages of region results.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.list_regions_request.ListRegionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.list_regions_response.ListRegionsResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_regions

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_regions.async_list_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.list_regions_request.ListRegionsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_regions(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_workspaces_instances.types.region.Region]":
        _token = next_token
        while True:
            _response = await self.list_regions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("regions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves tags for a WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>Unique identifier of the WorkSpace Instance.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_workspace_instances(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        provision_states: Optional[
            "aws_sdk_workspaces_instances.types.provision_states.ProvisionStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_workspaces_instances.types.list_workspace_instances_response.ListWorkspaceInstancesResponse":
        """<p>Retrieves a collection of WorkSpaces Instances based on specified filters.</p>

        Args:
            provision_states: <p>Filter WorkSpaces Instances by their current provisioning states.</p>
            max_results: <p>Maximum number of WorkSpaces Instances to return in a single response.</p>
            next_token: <p>Pagination token for retrieving subsequent pages of WorkSpaces Instances.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.list_workspace_instances_request.ListWorkspaceInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.list_workspace_instances_response.ListWorkspaceInstancesResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_workspace_instances

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.list_workspace_instances.async_list_workspace_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.list_workspace_instances_request.ListWorkspaceInstancesRequest = {}  # type: ignore[typeddict-item]
        if provision_states is not None:
            input_["provision_states"] = provision_states
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

    async def iter_list_workspace_instances(
        self,
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
        provision_states: Optional[
            "aws_sdk_workspaces_instances.types.provision_states.ProvisionStates"
        ] = None,
        max_results: Optional[
            "aws_sdk_workspaces_instances.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_instances.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_workspaces_instances.types.workspace_instance.WorkspaceInstance]":
        _token = next_token
        while True:
            _response = await self.list_workspace_instances(
                config_overrides=config_overrides,
                provision_states=provision_states,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workspace_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        tags: "aws_sdk_workspaces_instances.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>Unique identifier of the WorkSpace Instance to tag.</p>
            tags: <p>Tags to be added to the WorkSpace Instance.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        workspace_instance_id: "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId",
        tag_keys: "aws_sdk_workspaces_instances.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncWorkspacesInstancesClientConfig] = None,
    ) -> "aws_sdk_workspaces_instances.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a WorkSpace Instance.</p>

        Args:
            workspace_instance_id: <p>Unique identifier of the WorkSpace Instance to untag.</p>
            tag_keys: <p>Keys of tags to be removed.</p>

        Raises:
            aws_sdk_workspaces_instances.errors.access_denied_exception.AccessDeniedException: <p>Indicates insufficient permissions to perform the requested action.</p>
            aws_sdk_workspaces_instances.errors.internal_server_exception.InternalServerException: <p>Indicates an unexpected server-side error occurred.</p>
            aws_sdk_workspaces_instances.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates the requested resource could not be found.</p>
            aws_sdk_workspaces_instances.errors.throttling_exception.ThrottlingException: <p>Indicates the request rate has exceeded limits.</p>
            aws_sdk_workspaces_instances.errors.validation_exception.ValidationException: <p>Indicates invalid input parameters in the request.</p>
            aws_sdk_workspaces_instances.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workspaces_instances.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workspaces_instances.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_workspaces_instances._operations.eucmi_frontend_api_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_instances.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_instance_id"] = workspace_instance_id
        input_["tag_keys"] = tag_keys

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
