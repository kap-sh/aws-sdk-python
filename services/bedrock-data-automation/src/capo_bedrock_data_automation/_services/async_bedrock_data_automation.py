"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AmazonBedrockKeystoneBuildTimeService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bedrock_data_automation._auth._signers
import capo_bedrock_data_automation._auth._sigv4
from capo_bedrock_data_automation._auth._identity import Credentials
from capo_bedrock_data_automation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_data_automation._auth._zapros_handler import AuthMiddleware
from capo_bedrock_data_automation._pagination import resolve_path as _resolve_path
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.blueprint_optimization_job_resource import (
    AsyncBlueprintOptimizationJobResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.blueprint_resource import (
    AsyncBlueprintResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_library_ingestion_job_resource import (
    AsyncDataAutomationLibraryIngestionJobResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_library_resource import (
    AsyncDataAutomationLibraryResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_project_resource import (
    AsyncDataAutomationProjectResource,
)
from capo_bedrock_data_automation._services._aws_config import aaws_config
from capo_bedrock_data_automation._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.copy_blueprint_stage_request
    import capo_bedrock_data_automation.types.copy_blueprint_stage_response
    import capo_bedrock_data_automation.types.create_blueprint_version_request
    import capo_bedrock_data_automation.types.create_blueprint_version_response
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary
    import capo_bedrock_data_automation.types.entity_id
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.get_data_automation_library_entity_request
    import capo_bedrock_data_automation.types.get_data_automation_library_entity_response
    import capo_bedrock_data_automation.types.list_data_automation_library_entities_request
    import capo_bedrock_data_automation.types.list_data_automation_library_entities_response
    import capo_bedrock_data_automation.types.list_tags_for_resource_request
    import capo_bedrock_data_automation.types.list_tags_for_resource_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.tag_key_list
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.tag_resource_request
    import capo_bedrock_data_automation.types.tag_resource_response
    import capo_bedrock_data_automation.types.taggable_resource_arn
    import capo_bedrock_data_automation.types.untag_resource_request
    import capo_bedrock_data_automation.types.untag_resource_response


class AsyncBedrockDataAutomationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBedrockDataAutomationClient:
    """A client for the ``BedrockDataAutomation`` service.

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
        self._config = AsyncBedrockDataAutomationClientConfig(
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

        # resources
        self.blueprint_optimization_job_resource = (
            AsyncBlueprintOptimizationJobResource(self)
        )
        self.blueprint_resource = AsyncBlueprintResource(self)
        self.data_automation_library_ingestion_job_resource = (
            AsyncDataAutomationLibraryIngestionJobResource(self)
        )
        self.data_automation_library_resource = AsyncDataAutomationLibraryResource(self)
        self.data_automation_project_resource = AsyncDataAutomationProjectResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockDataAutomationClientConfig = config_overrides or {}
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

    async def copy_blueprint_stage(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        source_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage",
        target_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.copy_blueprint_stage_response.CopyBlueprintStageResponse":
        """Copies a Blueprint from one stage to another

        Args:
            blueprint_arn: Blueprint to be copied
            source_stage: Source stage to copy from
            target_stage: Target stage to copy to
            client_token: Client token for idempotency

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.copy_blueprint_stage_request.CopyBlueprintStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.copy_blueprint_stage_response.CopyBlueprintStageResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.copy_blueprint_stage

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.copy_blueprint_stage.async_copy_blueprint_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.copy_blueprint_stage_request.CopyBlueprintStageRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        input_["source_stage"] = source_stage
        input_["target_stage"] = target_stage
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_blueprint_version(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.create_blueprint_version_response.CreateBlueprintVersionResponse":
        """Creates a new version of an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_blueprint_version_request.CreateBlueprintVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_blueprint_version_response.CreateBlueprintVersionResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint_version

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint_version.async_create_blueprint_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.create_blueprint_version_request.CreateBlueprintVersionRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_automation_library_entity(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        entity_id: "capo_bedrock_data_automation.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_entity_response.GetDataAutomationLibraryEntityResponse":
        """Gets an existing entity based on entity type from the library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            entity_type: The entity type for which the entity is requested
            entity_id: Unique identifier for the entity

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_entity_request.GetDataAutomationLibraryEntityRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_entity_response.GetDataAutomationLibraryEntityResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_entity

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_entity.async_get_data_automation_library_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_data_automation_library_entity_request.GetDataAutomationLibraryEntityRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        input_["entity_type"] = entity_type
        input_["entity_id"] = entity_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_data_automation_library_entities(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_library_entities_response.ListDataAutomationLibraryEntitiesResponse":
        """Lists all stored entities in the library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            entity_type: The entity type for which the entity list is requested
            next_token: Pagination token for retrieving the next set of results

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_library_entities_request.ListDataAutomationLibraryEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_library_entities_response.ListDataAutomationLibraryEntitiesResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_entities

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_entities.async_list_data_automation_library_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_data_automation_library_entities_request.ListDataAutomationLibraryEntitiesRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        input_["entity_type"] = entity_type
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

    async def iter_list_data_automation_library_entities(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.data_automation_library_entity_summary.DataAutomationLibraryEntitySummary]":
        _token = next_token
        while True:
            _response = await self.list_data_automation_library_entities(
                library_arn,
                entity_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_bedrock_data_automation.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.tag_resource_response.TagResourceResponse":
        """Tag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_bedrock_data_automation.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.untag_resource_response.UntagResourceResponse":
        """Untag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
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
