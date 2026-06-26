"""Generated from Smithy shape ``com.amazonaws.imagebuilder#imagebuilder``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_imagebuilder._auth._signers
import aws_sdk_imagebuilder._auth._sigv4
from aws_sdk_imagebuilder._auth._identity import Credentials
from aws_sdk_imagebuilder._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_imagebuilder._auth._zapros_handler import AuthMiddleware
from aws_sdk_imagebuilder._pagination import resolve_path as _resolve_path
from aws_sdk_imagebuilder._services._aws_config import aws_config
from aws_sdk_imagebuilder._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.additional_instance_configuration
    import aws_sdk_imagebuilder.types.boolean
    import aws_sdk_imagebuilder.types.cancel_image_creation_request
    import aws_sdk_imagebuilder.types.cancel_image_creation_response
    import aws_sdk_imagebuilder.types.cancel_lifecycle_execution_request
    import aws_sdk_imagebuilder.types.cancel_lifecycle_execution_response
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.component_build_version_arn
    import aws_sdk_imagebuilder.types.component_configuration_list
    import aws_sdk_imagebuilder.types.component_format
    import aws_sdk_imagebuilder.types.component_summary
    import aws_sdk_imagebuilder.types.component_type
    import aws_sdk_imagebuilder.types.component_version
    import aws_sdk_imagebuilder.types.component_version_arn
    import aws_sdk_imagebuilder.types.component_version_arn_or_build_version_arn
    import aws_sdk_imagebuilder.types.container_recipe_arn
    import aws_sdk_imagebuilder.types.container_recipe_summary
    import aws_sdk_imagebuilder.types.container_type
    import aws_sdk_imagebuilder.types.create_component_request
    import aws_sdk_imagebuilder.types.create_component_response
    import aws_sdk_imagebuilder.types.create_container_recipe_request
    import aws_sdk_imagebuilder.types.create_container_recipe_response
    import aws_sdk_imagebuilder.types.create_distribution_configuration_request
    import aws_sdk_imagebuilder.types.create_distribution_configuration_response
    import aws_sdk_imagebuilder.types.create_image_pipeline_request
    import aws_sdk_imagebuilder.types.create_image_pipeline_response
    import aws_sdk_imagebuilder.types.create_image_recipe_request
    import aws_sdk_imagebuilder.types.create_image_recipe_response
    import aws_sdk_imagebuilder.types.create_image_request
    import aws_sdk_imagebuilder.types.create_image_response
    import aws_sdk_imagebuilder.types.create_infrastructure_configuration_request
    import aws_sdk_imagebuilder.types.create_infrastructure_configuration_response
    import aws_sdk_imagebuilder.types.create_lifecycle_policy_request
    import aws_sdk_imagebuilder.types.create_lifecycle_policy_response
    import aws_sdk_imagebuilder.types.create_workflow_request
    import aws_sdk_imagebuilder.types.create_workflow_response
    import aws_sdk_imagebuilder.types.date_time_timestamp
    import aws_sdk_imagebuilder.types.delete_component_request
    import aws_sdk_imagebuilder.types.delete_component_response
    import aws_sdk_imagebuilder.types.delete_container_recipe_request
    import aws_sdk_imagebuilder.types.delete_container_recipe_response
    import aws_sdk_imagebuilder.types.delete_distribution_configuration_request
    import aws_sdk_imagebuilder.types.delete_distribution_configuration_response
    import aws_sdk_imagebuilder.types.delete_image_pipeline_request
    import aws_sdk_imagebuilder.types.delete_image_pipeline_response
    import aws_sdk_imagebuilder.types.delete_image_recipe_request
    import aws_sdk_imagebuilder.types.delete_image_recipe_response
    import aws_sdk_imagebuilder.types.delete_image_request
    import aws_sdk_imagebuilder.types.delete_image_response
    import aws_sdk_imagebuilder.types.delete_infrastructure_configuration_request
    import aws_sdk_imagebuilder.types.delete_infrastructure_configuration_response
    import aws_sdk_imagebuilder.types.delete_lifecycle_policy_request
    import aws_sdk_imagebuilder.types.delete_lifecycle_policy_response
    import aws_sdk_imagebuilder.types.delete_workflow_request
    import aws_sdk_imagebuilder.types.delete_workflow_response
    import aws_sdk_imagebuilder.types.distribute_image_request
    import aws_sdk_imagebuilder.types.distribute_image_response
    import aws_sdk_imagebuilder.types.distribution_configuration_arn
    import aws_sdk_imagebuilder.types.distribution_configuration_summary
    import aws_sdk_imagebuilder.types.distribution_list
    import aws_sdk_imagebuilder.types.filter
    import aws_sdk_imagebuilder.types.filter_list
    import aws_sdk_imagebuilder.types.get_component_policy_request
    import aws_sdk_imagebuilder.types.get_component_policy_response
    import aws_sdk_imagebuilder.types.get_component_request
    import aws_sdk_imagebuilder.types.get_component_response
    import aws_sdk_imagebuilder.types.get_container_recipe_policy_request
    import aws_sdk_imagebuilder.types.get_container_recipe_policy_response
    import aws_sdk_imagebuilder.types.get_container_recipe_request
    import aws_sdk_imagebuilder.types.get_container_recipe_response
    import aws_sdk_imagebuilder.types.get_distribution_configuration_request
    import aws_sdk_imagebuilder.types.get_distribution_configuration_response
    import aws_sdk_imagebuilder.types.get_image_pipeline_request
    import aws_sdk_imagebuilder.types.get_image_pipeline_response
    import aws_sdk_imagebuilder.types.get_image_policy_request
    import aws_sdk_imagebuilder.types.get_image_policy_response
    import aws_sdk_imagebuilder.types.get_image_recipe_policy_request
    import aws_sdk_imagebuilder.types.get_image_recipe_policy_response
    import aws_sdk_imagebuilder.types.get_image_recipe_request
    import aws_sdk_imagebuilder.types.get_image_recipe_response
    import aws_sdk_imagebuilder.types.get_image_request
    import aws_sdk_imagebuilder.types.get_image_response
    import aws_sdk_imagebuilder.types.get_infrastructure_configuration_request
    import aws_sdk_imagebuilder.types.get_infrastructure_configuration_response
    import aws_sdk_imagebuilder.types.get_lifecycle_execution_request
    import aws_sdk_imagebuilder.types.get_lifecycle_execution_response
    import aws_sdk_imagebuilder.types.get_lifecycle_policy_request
    import aws_sdk_imagebuilder.types.get_lifecycle_policy_response
    import aws_sdk_imagebuilder.types.get_marketplace_resource_request
    import aws_sdk_imagebuilder.types.get_marketplace_resource_response
    import aws_sdk_imagebuilder.types.get_workflow_execution_request
    import aws_sdk_imagebuilder.types.get_workflow_execution_response
    import aws_sdk_imagebuilder.types.get_workflow_request
    import aws_sdk_imagebuilder.types.get_workflow_response
    import aws_sdk_imagebuilder.types.get_workflow_step_execution_request
    import aws_sdk_imagebuilder.types.get_workflow_step_execution_response
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.image_logging_configuration
    import aws_sdk_imagebuilder.types.image_package
    import aws_sdk_imagebuilder.types.image_pipeline
    import aws_sdk_imagebuilder.types.image_pipeline_arn
    import aws_sdk_imagebuilder.types.image_recipe_arn
    import aws_sdk_imagebuilder.types.image_recipe_summary
    import aws_sdk_imagebuilder.types.image_scan_finding
    import aws_sdk_imagebuilder.types.image_scan_finding_aggregation
    import aws_sdk_imagebuilder.types.image_scan_findings_filter_list
    import aws_sdk_imagebuilder.types.image_scanning_configuration
    import aws_sdk_imagebuilder.types.image_summary
    import aws_sdk_imagebuilder.types.image_tests_configuration
    import aws_sdk_imagebuilder.types.image_version
    import aws_sdk_imagebuilder.types.image_version_arn
    import aws_sdk_imagebuilder.types.image_version_arn_or_build_version_arn
    import aws_sdk_imagebuilder.types.import_component_request
    import aws_sdk_imagebuilder.types.import_component_response
    import aws_sdk_imagebuilder.types.import_disk_image_request
    import aws_sdk_imagebuilder.types.import_disk_image_response
    import aws_sdk_imagebuilder.types.import_vm_image_request
    import aws_sdk_imagebuilder.types.import_vm_image_response
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn
    import aws_sdk_imagebuilder.types.infrastructure_configuration_summary
    import aws_sdk_imagebuilder.types.inline_component_data
    import aws_sdk_imagebuilder.types.inline_docker_file_template
    import aws_sdk_imagebuilder.types.inline_workflow_data
    import aws_sdk_imagebuilder.types.instance_block_device_mappings
    import aws_sdk_imagebuilder.types.instance_configuration
    import aws_sdk_imagebuilder.types.instance_metadata_options
    import aws_sdk_imagebuilder.types.instance_profile_name_type
    import aws_sdk_imagebuilder.types.instance_type_list
    import aws_sdk_imagebuilder.types.lifecycle_execution
    import aws_sdk_imagebuilder.types.lifecycle_execution_id
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource
    import aws_sdk_imagebuilder.types.lifecycle_policy_arn
    import aws_sdk_imagebuilder.types.lifecycle_policy_details
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type
    import aws_sdk_imagebuilder.types.lifecycle_policy_status
    import aws_sdk_imagebuilder.types.lifecycle_policy_summary
    import aws_sdk_imagebuilder.types.list_component_build_versions_request
    import aws_sdk_imagebuilder.types.list_component_build_versions_response
    import aws_sdk_imagebuilder.types.list_components_request
    import aws_sdk_imagebuilder.types.list_components_response
    import aws_sdk_imagebuilder.types.list_container_recipes_request
    import aws_sdk_imagebuilder.types.list_container_recipes_response
    import aws_sdk_imagebuilder.types.list_distribution_configurations_request
    import aws_sdk_imagebuilder.types.list_distribution_configurations_response
    import aws_sdk_imagebuilder.types.list_image_build_versions_request
    import aws_sdk_imagebuilder.types.list_image_build_versions_response
    import aws_sdk_imagebuilder.types.list_image_packages_request
    import aws_sdk_imagebuilder.types.list_image_packages_response
    import aws_sdk_imagebuilder.types.list_image_pipeline_images_request
    import aws_sdk_imagebuilder.types.list_image_pipeline_images_response
    import aws_sdk_imagebuilder.types.list_image_pipelines_request
    import aws_sdk_imagebuilder.types.list_image_pipelines_response
    import aws_sdk_imagebuilder.types.list_image_recipes_request
    import aws_sdk_imagebuilder.types.list_image_recipes_response
    import aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_request
    import aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_response
    import aws_sdk_imagebuilder.types.list_image_scan_findings_request
    import aws_sdk_imagebuilder.types.list_image_scan_findings_response
    import aws_sdk_imagebuilder.types.list_images_request
    import aws_sdk_imagebuilder.types.list_images_response
    import aws_sdk_imagebuilder.types.list_infrastructure_configurations_request
    import aws_sdk_imagebuilder.types.list_infrastructure_configurations_response
    import aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_request
    import aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_response
    import aws_sdk_imagebuilder.types.list_lifecycle_executions_request
    import aws_sdk_imagebuilder.types.list_lifecycle_executions_response
    import aws_sdk_imagebuilder.types.list_lifecycle_policies_request
    import aws_sdk_imagebuilder.types.list_lifecycle_policies_response
    import aws_sdk_imagebuilder.types.list_tags_for_resource_request
    import aws_sdk_imagebuilder.types.list_tags_for_resource_response
    import aws_sdk_imagebuilder.types.list_waiting_workflow_steps_request
    import aws_sdk_imagebuilder.types.list_waiting_workflow_steps_response
    import aws_sdk_imagebuilder.types.list_workflow_build_versions_request
    import aws_sdk_imagebuilder.types.list_workflow_build_versions_response
    import aws_sdk_imagebuilder.types.list_workflow_executions_request
    import aws_sdk_imagebuilder.types.list_workflow_executions_response
    import aws_sdk_imagebuilder.types.list_workflow_step_executions_request
    import aws_sdk_imagebuilder.types.list_workflow_step_executions_response
    import aws_sdk_imagebuilder.types.list_workflows_request
    import aws_sdk_imagebuilder.types.list_workflows_response
    import aws_sdk_imagebuilder.types.logging
    import aws_sdk_imagebuilder.types.marketplace_resource_location
    import aws_sdk_imagebuilder.types.marketplace_resource_type
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.os_version
    import aws_sdk_imagebuilder.types.os_version_list
    import aws_sdk_imagebuilder.types.ownership
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.pipeline_logging_configuration
    import aws_sdk_imagebuilder.types.pipeline_status
    import aws_sdk_imagebuilder.types.placement
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.put_component_policy_request
    import aws_sdk_imagebuilder.types.put_component_policy_response
    import aws_sdk_imagebuilder.types.put_container_recipe_policy_request
    import aws_sdk_imagebuilder.types.put_container_recipe_policy_response
    import aws_sdk_imagebuilder.types.put_image_policy_request
    import aws_sdk_imagebuilder.types.put_image_policy_response
    import aws_sdk_imagebuilder.types.put_image_recipe_policy_request
    import aws_sdk_imagebuilder.types.put_image_recipe_policy_response
    import aws_sdk_imagebuilder.types.register_image_options
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.resource_policy_document
    import aws_sdk_imagebuilder.types.resource_state
    import aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules
    import aws_sdk_imagebuilder.types.resource_state_update_include_resources
    import aws_sdk_imagebuilder.types.resource_tag_map
    import aws_sdk_imagebuilder.types.restricted_integer
    import aws_sdk_imagebuilder.types.retry_image_request
    import aws_sdk_imagebuilder.types.retry_image_response
    import aws_sdk_imagebuilder.types.role_name_or_arn
    import aws_sdk_imagebuilder.types.schedule
    import aws_sdk_imagebuilder.types.security_group_ids
    import aws_sdk_imagebuilder.types.send_workflow_step_action_request
    import aws_sdk_imagebuilder.types.send_workflow_step_action_response
    import aws_sdk_imagebuilder.types.sns_topic_arn
    import aws_sdk_imagebuilder.types.start_image_pipeline_execution_request
    import aws_sdk_imagebuilder.types.start_image_pipeline_execution_response
    import aws_sdk_imagebuilder.types.start_resource_state_update_request
    import aws_sdk_imagebuilder.types.start_resource_state_update_response
    import aws_sdk_imagebuilder.types.tag_key_list
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.tag_resource_request
    import aws_sdk_imagebuilder.types.tag_resource_response
    import aws_sdk_imagebuilder.types.target_container_repository
    import aws_sdk_imagebuilder.types.untag_resource_request
    import aws_sdk_imagebuilder.types.untag_resource_response
    import aws_sdk_imagebuilder.types.update_distribution_configuration_request
    import aws_sdk_imagebuilder.types.update_distribution_configuration_response
    import aws_sdk_imagebuilder.types.update_image_pipeline_request
    import aws_sdk_imagebuilder.types.update_image_pipeline_response
    import aws_sdk_imagebuilder.types.update_infrastructure_configuration_request
    import aws_sdk_imagebuilder.types.update_infrastructure_configuration_response
    import aws_sdk_imagebuilder.types.update_lifecycle_policy_request
    import aws_sdk_imagebuilder.types.update_lifecycle_policy_response
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.version_number
    import aws_sdk_imagebuilder.types.wildcard_version_number
    import aws_sdk_imagebuilder.types.windows_configuration
    import aws_sdk_imagebuilder.types.workflow_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_configuration_list
    import aws_sdk_imagebuilder.types.workflow_execution_id
    import aws_sdk_imagebuilder.types.workflow_execution_metadata
    import aws_sdk_imagebuilder.types.workflow_step_action_type
    import aws_sdk_imagebuilder.types.workflow_step_execution
    import aws_sdk_imagebuilder.types.workflow_step_execution_id
    import aws_sdk_imagebuilder.types.workflow_step_metadata
    import aws_sdk_imagebuilder.types.workflow_summary
    import aws_sdk_imagebuilder.types.workflow_type
    import aws_sdk_imagebuilder.types.workflow_version
    import aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_wildcard_version_arn


class imagebuilderClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class imagebuilderClient:
    """A client for the ``imagebuilder`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = imagebuilderClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[imagebuilderClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: imagebuilderClientConfig = config_overrides or {}
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

    def cancel_image_creation(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.cancel_image_creation_response.CancelImageCreationResponse":
        r"""<p>CancelImageCreation cancels the creation of Image. This operation can only be used on images in a non-terminal state.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image that you want to cancel creation for.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.cancel_image_creation_request.CancelImageCreationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.cancel_image_creation_response.CancelImageCreationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.cancel_image_creation

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.cancel_image_creation.cancel_image_creation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.cancel_image_creation_request.CancelImageCreationRequest = {}  # type: ignore[typeddict-item]
        input_["image_build_version_arn"] = image_build_version_arn
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_lifecycle_execution(
        self,
        lifecycle_execution_id: "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.cancel_lifecycle_execution_response.CancelLifecycleExecutionResponse":
        r"""<p>Cancel a specific image lifecycle policy runtime instance.</p>

        Args:
            lifecycle_execution_id: <p>Identifies the specific runtime instance of the image lifecycle to cancel.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.cancel_lifecycle_execution_request.CancelLifecycleExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.cancel_lifecycle_execution_response.CancelLifecycleExecutionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.cancel_lifecycle_execution

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.cancel_lifecycle_execution.cancel_lifecycle_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.cancel_lifecycle_execution_request.CancelLifecycleExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_execution_id"] = lifecycle_execution_id
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_component(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber",
        platform: "aws_sdk_imagebuilder.types.platform.Platform",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        supported_os_versions: Optional[
            "aws_sdk_imagebuilder.types.os_version_list.OsVersionList"
        ] = None,
        data: Optional[
            "aws_sdk_imagebuilder.types.inline_component_data.InlineComponentData"
        ] = None,
        uri: Optional["aws_sdk_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_component_response.CreateComponentResponse":
        r"""<p>Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:</p> <ul> <li> <p>Inline, using the <code>data</code> property in the request body.</p> </li> <li> <p>A URL that points to a YAML document file stored in Amazon S3, using the <code>uri</code> property in the request body.</p> </li> </ul>

        Args:
            name: <p>The name of the component.</p>
            semantic_version: <p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>Describes the contents of the component.</p>
            change_description: <p>The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.</p>
            platform: <p>The operating system platform of the component.</p>
            supported_os_versions: <p>The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.</p>
            data: <p>Component <code>data</code> contains inline YAML document content for the component. Alternatively, you can specify the <code>uri</code> of a YAML document file stored in Amazon S3. However, you cannot specify both properties.</p>
            uri: <p>The <code>uri</code> of a YAML component document file. This must be an S3 URL (<code>s3://bucket/key</code>), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.</p> <p>Alternatively, you can specify the YAML document inline, using the component <code>data</code> property. You cannot specify both properties.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>
            tags: <p>The tags that apply to the component.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions for the operation and the request parameters, without actually making the request, and provides an error response. Upon a successful request, the error response is <code>DryRunOperationException</code>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_component_request.CreateComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_component

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_component.create_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_component_request.CreateComponentRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["semantic_version"] = semantic_version
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        input_["platform"] = platform
        if supported_os_versions is not None:
            input_["supported_os_versions"] = supported_os_versions
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_container_recipe(
        self,
        container_type: "aws_sdk_imagebuilder.types.container_type.ContainerType",
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.wildcard_version_number.WildcardVersionNumber",
        parent_image: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        target_repository: "aws_sdk_imagebuilder.types.target_container_repository.TargetContainerRepository",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        components: Optional[
            "aws_sdk_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
        ] = None,
        instance_configuration: Optional[
            "aws_sdk_imagebuilder.types.instance_configuration.InstanceConfiguration"
        ] = None,
        dockerfile_template_data: Optional[
            "aws_sdk_imagebuilder.types.inline_docker_file_template.InlineDockerFileTemplate"
        ] = None,
        dockerfile_template_uri: Optional["aws_sdk_imagebuilder.types.uri.Uri"] = None,
        platform_override: Optional[
            "aws_sdk_imagebuilder.types.platform.Platform"
        ] = None,
        image_os_version_override: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        working_directory: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        kms_key_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.create_container_recipe_response.CreateContainerRecipeResponse":
        r"""<p>Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.</p>

        Args:
            container_type: <p>The type of container to create.</p>
            name: <p>The name of the container recipe.</p>
            description: <p>The description of the container recipe.</p>
            semantic_version: <p>The semantic version of the container recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            components: <p>The components included in the container recipe.</p>
            instance_configuration: <p>A group of options that can be used to configure an instance for building and testing container images.</p>
            dockerfile_template_data: <p>The Dockerfile template used to build your image as an inline data blob.</p>
            dockerfile_template_uri: <p>The Amazon S3 URI for the Dockerfile that will be used to build your container image.</p>
            platform_override: <p>Specifies the operating system platform when you use a custom base image.</p>
            image_os_version_override: <p>Specifies the operating system version for the base image.</p>
            parent_image: <p>The base image for the container recipe.</p>
            tags: <p>Tags that are attached to the container recipe.</p>
            working_directory: <p>The working directory for use during build and test workflows.</p>
            target_repository: <p>The destination repository for the container image.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the Dockerfile template. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_container_recipe_request.CreateContainerRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_container_recipe_response.CreateContainerRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_container_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_container_recipe.create_container_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_container_recipe_request.CreateContainerRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["container_type"] = container_type
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["semantic_version"] = semantic_version
        if components is not None:
            input_["components"] = components
        if instance_configuration is not None:
            input_["instance_configuration"] = instance_configuration
        if dockerfile_template_data is not None:
            input_["dockerfile_template_data"] = dockerfile_template_data
        if dockerfile_template_uri is not None:
            input_["dockerfile_template_uri"] = dockerfile_template_uri
        if platform_override is not None:
            input_["platform_override"] = platform_override
        if image_os_version_override is not None:
            input_["image_os_version_override"] = image_os_version_override
        input_["parent_image"] = parent_image
        if tags is not None:
            input_["tags"] = tags
        if working_directory is not None:
            input_["working_directory"] = working_directory
        input_["target_repository"] = target_repository
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_distribution_configuration(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        distributions: "aws_sdk_imagebuilder.types.distribution_list.DistributionList",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_distribution_configuration_response.CreateDistributionConfigurationResponse":
        r"""<p>Creates a new distribution configuration. Distribution configurations define and configure the outputs of your pipeline.</p>

        Args:
            name: <p>The name of the distribution configuration.</p>
            description: <p>The description of the distribution configuration.</p>
            distributions: <p>The distributions of the distribution configuration.</p>
            tags: <p>The tags of the distribution configuration.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_distribution_configuration_request.CreateDistributionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_distribution_configuration_response.CreateDistributionConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_distribution_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_distribution_configuration.create_distribution_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_distribution_configuration_request.CreateDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["distributions"] = distributions
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_image(
        self,
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        image_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        image_scanning_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "aws_sdk_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        execution_role: Optional[
            "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.create_image_response.CreateImageResponse":
        r"""<p>Creates a new image. This request will create a new image along with all of the configured output resources defined in the distribution configuration. You must specify exactly one recipe for your image, using either a ContainerRecipeArn or an ImageRecipeArn.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.</p>
            image_tests_configuration: <p>The image tests configuration of the image.</p>
            enhanced_image_metadata_enabled: <p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>
            tags: <p>The tags of the image.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Contains settings for vulnerability scans.</p>
            workflows: <p>Contains an array of workflow configuration objects.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>
            logging_configuration: <p>Define logging configuration for the image build process.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_image_request.CreateImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_image_response.CreateImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_image.create_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_image_request.CreateImageRequest = {}  # type: ignore[typeddict-item]
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_image_pipeline(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        image_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        schedule: Optional["aws_sdk_imagebuilder.types.schedule.Schedule"] = None,
        status: Optional[
            "aws_sdk_imagebuilder.types.pipeline_status.PipelineStatus"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        image_tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        image_scanning_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "aws_sdk_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        execution_role: Optional[
            "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.create_image_pipeline_response.CreateImagePipelineResponse":
        r"""<p>Creates a new image pipeline. Image pipelines enable you to automate the creation and distribution of images.</p>

        Args:
            name: <p>The name of the image pipeline.</p>
            description: <p>The description of the image pipeline.</p>
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that will be used to configure images created by this image pipeline.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images created by this image pipeline.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that will be used to configure and distribute images created by this image pipeline.</p>
            image_tests_configuration: <p>The image test configuration of the image pipeline.</p>
            enhanced_image_metadata_enabled: <p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>
            schedule: <p>The schedule of the image pipeline.</p>
            status: <p>The status of the image pipeline.</p>
            tags: <p>The tags of the image pipeline.</p>
            image_tags: <p>The tags to be applied to the images produced by this pipeline.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Contains settings for vulnerability scans.</p>
            workflows: <p>Contains an array of workflow configuration objects.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>
            logging_configuration: <p>Define logging configuration for the image build process.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_image_pipeline_request.CreateImagePipelineRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_image_pipeline_response.CreateImagePipelineResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_image_pipeline

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_image_pipeline.create_image_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_image_pipeline_request.CreateImagePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if schedule is not None:
            input_["schedule"] = schedule
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if image_tags is not None:
            input_["image_tags"] = image_tags
        input_["client_token"] = client_token
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_image_recipe(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.wildcard_version_number.WildcardVersionNumber",
        parent_image: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        components: Optional[
            "aws_sdk_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
        ] = None,
        block_device_mappings: Optional[
            "aws_sdk_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        working_directory: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        additional_instance_configuration: Optional[
            "aws_sdk_imagebuilder.types.additional_instance_configuration.AdditionalInstanceConfiguration"
        ] = None,
        ami_tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_image_recipe_response.CreateImageRecipeResponse":
        r"""<p>Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.</p>

        Args:
            name: <p>The name of the image recipe.</p>
            description: <p>The description of the image recipe.</p>
            semantic_version: <p>The semantic version of the image recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            components: <p>The components included in the image recipe.</p>
            parent_image: <p>The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:</p> <ul> <li> <p>AMI ID</p> </li> <li> <p>Image Builder image Amazon Resource Name (ARN)</p> </li> <li> <p>Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>Amazon Web Services Marketplace product ID</p> </li> </ul> <p>If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI, and the AMI must be in the source Region.</p>
            block_device_mappings: <p>The block device mappings of the image recipe.</p>
            tags: <p>The tags of the image recipe.</p>
            working_directory: <p>The working directory used during build and test workflows.</p>
            additional_instance_configuration: <p>Specify additional settings and launch scripts for your build instances.</p>
            ami_tags: <p>Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_image_recipe_request.CreateImageRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_image_recipe_response.CreateImageRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_image_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_image_recipe.create_image_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_image_recipe_request.CreateImageRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["semantic_version"] = semantic_version
        if components is not None:
            input_["components"] = components
        input_["parent_image"] = parent_image
        if block_device_mappings is not None:
            input_["block_device_mappings"] = block_device_mappings
        if tags is not None:
            input_["tags"] = tags
        if working_directory is not None:
            input_["working_directory"] = working_directory
        if additional_instance_configuration is not None:
            input_["additional_instance_configuration"] = (
                additional_instance_configuration
            )
        if ami_tags is not None:
            input_["ami_tags"] = ami_tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_infrastructure_configuration(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        instance_profile_name: "aws_sdk_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        instance_types: Optional[
            "aws_sdk_imagebuilder.types.instance_type_list.InstanceTypeList"
        ] = None,
        security_group_ids: Optional[
            "aws_sdk_imagebuilder.types.security_group_ids.SecurityGroupIds"
        ] = None,
        subnet_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        logging: Optional["aws_sdk_imagebuilder.types.logging.Logging"] = None,
        key_pair: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        terminate_instance_on_failure: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        sns_topic_arn: Optional[
            "aws_sdk_imagebuilder.types.sns_topic_arn.SnsTopicArn"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_imagebuilder.types.resource_tag_map.ResourceTagMap"
        ] = None,
        instance_metadata_options: Optional[
            "aws_sdk_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        placement: Optional["aws_sdk_imagebuilder.types.placement.Placement"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_infrastructure_configuration_response.CreateInfrastructureConfigurationResponse":
        r"""<p>Creates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.</p>

        Args:
            name: <p>The name of the infrastructure configuration.</p>
            description: <p>The description of the infrastructure configuration.</p>
            instance_types: <p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.</p>
            instance_profile_name: <p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI.</p>
            security_group_ids: <p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>
            subnet_id: <p>The subnet ID in which to place the instance used to customize your Amazon EC2 AMI.</p>
            logging: <p>The logging configuration of the infrastructure configuration.</p>
            key_pair: <p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>
            terminate_instance_on_failure: <p>The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.</p> <note> <p>EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.</p> </note>
            resource_tags: <p>The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs.</p>
            instance_metadata_options: <p>The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances.</p>
            tags: <p>The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.</p>
            placement: <p>The instance placement settings that define where the instances that are launched from your image will run.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_infrastructure_configuration_request.CreateInfrastructureConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_infrastructure_configuration_response.CreateInfrastructureConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_infrastructure_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_infrastructure_configuration.create_infrastructure_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_infrastructure_configuration_request.CreateInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if instance_types is not None:
            input_["instance_types"] = instance_types
        input_["instance_profile_name"] = instance_profile_name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if logging is not None:
            input_["logging"] = logging
        if key_pair is not None:
            input_["key_pair"] = key_pair
        if terminate_instance_on_failure is not None:
            input_["terminate_instance_on_failure"] = terminate_instance_on_failure
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if instance_metadata_options is not None:
            input_["instance_metadata_options"] = instance_metadata_options
        if tags is not None:
            input_["tags"] = tags
        if placement is not None:
            input_["placement"] = placement
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_lifecycle_policy(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        execution_role: "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        resource_type: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType",
        policy_details: "aws_sdk_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails",
        resource_selection: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        status: Optional[
            "aws_sdk_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse":
        r"""<p>Create a lifecycle policy resource.</p>

        Args:
            name: <p>The name of the lifecycle policy to create.</p>
            description: <p>Optional description for the lifecycle policy.</p>
            status: <p>Indicates whether the lifecycle policy resource is enabled.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.</p>
            resource_type: <p>The type of Image Builder resource that the lifecycle policy applies to.</p>
            policy_details: <p>Configuration details for the lifecycle policy rules.</p>
            resource_selection: <p>Selection criteria for the resources that the lifecycle policy applies to. </p>
            tags: <p>Tags to apply to the lifecycle policy resource.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_lifecycle_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_lifecycle_policy.create_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        input_["execution_role"] = execution_role
        input_["resource_type"] = resource_type
        input_["policy_details"] = policy_details
        input_["resource_selection"] = resource_selection
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_workflow(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        type: "aws_sdk_imagebuilder.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        data: Optional[
            "aws_sdk_imagebuilder.types.inline_workflow_data.InlineWorkflowData"
        ] = None,
        uri: Optional["aws_sdk_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_imagebuilder.types.create_workflow_response.CreateWorkflowResponse":
        r"""<p>Create a new workflow or a new version of an existing workflow.</p>

        Args:
            name: <p>The name of the workflow to create.</p>
            semantic_version: <p>The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>Describes the workflow.</p>
            change_description: <p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>
            data: <p>Contains the UTF-8 encoded YAML document content for the workflow. Alternatively, you can specify the <code>uri</code> of a YAML document file stored in Amazon S3. However, you cannot specify both properties.</p>
            uri: <p>The <code>uri</code> of a YAML component document file. This must be an S3 URL (<code>s3://bucket/key</code>), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.</p> <p>Alternatively, you can specify the YAML document inline, using the component <code>data</code> property. You cannot specify both properties.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>
            tags: <p>Tags that apply to the workflow resource.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            type: <p>The phase in the image build process for which the workflow resource is responsible.</p>
            dry_run: <p>Validates the required permissions for the operation and the request parameters, without actually making the request, and provides an error response. Upon a successful request, the error response is <code>DryRunOperationException</code>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.create_workflow

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.create_workflow_request.CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["semantic_version"] = semantic_version
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token
        input_["type"] = type
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_component(
        self,
        component_build_version_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_component_response.DeleteComponentResponse":
        """<p>Deletes a component build version.</p>

        Args:
            component_build_version_arn: <p>The Amazon Resource Name (ARN) of the component build version to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_component_response.DeleteComponentResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_component

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_component.delete_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_component_request.DeleteComponentRequest = {}  # type: ignore[typeddict-item]
        input_["component_build_version_arn"] = component_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_container_recipe(
        self,
        container_recipe_arn: "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_container_recipe_response.DeleteContainerRecipeResponse":
        """<p>Deletes a container recipe.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_container_recipe_request.DeleteContainerRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_container_recipe_response.DeleteContainerRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_container_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_container_recipe.delete_container_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_container_recipe_request.DeleteContainerRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["container_recipe_arn"] = container_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_distribution_configuration(
        self,
        distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_distribution_configuration_response.DeleteDistributionConfigurationResponse":
        """<p>Deletes a distribution configuration.</p>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_distribution_configuration_request.DeleteDistributionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_distribution_configuration_response.DeleteDistributionConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_distribution_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_distribution_configuration.delete_distribution_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_distribution_configuration_request.DeleteDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_configuration_arn"] = distribution_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_image_response.DeleteImageResponse":
        r"""<p>Deletes an Image Builder image resource. This does not delete any EC2 AMIs or ECR container images that are created during the image build process. You must clean those up separately, using the appropriate Amazon EC2 or Amazon ECR console actions, or API or CLI commands.</p> <ul> <li> <p>To deregister an EC2 Linux AMI, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html\">Deregister your Linux AMI</a> in the <i> <i>Amazon EC2 User Guide</i> </i>.</p> </li> <li> <p>To deregister an EC2 Windows AMI, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/deregister-ami.html\">Deregister your Windows AMI</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i>.</p> </li> <li> <p>To delete a container image from Amazon ECR, see <a href=\"https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html\">Deleting an image</a> in the <i>Amazon ECR User Guide</i>.</p> </li> </ul>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the Image Builder image resource to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_image_request.DeleteImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_image_response.DeleteImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_image.delete_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_image_request.DeleteImageRequest = {}  # type: ignore[typeddict-item]
        input_["image_build_version_arn"] = image_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image_pipeline(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_image_pipeline_response.DeleteImagePipelineResponse":
        """<p>Deletes an image pipeline.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_image_pipeline_request.DeleteImagePipelineRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_image_pipeline_response.DeleteImagePipelineResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_image_pipeline

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_image_pipeline.delete_image_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_image_pipeline_request.DeleteImagePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["image_pipeline_arn"] = image_pipeline_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image_recipe(
        self,
        image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_image_recipe_response.DeleteImageRecipeResponse":
        """<p>Deletes an image recipe.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_image_recipe_request.DeleteImageRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_image_recipe_response.DeleteImageRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_image_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_image_recipe.delete_image_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_image_recipe_request.DeleteImageRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["image_recipe_arn"] = image_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_infrastructure_configuration_response.DeleteInfrastructureConfigurationResponse":
        """<p>Deletes an infrastructure configuration.</p>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_infrastructure_configuration_request.DeleteInfrastructureConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_infrastructure_configuration_response.DeleteInfrastructureConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_infrastructure_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_infrastructure_configuration.delete_infrastructure_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_infrastructure_configuration_request.DeleteInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_lifecycle_policy(
        self,
        lifecycle_policy_arn: "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse":
        """<p>Delete the specified lifecycle policy resource.</p>

        Args:
            lifecycle_policy_arn: <p>The Amazon Resource Name (ARN) of the lifecycle policy resource to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_lifecycle_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_lifecycle_policy.delete_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_policy_arn"] = lifecycle_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_workflow(
        self,
        workflow_build_version_arn: "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a specific workflow resource.</p>

        Args:
            workflow_build_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource to delete.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.delete_workflow

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.delete_workflow_request.DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_build_version_arn"] = workflow_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def distribute_image(
        self,
        source_image: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        execution_role: "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.distribute_image_response.DistributeImageResponse":
        r"""<p>DistributeImage distributes existing AMIs to additional regions and accounts without rebuilding the image.</p>

        Args:
            source_image: <p>The source image Amazon Resource Name (ARN) to distribute.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration to use.</p>
            execution_role: <p>The IAM role to use for the distribution.</p>
            tags: <p>The tags to apply to the distributed image.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            logging_configuration: <p>The logging configuration for the distribution.</p>

        Raises:
            aws_sdk_imagebuilder.errors.access_denied_exception.AccessDeniedException: <p>You do not have permissions to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder\">EC2 Image Builder endpoints and quotas</a>.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.too_many_requests_exception.TooManyRequestsException: <p>You have attempted too many requests for the specific operation.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.distribute_image_request.DistributeImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.distribute_image_response.DistributeImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.distribute_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.distribute_image.distribute_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.distribute_image_request.DistributeImageRequest = {}  # type: ignore[typeddict-item]
        input_["source_image"] = source_image
        input_["distribution_configuration_arn"] = distribution_configuration_arn
        input_["execution_role"] = execution_role
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_component(
        self,
        component_build_version_arn: "aws_sdk_imagebuilder.types.component_version_arn_or_build_version_arn.ComponentVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_component_response.GetComponentResponse":
        r"""<p>Gets a component object.</p>

        Args:
            component_build_version_arn: <p>The Amazon Resource Name (ARN) of the component that you want to get. Regex requires the suffix <code>/\d+$</code>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_component_request.GetComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_component_response.GetComponentResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_component

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_component.get_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_component_request.GetComponentRequest = {}  # type: ignore[typeddict-item]
        input_["component_build_version_arn"] = component_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_component_policy(
        self,
        component_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_component_policy_response.GetComponentPolicyResponse":
        """<p>Gets a component policy.</p>

        Args:
            component_arn: <p>The Amazon Resource Name (ARN) of the component whose policy you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_component_policy_request.GetComponentPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_component_policy_response.GetComponentPolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_component_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_component_policy.get_component_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_component_policy_request.GetComponentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["component_arn"] = component_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_container_recipe(
        self,
        container_recipe_arn: "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_container_recipe_response.GetContainerRecipeResponse":
        """<p>Retrieves a container recipe.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_container_recipe_request.GetContainerRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_container_recipe_response.GetContainerRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_container_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_container_recipe.get_container_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_container_recipe_request.GetContainerRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["container_recipe_arn"] = container_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_container_recipe_policy(
        self,
        container_recipe_arn: "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_container_recipe_policy_response.GetContainerRecipePolicyResponse":
        """<p>Retrieves the policy for a container recipe.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe for the policy being requested.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_container_recipe_policy_request.GetContainerRecipePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_container_recipe_policy_response.GetContainerRecipePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_container_recipe_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_container_recipe_policy.get_container_recipe_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_container_recipe_policy_request.GetContainerRecipePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["container_recipe_arn"] = container_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_distribution_configuration(
        self,
        distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_distribution_configuration_response.GetDistributionConfigurationResponse":
        """<p>Gets a distribution configuration.</p>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_distribution_configuration_request.GetDistributionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_distribution_configuration_response.GetDistributionConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_distribution_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_distribution_configuration.get_distribution_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_distribution_configuration_request.GetDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_configuration_arn"] = distribution_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_image(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_version_arn_or_build_version_arn.ImageVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_image_response.GetImageResponse":
        """<p>Gets an image.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image that you want to get.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_image_request.GetImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_image_response.GetImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_image.get_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_image_request.GetImageRequest = {}  # type: ignore[typeddict-item]
        input_["image_build_version_arn"] = image_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_image_pipeline(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_image_pipeline_response.GetImagePipelineResponse":
        """<p>Gets an image pipeline.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_image_pipeline_request.GetImagePipelineRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_image_pipeline_response.GetImagePipelineResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_image_pipeline

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_image_pipeline.get_image_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_image_pipeline_request.GetImagePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["image_pipeline_arn"] = image_pipeline_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_image_policy(
        self,
        image_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_image_policy_response.GetImagePolicyResponse":
        """<p>Gets an image policy.</p>

        Args:
            image_arn: <p>The Amazon Resource Name (ARN) of the image whose policy you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_image_policy_request.GetImagePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_image_policy_response.GetImagePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_image_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_image_policy.get_image_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_image_policy_request.GetImagePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["image_arn"] = image_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_image_recipe(
        self,
        image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_image_recipe_response.GetImageRecipeResponse":
        """<p>Gets an image recipe.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_image_recipe_request.GetImageRecipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_image_recipe_response.GetImageRecipeResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_image_recipe

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_image_recipe.get_image_recipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_image_recipe_request.GetImageRecipeRequest = {}  # type: ignore[typeddict-item]
        input_["image_recipe_arn"] = image_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_image_recipe_policy(
        self,
        image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_image_recipe_policy_response.GetImageRecipePolicyResponse":
        """<p>Gets an image recipe policy.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe whose policy you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_image_recipe_policy_request.GetImageRecipePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_image_recipe_policy_response.GetImageRecipePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_image_recipe_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_image_recipe_policy.get_image_recipe_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_image_recipe_policy_request.GetImageRecipePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["image_recipe_arn"] = image_recipe_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_infrastructure_configuration_response.GetInfrastructureConfigurationResponse":
        """<p>Gets an infrastructure configuration.</p>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_infrastructure_configuration_request.GetInfrastructureConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_infrastructure_configuration_response.GetInfrastructureConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_infrastructure_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_infrastructure_configuration.get_infrastructure_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_infrastructure_configuration_request.GetInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lifecycle_execution(
        self,
        lifecycle_execution_id: "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_lifecycle_execution_response.GetLifecycleExecutionResponse":
        """<p>Get the runtime information that was logged for a specific runtime instance of the lifecycle policy.</p>

        Args:
            lifecycle_execution_id: <p>Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_lifecycle_execution_request.GetLifecycleExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_lifecycle_execution_response.GetLifecycleExecutionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_lifecycle_execution

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_lifecycle_execution.get_lifecycle_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_lifecycle_execution_request.GetLifecycleExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_execution_id"] = lifecycle_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lifecycle_policy(
        self,
        lifecycle_policy_arn: "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse":
        """<p>Get details for the specified image lifecycle policy.</p>

        Args:
            lifecycle_policy_arn: <p>Specifies the Amazon Resource Name (ARN) of the image lifecycle policy resource to get.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_lifecycle_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_lifecycle_policy.get_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_policy_arn"] = lifecycle_policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_marketplace_resource(
        self,
        resource_type: "aws_sdk_imagebuilder.types.marketplace_resource_type.MarketplaceResourceType",
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        resource_location: Optional[
            "aws_sdk_imagebuilder.types.marketplace_resource_location.MarketplaceResourceLocation"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.get_marketplace_resource_response.GetMarketplaceResourceResponse":
        """<p>Verify the subscription and perform resource dependency checks on the requested Amazon Web Services Marketplace resource. For Amazon Web Services Marketplace components, the response contains fields to download the components and their artifacts.</p>

        Args:
            resource_type: <p>Specifies which type of Amazon Web Services Marketplace resource Image Builder retrieves.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an Amazon Web Services Marketplace resource.</p>
            resource_location: <p>The bucket path that you can specify to download the resource from Amazon S3.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_marketplace_resource_request.GetMarketplaceResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_marketplace_resource_response.GetMarketplaceResourceResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_marketplace_resource

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_marketplace_resource.get_marketplace_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_marketplace_resource_request.GetMarketplaceResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_type"] = resource_type
        input_["resource_arn"] = resource_arn
        if resource_location is not None:
            input_["resource_location"] = resource_location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_workflow(
        self,
        workflow_build_version_arn: "aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn.WorkflowVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_workflow_response.GetWorkflowResponse":
        """<p>Get a workflow resource object.</p>

        Args:
            workflow_build_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource that you want to get.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_workflow

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_workflow_request.GetWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_build_version_arn"] = workflow_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_workflow_execution(
        self,
        workflow_execution_id: "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse":
        """<p>Get the runtime information that was logged for a specific runtime instance of the workflow.</p>

        Args:
            workflow_execution_id: <p>Use the unique identifier for a runtime instance of the workflow to get runtime details.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_workflow_execution

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_workflow_execution.get_workflow_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_execution_id"] = workflow_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_workflow_step_execution(
        self,
        step_execution_id: "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.get_workflow_step_execution_response.GetWorkflowStepExecutionResponse":
        """<p>Get the runtime information that was logged for a specific runtime instance of the workflow step.</p>

        Args:
            step_execution_id: <p>Use the unique identifier for a specific runtime instance of the workflow step to get runtime details for that step.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.get_workflow_step_execution_request.GetWorkflowStepExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.get_workflow_step_execution_response.GetWorkflowStepExecutionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.get_workflow_step_execution

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.get_workflow_step_execution.get_workflow_step_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.get_workflow_step_execution_request.GetWorkflowStepExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["step_execution_id"] = step_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_component(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber",
        type: "aws_sdk_imagebuilder.types.component_type.ComponentType",
        format: "aws_sdk_imagebuilder.types.component_format.ComponentFormat",
        platform: "aws_sdk_imagebuilder.types.platform.Platform",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        data: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        uri: Optional["aws_sdk_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.import_component_response.ImportComponentResponse":
        r"""<p>Imports a component and transforms its data into a component document.</p>

        Args:
            name: <p>The name of the component.</p>
            semantic_version: <p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>
            description: <p>The description of the component. Describes the contents of the component.</p>
            change_description: <p>The change description of the component. This description indicates the change that has been made in this version, or what makes this version different from other versions of the component.</p>
            type: <p>The type of the component denotes whether the component is used to build the image, or only to test it.</p>
            format: <p>The format of the resource that you want to import as a component.</p>
            platform: <p>The platform of the component.</p>
            data: <p>The data of the component. Used to specify the data inline. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>
            uri: <p>The uri of the component. Must be an Amazon S3 URL and the requester must have permission to access the Amazon S3 bucket. If you use Amazon S3, you can specify component content up to your service quota. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>
            tags: <p>The tags of the component.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.import_component_request.ImportComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.import_component_response.ImportComponentResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.import_component

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.import_component.import_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.import_component_request.ImportComponentRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["semantic_version"] = semantic_version
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        input_["type"] = type
        input_["format"] = format
        input_["platform"] = platform
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_disk_image(
        self,
        name: "aws_sdk_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber",
        platform: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        os_version: "aws_sdk_imagebuilder.types.os_version.OsVersion",
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        uri: "aws_sdk_imagebuilder.types.uri.Uri",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        execution_role: Optional[
            "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
        register_image_options: Optional[
            "aws_sdk_imagebuilder.types.register_image_options.RegisterImageOptions"
        ] = None,
        windows_configuration: Optional[
            "aws_sdk_imagebuilder.types.windows_configuration.WindowsConfiguration"
        ] = None,
    ) -> (
        "aws_sdk_imagebuilder.types.import_disk_image_response.ImportDiskImageResponse"
    ):
        r"""<p>Import a Windows operating system image from a verified Microsoft ISO disk file. The following disk images are supported:</p> <ul> <li> <p>Windows 11 Enterprise</p> </li> </ul>

        Args:
            name: <p>The name of the image resource that's created from the import.</p>
            semantic_version: <p>The semantic version to attach to the image that's created during the import process. This version follows the semantic version syntax.</p>
            description: <p>The description for your disk image import.</p>
            platform: <p>The operating system platform for the imported image. Allowed values include the following: <code>Windows</code>.</p>
            os_version: <p>The operating system version for the imported image. Allowed values include the following: <code>Microsoft Windows 11</code>.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions to import an image from a Microsoft ISO file.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration resource that's used for launching the EC2 instance on which the ISO image is built.</p>
            uri: <p>The <code>uri</code> of the ISO disk file that's stored in Amazon S3.</p>
            logging_configuration: <p>Define logging configuration for the image build process.</p>
            tags: <p>Tags that are attached to image resources created from the import.</p>
            register_image_options: <p>Configures Secure Boot and UEFI settings for the imported image.</p>
            windows_configuration: <p>Specifies Windows settings for ISO imports.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.access_denied_exception.AccessDeniedException: <p>You do not have permissions to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.too_many_requests_exception.TooManyRequestsException: <p>You have attempted too many requests for the specific operation.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.import_disk_image_request.ImportDiskImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.import_disk_image_response.ImportDiskImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.import_disk_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.import_disk_image.import_disk_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.import_disk_image_request.ImportDiskImageRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["semantic_version"] = semantic_version
        if description is not None:
            input_["description"] = description
        input_["platform"] = platform
        input_["os_version"] = os_version
        if execution_role is not None:
            input_["execution_role"] = execution_role
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn
        input_["uri"] = uri
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tags is not None:
            input_["tags"] = tags
        if register_image_options is not None:
            input_["register_image_options"] = register_image_options
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_vm_image(
        self,
        name: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber",
        platform: "aws_sdk_imagebuilder.types.platform.Platform",
        vm_import_task_id: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        os_version: Optional["aws_sdk_imagebuilder.types.os_version.OsVersion"] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.import_vm_image_response.ImportVmImageResponse":
        r"""<p>When you export your virtual machine (VM) from its virtualization environment, that process creates a set of one or more disk container files that act as snapshots of your VM’s environment, settings, and data. The Amazon EC2 API <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html\">ImportImage</a> action uses those files to import your VM and create an AMI. To import using the CLI command, see <a href=\"https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html\">import-image</a> </p> <p>You can reference the task ID from the VM import to pull in the AMI that the import created as the base image for your Image Builder recipe.</p>

        Args:
            name: <p>The name of the base image that is created by the import process.</p>
            semantic_version: <p>The semantic version to attach to the base image that was created during the import process. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>The description for the base image that is created by the import process.</p>
            platform: <p>The operating system platform for the imported VM.</p>
            os_version: <p>The operating system version for the imported VM.</p>
            vm_import_task_id: <p>The <code>importTaskId</code> (API) or <code>ImportTaskId</code> (CLI) from the Amazon EC2 VM import process. Image Builder retrieves information from the import process to pull in the AMI that is created from the VM source as the base image for your recipe.</p>
            logging_configuration: <p>Define logging configuration for the image build process.</p>
            tags: <p>Tags that are attached to the import resources.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.import_vm_image_request.ImportVmImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.import_vm_image_response.ImportVmImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.import_vm_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.import_vm_image.import_vm_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.import_vm_image_request.ImportVmImageRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["semantic_version"] = semantic_version
        if description is not None:
            input_["description"] = description
        input_["platform"] = platform
        if os_version is not None:
            input_["os_version"] = os_version
        input_["vm_import_task_id"] = vm_import_task_id
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_component_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        component_version_arn: Optional[
            "aws_sdk_imagebuilder.types.component_version_arn.ComponentVersionArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_component_build_versions_response.ListComponentBuildVersionsResponse":
        """<p>Returns the list of component build versions for the specified component version Amazon Resource Name (ARN).</p>

        Args:
            component_version_arn: <p>The component version Amazon Resource Name (ARN) whose versions you want to list.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_component_build_versions_request.ListComponentBuildVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_component_build_versions_response.ListComponentBuildVersionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_component_build_versions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_component_build_versions.list_component_build_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_component_build_versions_request.ListComponentBuildVersionsRequest = {}  # type: ignore[typeddict-item]
        if component_version_arn is not None:
            input_["component_version_arn"] = component_version_arn
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

    def iter_list_component_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        component_version_arn: Optional[
            "aws_sdk_imagebuilder.types.component_version_arn.ComponentVersionArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.component_summary.ComponentSummary]":
        _token = next_token
        while True:
            _response = self.list_component_build_versions(
                config_overrides=config_overrides,
                component_version_arn=component_version_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("component_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_components(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_components_response.ListComponentsResponse":
        """<p>Returns the list of components that can be filtered by name, or by using the listed <code>filters</code> to streamline results. Newly created components can take up to two minutes to appear in the ListComponents API Results.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>

        Args:
            owner: <p>Filters results based on the type of owner for the component. By default, this request returns a list of components that your account owns. To see results for other types of owners, you can specify components that Amazon manages, third party components, or components that other accounts have shared with you.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>description</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>supportedOsVersion</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            by_name: <p>Returns the list of components for the specified name.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_components_request.ListComponentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_components

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_components_request.ListComponentsRequest = {}  # type: ignore[typeddict-item]
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
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

    def iter_list_components(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.component_version.ComponentVersion]":
        _token = next_token
        while True:
            _response = self.list_components(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("component_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_container_recipes(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_container_recipes_response.ListContainerRecipesResponse":
        """<p>Returns a list of container recipes.</p>

        Args:
            owner: <p>Returns container recipes belonging to the specified owner, that have been shared with you. You can omit this field to return container recipes belonging to your account.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>containerType</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_container_recipes_request.ListContainerRecipesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_container_recipes_response.ListContainerRecipesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_container_recipes

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_container_recipes.list_container_recipes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_container_recipes_request.ListContainerRecipesRequest = {}  # type: ignore[typeddict-item]
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_container_recipes(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.container_recipe_summary.ContainerRecipeSummary]":
        _token = next_token
        while True:
            _response = self.list_container_recipes(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_recipe_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_distribution_configurations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_distribution_configurations_response.ListDistributionConfigurationsResponse":
        """<p>Returns a list of distribution configurations.</p>

        Args:
            filters: <p>You can filter on <code>name</code> to streamline results.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_distribution_configurations_request.ListDistributionConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_distribution_configurations_response.ListDistributionConfigurationsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_distribution_configurations

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_distribution_configurations.list_distribution_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_distribution_configurations_request.ListDistributionConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_distribution_configurations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.distribution_configuration_summary.DistributionConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_distribution_configurations(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("distribution_configuration_summary_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        image_version_arn: Optional[
            "aws_sdk_imagebuilder.types.image_version_arn.ImageVersionArn"
        ] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_build_versions_response.ListImageBuildVersionsResponse":
        """<p>Returns a list of image build versions.</p>

        Args:
            image_version_arn: <p>The Amazon Resource Name (ARN) of the image whose build versions you want to retrieve.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_build_versions_request.ListImageBuildVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_build_versions_response.ListImageBuildVersionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_build_versions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_build_versions.list_image_build_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_build_versions_request.ListImageBuildVersionsRequest = {}  # type: ignore[typeddict-item]
        if image_version_arn is not None:
            input_["image_version_arn"] = image_version_arn
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_image_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        image_version_arn: Optional[
            "aws_sdk_imagebuilder.types.image_version_arn.ImageVersionArn"
        ] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_summary.ImageSummary]":
        _token = next_token
        while True:
            _response = self.list_image_build_versions(
                config_overrides=config_overrides,
                image_version_arn=image_version_arn,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_packages(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_packages_response.ListImagePackagesResponse":
        """<p>List the Packages that are associated with an Image Build Version, as determined by Amazon Web Services Systems Manager Inventory at build time.</p>

        Args:
            image_build_version_arn: <p>Filter results for the ListImagePackages request by the Image Build Version ARN</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_packages_request.ListImagePackagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_packages_response.ListImagePackagesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_packages

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_packages.list_image_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_packages_request.ListImagePackagesRequest = {}  # type: ignore[typeddict-item]
        input_["image_build_version_arn"] = image_build_version_arn
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

    def iter_list_image_packages(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_package.ImagePackage]":
        _token = next_token
        while True:
            _response = self.list_image_packages(
                image_build_version_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_package_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_pipeline_images(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_pipeline_images_response.ListImagePipelineImagesResponse":
        """<p>Returns a list of images created by the specified pipeline.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline whose images you want to view.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_pipeline_images_request.ListImagePipelineImagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_pipeline_images_response.ListImagePipelineImagesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_pipeline_images

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_pipeline_images.list_image_pipeline_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_pipeline_images_request.ListImagePipelineImagesRequest = {}  # type: ignore[typeddict-item]
        input_["image_pipeline_arn"] = image_pipeline_arn
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_image_pipeline_images(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_summary.ImageSummary]":
        _token = next_token
        while True:
            _response = self.list_image_pipeline_images(
                image_pipeline_arn,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_pipelines(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_pipelines_response.ListImagePipelinesResponse":
        """<p>Returns a list of image pipelines.</p>

        Args:
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>description</code> </p> </li> <li> <p> <code>distributionConfigurationArn</code> </p> </li> <li> <p> <code>imageRecipeArn</code> </p> </li> <li> <p> <code>infrastructureConfigurationArn</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>status</code> </p> </li> </ul>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_pipelines_request.ListImagePipelinesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_pipelines_response.ListImagePipelinesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_pipelines

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_pipelines.list_image_pipelines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_pipelines_request.ListImagePipelinesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_image_pipelines(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_pipeline.ImagePipeline]":
        _token = next_token
        while True:
            _response = self.list_image_pipelines(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_pipeline_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_recipes(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_recipes_response.ListImageRecipesResponse":
        """<p>Returns a list of image recipes.</p>

        Args:
            owner: <p>You can specify the recipe owner to filter results by that owner. By default, this request will only show image recipes owned by your account. To filter by a different owner, specify one of the <code>Valid Values</code> that are listed for this parameter.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_recipes_request.ListImageRecipesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_recipes_response.ListImageRecipesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_recipes

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_recipes.list_image_recipes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_recipes_request.ListImageRecipesRequest = {}  # type: ignore[typeddict-item]
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_image_recipes(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_recipe_summary.ImageRecipeSummary]":
        _token = next_token
        while True:
            _response = self.list_image_recipes(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_recipe_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_images(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
        include_deprecated: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_images_response.ListImagesResponse":
        """<p>Returns the list of images that you have access to. Newly created images can take up to two minutes to appear in the ListImages API Results.</p>

        Args:
            owner: <p>The owner defines which images you want to list. By default, this request will only show images owned by your account. You can use this field to specify if you want to view images owned by yourself, by Amazon, or those images that have been shared with you by other customers.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            by_name: <p>Requests a list of images with a specific recipe name.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>
            include_deprecated: <p>Includes deprecated images in the response list.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_images_request.ListImagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_images_response.ListImagesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_images

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_images.list_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_images_request.ListImagesRequest = {}  # type: ignore[typeddict-item]
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_deprecated is not None:
            input_["include_deprecated"] = include_deprecated

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_images(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
        include_deprecated: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_version.ImageVersion]":
        _token = next_token
        while True:
            _response = self.list_images(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
                include_deprecated=include_deprecated,
            )
            _page = _resolve_path(_response, ("image_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_scan_finding_aggregations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filter: Optional["aws_sdk_imagebuilder.types.filter.Filter"] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_response.ListImageScanFindingAggregationsResponse":
        """<p>Returns a list of image scan aggregations for your account. You can filter by the type of key that Image Builder uses to group results. For example, if you want to get a list of findings by severity level for one of your pipelines, you might specify your pipeline with the <code>imagePipelineArn</code> filter. If you don't specify a filter, Image Builder returns an aggregation for your account.</p> <p>To streamline results, you can use the following filters in your request:</p> <ul> <li> <p> <code>accountId</code> </p> </li> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> </ul>

        Args:
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_request.ListImageScanFindingAggregationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_response.ListImageScanFindingAggregationsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_scan_finding_aggregations

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_scan_finding_aggregations.list_image_scan_finding_aggregations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_scan_finding_aggregations_request.ListImageScanFindingAggregationsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_image_scan_finding_aggregations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filter: Optional["aws_sdk_imagebuilder.types.filter.Filter"] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_scan_finding_aggregation.ImageScanFindingAggregation]":
        _token = next_token
        while True:
            _response = self.list_image_scan_finding_aggregations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("responses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_scan_findings(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional[
            "aws_sdk_imagebuilder.types.image_scan_findings_filter_list.ImageScanFindingsFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_image_scan_findings_response.ListImageScanFindingsResponse":
        """<p>Returns a list of image scan findings for your account.</p>

        Args:
            filters: <p>An array of name value pairs that you can use to filter your results. You can use the following filters to streamline results:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> <li> <p> <code>severity</code> </p> </li> </ul> <p>If you don't request a filter, then all findings in your account are listed.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_image_scan_findings_request.ListImageScanFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_image_scan_findings_response.ListImageScanFindingsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_image_scan_findings

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_image_scan_findings.list_image_scan_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_image_scan_findings_request.ListImageScanFindingsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_image_scan_findings(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional[
            "aws_sdk_imagebuilder.types.image_scan_findings_filter_list.ImageScanFindingsFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.image_scan_finding.ImageScanFinding]":
        _token = next_token
        while True:
            _response = self.list_image_scan_findings(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_infrastructure_configurations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_infrastructure_configurations_response.ListInfrastructureConfigurationsResponse":
        """<p>Returns a list of infrastructure configurations.</p>

        Args:
            filters: <p>You can filter on <code>name</code> to streamline results.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_infrastructure_configurations_request.ListInfrastructureConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_infrastructure_configurations_response.ListInfrastructureConfigurationsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_infrastructure_configurations

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_infrastructure_configurations.list_infrastructure_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_infrastructure_configurations_request.ListInfrastructureConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_infrastructure_configurations(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.infrastructure_configuration_summary.InfrastructureConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_infrastructure_configurations(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("infrastructure_configuration_summary_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lifecycle_execution_resources(
        self,
        lifecycle_execution_id: "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        parent_resource_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_response.ListLifecycleExecutionResourcesResponse":
        """<p>List resources that the runtime instance of the image lifecycle identified for lifecycle actions.</p>

        Args:
            lifecycle_execution_id: <p>Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.</p>
            parent_resource_id: <p>You can leave this empty to get a list of Image Builder resources that were identified for lifecycle actions.</p> <p>To get a list of associated resources that are impacted for an individual resource (the parent), specify its Amazon Resource Name (ARN). Associated resources are produced from your image and distributed when you run a build, such as AMIs or container images stored in ECR repositories.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_request.ListLifecycleExecutionResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_response.ListLifecycleExecutionResourcesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_execution_resources

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_execution_resources.list_lifecycle_execution_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_lifecycle_execution_resources_request.ListLifecycleExecutionResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_execution_id"] = lifecycle_execution_id
        if parent_resource_id is not None:
            input_["parent_resource_id"] = parent_resource_id
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

    def iter_list_lifecycle_execution_resources(
        self,
        lifecycle_execution_id: "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        parent_resource_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.lifecycle_execution_resource.LifecycleExecutionResource]":
        _token = next_token
        while True:
            _response = self.list_lifecycle_execution_resources(
                lifecycle_execution_id,
                config_overrides=config_overrides,
                parent_resource_id=parent_resource_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lifecycle_executions(
        self,
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_lifecycle_executions_response.ListLifecycleExecutionsResponse":
        """<p>Get the lifecycle runtime history for the specified resource.</p>

        Args:
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to get a list of lifecycle runtime instances.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_lifecycle_executions_request.ListLifecycleExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_lifecycle_executions_response.ListLifecycleExecutionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_executions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_executions.list_lifecycle_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_lifecycle_executions_request.ListLifecycleExecutionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_lifecycle_executions(
        self,
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.lifecycle_execution.LifecycleExecution]":
        _token = next_token
        while True:
            _response = self.list_lifecycle_executions(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lifecycle_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lifecycle_policies(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse":
        """<p>Get a list of lifecycle policies in your Amazon Web Services account.</p>

        Args:
            filters: <p>Streamline results based on one of the following values: <code>Name</code>, <code>Status</code>.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_policies

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_lifecycle_policies.list_lifecycle_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_lifecycle_policies(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.lifecycle_policy_summary.LifecyclePolicySummary]":
        _token = next_token
        while True:
            _response = self.list_lifecycle_policies(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lifecycle_policy_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the list of tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p>

        Raises:
            aws_sdk_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_tags_for_resource

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_waiting_workflow_steps(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_waiting_workflow_steps_response.ListWaitingWorkflowStepsResponse":
        """<p>Get a list of workflow steps that are waiting for action for workflows in your Amazon Web Services account.</p>

        Args:
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_waiting_workflow_steps_request.ListWaitingWorkflowStepsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_waiting_workflow_steps_response.ListWaitingWorkflowStepsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_waiting_workflow_steps

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_waiting_workflow_steps.list_waiting_workflow_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_waiting_workflow_steps_request.ListWaitingWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_waiting_workflow_steps(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.workflow_step_execution.WorkflowStepExecution]":
        _token = next_token
        while True:
            _response = self.list_waiting_workflow_steps(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflow_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        workflow_version_arn: Optional[
            "aws_sdk_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_workflow_build_versions_response.ListWorkflowBuildVersionsResponse":
        """<p>Returns a list of build versions for a specific workflow resource.</p>

        Args:
            workflow_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource for which to get a list of build versions.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_workflow_build_versions_request.ListWorkflowBuildVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_workflow_build_versions_response.ListWorkflowBuildVersionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_build_versions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_build_versions.list_workflow_build_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_workflow_build_versions_request.ListWorkflowBuildVersionsRequest = {}  # type: ignore[typeddict-item]
        if workflow_version_arn is not None:
            input_["workflow_version_arn"] = workflow_version_arn
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

    def iter_list_workflow_build_versions(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        workflow_version_arn: Optional[
            "aws_sdk_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.workflow_summary.WorkflowSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_build_versions(
                config_overrides=config_overrides,
                workflow_version_arn=workflow_version_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflow_executions(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_workflow_executions_response.ListWorkflowExecutionsResponse":
        """<p>Returns a list of workflow runtime instance metadata objects for a specific image build version.</p>

        Args:
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>
            image_build_version_arn: <p>List all workflow runtime instances for the specified image build version resource ARN.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_workflow_executions_request.ListWorkflowExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_workflow_executions_response.ListWorkflowExecutionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_executions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_executions.list_workflow_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_workflow_executions_request.ListWorkflowExecutionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["image_build_version_arn"] = image_build_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_workflow_executions(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.workflow_execution_metadata.WorkflowExecutionMetadata]":
        _token = next_token
        while True:
            _response = self.list_workflow_executions(
                image_build_version_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflows(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists workflow build versions based on filtering parameters.</p>

        Args:
            owner: <p>Used to get a list of workflow build version filtered by the identity of the creator.</p>
            filters: <p>Used to streamline search results.</p>
            by_name: <p>Specify all or part of the workflow name to streamline results.</p>
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_workflows

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_workflows_request.ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
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

    def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        owner: Optional["aws_sdk_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["aws_sdk_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["aws_sdk_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.workflow_version.WorkflowVersion]":
        _token = next_token
        while True:
            _response = self.list_workflows(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflow_step_executions(
        self,
        workflow_execution_id: "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.list_workflow_step_executions_response.ListWorkflowStepExecutionsResponse":
        """<p>Returns runtime data for each step in a runtime instance of the workflow that you specify in the request.</p>

        Args:
            max_results: <p>Specify the maximum number of items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>
            workflow_execution_id: <p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.list_workflow_step_executions_request.ListWorkflowStepExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.list_workflow_step_executions_response.ListWorkflowStepExecutionsResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_step_executions

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.list_workflow_step_executions.list_workflow_step_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.list_workflow_step_executions_request.ListWorkflowStepExecutionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_execution_id"] = workflow_execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_workflow_step_executions(
        self,
        workflow_execution_id: "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        max_results: Optional[
            "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_imagebuilder.types.workflow_step_metadata.WorkflowStepMetadata]":
        _token = next_token
        while True:
            _response = self.list_workflow_step_executions(
                workflow_execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_component_policy(
        self,
        component_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse":
        r"""<p>Applies a policy to a component. We recommend that you call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html\">CreateResourceShare</a> to share resources. If you call the Image Builder API <code>PutComponentPolicy</code>, you must also call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html\">PromoteResourceShareCreatedFromPolicy</a> in order for the resource to be visible to all principals with whom the resource is shared.</p>

        Args:
            component_arn: <p>The Amazon Resource Name (ARN) of the component that this policy should be applied to.</p>
            policy: <p>The policy to apply.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.put_component_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.put_component_policy.put_component_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["component_arn"] = component_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_container_recipe_policy(
        self,
        container_recipe_arn: "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.put_container_recipe_policy_response.PutContainerRecipePolicyResponse":
        """<p>Applies a policy to a container image. We recommend that you call the RAM API CreateResourceShare (https://docs.aws.amazon.com//ram/latest/APIReference/API_CreateResourceShare.html) to share resources. If you call the Image Builder API <code>PutContainerImagePolicy</code>, you must also call the RAM API PromoteResourceShareCreatedFromPolicy (https://docs.aws.amazon.com//ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) in order for the resource to be visible to all principals with whom the resource is shared.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that this policy should be applied to.</p>
            policy: <p>The policy to apply to the container recipe.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.put_container_recipe_policy_request.PutContainerRecipePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.put_container_recipe_policy_response.PutContainerRecipePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.put_container_recipe_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.put_container_recipe_policy.put_container_recipe_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.put_container_recipe_policy_request.PutContainerRecipePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["container_recipe_arn"] = container_recipe_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_image_policy(
        self,
        image_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.put_image_policy_response.PutImagePolicyResponse":
        r"""<p>Applies a policy to an image. We recommend that you call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html\">CreateResourceShare</a> to share resources. If you call the Image Builder API <code>PutImagePolicy</code>, you must also call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html\">PromoteResourceShareCreatedFromPolicy</a> in order for the resource to be visible to all principals with whom the resource is shared.</p>

        Args:
            image_arn: <p>The Amazon Resource Name (ARN) of the image that this policy should be applied to.</p>
            policy: <p>The policy to apply.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.put_image_policy_request.PutImagePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.put_image_policy_response.PutImagePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.put_image_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.put_image_policy.put_image_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.put_image_policy_request.PutImagePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["image_arn"] = image_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_image_recipe_policy(
        self,
        image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.put_image_recipe_policy_response.PutImageRecipePolicyResponse":
        r"""<p>Applies a policy to an image recipe. We recommend that you call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html\">CreateResourceShare</a> to share resources. If you call the Image Builder API <code>PutImageRecipePolicy</code>, you must also call the RAM API <a href=\"https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html\">PromoteResourceShareCreatedFromPolicy</a> in order for the resource to be visible to all principals with whom the resource is shared.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that this policy should be applied to.</p>
            policy: <p>The policy to apply.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.put_image_recipe_policy_request.PutImageRecipePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.put_image_recipe_policy_response.PutImageRecipePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.put_image_recipe_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.put_image_recipe_policy.put_image_recipe_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.put_image_recipe_policy_request.PutImageRecipePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["image_recipe_arn"] = image_recipe_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def retry_image(
        self,
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.retry_image_response.RetryImageResponse":
        r"""<p>RetryImage retries an image distribution without rebuilding the image.</p>

        Args:
            image_build_version_arn: <p>The source image Amazon Resource Name (ARN) to retry.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.retry_image_request.RetryImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.retry_image_response.RetryImageResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.retry_image

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.retry_image.retry_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.retry_image_request.RetryImageRequest = {}  # type: ignore[typeddict-item]
        input_["image_build_version_arn"] = image_build_version_arn
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_workflow_step_action(
        self,
        step_execution_id: "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId",
        image_build_version_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        action: "aws_sdk_imagebuilder.types.workflow_step_action_type.WorkflowStepActionType",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        reason: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.send_workflow_step_action_response.SendWorkflowStepActionResponse":
        r"""<p>Pauses or resumes image creation when the associated workflow runs a <code>WaitForAction</code> step.</p>

        Args:
            step_execution_id: <p>Uniquely identifies the workflow step that sent the step action.</p>
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image build version to send action for.</p>
            action: <p>The action for the image creation process to take while a workflow <code>WaitForAction</code> step waits for an asynchronous action to complete.</p>
            reason: <p>The reason why this action is sent.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.send_workflow_step_action_request.SendWorkflowStepActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.send_workflow_step_action_response.SendWorkflowStepActionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.send_workflow_step_action

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.send_workflow_step_action.send_workflow_step_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.send_workflow_step_action_request.SendWorkflowStepActionRequest = {}  # type: ignore[typeddict-item]
        input_["step_execution_id"] = step_execution_id
        input_["image_build_version_arn"] = image_build_version_arn
        input_["action"] = action
        if reason is not None:
            input_["reason"] = reason
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_image_pipeline_execution(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.start_image_pipeline_execution_response.StartImagePipelineExecutionResponse":
        r"""<p>Manually triggers a pipeline to create an image.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to manually invoke.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            tags: <p>Specify tags for Image Builder to apply to the image resource that's created When it starts pipeline execution.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.start_image_pipeline_execution_request.StartImagePipelineExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.start_image_pipeline_execution_response.StartImagePipelineExecutionResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.start_image_pipeline_execution

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.start_image_pipeline_execution.start_image_pipeline_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.start_image_pipeline_execution_request.StartImagePipelineExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["image_pipeline_arn"] = image_pipeline_arn
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_resource_state_update(
        self,
        resource_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        state: "aws_sdk_imagebuilder.types.resource_state.ResourceState",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        execution_role: Optional[
            "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        include_resources: Optional[
            "aws_sdk_imagebuilder.types.resource_state_update_include_resources.ResourceStateUpdateIncludeResources"
        ] = None,
        exclusion_rules: Optional[
            "aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules.ResourceStateUpdateExclusionRules"
        ] = None,
        update_at: Optional[
            "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.start_resource_state_update_response.StartResourceStateUpdateResponse":
        r"""<p>Begin asynchronous resource state update for lifecycle changes to the specified image resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Image Builder resource that is updated. The state update might also impact associated resources.</p>
            state: <p>Indicates the lifecycle action to take for this request.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) of the IAM role that’s used to update image state.</p>
            include_resources: <p>A list of image resources to update state for.</p>
            exclusion_rules: <p>Skip action on the image resource and associated resources if specified exclusion rules are met.</p>
            update_at: <p>The timestamp that indicates when resources are updated by a lifecycle action.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.start_resource_state_update_request.StartResourceStateUpdateRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.start_resource_state_update_response.StartResourceStateUpdateResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.start_resource_state_update

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.start_resource_state_update.start_resource_state_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.start_resource_state_update_request.StartResourceStateUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["state"] = state
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if include_resources is not None:
            input_["include_resources"] = include_resources
        if exclusion_rules is not None:
            input_["exclusion_rules"] = exclusion_rules
        if update_at is not None:
            input_["update_at"] = update_at
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        tags: "aws_sdk_imagebuilder.types.tag_map.TagMap",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to apply to the resource.</p>

        Raises:
            aws_sdk_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.tag_resource

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        tag_keys: "aws_sdk_imagebuilder.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
    ) -> "aws_sdk_imagebuilder.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            aws_sdk_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.untag_resource

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_distribution_configuration(
        self,
        distribution_configuration_arn: "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        distributions: "aws_sdk_imagebuilder.types.distribution_list.DistributionList",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.update_distribution_configuration_response.UpdateDistributionConfigurationResponse":
        r"""<p>Updates a new distribution configuration. Distribution configurations define and configure the outputs of your pipeline.</p>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that you want to update.</p>
            description: <p>The description of the distribution configuration.</p>
            distributions: <p>The distributions of the distribution configuration.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.update_distribution_configuration_request.UpdateDistributionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.update_distribution_configuration_response.UpdateDistributionConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.update_distribution_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.update_distribution_configuration.update_distribution_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.update_distribution_configuration_request.UpdateDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_configuration_arn"] = distribution_configuration_arn
        if description is not None:
            input_["description"] = description
        input_["distributions"] = distributions
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_image_pipeline(
        self,
        image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        image_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "aws_sdk_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        schedule: Optional["aws_sdk_imagebuilder.types.schedule.Schedule"] = None,
        status: Optional[
            "aws_sdk_imagebuilder.types.pipeline_status.PipelineStatus"
        ] = None,
        image_scanning_configuration: Optional[
            "aws_sdk_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "aws_sdk_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        logging_configuration: Optional[
            "aws_sdk_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
        ] = None,
        execution_role: Optional[
            "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        image_tags: Optional["aws_sdk_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_imagebuilder.types.update_image_pipeline_response.UpdateImagePipelineResponse":
        r"""<p>Updates an image pipeline. Image pipelines enable you to automate the creation and distribution of images. You must specify exactly one recipe for your image, using either a <code>containerRecipeArn</code> or an <code>imageRecipeArn</code>.</p> <note> <p>UpdateImagePipeline does not support selective updates for the pipeline. You must specify all of the required properties in the update request, not just the properties that have changed.</p> </note>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to update.</p>
            description: <p>The description of the image pipeline.</p>
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container pipeline to update.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images that this image pipeline has updated.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images that this image pipeline has updated.</p>
            image_tests_configuration: <p>The image test configuration of the image pipeline.</p>
            enhanced_image_metadata_enabled: <p>Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.</p>
            schedule: <p>The schedule of the image pipeline.</p>
            status: <p>The status of the image pipeline.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Contains settings for vulnerability scans.</p>
            workflows: <p>Contains the workflows to run for the pipeline.</p>
            logging_configuration: <p>Update logging configuration for the output image that's created when the pipeline runs.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>
            image_tags: <p>The tags to be applied to the images produced by this pipeline.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.update_image_pipeline_request.UpdateImagePipelineRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.update_image_pipeline_response.UpdateImagePipelineResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.update_image_pipeline

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.update_image_pipeline.update_image_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.update_image_pipeline_request.UpdateImagePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["image_pipeline_arn"] = image_pipeline_arn
        if description is not None:
            input_["description"] = description
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if schedule is not None:
            input_["schedule"] = schedule
        if status is not None:
            input_["status"] = status
        input_["client_token"] = client_token
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if image_tags is not None:
            input_["image_tags"] = image_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        instance_profile_name: "aws_sdk_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        instance_types: Optional[
            "aws_sdk_imagebuilder.types.instance_type_list.InstanceTypeList"
        ] = None,
        security_group_ids: Optional[
            "aws_sdk_imagebuilder.types.security_group_ids.SecurityGroupIds"
        ] = None,
        subnet_id: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        logging: Optional["aws_sdk_imagebuilder.types.logging.Logging"] = None,
        key_pair: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        terminate_instance_on_failure: Optional[
            "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        sns_topic_arn: Optional[
            "aws_sdk_imagebuilder.types.sns_topic_arn.SnsTopicArn"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_imagebuilder.types.resource_tag_map.ResourceTagMap"
        ] = None,
        instance_metadata_options: Optional[
            "aws_sdk_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
        ] = None,
        placement: Optional["aws_sdk_imagebuilder.types.placement.Placement"] = None,
    ) -> "aws_sdk_imagebuilder.types.update_infrastructure_configuration_response.UpdateInfrastructureConfigurationResponse":
        r"""<p>Updates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.</p>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.</p>
            description: <p>The description of the infrastructure configuration.</p>
            instance_types: <p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.</p>
            instance_profile_name: <p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI.</p>
            security_group_ids: <p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>
            subnet_id: <p>The subnet ID to place the instance used to customize your Amazon EC2 AMI in.</p>
            logging: <p>The logging configuration of the infrastructure configuration.</p>
            key_pair: <p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>
            terminate_instance_on_failure: <p>The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.</p> <note> <p>EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.</p> </note>
            resource_tags: <p>The tags attached to the resource created by Image Builder.</p>
            instance_metadata_options: <p>The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances. For more information about instance metadata options, see one of the following links:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html\">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i> for Linux instances.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html\">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i> for Windows instances.</p> </li> </ul>
            placement: <p>The instance placement settings that define where the instances that are launched from your image will run.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.update_infrastructure_configuration_request.UpdateInfrastructureConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.update_infrastructure_configuration_response.UpdateInfrastructureConfigurationResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.update_infrastructure_configuration

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.update_infrastructure_configuration.update_infrastructure_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.update_infrastructure_configuration_request.UpdateInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["infrastructure_configuration_arn"] = infrastructure_configuration_arn
        if description is not None:
            input_["description"] = description
        if instance_types is not None:
            input_["instance_types"] = instance_types
        input_["instance_profile_name"] = instance_profile_name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if logging is not None:
            input_["logging"] = logging
        if key_pair is not None:
            input_["key_pair"] = key_pair
        if terminate_instance_on_failure is not None:
            input_["terminate_instance_on_failure"] = terminate_instance_on_failure
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if instance_metadata_options is not None:
            input_["instance_metadata_options"] = instance_metadata_options
        if placement is not None:
            input_["placement"] = placement
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_lifecycle_policy(
        self,
        lifecycle_policy_arn: "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        execution_role: "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        resource_type: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType",
        policy_details: "aws_sdk_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails",
        resource_selection: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection",
        client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[imagebuilderClientConfig] = None,
        description: Optional[
            "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        status: Optional[
            "aws_sdk_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
        ] = None,
    ) -> "aws_sdk_imagebuilder.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse":
        r"""<p>Update the specified lifecycle policy.</p>

        Args:
            lifecycle_policy_arn: <p>The Amazon Resource Name (ARN) of the lifecycle policy resource.</p>
            description: <p>Optional description for the lifecycle policy.</p>
            status: <p>Indicates whether the lifecycle policy resource is enabled.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to update the lifecycle policy.</p>
            resource_type: <p>The type of image resource that the lifecycle policy applies to.</p>
            policy_details: <p>The configuration details for a lifecycle policy resource.</p>
            resource_selection: <p>Selection criteria for resources that the lifecycle policy applies to.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the specific operation.</p>
            aws_sdk_imagebuilder.errors.client_exception.ClientException: <p>These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.</p>
            aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            aws_sdk_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            aws_sdk_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified two or more mutually exclusive parameters. Review the error message for details.</p>
            aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>You have requested an action that that the service doesn't support.</p>
            aws_sdk_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            aws_sdk_imagebuilder.errors.service_exception.ServiceException: <p>This exception is thrown when the service encounters an unrecoverable exception.</p>
            aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            aws_sdk_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_imagebuilder.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_imagebuilder.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import aws_sdk_imagebuilder._operations.imagebuilder.update_lifecycle_policy

            output, http_response = (
                aws_sdk_imagebuilder._operations.imagebuilder.update_lifecycle_policy.update_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_imagebuilder.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_policy_arn"] = lifecycle_policy_arn
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        input_["execution_role"] = execution_role
        input_["resource_type"] = resource_type
        input_["policy_details"] = policy_details
        input_["resource_selection"] = resource_selection
        input_["client_token"] = client_token

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
