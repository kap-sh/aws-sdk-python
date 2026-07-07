"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#IotThingsGraphFrontEndService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_iotthingsgraph._auth._signers
import aws_sdk_iotthingsgraph._auth._sigv4
from aws_sdk_iotthingsgraph._auth._identity import Credentials
from aws_sdk_iotthingsgraph._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_iotthingsgraph._auth._zapros_handler import AuthMiddleware
from aws_sdk_iotthingsgraph._pagination import resolve_path as _resolve_path
from aws_sdk_iotthingsgraph._services._aws_config import aws_config
from aws_sdk_iotthingsgraph._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.associate_entity_to_thing_request
    import aws_sdk_iotthingsgraph.types.associate_entity_to_thing_response
    import aws_sdk_iotthingsgraph.types.create_flow_template_request
    import aws_sdk_iotthingsgraph.types.create_flow_template_response
    import aws_sdk_iotthingsgraph.types.create_system_instance_request
    import aws_sdk_iotthingsgraph.types.create_system_instance_response
    import aws_sdk_iotthingsgraph.types.create_system_template_request
    import aws_sdk_iotthingsgraph.types.create_system_template_response
    import aws_sdk_iotthingsgraph.types.definition_document
    import aws_sdk_iotthingsgraph.types.delete_flow_template_request
    import aws_sdk_iotthingsgraph.types.delete_flow_template_response
    import aws_sdk_iotthingsgraph.types.delete_namespace_request
    import aws_sdk_iotthingsgraph.types.delete_namespace_response
    import aws_sdk_iotthingsgraph.types.delete_system_instance_request
    import aws_sdk_iotthingsgraph.types.delete_system_instance_response
    import aws_sdk_iotthingsgraph.types.delete_system_template_request
    import aws_sdk_iotthingsgraph.types.delete_system_template_response
    import aws_sdk_iotthingsgraph.types.deploy_system_instance_request
    import aws_sdk_iotthingsgraph.types.deploy_system_instance_response
    import aws_sdk_iotthingsgraph.types.deployment_target
    import aws_sdk_iotthingsgraph.types.deprecate_existing_entities
    import aws_sdk_iotthingsgraph.types.deprecate_flow_template_request
    import aws_sdk_iotthingsgraph.types.deprecate_flow_template_response
    import aws_sdk_iotthingsgraph.types.deprecate_system_template_request
    import aws_sdk_iotthingsgraph.types.deprecate_system_template_response
    import aws_sdk_iotthingsgraph.types.describe_namespace_request
    import aws_sdk_iotthingsgraph.types.describe_namespace_response
    import aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_request
    import aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_response
    import aws_sdk_iotthingsgraph.types.entity_description
    import aws_sdk_iotthingsgraph.types.entity_filters
    import aws_sdk_iotthingsgraph.types.entity_type
    import aws_sdk_iotthingsgraph.types.entity_types
    import aws_sdk_iotthingsgraph.types.flow_execution_id
    import aws_sdk_iotthingsgraph.types.flow_execution_message
    import aws_sdk_iotthingsgraph.types.flow_execution_summary
    import aws_sdk_iotthingsgraph.types.flow_template_filters
    import aws_sdk_iotthingsgraph.types.flow_template_summary
    import aws_sdk_iotthingsgraph.types.get_entities_request
    import aws_sdk_iotthingsgraph.types.get_entities_response
    import aws_sdk_iotthingsgraph.types.get_flow_template_request
    import aws_sdk_iotthingsgraph.types.get_flow_template_response
    import aws_sdk_iotthingsgraph.types.get_flow_template_revisions_request
    import aws_sdk_iotthingsgraph.types.get_flow_template_revisions_response
    import aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_request
    import aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_response
    import aws_sdk_iotthingsgraph.types.get_system_instance_request
    import aws_sdk_iotthingsgraph.types.get_system_instance_response
    import aws_sdk_iotthingsgraph.types.get_system_template_request
    import aws_sdk_iotthingsgraph.types.get_system_template_response
    import aws_sdk_iotthingsgraph.types.get_system_template_revisions_request
    import aws_sdk_iotthingsgraph.types.get_system_template_revisions_response
    import aws_sdk_iotthingsgraph.types.get_upload_status_request
    import aws_sdk_iotthingsgraph.types.get_upload_status_response
    import aws_sdk_iotthingsgraph.types.group_name
    import aws_sdk_iotthingsgraph.types.list_flow_execution_messages_request
    import aws_sdk_iotthingsgraph.types.list_flow_execution_messages_response
    import aws_sdk_iotthingsgraph.types.list_tags_for_resource_request
    import aws_sdk_iotthingsgraph.types.list_tags_for_resource_response
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.metrics_configuration
    import aws_sdk_iotthingsgraph.types.namespace_name
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.resource_arn
    import aws_sdk_iotthingsgraph.types.role_arn
    import aws_sdk_iotthingsgraph.types.s3_bucket_name
    import aws_sdk_iotthingsgraph.types.search_entities_request
    import aws_sdk_iotthingsgraph.types.search_entities_response
    import aws_sdk_iotthingsgraph.types.search_flow_executions_request
    import aws_sdk_iotthingsgraph.types.search_flow_executions_response
    import aws_sdk_iotthingsgraph.types.search_flow_templates_request
    import aws_sdk_iotthingsgraph.types.search_flow_templates_response
    import aws_sdk_iotthingsgraph.types.search_system_instances_request
    import aws_sdk_iotthingsgraph.types.search_system_instances_response
    import aws_sdk_iotthingsgraph.types.search_system_templates_request
    import aws_sdk_iotthingsgraph.types.search_system_templates_response
    import aws_sdk_iotthingsgraph.types.search_things_request
    import aws_sdk_iotthingsgraph.types.search_things_response
    import aws_sdk_iotthingsgraph.types.sync_with_public_namespace
    import aws_sdk_iotthingsgraph.types.system_instance_filters
    import aws_sdk_iotthingsgraph.types.system_instance_summary
    import aws_sdk_iotthingsgraph.types.system_template_filters
    import aws_sdk_iotthingsgraph.types.system_template_summary
    import aws_sdk_iotthingsgraph.types.tag
    import aws_sdk_iotthingsgraph.types.tag_key_list
    import aws_sdk_iotthingsgraph.types.tag_list
    import aws_sdk_iotthingsgraph.types.tag_resource_request
    import aws_sdk_iotthingsgraph.types.tag_resource_response
    import aws_sdk_iotthingsgraph.types.thing
    import aws_sdk_iotthingsgraph.types.thing_name
    import aws_sdk_iotthingsgraph.types.timestamp
    import aws_sdk_iotthingsgraph.types.undeploy_system_instance_request
    import aws_sdk_iotthingsgraph.types.undeploy_system_instance_response
    import aws_sdk_iotthingsgraph.types.untag_resource_request
    import aws_sdk_iotthingsgraph.types.untag_resource_response
    import aws_sdk_iotthingsgraph.types.update_flow_template_request
    import aws_sdk_iotthingsgraph.types.update_flow_template_response
    import aws_sdk_iotthingsgraph.types.update_system_template_request
    import aws_sdk_iotthingsgraph.types.update_system_template_response
    import aws_sdk_iotthingsgraph.types.upload_entity_definitions_request
    import aws_sdk_iotthingsgraph.types.upload_entity_definitions_response
    import aws_sdk_iotthingsgraph.types.upload_id
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.urns
    import aws_sdk_iotthingsgraph.types.version


class IoTThingsGraphClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTThingsGraphClient:
    """A client for the ``IoTThingsGraph`` service.

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
        self._config = IoTThingsGraphClientConfig(
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
        self, config_overrides: Optional[IoTThingsGraphClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTThingsGraphClientConfig = config_overrides or {}
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

    def associate_entity_to_thing(
        self,
        thing_name: "aws_sdk_iotthingsgraph.types.thing_name.ThingName",
        entity_id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.associate_entity_to_thing_response.AssociateEntityToThingResponse":
        """<p>Associates a device with a concrete thing that is in the user's registry.</p> <p>A thing can be associated with only one device at a time. If you associate a thing with a new device id, its previous association will be removed.</p>

        Args:
            thing_name: <p>The name of the thing to which the entity is to be associated.</p>
            entity_id: <p>The ID of the device to be associated with the thing.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>
            namespace_version: <p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.associate_entity_to_thing_request.AssociateEntityToThingRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.associate_entity_to_thing_response.AssociateEntityToThingResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.associate_entity_to_thing

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.associate_entity_to_thing.associate_entity_to_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.associate_entity_to_thing_request.AssociateEntityToThingRequest = {}  # type: ignore[typeddict-item]
        input_["thing_name"] = thing_name
        input_["entity_id"] = entity_id
        if namespace_version is not None:
            input_["namespace_version"] = namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_flow_template(
        self,
        definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        compatible_namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.create_flow_template_response.CreateFlowTemplateResponse":
        """<p>Creates a workflow template. Workflows can be created only in the user's namespace. (The public namespace contains only entities.) The workflow can contain only entities in the specified namespace. The workflow is validated against the entities in the latest version of the user's namespace unless another namespace version is specified in the request.</p>

        Args:
            definition: <p>The workflow <code>DefinitionDocument</code>.</p>
            compatible_namespace_version: <p>The namespace version in which the workflow is to be created.</p> <p>If no value is specified, the latest version is used by default.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.limit_exceeded_exception.LimitExceededException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.create_flow_template_request.CreateFlowTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.create_flow_template_response.CreateFlowTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_flow_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_flow_template.create_flow_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.create_flow_template_request.CreateFlowTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["definition"] = definition
        if compatible_namespace_version is not None:
            input_["compatible_namespace_version"] = compatible_namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_system_instance(
        self,
        definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument",
        target: "aws_sdk_iotthingsgraph.types.deployment_target.DeploymentTarget",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        tags: Optional["aws_sdk_iotthingsgraph.types.tag_list.TagList"] = None,
        greengrass_group_name: Optional[
            "aws_sdk_iotthingsgraph.types.group_name.GroupName"
        ] = None,
        s3_bucket_name: Optional[
            "aws_sdk_iotthingsgraph.types.s3_bucket_name.S3BucketName"
        ] = None,
        metrics_configuration: Optional[
            "aws_sdk_iotthingsgraph.types.metrics_configuration.MetricsConfiguration"
        ] = None,
        flow_actions_role_arn: Optional[
            "aws_sdk_iotthingsgraph.types.role_arn.RoleArn"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.create_system_instance_response.CreateSystemInstanceResponse":
        """<p>Creates a system instance. </p> <p>This action validates the system instance, prepares the deployment-related resources. For Greengrass deployments, it updates the Greengrass group that is specified by the <code>greengrassGroupName</code> parameter. It also adds a file to the S3 bucket specified by the <code>s3BucketName</code> parameter. You need to call <code>DeploySystemInstance</code> after running this action.</p> <p>For Greengrass deployments, since this action modifies and adds resources to a Greengrass group and an S3 bucket on the caller's behalf, the calling identity must have write permissions to both the specified Greengrass group and S3 bucket. Otherwise, the call will fail with an authorization error.</p> <p>For cloud deployments, this action requires a <code>flowActionsRoleArn</code> value. This is an IAM role that has permissions to access AWS services, such as AWS Lambda and AWS IoT, that the flow uses when it executes.</p> <p>If the definition document doesn't specify a version of the user's namespace, the latest version will be used by default.</p>

        Args:
            tags: <p>Metadata, consisting of key-value pairs, that can be used to categorize your system instances.</p>
            target: <p>The target type of the deployment. Valid values are <code>GREENGRASS</code> and <code>CLOUD</code>.</p>
            greengrass_group_name: <p>The name of the Greengrass group where the system instance will be deployed. This value is required if the value of the <code>target</code> parameter is <code>GREENGRASS</code>.</p>
            s3_bucket_name: <p>The name of the Amazon Simple Storage Service bucket that will be used to store and deploy the system instance's resource file. This value is required if the value of the <code>target</code> parameter is <code>GREENGRASS</code>.</p>
            flow_actions_role_arn: <p>The ARN of the IAM role that AWS IoT Things Graph will assume when it executes the flow. This role must have read and write access to AWS Lambda and AWS IoT and any other AWS services that the flow uses when it executes. This value is required if the value of the <code>target</code> parameter is <code>CLOUD</code>.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.limit_exceeded_exception.LimitExceededException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.create_system_instance_request.CreateSystemInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.create_system_instance_response.CreateSystemInstanceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_system_instance

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_system_instance.create_system_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.create_system_instance_request.CreateSystemInstanceRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        input_["definition"] = definition
        input_["target"] = target
        if greengrass_group_name is not None:
            input_["greengrass_group_name"] = greengrass_group_name
        if s3_bucket_name is not None:
            input_["s3_bucket_name"] = s3_bucket_name
        if metrics_configuration is not None:
            input_["metrics_configuration"] = metrics_configuration
        if flow_actions_role_arn is not None:
            input_["flow_actions_role_arn"] = flow_actions_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_system_template(
        self,
        definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        compatible_namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.create_system_template_response.CreateSystemTemplateResponse":
        """<p>Creates a system. The system is validated against the entities in the latest version of the user's namespace unless another namespace version is specified in the request.</p>

        Args:
            definition: <p>The <code>DefinitionDocument</code> used to create the system.</p>
            compatible_namespace_version: <p>The namespace version in which the system is to be created.</p> <p>If no value is specified, the latest version is used by default.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.create_system_template_request.CreateSystemTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.create_system_template_response.CreateSystemTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_system_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.create_system_template.create_system_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.create_system_template_request.CreateSystemTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["definition"] = definition
        if compatible_namespace_version is not None:
            input_["compatible_namespace_version"] = compatible_namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_flow_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.delete_flow_template_response.DeleteFlowTemplateResponse":
        """<p>Deletes a workflow. Any new system or deployment that contains this workflow will fail to update or deploy. Existing deployments that contain the workflow will continue to run (since they use a snapshot of the workflow taken at the time of deployment).</p>

        Args:
            id: <p>The ID of the workflow to be deleted.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_in_use_exception.ResourceInUseException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.delete_flow_template_request.DeleteFlowTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.delete_flow_template_response.DeleteFlowTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_flow_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_flow_template.delete_flow_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.delete_flow_template_request.DeleteFlowTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_namespace(
        self, *, config_overrides: Optional[IoTThingsGraphClientConfig] = None
    ) -> (
        "aws_sdk_iotthingsgraph.types.delete_namespace_response.DeleteNamespaceResponse"
    ):
        """<p>Deletes the specified namespace. This action deletes all of the entities in the namespace. Delete the systems and flows that use entities in the namespace before performing this action. This action takes no request parameters.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_namespace

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.delete_namespace_request.DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_system_instance(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        id: Optional["aws_sdk_iotthingsgraph.types.urn.Urn"] = None,
    ) -> "aws_sdk_iotthingsgraph.types.delete_system_instance_response.DeleteSystemInstanceResponse":
        """<p>Deletes a system instance. Only system instances that have never been deployed, or that have been undeployed can be deleted.</p> <p>Users can create a new system instance that has the same ID as a deleted system instance.</p>

        Args:
            id: <p>The ID of the system instance to be deleted.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_in_use_exception.ResourceInUseException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.delete_system_instance_request.DeleteSystemInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.delete_system_instance_response.DeleteSystemInstanceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_system_instance

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_system_instance.delete_system_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.delete_system_instance_request.DeleteSystemInstanceRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_system_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.delete_system_template_response.DeleteSystemTemplateResponse":
        """<p>Deletes a system. New deployments can't contain the system after its deletion. Existing deployments that contain the system will continue to work because they use a snapshot of the system that is taken when it is deployed.</p>

        Args:
            id: <p>The ID of the system to be deleted.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_in_use_exception.ResourceInUseException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.delete_system_template_request.DeleteSystemTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.delete_system_template_response.DeleteSystemTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_system_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.delete_system_template.delete_system_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.delete_system_template_request.DeleteSystemTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deploy_system_instance(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        id: Optional["aws_sdk_iotthingsgraph.types.urn.Urn"] = None,
    ) -> "aws_sdk_iotthingsgraph.types.deploy_system_instance_response.DeploySystemInstanceResponse":
        r"""<p> <b>Greengrass and Cloud Deployments</b> </p> <p>Deploys the system instance to the target specified in <code>CreateSystemInstance</code>. </p> <p> <b>Greengrass Deployments</b> </p> <p>If the system or any workflows and entities have been updated before this action is called, then the deployment will create a new Amazon Simple Storage Service resource file and then deploy it.</p> <p>Since this action creates a Greengrass deployment on the caller's behalf, the calling identity must have write permissions to the specified Greengrass group. Otherwise, the call will fail with an authorization error.</p> <p>For information about the artifacts that get added to your Greengrass core device when you use this API, see <a href=\"https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-greengrass.html\">AWS IoT Things Graph and AWS IoT Greengrass</a>.</p>

        Args:
            id: <p>The ID of the system instance. This value is returned by the <code>CreateSystemInstance</code> action.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_in_use_exception.ResourceInUseException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.deploy_system_instance_request.DeploySystemInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.deploy_system_instance_response.DeploySystemInstanceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deploy_system_instance

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deploy_system_instance.deploy_system_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.deploy_system_instance_request.DeploySystemInstanceRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deprecate_flow_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.deprecate_flow_template_response.DeprecateFlowTemplateResponse":
        """<p>Deprecates the specified workflow. This action marks the workflow for deletion. Deprecated flows can't be deployed, but existing deployments will continue to run.</p>

        Args:
            id: <p>The ID of the workflow to be deleted.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.deprecate_flow_template_request.DeprecateFlowTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.deprecate_flow_template_response.DeprecateFlowTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deprecate_flow_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deprecate_flow_template.deprecate_flow_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.deprecate_flow_template_request.DeprecateFlowTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deprecate_system_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.deprecate_system_template_response.DeprecateSystemTemplateResponse":
        """<p>Deprecates the specified system.</p>

        Args:
            id: <p>The ID of the system to delete.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.deprecate_system_template_request.DeprecateSystemTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.deprecate_system_template_response.DeprecateSystemTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deprecate_system_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.deprecate_system_template.deprecate_system_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.deprecate_system_template_request.DeprecateSystemTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_namespace(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        namespace_name: Optional[
            "aws_sdk_iotthingsgraph.types.namespace_name.NamespaceName"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.describe_namespace_response.DescribeNamespaceResponse":
        """<p>Gets the latest version of the user's namespace and the public version that it is tracking.</p>

        Args:
            namespace_name: <p>The name of the user's namespace. Set this to <code>aws</code> to get the public namespace.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.describe_namespace_request.DescribeNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.describe_namespace_response.DescribeNamespaceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.describe_namespace

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.describe_namespace.describe_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.describe_namespace_request.DescribeNamespaceRequest = {}  # type: ignore[typeddict-item]
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def dissociate_entity_from_thing(
        self,
        thing_name: "aws_sdk_iotthingsgraph.types.thing_name.ThingName",
        entity_type: "aws_sdk_iotthingsgraph.types.entity_type.EntityType",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_response.DissociateEntityFromThingResponse":
        """<p>Dissociates a device entity from a concrete thing. The action takes only the type of the entity that you need to dissociate because only one entity of a particular type can be associated with a thing.</p>

        Args:
            thing_name: <p>The name of the thing to disassociate.</p>
            entity_type: <p>The entity type from which to disassociate the thing.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_request.DissociateEntityFromThingRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_response.DissociateEntityFromThingResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.dissociate_entity_from_thing

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.dissociate_entity_from_thing.dissociate_entity_from_thing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.dissociate_entity_from_thing_request.DissociateEntityFromThingRequest = {}  # type: ignore[typeddict-item]
        input_["thing_name"] = thing_name
        input_["entity_type"] = entity_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_entities(
        self,
        ids: "aws_sdk_iotthingsgraph.types.urns.Urns",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_entities_response.GetEntitiesResponse":
        """<p>Gets definitions of the specified entities. Uses the latest version of the user's namespace by default. This API returns the following TDM entities.</p> <ul> <li> <p>Properties</p> </li> <li> <p>States</p> </li> <li> <p>Events</p> </li> <li> <p>Actions</p> </li> <li> <p>Capabilities</p> </li> <li> <p>Mappings</p> </li> <li> <p>Devices</p> </li> <li> <p>Device Models</p> </li> <li> <p>Services</p> </li> </ul> <p>This action doesn't return definitions for systems, flows, and deployments.</p>

        Args:
            ids: <p>An array of entity IDs.</p> <p>The IDs should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>
            namespace_version: <p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_entities_request.GetEntitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_entities_response.GetEntitiesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_entities

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_entities.get_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_entities_request.GetEntitiesRequest = {}  # type: ignore[typeddict-item]
        input_["ids"] = ids
        if namespace_version is not None:
            input_["namespace_version"] = namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_flow_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        revision_number: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_flow_template_response.GetFlowTemplateResponse":
        """<p>Gets the latest version of the <code>DefinitionDocument</code> and <code>FlowTemplateSummary</code> for the specified workflow.</p>

        Args:
            id: <p>The ID of the workflow.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>
            revision_number: <p>The number of the workflow revision to retrieve.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_flow_template_request.GetFlowTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_flow_template_response.GetFlowTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_flow_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_flow_template.get_flow_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_flow_template_request.GetFlowTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if revision_number is not None:
            input_["revision_number"] = revision_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_flow_template_revisions(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_flow_template_revisions_response.GetFlowTemplateRevisionsResponse":
        """<p>Gets revisions of the specified workflow. Only the last 100 revisions are stored. If the workflow has been deprecated, this action will return revisions that occurred before the deprecation. This action won't work for workflows that have been deleted.</p>

        Args:
            id: <p>The ID of the workflow.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_flow_template_revisions_request.GetFlowTemplateRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_flow_template_revisions_response.GetFlowTemplateRevisionsResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_flow_template_revisions

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_flow_template_revisions.get_flow_template_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_flow_template_revisions_request.GetFlowTemplateRevisionsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    def iter_get_flow_template_revisions(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.flow_template_summary.FlowTemplateSummary]":
        _token = next_token
        while True:
            _response = self.get_flow_template_revisions(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_namespace_deletion_status(
        self, *, config_overrides: Optional[IoTThingsGraphClientConfig] = None
    ) -> "aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_response.GetNamespaceDeletionStatusResponse":
        """<p>Gets the status of a namespace deletion task.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_request.GetNamespaceDeletionStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_response.GetNamespaceDeletionStatusResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_namespace_deletion_status

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_namespace_deletion_status.get_namespace_deletion_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_namespace_deletion_status_request.GetNamespaceDeletionStatusRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_system_instance(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_system_instance_response.GetSystemInstanceResponse":
        """<p>Gets a system instance.</p>

        Args:
            id: <p>The ID of the system deployment instance. This value is returned by <code>CreateSystemInstance</code>.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME</code> </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_system_instance_request.GetSystemInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_system_instance_response.GetSystemInstanceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_instance

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_instance.get_system_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_system_instance_request.GetSystemInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_system_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        revision_number: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_system_template_response.GetSystemTemplateResponse":
        """<p>Gets a system.</p>

        Args:
            id: <p>The ID of the system to get. This ID must be in the user's namespace.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>
            revision_number: <p>The number that specifies the revision of the system to get.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_system_template_request.GetSystemTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_system_template_response.GetSystemTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_template.get_system_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_system_template_request.GetSystemTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if revision_number is not None:
            input_["revision_number"] = revision_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_system_template_revisions(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_system_template_revisions_response.GetSystemTemplateRevisionsResponse":
        """<p>Gets revisions made to the specified system template. Only the previous 100 revisions are stored. If the system has been deprecated, this action will return the revisions that occurred before its deprecation. This action won't work with systems that have been deleted.</p>

        Args:
            id: <p>The ID of the system template.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_system_template_revisions_request.GetSystemTemplateRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_system_template_revisions_response.GetSystemTemplateRevisionsResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_template_revisions

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_system_template_revisions.get_system_template_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_system_template_revisions_request.GetSystemTemplateRevisionsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    def iter_get_system_template_revisions(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.system_template_summary.SystemTemplateSummary]":
        _token = next_token
        while True:
            _response = self.get_system_template_revisions(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_upload_status(
        self,
        upload_id: "aws_sdk_iotthingsgraph.types.upload_id.UploadId",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.get_upload_status_response.GetUploadStatusResponse":
        """<p>Gets the status of the specified upload.</p>

        Args:
            upload_id: <p>The ID of the upload. This value is returned by the <code>UploadEntityDefinitions</code> action.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.get_upload_status_request.GetUploadStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.get_upload_status_response.GetUploadStatusResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_upload_status

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.get_upload_status.get_upload_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.get_upload_status_request.GetUploadStatusRequest = {}  # type: ignore[typeddict-item]
        input_["upload_id"] = upload_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_flow_execution_messages(
        self,
        flow_execution_id: "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.list_flow_execution_messages_response.ListFlowExecutionMessagesResponse":
        """<p>Returns a list of objects that contain information about events in a flow execution.</p>

        Args:
            flow_execution_id: <p>The ID of the flow execution.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.list_flow_execution_messages_request.ListFlowExecutionMessagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.list_flow_execution_messages_response.ListFlowExecutionMessagesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.list_flow_execution_messages

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.list_flow_execution_messages.list_flow_execution_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.list_flow_execution_messages_request.ListFlowExecutionMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["flow_execution_id"] = flow_execution_id
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

    def iter_list_flow_execution_messages(
        self,
        flow_execution_id: "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.flow_execution_message.FlowExecutionMessage]":
        _token = next_token
        while True:
            _response = self.list_flow_execution_messages(
                flow_execution_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("messages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotthingsgraph.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags on an AWS IoT Things Graph resource.</p>

        Args:
            max_results: <p>The maximum number of tags to return.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags are to be returned.</p>
            next_token: <p>The token that specifies the next page of results to return.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotthingsgraph.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.tag.Tag]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
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

    def search_entities(
        self,
        entity_types: "aws_sdk_iotthingsgraph.types.entity_types.EntityTypes",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.entity_filters.EntityFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_entities_response.SearchEntitiesResponse":
        """<p>Searches for entities of the specified type. You can search for entities in your namespace and the public namespace that you're tracking.</p>

        Args:
            entity_types: <p>The entity types for which to search.</p>
            filters: <p>Optional filter to apply to the search. Valid filters are <code>NAME</code> <code>NAMESPACE</code>, <code>SEMANTIC_TYPE_PATH</code> and <code>REFERENCED_ENTITY_ID</code>. <code>REFERENCED_ENTITY_ID</code> filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.</p> <p>Multiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            namespace_version: <p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_entities_request.SearchEntitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_entities_response.SearchEntitiesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_entities

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_entities.search_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_entities_request.SearchEntitiesRequest = {}  # type: ignore[typeddict-item]
        input_["entity_types"] = entity_types
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_version is not None:
            input_["namespace_version"] = namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_entities(
        self,
        entity_types: "aws_sdk_iotthingsgraph.types.entity_types.EntityTypes",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.entity_filters.EntityFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.entity_description.EntityDescription]":
        _token = next_token
        while True:
            _response = self.search_entities(
                entity_types,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
                namespace_version=namespace_version,
            )
            _page = _resolve_path(_response, ("descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_flow_executions(
        self,
        system_instance_id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        flow_execution_id: Optional[
            "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
        ] = None,
        start_time: Optional["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_flow_executions_response.SearchFlowExecutionsResponse":
        """<p>Searches for AWS IoT Things Graph workflow execution instances.</p>

        Args:
            system_instance_id: <p>The ID of the system instance that contains the flow.</p>
            flow_execution_id: <p>The ID of a flow execution.</p>
            start_time: <p>The date and time of the earliest flow execution to return.</p>
            end_time: <p>The date and time of the latest flow execution to return.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_flow_executions_request.SearchFlowExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_flow_executions_response.SearchFlowExecutionsResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_flow_executions

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_flow_executions.search_flow_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_flow_executions_request.SearchFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["system_instance_id"] = system_instance_id
        if flow_execution_id is not None:
            input_["flow_execution_id"] = flow_execution_id
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    def iter_search_flow_executions(
        self,
        system_instance_id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        flow_execution_id: Optional[
            "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
        ] = None,
        start_time: Optional["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.flow_execution_summary.FlowExecutionSummary]":
        _token = next_token
        while True:
            _response = self.search_flow_executions(
                system_instance_id,
                config_overrides=config_overrides,
                flow_execution_id=flow_execution_id,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_flow_templates(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.flow_template_filters.FlowTemplateFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_flow_templates_response.SearchFlowTemplatesResponse":
        """<p>Searches for summary information about workflows.</p>

        Args:
            filters: <p>An array of objects that limit the result set. The only valid filter is <code>DEVICE_MODEL_ID</code>.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_flow_templates_request.SearchFlowTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_flow_templates_response.SearchFlowTemplatesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_flow_templates

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_flow_templates.search_flow_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_flow_templates_request.SearchFlowTemplatesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_search_flow_templates(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.flow_template_filters.FlowTemplateFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.flow_template_summary.FlowTemplateSummary]":
        _token = next_token
        while True:
            _response = self.search_flow_templates(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_system_instances(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.system_instance_filters.SystemInstanceFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_system_instances_response.SearchSystemInstancesResponse":
        """<p>Searches for system instances in the user's account.</p>

        Args:
            filters: <p>Optional filter to apply to the search. Valid filters are <code>SYSTEM_TEMPLATE_ID</code>, <code>STATUS</code>, and <code>GREENGRASS_GROUP_NAME</code>.</p> <p>Multiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_system_instances_request.SearchSystemInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_system_instances_response.SearchSystemInstancesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_system_instances

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_system_instances.search_system_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_system_instances_request.SearchSystemInstancesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_search_system_instances(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.system_instance_filters.SystemInstanceFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary]":
        _token = next_token
        while True:
            _response = self.search_system_instances(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_system_templates(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.system_template_filters.SystemTemplateFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_system_templates_response.SearchSystemTemplatesResponse":
        """<p>Searches for summary information about systems in the user's account. You can filter by the ID of a workflow to return only systems that use the specified workflow.</p>

        Args:
            filters: <p>An array of filters that limit the result set. The only valid filter is <code>FLOW_TEMPLATE_ID</code>.</p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_system_templates_request.SearchSystemTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_system_templates_response.SearchSystemTemplatesResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_system_templates

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_system_templates.search_system_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_system_templates_request.SearchSystemTemplatesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def iter_search_system_templates(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        filters: Optional[
            "aws_sdk_iotthingsgraph.types.system_template_filters.SystemTemplateFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.system_template_summary.SystemTemplateSummary]":
        _token = next_token
        while True:
            _response = self.search_system_templates(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_things(
        self,
        entity_id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.search_things_response.SearchThingsResponse":
        """<p>Searches for things associated with the specified entity. You can search by both device and device model.</p> <p>For example, if two different devices, camera1 and camera2, implement the camera device model, the user can associate thing1 to camera1 and thing2 to camera2. <code>SearchThings(camera2)</code> will return only thing2, but <code>SearchThings(camera)</code> will return both thing1 and thing2.</p> <p>This action searches for exact matches and doesn't perform partial text matching.</p>

        Args:
            entity_id: <p>The ID of the entity to which the things are associated.</p> <p>The IDs should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>
            next_token: <p>The string that specifies the next page of results. Use this when you're paginating results.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            namespace_version: <p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.search_things_request.SearchThingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.search_things_response.SearchThingsResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_things

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.search_things.search_things(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.search_things_request.SearchThingsRequest = {}  # type: ignore[typeddict-item]
        input_["entity_id"] = entity_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_version is not None:
            input_["namespace_version"] = namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_things(
        self,
        entity_id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotthingsgraph.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotthingsgraph.types.max_results.MaxResults"
        ] = None,
        namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "Iterator[aws_sdk_iotthingsgraph.types.thing.Thing]":
        _token = next_token
        while True:
            _response = self.search_things(
                entity_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                namespace_version=namespace_version,
            )
            _page = _resolve_path(_response, ("things",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def tag_resource(
        self,
        resource_arn: "aws_sdk_iotthingsgraph.types.resource_arn.ResourceArn",
        tags: "aws_sdk_iotthingsgraph.types.tag_list.TagList",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.tag_resource_response.TagResourceResponse":
        """<p>Creates a tag for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags are returned.</p>
            tags: <p>A list of tags to add to the resource.></p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.tag_resource

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def undeploy_system_instance(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        id: Optional["aws_sdk_iotthingsgraph.types.urn.Urn"] = None,
    ) -> "aws_sdk_iotthingsgraph.types.undeploy_system_instance_response.UndeploySystemInstanceResponse":
        """<p>Removes a system instance from its target (Cloud or Greengrass).</p>

        Args:
            id: <p>The ID of the system instance to remove from its target.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_in_use_exception.ResourceInUseException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.undeploy_system_instance_request.UndeploySystemInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.undeploy_system_instance_response.UndeploySystemInstanceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.undeploy_system_instance

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.undeploy_system_instance.undeploy_system_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.undeploy_system_instance_request.UndeploySystemInstanceRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_iotthingsgraph.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_iotthingsgraph.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
    ) -> "aws_sdk_iotthingsgraph.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes a tag from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags are to be removed.</p>
            tag_keys: <p>A list of tag key names to remove from the resource. You don't specify the value. Both the key and its associated value are removed. </p> <p>This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html#cli-using-param-json\">Using JSON for Parameters</a> in the <i>AWS CLI User Guide</i>. </p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.untag_resource

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_flow_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        compatible_namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.update_flow_template_response.UpdateFlowTemplateResponse":
        """<p>Updates the specified workflow. All deployed systems and system instances that use the workflow will see the changes in the flow when it is redeployed. If you don't want this behavior, copy the workflow (creating a new workflow with a different ID), and update the copy. The workflow can contain only entities in the specified namespace. </p>

        Args:
            id: <p>The ID of the workflow to be updated.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>
            definition: <p>The <code>DefinitionDocument</code> that contains the updated workflow definition.</p>
            compatible_namespace_version: <p>The version of the user's namespace.</p> <p>If no value is specified, the latest version is used by default. Use the <code>GetFlowTemplateRevisions</code> if you want to find earlier revisions of the flow to update.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.update_flow_template_request.UpdateFlowTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.update_flow_template_response.UpdateFlowTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.update_flow_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.update_flow_template.update_flow_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.update_flow_template_request.UpdateFlowTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["definition"] = definition
        if compatible_namespace_version is not None:
            input_["compatible_namespace_version"] = compatible_namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_system_template(
        self,
        id: "aws_sdk_iotthingsgraph.types.urn.Urn",
        definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument",
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        compatible_namespace_version: Optional[
            "aws_sdk_iotthingsgraph.types.version.Version"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.update_system_template_response.UpdateSystemTemplateResponse":
        """<p>Updates the specified system. You don't need to run this action after updating a workflow. Any deployment that uses the system will see the changes in the system when it is redeployed.</p>

        Args:
            id: <p>The ID of the system to be updated.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>
            definition: <p>The <code>DefinitionDocument</code> that contains the updated system definition.</p>
            compatible_namespace_version: <p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p> <p>If no value is specified, the latest version is used by default.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.update_system_template_request.UpdateSystemTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.update_system_template_response.UpdateSystemTemplateResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.update_system_template

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.update_system_template.update_system_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.update_system_template_request.UpdateSystemTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["definition"] = definition
        if compatible_namespace_version is not None:
            input_["compatible_namespace_version"] = compatible_namespace_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def upload_entity_definitions(
        self,
        *,
        config_overrides: Optional[IoTThingsGraphClientConfig] = None,
        document: Optional[
            "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument"
        ] = None,
        sync_with_public_namespace: Optional[
            "aws_sdk_iotthingsgraph.types.sync_with_public_namespace.SyncWithPublicNamespace"
        ] = None,
        deprecate_existing_entities: Optional[
            "aws_sdk_iotthingsgraph.types.deprecate_existing_entities.DeprecateExistingEntities"
        ] = None,
    ) -> "aws_sdk_iotthingsgraph.types.upload_entity_definitions_response.UploadEntityDefinitionsResponse":
        """<p>Asynchronously uploads one or more entity definitions to the user's namespace. The <code>document</code> parameter is required if <code>syncWithPublicNamespace</code> and <code>deleteExistingEntites</code> are false. If the <code>syncWithPublicNamespace</code> parameter is set to <code>true</code>, the user's namespace will synchronize with the latest version of the public namespace. If <code>deprecateExistingEntities</code> is set to true, all entities in the latest version will be deleted before the new <code>DefinitionDocument</code> is uploaded.</p> <p>When a user uploads entity definitions for the first time, the service creates a new namespace for the user. The new namespace tracks the public namespace. Currently users can have only one namespace. The namespace version increments whenever a user uploads entity definitions that are backwards-incompatible and whenever a user sets the <code>syncWithPublicNamespace</code> parameter or the <code>deprecateExistingEntities</code> parameter to <code>true</code>.</p> <p>The IDs for all of the entities should be in URN format. Each entity must be in the user's namespace. Users can't create entities in the public namespace, but entity definitions can refer to entities in the public namespace.</p> <p>Valid entities are <code>Device</code>, <code>DeviceModel</code>, <code>Service</code>, <code>Capability</code>, <code>State</code>, <code>Action</code>, <code>Event</code>, <code>Property</code>, <code>Mapping</code>, <code>Enum</code>. </p>

        Args:
            document: <p>The <code>DefinitionDocument</code> that defines the updated entities.</p>
            sync_with_public_namespace: <p>A Boolean that specifies whether to synchronize with the latest version of the public namespace. If set to <code>true</code>, the upload will create a new namespace version.</p>
            deprecate_existing_entities: <p>A Boolean that specifies whether to deprecate all entities in the latest version before uploading the new <code>DefinitionDocument</code>. If set to <code>true</code>, the upload will create a new namespace version.</p>

        Raises:
            aws_sdk_iotthingsgraph.errors.internal_failure_exception.InternalFailureException: <p></p>
            aws_sdk_iotthingsgraph.errors.invalid_request_exception.InvalidRequestException: <p></p>
            aws_sdk_iotthingsgraph.errors.throttling_exception.ThrottlingException: <p></p>
            aws_sdk_iotthingsgraph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotthingsgraph.types.upload_entity_definitions_request.UploadEntityDefinitionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotthingsgraph.types.upload_entity_definitions_response.UploadEntityDefinitionsResponse"
        ]:
            import aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.upload_entity_definitions

            output, http_response = (
                aws_sdk_iotthingsgraph._operations.iot_things_graph_front_end_service.upload_entity_definitions.upload_entity_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotthingsgraph.types.upload_entity_definitions_request.UploadEntityDefinitionsRequest = {}  # type: ignore[typeddict-item]
        if document is not None:
            input_["document"] = document
        if sync_with_public_namespace is not None:
            input_["sync_with_public_namespace"] = sync_with_public_namespace
        if deprecate_existing_entities is not None:
            input_["deprecate_existing_entities"] = deprecate_existing_entities

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
