"""Generated from Smithy shape ``com.amazonaws.panorama#OmniCloudServiceLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_panorama._auth._signers
import aws_sdk_panorama._auth._sigv4
from aws_sdk_panorama._auth._identity import Credentials
from aws_sdk_panorama._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_panorama._auth._zapros_handler import AuthMiddleware
from aws_sdk_panorama._services._aws_config import aws_config
from aws_sdk_panorama._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id
    import aws_sdk_panorama.types.application_instance_name
    import aws_sdk_panorama.types.boolean
    import aws_sdk_panorama.types.client_token
    import aws_sdk_panorama.types.create_application_instance_request
    import aws_sdk_panorama.types.create_application_instance_response
    import aws_sdk_panorama.types.create_job_for_devices_request
    import aws_sdk_panorama.types.create_job_for_devices_response
    import aws_sdk_panorama.types.create_node_from_template_job_request
    import aws_sdk_panorama.types.create_node_from_template_job_response
    import aws_sdk_panorama.types.create_package_import_job_request
    import aws_sdk_panorama.types.create_package_import_job_response
    import aws_sdk_panorama.types.create_package_request
    import aws_sdk_panorama.types.create_package_response
    import aws_sdk_panorama.types.default_runtime_context_device
    import aws_sdk_panorama.types.delete_device_request
    import aws_sdk_panorama.types.delete_device_response
    import aws_sdk_panorama.types.delete_package_request
    import aws_sdk_panorama.types.delete_package_response
    import aws_sdk_panorama.types.deregister_package_version_request
    import aws_sdk_panorama.types.deregister_package_version_response
    import aws_sdk_panorama.types.describe_application_instance_details_request
    import aws_sdk_panorama.types.describe_application_instance_details_response
    import aws_sdk_panorama.types.describe_application_instance_request
    import aws_sdk_panorama.types.describe_application_instance_response
    import aws_sdk_panorama.types.describe_device_job_request
    import aws_sdk_panorama.types.describe_device_job_response
    import aws_sdk_panorama.types.describe_device_request
    import aws_sdk_panorama.types.describe_device_response
    import aws_sdk_panorama.types.describe_node_from_template_job_request
    import aws_sdk_panorama.types.describe_node_from_template_job_response
    import aws_sdk_panorama.types.describe_node_request
    import aws_sdk_panorama.types.describe_node_response
    import aws_sdk_panorama.types.describe_package_import_job_request
    import aws_sdk_panorama.types.describe_package_import_job_response
    import aws_sdk_panorama.types.describe_package_request
    import aws_sdk_panorama.types.describe_package_response
    import aws_sdk_panorama.types.describe_package_version_request
    import aws_sdk_panorama.types.describe_package_version_response
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.device_aggregated_status
    import aws_sdk_panorama.types.device_id
    import aws_sdk_panorama.types.device_id_list
    import aws_sdk_panorama.types.device_job_config
    import aws_sdk_panorama.types.device_name
    import aws_sdk_panorama.types.job_id
    import aws_sdk_panorama.types.job_tags_list
    import aws_sdk_panorama.types.job_type
    import aws_sdk_panorama.types.list_application_instance_dependencies_request
    import aws_sdk_panorama.types.list_application_instance_dependencies_response
    import aws_sdk_panorama.types.list_application_instance_node_instances_request
    import aws_sdk_panorama.types.list_application_instance_node_instances_response
    import aws_sdk_panorama.types.list_application_instances_request
    import aws_sdk_panorama.types.list_application_instances_response
    import aws_sdk_panorama.types.list_devices_jobs_request
    import aws_sdk_panorama.types.list_devices_jobs_response
    import aws_sdk_panorama.types.list_devices_request
    import aws_sdk_panorama.types.list_devices_response
    import aws_sdk_panorama.types.list_devices_sort_by
    import aws_sdk_panorama.types.list_node_from_template_jobs_request
    import aws_sdk_panorama.types.list_node_from_template_jobs_response
    import aws_sdk_panorama.types.list_nodes_request
    import aws_sdk_panorama.types.list_nodes_response
    import aws_sdk_panorama.types.list_package_import_jobs_request
    import aws_sdk_panorama.types.list_package_import_jobs_response
    import aws_sdk_panorama.types.list_packages_request
    import aws_sdk_panorama.types.list_packages_response
    import aws_sdk_panorama.types.list_tags_for_resource_request
    import aws_sdk_panorama.types.list_tags_for_resource_response
    import aws_sdk_panorama.types.manifest_overrides_payload
    import aws_sdk_panorama.types.manifest_payload
    import aws_sdk_panorama.types.mark_latest_patch
    import aws_sdk_panorama.types.max_size25
    import aws_sdk_panorama.types.name_filter
    import aws_sdk_panorama.types.network_payload
    import aws_sdk_panorama.types.next_token
    import aws_sdk_panorama.types.node_category
    import aws_sdk_panorama.types.node_id
    import aws_sdk_panorama.types.node_name
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.node_signal_list
    import aws_sdk_panorama.types.package_import_job_input_config
    import aws_sdk_panorama.types.package_import_job_output_config
    import aws_sdk_panorama.types.package_import_job_type
    import aws_sdk_panorama.types.package_owner_account
    import aws_sdk_panorama.types.provision_device_request
    import aws_sdk_panorama.types.provision_device_response
    import aws_sdk_panorama.types.register_package_version_request
    import aws_sdk_panorama.types.register_package_version_response
    import aws_sdk_panorama.types.remove_application_instance_request
    import aws_sdk_panorama.types.remove_application_instance_response
    import aws_sdk_panorama.types.resource_arn
    import aws_sdk_panorama.types.runtime_role_arn
    import aws_sdk_panorama.types.signal_application_instance_node_instances_request
    import aws_sdk_panorama.types.signal_application_instance_node_instances_response
    import aws_sdk_panorama.types.sort_order
    import aws_sdk_panorama.types.status_filter
    import aws_sdk_panorama.types.tag_key_list
    import aws_sdk_panorama.types.tag_map
    import aws_sdk_panorama.types.tag_resource_request
    import aws_sdk_panorama.types.tag_resource_response
    import aws_sdk_panorama.types.template_parameters_map
    import aws_sdk_panorama.types.template_type
    import aws_sdk_panorama.types.token
    import aws_sdk_panorama.types.untag_resource_request
    import aws_sdk_panorama.types.untag_resource_response
    import aws_sdk_panorama.types.update_device_metadata_request
    import aws_sdk_panorama.types.update_device_metadata_response


class PanoramaClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class PanoramaClient:
    """A client for the ``Panorama`` service.

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
        self._config = PanoramaClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[PanoramaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PanoramaClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_application_instance(
        self,
        manifest_payload: "aws_sdk_panorama.types.manifest_payload.ManifestPayload",
        default_runtime_context_device: "aws_sdk_panorama.types.default_runtime_context_device.DefaultRuntimeContextDevice",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        name: Optional[
            "aws_sdk_panorama.types.application_instance_name.ApplicationInstanceName"
        ] = None,
        description: Optional["aws_sdk_panorama.types.description.Description"] = None,
        manifest_overrides_payload: Optional[
            "aws_sdk_panorama.types.manifest_overrides_payload.ManifestOverridesPayload"
        ] = None,
        application_instance_id_to_replace: Optional[
            "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
        ] = None,
        runtime_role_arn: Optional[
            "aws_sdk_panorama.types.runtime_role_arn.RuntimeRoleArn"
        ] = None,
        tags: Optional["aws_sdk_panorama.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_panorama.types.create_application_instance_response.CreateApplicationInstanceResponse":
        """<p>Creates an application instance and deploys it to a device.</p>

        Args:
            name: <p>A name for the application instance.</p>
            description: <p>A description for the application instance.</p>
            manifest_payload: <p>The application's manifest document.</p>
            manifest_overrides_payload: <p>Setting overrides for the application manifest.</p>
            application_instance_id_to_replace: <p>The ID of an application instance to replace with the new instance.</p>
            runtime_role_arn: <p>The ARN of a runtime role for the application instance.</p>
            default_runtime_context_device: <p>A device's ID.</p>
            tags: <p>Tags for the application instance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.create_application_instance_request.CreateApplicationInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.create_application_instance_response.CreateApplicationInstanceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.create_application_instance

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.create_application_instance.create_application_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.create_application_instance_request.CreateApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["manifest_payload"] = manifest_payload
        if manifest_overrides_payload is not None:
            input_["manifest_overrides_payload"] = manifest_overrides_payload
        if application_instance_id_to_replace is not None:
            input_["application_instance_id_to_replace"] = (
                application_instance_id_to_replace
            )
        if runtime_role_arn is not None:
            input_["runtime_role_arn"] = runtime_role_arn
        input_["default_runtime_context_device"] = default_runtime_context_device
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_job_for_devices(
        self,
        device_ids: "aws_sdk_panorama.types.device_id_list.DeviceIdList",
        job_type: "aws_sdk_panorama.types.job_type.JobType",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        device_job_config: Optional[
            "aws_sdk_panorama.types.device_job_config.DeviceJobConfig"
        ] = None,
    ) -> "aws_sdk_panorama.types.create_job_for_devices_response.CreateJobForDevicesResponse":
        """<p>Creates a job to run on a device. A job can update a device's software or reboot it.</p>

        Args:
            device_ids: <p>ID of target device.</p>
            device_job_config: <p>Configuration settings for a software update job.</p>
            job_type: <p>The type of job to run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.create_job_for_devices_request.CreateJobForDevicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.create_job_for_devices_response.CreateJobForDevicesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.create_job_for_devices

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.create_job_for_devices.create_job_for_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.create_job_for_devices_request.CreateJobForDevicesRequest = {}  # type: ignore[typeddict-item]
        input_["device_ids"] = device_ids
        if device_job_config is not None:
            input_["device_job_config"] = device_job_config
        input_["job_type"] = job_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_node_from_template_job(
        self,
        template_type: "aws_sdk_panorama.types.template_type.TemplateType",
        output_package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName",
        output_package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion",
        node_name: "aws_sdk_panorama.types.node_name.NodeName",
        template_parameters: "aws_sdk_panorama.types.template_parameters_map.TemplateParametersMap",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        node_description: Optional[
            "aws_sdk_panorama.types.description.Description"
        ] = None,
        job_tags: Optional["aws_sdk_panorama.types.job_tags_list.JobTagsList"] = None,
    ) -> "aws_sdk_panorama.types.create_node_from_template_job_response.CreateNodeFromTemplateJobResponse":
        """<p>Creates a camera stream node.</p>

        Args:
            template_type: <p>The type of node.</p>
            output_package_name: <p>An output package name for the node.</p>
            output_package_version: <p>An output package version for the node.</p>
            node_name: <p>A name for the node.</p>
            node_description: <p>A description for the node.</p>
            template_parameters: <p>Template parameters for the node.</p>
            job_tags: <p>Tags for the job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.create_node_from_template_job_request.CreateNodeFromTemplateJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.create_node_from_template_job_response.CreateNodeFromTemplateJobResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.create_node_from_template_job

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.create_node_from_template_job.create_node_from_template_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.create_node_from_template_job_request.CreateNodeFromTemplateJobRequest = {}  # type: ignore[typeddict-item]
        input_["template_type"] = template_type
        input_["output_package_name"] = output_package_name
        input_["output_package_version"] = output_package_version
        input_["node_name"] = node_name
        if node_description is not None:
            input_["node_description"] = node_description
        input_["template_parameters"] = template_parameters
        if job_tags is not None:
            input_["job_tags"] = job_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_package(
        self,
        package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        tags: Optional["aws_sdk_panorama.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_panorama.types.create_package_response.CreatePackageResponse":
        """<p>Creates a package and storage location in an Amazon S3 access point.</p>

        Args:
            package_name: <p>A name for the package.</p>
            tags: <p>Tags for the package.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.create_package_request.CreatePackageRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.create_package_response.CreatePackageResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.create_package

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.create_package.create_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.create_package_request.CreatePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_name"] = package_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_package_import_job(
        self,
        job_type: "aws_sdk_panorama.types.package_import_job_type.PackageImportJobType",
        input_config: "aws_sdk_panorama.types.package_import_job_input_config.PackageImportJobInputConfig",
        output_config: "aws_sdk_panorama.types.package_import_job_output_config.PackageImportJobOutputConfig",
        client_token: "aws_sdk_panorama.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        job_tags: Optional["aws_sdk_panorama.types.job_tags_list.JobTagsList"] = None,
    ) -> "aws_sdk_panorama.types.create_package_import_job_response.CreatePackageImportJobResponse":
        """<p>Imports a node package.</p>

        Args:
            job_type: <p>A job type for the package import job.</p>
            input_config: <p>An input config for the package import job.</p>
            output_config: <p>An output config for the package import job.</p>
            client_token: <p>A client token for the package import job.</p>
            job_tags: <p>Tags for the package import job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.create_package_import_job_request.CreatePackageImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.create_package_import_job_response.CreatePackageImportJobResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.create_package_import_job

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.create_package_import_job.create_package_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.create_package_import_job_request.CreatePackageImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_type"] = job_type
        input_["input_config"] = input_config
        input_["output_config"] = output_config
        input_["client_token"] = client_token
        if job_tags is not None:
            input_["job_tags"] = job_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_device(
        self,
        device_id: "aws_sdk_panorama.types.device_id.DeviceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.delete_device_response.DeleteDeviceResponse":
        """<p>Deletes a device.</p>

        Args:
            device_id: <p>The device's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.delete_device_request.DeleteDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.delete_device_response.DeleteDeviceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.delete_device

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.delete_device.delete_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.delete_device_request.DeleteDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_package(
        self,
        package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        force_delete: Optional["aws_sdk_panorama.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_panorama.types.delete_package_response.DeletePackageResponse":
        """<p>Deletes a package.</p> <note> <p>To delete a package, you need permission to call <code>s3:DeleteObject</code> in addition to permissions for the AWS Panorama API.</p> </note>

        Args:
            package_id: <p>The package's ID.</p>
            force_delete: <p>Delete the package even if it has artifacts stored in its access point. Deletes the package's artifacts from Amazon S3.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.delete_package_request.DeletePackageRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.delete_package_response.DeletePackageResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.delete_package

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.delete_package.delete_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.delete_package_request.DeletePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_package_version(
        self,
        package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId",
        package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion",
        patch_version: "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        owner_account: Optional[
            "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
        ] = None,
        updated_latest_patch_version: Optional[
            "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
        ] = None,
    ) -> "aws_sdk_panorama.types.deregister_package_version_response.DeregisterPackageVersionResponse":
        """<p>Deregisters a package version.</p>

        Args:
            owner_account: <p>An owner account.</p>
            package_id: <p>A package ID.</p>
            package_version: <p>A package version.</p>
            patch_version: <p>A patch version.</p>
            updated_latest_patch_version: <p>If the version was marked latest, the new version to maker as latest.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.deregister_package_version_request.DeregisterPackageVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.deregister_package_version_response.DeregisterPackageVersionResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.deregister_package_version

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.deregister_package_version.deregister_package_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.deregister_package_version_request.DeregisterPackageVersionRequest = {}  # type: ignore[typeddict-item]
        if owner_account is not None:
            input_["owner_account"] = owner_account
        input_["package_id"] = package_id
        input_["package_version"] = package_version
        input_["patch_version"] = patch_version
        if updated_latest_patch_version is not None:
            input_["updated_latest_patch_version"] = updated_latest_patch_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application_instance(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_application_instance_response.DescribeApplicationInstanceResponse":
        """<p>Returns information about an application instance on a device.</p>

        Args:
            application_instance_id: <p>The application instance's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_application_instance_request.DescribeApplicationInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_application_instance_response.DescribeApplicationInstanceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_application_instance

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_application_instance.describe_application_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_application_instance_request.DescribeApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application_instance_details(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_application_instance_details_response.DescribeApplicationInstanceDetailsResponse":
        """<p>Returns information about an application instance's configuration manifest.</p>

        Args:
            application_instance_id: <p>The application instance's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_application_instance_details_request.DescribeApplicationInstanceDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_application_instance_details_response.DescribeApplicationInstanceDetailsResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_application_instance_details

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_application_instance_details.describe_application_instance_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_application_instance_details_request.DescribeApplicationInstanceDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_device(
        self,
        device_id: "aws_sdk_panorama.types.device_id.DeviceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_device_response.DescribeDeviceResponse":
        """<p>Returns information about a device.</p>

        Args:
            device_id: <p>The device's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_device_request.DescribeDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_device_response.DescribeDeviceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_device

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_device.describe_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_device_request.DescribeDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_device_job(
        self,
        job_id: "aws_sdk_panorama.types.job_id.JobId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> (
        "aws_sdk_panorama.types.describe_device_job_response.DescribeDeviceJobResponse"
    ):
        """<p>Returns information about a device job.</p>

        Args:
            job_id: <p>The job's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_device_job_request.DescribeDeviceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_device_job_response.DescribeDeviceJobResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_device_job

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_device_job.describe_device_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_device_job_request.DescribeDeviceJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_node(
        self,
        node_id: "aws_sdk_panorama.types.node_id.NodeId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        owner_account: Optional[
            "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
        ] = None,
    ) -> "aws_sdk_panorama.types.describe_node_response.DescribeNodeResponse":
        """<p>Returns information about a node.</p>

        Args:
            node_id: <p>The node's ID.</p>
            owner_account: <p>The account ID of the node's owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_node_request.DescribeNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_node_response.DescribeNodeResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_node

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_node.describe_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_node_request.DescribeNodeRequest = {}  # type: ignore[typeddict-item]
        input_["node_id"] = node_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_node_from_template_job(
        self,
        job_id: "aws_sdk_panorama.types.job_id.JobId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_node_from_template_job_response.DescribeNodeFromTemplateJobResponse":
        """<p>Returns information about a job to create a camera stream node.</p>

        Args:
            job_id: <p>The job's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_node_from_template_job_request.DescribeNodeFromTemplateJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_node_from_template_job_response.DescribeNodeFromTemplateJobResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_node_from_template_job

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_node_from_template_job.describe_node_from_template_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_node_from_template_job_request.DescribeNodeFromTemplateJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_package(
        self,
        package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_package_response.DescribePackageResponse":
        """<p>Returns information about a package.</p>

        Args:
            package_id: <p>The package's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_package_request.DescribePackageRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_package_response.DescribePackageResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package.describe_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_package_request.DescribePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_package_import_job(
        self,
        job_id: "aws_sdk_panorama.types.job_id.JobId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.describe_package_import_job_response.DescribePackageImportJobResponse":
        """<p>Returns information about a package import job.</p>

        Args:
            job_id: <p>The job's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_package_import_job_request.DescribePackageImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_package_import_job_response.DescribePackageImportJobResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package_import_job

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package_import_job.describe_package_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_package_import_job_request.DescribePackageImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_package_version(
        self,
        package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId",
        package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        owner_account: Optional[
            "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
        ] = None,
        patch_version: Optional[
            "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
        ] = None,
    ) -> "aws_sdk_panorama.types.describe_package_version_response.DescribePackageVersionResponse":
        """<p>Returns information about a package version.</p>

        Args:
            owner_account: <p>The version's owner account.</p>
            package_id: <p>The version's ID.</p>
            package_version: <p>The version's version.</p>
            patch_version: <p>The version's patch version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.describe_package_version_request.DescribePackageVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.describe_package_version_response.DescribePackageVersionResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package_version

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.describe_package_version.describe_package_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.describe_package_version_request.DescribePackageVersionRequest = {}  # type: ignore[typeddict-item]
        if owner_account is not None:
            input_["owner_account"] = owner_account
        input_["package_id"] = package_id
        input_["package_version"] = package_version
        if patch_version is not None:
            input_["patch_version"] = patch_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_application_instance_dependencies(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_panorama.types.list_application_instance_dependencies_response.ListApplicationInstanceDependenciesResponse":
        """<p>Returns a list of application instance dependencies.</p>

        Args:
            application_instance_id: <p>The application instance's ID.</p>
            max_results: <p>The maximum number of application instance dependencies to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_application_instance_dependencies_request.ListApplicationInstanceDependenciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_application_instance_dependencies_response.ListApplicationInstanceDependenciesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instance_dependencies

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instance_dependencies.list_application_instance_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_application_instance_dependencies_request.ListApplicationInstanceDependenciesRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_application_instance_node_instances(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_panorama.types.list_application_instance_node_instances_response.ListApplicationInstanceNodeInstancesResponse":
        """<p>Returns a list of application node instances.</p>

        Args:
            application_instance_id: <p>The node instances' application instance ID.</p>
            max_results: <p>The maximum number of node instances to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_application_instance_node_instances_request.ListApplicationInstanceNodeInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_application_instance_node_instances_response.ListApplicationInstanceNodeInstancesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instance_node_instances

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instance_node_instances.list_application_instance_node_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_application_instance_node_instances_request.ListApplicationInstanceNodeInstancesRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_application_instances(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        device_id: Optional["aws_sdk_panorama.types.device_id.DeviceId"] = None,
        status_filter: Optional[
            "aws_sdk_panorama.types.status_filter.StatusFilter"
        ] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_panorama.types.list_application_instances_response.ListApplicationInstancesResponse":
        """<p>Returns a list of application instances.</p>

        Args:
            device_id: <p>The application instances' device ID.</p>
            status_filter: <p>Only include instances with a specific status.</p>
            max_results: <p>The maximum number of application instances to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_application_instances_request.ListApplicationInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_application_instances_response.ListApplicationInstancesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instances

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_application_instances.list_application_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_application_instances_request.ListApplicationInstancesRequest = {}  # type: ignore[typeddict-item]
        if device_id is not None:
            input_["device_id"] = device_id
        if status_filter is not None:
            input_["status_filter"] = status_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_devices(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
        sort_by: Optional[
            "aws_sdk_panorama.types.list_devices_sort_by.ListDevicesSortBy"
        ] = None,
        sort_order: Optional["aws_sdk_panorama.types.sort_order.SortOrder"] = None,
        name_filter: Optional["aws_sdk_panorama.types.name_filter.NameFilter"] = None,
        device_aggregated_status_filter: Optional[
            "aws_sdk_panorama.types.device_aggregated_status.DeviceAggregatedStatus"
        ] = None,
    ) -> "aws_sdk_panorama.types.list_devices_response.ListDevicesResponse":
        """<p>Returns a list of devices.</p>

        Args:
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of devices to return in one page of results.</p>
            sort_by: <p>The target column to be sorted on. Default column sort is CREATED_TIME.</p>
            sort_order: <p>The sorting order for the returned list. SortOrder is DESCENDING by default based on CREATED_TIME. Otherwise, SortOrder is ASCENDING.</p>
            name_filter: <p>Filter based on device's name. Prefixes supported.</p>
            device_aggregated_status_filter: <p>Filter based on a device's status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_devices_request.ListDevicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_devices_response.ListDevicesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_devices

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_devices_request.ListDevicesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if name_filter is not None:
            input_["name_filter"] = name_filter
        if device_aggregated_status_filter is not None:
            input_["device_aggregated_status_filter"] = device_aggregated_status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_devices_jobs(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        device_id: Optional["aws_sdk_panorama.types.device_id.DeviceId"] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
    ) -> "aws_sdk_panorama.types.list_devices_jobs_response.ListDevicesJobsResponse":
        """<p>Returns a list of jobs.</p>

        Args:
            device_id: <p>Filter results by the job's target device ID.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of device jobs to return in one page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_devices_jobs_request.ListDevicesJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_devices_jobs_response.ListDevicesJobsResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_devices_jobs

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_devices_jobs.list_devices_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_devices_jobs_request.ListDevicesJobsRequest = {}  # type: ignore[typeddict-item]
        if device_id is not None:
            input_["device_id"] = device_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_node_from_template_jobs(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
    ) -> "aws_sdk_panorama.types.list_node_from_template_jobs_response.ListNodeFromTemplateJobsResponse":
        """<p>Returns a list of camera stream node jobs.</p>

        Args:
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of node from template jobs to return in one page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_node_from_template_jobs_request.ListNodeFromTemplateJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_node_from_template_jobs_response.ListNodeFromTemplateJobsResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_node_from_template_jobs

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_node_from_template_jobs.list_node_from_template_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_node_from_template_jobs_request.ListNodeFromTemplateJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_nodes(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        category: Optional["aws_sdk_panorama.types.node_category.NodeCategory"] = None,
        owner_account: Optional[
            "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
        ] = None,
        package_name: Optional[
            "aws_sdk_panorama.types.node_package_name.NodePackageName"
        ] = None,
        package_version: Optional[
            "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
        ] = None,
        patch_version: Optional[
            "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
        ] = None,
        next_token: Optional["aws_sdk_panorama.types.token.Token"] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
    ) -> "aws_sdk_panorama.types.list_nodes_response.ListNodesResponse":
        """<p>Returns a list of nodes.</p>

        Args:
            category: <p>Search for nodes by category.</p>
            owner_account: <p>Search for nodes by the account ID of the nodes' owner.</p>
            package_name: <p>Search for nodes by name.</p>
            package_version: <p>Search for nodes by version.</p>
            patch_version: <p>Search for nodes by patch version.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of nodes to return in one page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_nodes_request.ListNodesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_nodes_response.ListNodesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_nodes

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_nodes.list_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_nodes_request.ListNodesRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if package_name is not None:
            input_["package_name"] = package_name
        if package_version is not None:
            input_["package_version"] = package_version
        if patch_version is not None:
            input_["patch_version"] = patch_version
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_package_import_jobs(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        next_token: Optional["aws_sdk_panorama.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
    ) -> "aws_sdk_panorama.types.list_package_import_jobs_response.ListPackageImportJobsResponse":
        """<p>Returns a list of package import jobs.</p>

        Args:
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of package import jobs to return in one page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_package_import_jobs_request.ListPackageImportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_package_import_jobs_response.ListPackageImportJobsResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_package_import_jobs

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_package_import_jobs.list_package_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_package_import_jobs_request.ListPackageImportJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_packages(
        self,
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        max_results: Optional["aws_sdk_panorama.types.max_size25.MaxSize25"] = None,
        next_token: Optional["aws_sdk_panorama.types.token.Token"] = None,
    ) -> "aws_sdk_panorama.types.list_packages_response.ListPackagesResponse":
        """<p>Returns a list of packages.</p>

        Args:
            max_results: <p>The maximum number of packages to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_packages_request.ListPackagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_packages_response.ListPackagesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_packages

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_packages.list_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_packages_request.ListPackagesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_panorama.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.list_tags_for_resource

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def provision_device(
        self,
        name: "aws_sdk_panorama.types.device_name.DeviceName",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        description: Optional["aws_sdk_panorama.types.description.Description"] = None,
        tags: Optional["aws_sdk_panorama.types.tag_map.TagMap"] = None,
        networking_configuration: Optional[
            "aws_sdk_panorama.types.network_payload.NetworkPayload"
        ] = None,
    ) -> "aws_sdk_panorama.types.provision_device_response.ProvisionDeviceResponse":
        """<p>Creates a device and returns a configuration archive. The configuration archive is a ZIP file that contains a provisioning certificate that is valid for 5 minutes. Name the configuration archive <code>certificates-omni_<i>device-name</i>.zip</code> and transfer it to the device within 5 minutes. Use the included USB storage device and connect it to the USB 3.0 port next to the HDMI output.</p>

        Args:
            name: <p>A name for the device.</p>
            description: <p>A description for the device.</p>
            tags: <p>Tags for the device.</p>
            networking_configuration: <p>A networking configuration for the device.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.provision_device_request.ProvisionDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.provision_device_response.ProvisionDeviceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.provision_device

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.provision_device.provision_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.provision_device_request.ProvisionDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if networking_configuration is not None:
            input_["networking_configuration"] = networking_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_package_version(
        self,
        package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId",
        package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion",
        patch_version: "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        owner_account: Optional[
            "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
        ] = None,
        mark_latest: Optional[
            "aws_sdk_panorama.types.mark_latest_patch.MarkLatestPatch"
        ] = None,
    ) -> "aws_sdk_panorama.types.register_package_version_response.RegisterPackageVersionResponse":
        """<p>Registers a package version.</p>

        Args:
            owner_account: <p>An owner account.</p>
            package_id: <p>A package ID.</p>
            package_version: <p>A package version.</p>
            patch_version: <p>A patch version.</p>
            mark_latest: <p>Whether to mark the new version as the latest version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.register_package_version_request.RegisterPackageVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.register_package_version_response.RegisterPackageVersionResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.register_package_version

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.register_package_version.register_package_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.register_package_version_request.RegisterPackageVersionRequest = {}  # type: ignore[typeddict-item]
        if owner_account is not None:
            input_["owner_account"] = owner_account
        input_["package_id"] = package_id
        input_["package_version"] = package_version
        input_["patch_version"] = patch_version
        if mark_latest is not None:
            input_["mark_latest"] = mark_latest

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_application_instance(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.remove_application_instance_response.RemoveApplicationInstanceResponse":
        """<p>Removes an application instance.</p>

        Args:
            application_instance_id: <p>An application instance ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.remove_application_instance_request.RemoveApplicationInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.remove_application_instance_response.RemoveApplicationInstanceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.remove_application_instance

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.remove_application_instance.remove_application_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.remove_application_instance_request.RemoveApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def signal_application_instance_node_instances(
        self,
        application_instance_id: "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId",
        node_signals: "aws_sdk_panorama.types.node_signal_list.NodeSignalList",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.signal_application_instance_node_instances_response.SignalApplicationInstanceNodeInstancesResponse":
        """<p>Signal camera nodes to stop or resume.</p>

        Args:
            application_instance_id: <p>An application instance ID.</p>
            node_signals: <p>A list of signals.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.signal_application_instance_node_instances_request.SignalApplicationInstanceNodeInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.signal_application_instance_node_instances_response.SignalApplicationInstanceNodeInstancesResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.signal_application_instance_node_instances

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.signal_application_instance_node_instances.signal_application_instance_node_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.signal_application_instance_node_instances_request.SignalApplicationInstanceNodeInstancesRequest = {}  # type: ignore[typeddict-item]
        input_["application_instance_id"] = application_instance_id
        input_["node_signals"] = node_signals

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_panorama.types.resource_arn.ResourceArn",
        tags: "aws_sdk_panorama.types.tag_map.TagMap",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.tag_resource

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_panorama.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_panorama.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
    ) -> "aws_sdk_panorama.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Tag keys to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.untag_resource

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_device_metadata(
        self,
        device_id: "aws_sdk_panorama.types.device_id.DeviceId",
        *,
        config_overrides: Optional[PanoramaClientConfig] = None,
        description: Optional["aws_sdk_panorama.types.description.Description"] = None,
    ) -> "aws_sdk_panorama.types.update_device_metadata_response.UpdateDeviceMetadataResponse":
        """<p>Updates a device's metadata.</p>

        Args:
            device_id: <p>The device's ID.</p>
            description: <p>A description for the device.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_panorama.types.update_device_metadata_request.UpdateDeviceMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_panorama.types.update_device_metadata_response.UpdateDeviceMetadataResponse"
        ]:
            import aws_sdk_panorama._operations.omni_cloud_service_lambda.update_device_metadata

            output, http_response = (
                aws_sdk_panorama._operations.omni_cloud_service_lambda.update_device_metadata.update_device_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_panorama.types.update_device_metadata_request.UpdateDeviceMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["device_id"] = device_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
