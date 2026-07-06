"""Generated from Smithy shape ``com.amazonaws.osis#AmazonOpenSearchIngestionService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_osis._auth._signers
import aws_sdk_osis._auth._sigv4
from aws_sdk_osis._auth._identity import Credentials
from aws_sdk_osis._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_osis._auth._zapros_handler import AuthMiddleware
from aws_sdk_osis._pagination import resolve_path as _resolve_path
from aws_sdk_osis._services._aws_config import aaws_config
from aws_sdk_osis._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_osis.types.blueprint_format
    import aws_sdk_osis.types.buffer_options
    import aws_sdk_osis.types.create_pipeline_endpoint_request
    import aws_sdk_osis.types.create_pipeline_endpoint_response
    import aws_sdk_osis.types.create_pipeline_request
    import aws_sdk_osis.types.create_pipeline_response
    import aws_sdk_osis.types.delete_pipeline_endpoint_request
    import aws_sdk_osis.types.delete_pipeline_endpoint_response
    import aws_sdk_osis.types.delete_pipeline_request
    import aws_sdk_osis.types.delete_pipeline_response
    import aws_sdk_osis.types.delete_resource_policy_request
    import aws_sdk_osis.types.delete_resource_policy_response
    import aws_sdk_osis.types.encryption_at_rest_options
    import aws_sdk_osis.types.get_pipeline_blueprint_request
    import aws_sdk_osis.types.get_pipeline_blueprint_response
    import aws_sdk_osis.types.get_pipeline_change_progress_request
    import aws_sdk_osis.types.get_pipeline_change_progress_response
    import aws_sdk_osis.types.get_pipeline_request
    import aws_sdk_osis.types.get_pipeline_response
    import aws_sdk_osis.types.get_resource_policy_request
    import aws_sdk_osis.types.get_resource_policy_response
    import aws_sdk_osis.types.list_pipeline_blueprints_request
    import aws_sdk_osis.types.list_pipeline_blueprints_response
    import aws_sdk_osis.types.list_pipeline_endpoint_connections_request
    import aws_sdk_osis.types.list_pipeline_endpoint_connections_response
    import aws_sdk_osis.types.list_pipeline_endpoints_request
    import aws_sdk_osis.types.list_pipeline_endpoints_response
    import aws_sdk_osis.types.list_pipelines_request
    import aws_sdk_osis.types.list_pipelines_response
    import aws_sdk_osis.types.list_tags_for_resource_request
    import aws_sdk_osis.types.list_tags_for_resource_response
    import aws_sdk_osis.types.log_publishing_options
    import aws_sdk_osis.types.max_results
    import aws_sdk_osis.types.next_token
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.pipeline_configuration_body
    import aws_sdk_osis.types.pipeline_endpoint
    import aws_sdk_osis.types.pipeline_endpoint_connection
    import aws_sdk_osis.types.pipeline_endpoint_id
    import aws_sdk_osis.types.pipeline_endpoint_ids_list
    import aws_sdk_osis.types.pipeline_endpoint_vpc_options
    import aws_sdk_osis.types.pipeline_name
    import aws_sdk_osis.types.pipeline_role_arn
    import aws_sdk_osis.types.pipeline_units
    import aws_sdk_osis.types.put_resource_policy_request
    import aws_sdk_osis.types.put_resource_policy_response
    import aws_sdk_osis.types.resource_policy
    import aws_sdk_osis.types.revoke_pipeline_endpoint_connections_request
    import aws_sdk_osis.types.revoke_pipeline_endpoint_connections_response
    import aws_sdk_osis.types.start_pipeline_request
    import aws_sdk_osis.types.start_pipeline_response
    import aws_sdk_osis.types.stop_pipeline_request
    import aws_sdk_osis.types.stop_pipeline_response
    import aws_sdk_osis.types.string
    import aws_sdk_osis.types.string_list
    import aws_sdk_osis.types.tag_list
    import aws_sdk_osis.types.tag_resource_request
    import aws_sdk_osis.types.tag_resource_response
    import aws_sdk_osis.types.untag_resource_request
    import aws_sdk_osis.types.untag_resource_response
    import aws_sdk_osis.types.update_pipeline_request
    import aws_sdk_osis.types.update_pipeline_response
    import aws_sdk_osis.types.validate_pipeline_request
    import aws_sdk_osis.types.validate_pipeline_response
    import aws_sdk_osis.types.vpc_options


class AsyncOSISClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncOSISClient:
    """A client for the ``OSIS`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncOSISClientConfig(
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
        self, config_overrides: Optional[AsyncOSISClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOSISClientConfig = config_overrides or {}
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

    async def create_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        min_units: "aws_sdk_osis.types.pipeline_units.PipelineUnits",
        max_units: "aws_sdk_osis.types.pipeline_units.PipelineUnits",
        pipeline_configuration_body: "aws_sdk_osis.types.pipeline_configuration_body.PipelineConfigurationBody",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        log_publishing_options: Optional[
            "aws_sdk_osis.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        vpc_options: Optional["aws_sdk_osis.types.vpc_options.VpcOptions"] = None,
        buffer_options: Optional[
            "aws_sdk_osis.types.buffer_options.BufferOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        tags: Optional["aws_sdk_osis.types.tag_list.TagList"] = None,
        pipeline_role_arn: Optional[
            "aws_sdk_osis.types.pipeline_role_arn.PipelineRoleArn"
        ] = None,
    ) -> "aws_sdk_osis.types.create_pipeline_response.CreatePipelineResponse":
        r"""<p>Creates an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html\">Creating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region.</p>
            min_units: <p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            max_units: <p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            vpc_options: <p>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion creates the pipeline with a public endpoint.</p>
            buffer_options: <p>Key-value pairs to configure persistent buffering for the pipeline.</p>
            encryption_at_rest_options: <p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>
            tags: <p>List of tags to add to the pipeline upon creation.</p>
            pipeline_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>You attempted to create a resource that already exists.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.create_pipeline_request.CreatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.create_pipeline_response.CreatePipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.create_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.create_pipeline.async_create_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.create_pipeline_request.CreatePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name
        input_["min_units"] = min_units
        input_["max_units"] = max_units
        input_["pipeline_configuration_body"] = pipeline_configuration_body
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if buffer_options is not None:
            input_["buffer_options"] = buffer_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if tags is not None:
            input_["tags"] = tags
        if pipeline_role_arn is not None:
            input_["pipeline_role_arn"] = pipeline_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_pipeline_endpoint(
        self,
        pipeline_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        vpc_options: "aws_sdk_osis.types.pipeline_endpoint_vpc_options.PipelineEndpointVpcOptions",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.create_pipeline_endpoint_response.CreatePipelineEndpointResponse":
        """<p>Creates a VPC endpoint for an OpenSearch Ingestion pipeline. Pipeline endpoints allow you to ingest data from your VPC into pipelines that you have access to.</p>

        Args:
            pipeline_arn: <p>The Amazon Resource Name (ARN) of the pipeline to create the endpoint for.</p>
            vpc_options: <p>Container for the VPC configuration for the pipeline endpoint, including subnet IDs and security group IDs.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.create_pipeline_endpoint_request.CreatePipelineEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.create_pipeline_endpoint_response.CreatePipelineEndpointResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.create_pipeline_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.create_pipeline_endpoint.async_create_pipeline_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.create_pipeline_endpoint_request.CreatePipelineEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_arn"] = pipeline_arn
        input_["vpc_options"] = vpc_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.delete_pipeline_response.DeletePipelineResponse":
        r"""<p>Deletes an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/delete-pipeline.html\">Deleting Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to delete.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.delete_pipeline_request.DeletePipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.delete_pipeline_response.DeletePipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_pipeline.async_delete_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.delete_pipeline_request.DeletePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_pipeline_endpoint(
        self,
        endpoint_id: "aws_sdk_osis.types.pipeline_endpoint_id.PipelineEndpointId",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.delete_pipeline_endpoint_response.DeletePipelineEndpointResponse":
        """<p>Deletes a VPC endpoint for an OpenSearch Ingestion pipeline.</p>

        Args:
            endpoint_id: <p>The unique identifier of the pipeline endpoint to delete.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.delete_pipeline_endpoint_request.DeletePipelineEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.delete_pipeline_endpoint_response.DeletePipelineEndpointResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_pipeline_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_pipeline_endpoint.async_delete_pipeline_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.delete_pipeline_endpoint_request.DeletePipelineEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource-based policy from an OpenSearch Ingestion resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to delete the policy.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.get_pipeline_response.GetPipelineResponse":
        """<p>Retrieves information about an OpenSearch Ingestion pipeline.</p>

        Args:
            pipeline_name: <p>The name of the pipeline.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.get_pipeline_request.GetPipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.get_pipeline_response.GetPipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline.async_get_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.get_pipeline_request.GetPipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pipeline_blueprint(
        self,
        blueprint_name: "aws_sdk_osis.types.string.String",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        format: Optional["aws_sdk_osis.types.blueprint_format.BlueprintFormat"] = None,
    ) -> "aws_sdk_osis.types.get_pipeline_blueprint_response.GetPipelineBlueprintResponse":
        r"""<p>Retrieves information about a specific blueprint for OpenSearch Ingestion. Blueprints are templates for the configuration needed for a <code>CreatePipeline</code> request. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint\">Using blueprints to create a pipeline</a>.</p>

        Args:
            blueprint_name: <p>The name of the blueprint to retrieve.</p>
            format: <p>The format format of the blueprint to retrieve.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.get_pipeline_blueprint_request.GetPipelineBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.get_pipeline_blueprint_response.GetPipelineBlueprintResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline_blueprint.async_get_pipeline_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.get_pipeline_blueprint_request.GetPipelineBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pipeline_change_progress(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.get_pipeline_change_progress_response.GetPipelineChangeProgressResponse":
        r"""<p>Returns progress information for the current change happening on an OpenSearch Ingestion pipeline. Currently, this operation only returns information when a pipeline is being created.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#get-pipeline-progress\">Tracking the status of pipeline creation</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.get_pipeline_change_progress_request.GetPipelineChangeProgressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.get_pipeline_change_progress_response.GetPipelineChangeProgressResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline_change_progress

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_pipeline_change_progress.async_get_pipeline_change_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.get_pipeline_change_progress_request.GetPipelineChangeProgressRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to an OpenSearch Ingestion resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve the policy.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_pipeline_blueprints(
        self, *, config_overrides: Optional[AsyncOSISClientConfig] = None
    ) -> "aws_sdk_osis.types.list_pipeline_blueprints_response.ListPipelineBlueprintsResponse":
        r"""<p>Retrieves a list of all available blueprints for Data Prepper. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint\">Using blueprints to create a pipeline</a>.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>An invalid pagination token provided in the request.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.list_pipeline_blueprints_request.ListPipelineBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.list_pipeline_blueprints_response.ListPipelineBlueprintsResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_blueprints

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_blueprints.async_list_pipeline_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.list_pipeline_blueprints_request.ListPipelineBlueprintsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_pipeline_endpoint_connections(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["aws_sdk_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_osis.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_osis.types.list_pipeline_endpoint_connections_response.ListPipelineEndpointConnectionsResponse":
        """<p>Lists the pipeline endpoints connected to pipelines in your account.</p>

        Args:
            max_results: <p>The maximum number of pipeline endpoint connections to return in the response.</p>
            next_token: <p>If your initial <code>ListPipelineEndpointConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelineEndpointConnections</code> operations, which returns results in the next page.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.list_pipeline_endpoint_connections_request.ListPipelineEndpointConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.list_pipeline_endpoint_connections_response.ListPipelineEndpointConnectionsResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoint_connections

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoint_connections.async_list_pipeline_endpoint_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.list_pipeline_endpoint_connections_request.ListPipelineEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_pipeline_endpoint_connections(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["aws_sdk_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_osis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_osis.types.pipeline_endpoint_connection.PipelineEndpointConnection]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_endpoint_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_endpoint_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipeline_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["aws_sdk_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_osis.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_osis.types.list_pipeline_endpoints_response.ListPipelineEndpointsResponse":
        """<p>Lists all pipeline endpoints in your account.</p>

        Args:
            max_results: <p>The maximum number of pipeline endpoints to return in the response.</p>
            next_token: <p>If your initial <code>ListPipelineEndpoints</code> operation returns a <code>NextToken</code>, you can include the returned <code>NextToken</code> in subsequent <code>ListPipelineEndpoints</code> operations, which returns results in the next page.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.list_pipeline_endpoints_request.ListPipelineEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.list_pipeline_endpoints_response.ListPipelineEndpointsResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoints.async_list_pipeline_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.list_pipeline_endpoints_request.ListPipelineEndpointsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_pipeline_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["aws_sdk_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_osis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_osis.types.pipeline_endpoint.PipelineEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["aws_sdk_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_osis.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_osis.types.list_pipelines_response.ListPipelinesResponse":
        r"""<p>Lists all OpenSearch Ingestion pipelines in the current Amazon Web Services account and Region. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/list-pipeline.html\">Viewing Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListPipelines</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelines</code> operations, which returns results in the next page.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>An invalid pagination token provided in the request.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.list_pipelines_request.ListPipelinesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.list_pipelines_response.ListPipelinesResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipelines

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_pipelines.async_list_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.list_pipelines_request.ListPipelinesRequest = {}  # type: ignore[typeddict-item]
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

    async def list_tags_for_resource(
        self,
        arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> (
        "aws_sdk_osis.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        r"""<p>Lists all resource tags associated with an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html\">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to retrieve tags for.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        policy: "aws_sdk_osis.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based policy to an OpenSearch Ingestion resource. Resource-based policies grant permissions to principals to perform actions on the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to attach the policy to.</p>
            policy: <p>The resource-based policy document in JSON format.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def revoke_pipeline_endpoint_connections(
        self,
        pipeline_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        endpoint_ids: "aws_sdk_osis.types.pipeline_endpoint_ids_list.PipelineEndpointIdsList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.revoke_pipeline_endpoint_connections_response.RevokePipelineEndpointConnectionsResponse":
        """<p>Revokes pipeline endpoints from specified endpoint IDs.</p>

        Args:
            pipeline_arn: <p>The Amazon Resource Name (ARN) of the pipeline from which to revoke endpoint connections.</p>
            endpoint_ids: <p>A list of endpoint IDs for which to revoke access to the pipeline.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.revoke_pipeline_endpoint_connections_request.RevokePipelineEndpointConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.revoke_pipeline_endpoint_connections_response.RevokePipelineEndpointConnectionsResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.revoke_pipeline_endpoint_connections

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.revoke_pipeline_endpoint_connections.async_revoke_pipeline_endpoint_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.revoke_pipeline_endpoint_connections_request.RevokePipelineEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_arn"] = pipeline_arn
        input_["endpoint_ids"] = endpoint_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.start_pipeline_response.StartPipelineResponse":
        r"""<p>Starts an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html#pipeline--start\">Starting an OpenSearch Ingestion pipeline</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to start.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.start_pipeline_request.StartPipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.start_pipeline_response.StartPipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.start_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.start_pipeline.async_start_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.start_pipeline_request.StartPipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.stop_pipeline_response.StopPipelineResponse":
        r"""<p>Stops an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html#pipeline--stop\">Stopping an OpenSearch Ingestion pipeline</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to stop.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.stop_pipeline_request.StopPipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.stop_pipeline_response.StopPipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.stop_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.stop_pipeline.async_stop_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.stop_pipeline_request.StopPipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        tags: "aws_sdk_osis.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.tag_resource_response.TagResourceResponse":
        r"""<p>Tags an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html\">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to tag.</p>
            tags: <p>The list of key-value tags to add to the pipeline.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn",
        tag_keys: "aws_sdk_osis.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes one or more tags from an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html\">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to remove tags from.</p>
            tag_keys: <p>The tag keys to remove.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pipeline(
        self,
        pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        min_units: Optional["aws_sdk_osis.types.pipeline_units.PipelineUnits"] = None,
        max_units: Optional["aws_sdk_osis.types.pipeline_units.PipelineUnits"] = None,
        pipeline_configuration_body: Optional[
            "aws_sdk_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
        ] = None,
        log_publishing_options: Optional[
            "aws_sdk_osis.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        buffer_options: Optional[
            "aws_sdk_osis.types.buffer_options.BufferOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        pipeline_role_arn: Optional[
            "aws_sdk_osis.types.pipeline_role_arn.PipelineRoleArn"
        ] = None,
    ) -> "aws_sdk_osis.types.update_pipeline_response.UpdatePipelineResponse":
        r"""<p>Updates an OpenSearch Ingestion pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/update-pipeline.html\">Updating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to update.</p>
            min_units: <p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            max_units: <p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs)</p>
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            buffer_options: <p>Key-value pairs to configure persistent buffering for the pipeline.</p>
            encryption_at_rest_options: <p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>
            pipeline_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.update_pipeline_request.UpdatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.update_pipeline_response.UpdatePipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.update_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.update_pipeline.async_update_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.update_pipeline_request.UpdatePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_name"] = pipeline_name
        if min_units is not None:
            input_["min_units"] = min_units
        if max_units is not None:
            input_["max_units"] = max_units
        if pipeline_configuration_body is not None:
            input_["pipeline_configuration_body"] = pipeline_configuration_body
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if buffer_options is not None:
            input_["buffer_options"] = buffer_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if pipeline_role_arn is not None:
            input_["pipeline_role_arn"] = pipeline_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def validate_pipeline(
        self,
        pipeline_configuration_body: "aws_sdk_osis.types.pipeline_configuration_body.PipelineConfigurationBody",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "aws_sdk_osis.types.validate_pipeline_response.ValidatePipelineResponse":
        r"""<p>Checks whether an OpenSearch Ingestion pipeline configuration is valid prior to creation. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html\">Creating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>

        Raises:
            aws_sdk_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            aws_sdk_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            aws_sdk_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            aws_sdk_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            aws_sdk_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_osis.types.validate_pipeline_request.ValidatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_osis.types.validate_pipeline_response.ValidatePipelineResponse"
        ]:
            import aws_sdk_osis._operations.amazon_open_search_ingestion_service.validate_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_osis._operations.amazon_open_search_ingestion_service.validate_pipeline.async_validate_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_osis.types.validate_pipeline_request.ValidatePipelineRequest = {}  # type: ignore[typeddict-item]
        input_["pipeline_configuration_body"] = pipeline_configuration_body

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
