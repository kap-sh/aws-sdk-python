"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#AWSIoTTwinMaker``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_iottwinmaker._auth._signers
import aws_sdk_iottwinmaker._auth._sigv4
from aws_sdk_iottwinmaker._auth._identity import Credentials
from aws_sdk_iottwinmaker._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_iottwinmaker._auth._zapros_handler import AuthMiddleware
from aws_sdk_iottwinmaker._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.batch_put_property_values_request
    import aws_sdk_iottwinmaker.types.batch_put_property_values_response
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_request
    import aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_response
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.component_type_name
    import aws_sdk_iottwinmaker.types.component_updates_map_request
    import aws_sdk_iottwinmaker.types.components_map_request
    import aws_sdk_iottwinmaker.types.composite_component_types_request
    import aws_sdk_iottwinmaker.types.composite_component_updates_map_request
    import aws_sdk_iottwinmaker.types.composite_components_map_request
    import aws_sdk_iottwinmaker.types.create_component_type_request
    import aws_sdk_iottwinmaker.types.create_component_type_response
    import aws_sdk_iottwinmaker.types.create_entity_request
    import aws_sdk_iottwinmaker.types.create_entity_response
    import aws_sdk_iottwinmaker.types.create_metadata_transfer_job_request
    import aws_sdk_iottwinmaker.types.create_metadata_transfer_job_response
    import aws_sdk_iottwinmaker.types.create_scene_request
    import aws_sdk_iottwinmaker.types.create_scene_response
    import aws_sdk_iottwinmaker.types.create_sync_job_request
    import aws_sdk_iottwinmaker.types.create_sync_job_response
    import aws_sdk_iottwinmaker.types.create_workspace_request
    import aws_sdk_iottwinmaker.types.create_workspace_response
    import aws_sdk_iottwinmaker.types.delete_component_type_request
    import aws_sdk_iottwinmaker.types.delete_component_type_response
    import aws_sdk_iottwinmaker.types.delete_entity_request
    import aws_sdk_iottwinmaker.types.delete_entity_response
    import aws_sdk_iottwinmaker.types.delete_scene_request
    import aws_sdk_iottwinmaker.types.delete_scene_response
    import aws_sdk_iottwinmaker.types.delete_sync_job_request
    import aws_sdk_iottwinmaker.types.delete_sync_job_response
    import aws_sdk_iottwinmaker.types.delete_workspace_request
    import aws_sdk_iottwinmaker.types.delete_workspace_response
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.destination_configuration
    import aws_sdk_iottwinmaker.types.destination_type
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.entity_name
    import aws_sdk_iottwinmaker.types.entries
    import aws_sdk_iottwinmaker.types.execute_query_request
    import aws_sdk_iottwinmaker.types.execute_query_response
    import aws_sdk_iottwinmaker.types.extends_from
    import aws_sdk_iottwinmaker.types.functions_request
    import aws_sdk_iottwinmaker.types.get_component_type_request
    import aws_sdk_iottwinmaker.types.get_component_type_response
    import aws_sdk_iottwinmaker.types.get_entity_request
    import aws_sdk_iottwinmaker.types.get_entity_response
    import aws_sdk_iottwinmaker.types.get_metadata_transfer_job_request
    import aws_sdk_iottwinmaker.types.get_metadata_transfer_job_response
    import aws_sdk_iottwinmaker.types.get_pricing_plan_request
    import aws_sdk_iottwinmaker.types.get_pricing_plan_response
    import aws_sdk_iottwinmaker.types.get_property_value_history_request
    import aws_sdk_iottwinmaker.types.get_property_value_history_response
    import aws_sdk_iottwinmaker.types.get_property_value_request
    import aws_sdk_iottwinmaker.types.get_property_value_response
    import aws_sdk_iottwinmaker.types.get_scene_request
    import aws_sdk_iottwinmaker.types.get_scene_response
    import aws_sdk_iottwinmaker.types.get_sync_job_request
    import aws_sdk_iottwinmaker.types.get_sync_job_response
    import aws_sdk_iottwinmaker.types.get_workspace_request
    import aws_sdk_iottwinmaker.types.get_workspace_response
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.id_or_arn
    import aws_sdk_iottwinmaker.types.interpolation_parameters
    import aws_sdk_iottwinmaker.types.list_component_types_filters
    import aws_sdk_iottwinmaker.types.list_component_types_request
    import aws_sdk_iottwinmaker.types.list_component_types_response
    import aws_sdk_iottwinmaker.types.list_components_request
    import aws_sdk_iottwinmaker.types.list_components_response
    import aws_sdk_iottwinmaker.types.list_entities_filters
    import aws_sdk_iottwinmaker.types.list_entities_request
    import aws_sdk_iottwinmaker.types.list_entities_response
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_request
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_response
    import aws_sdk_iottwinmaker.types.list_properties_request
    import aws_sdk_iottwinmaker.types.list_properties_response
    import aws_sdk_iottwinmaker.types.list_scenes_request
    import aws_sdk_iottwinmaker.types.list_scenes_response
    import aws_sdk_iottwinmaker.types.list_sync_jobs_request
    import aws_sdk_iottwinmaker.types.list_sync_jobs_response
    import aws_sdk_iottwinmaker.types.list_sync_resources_request
    import aws_sdk_iottwinmaker.types.list_sync_resources_response
    import aws_sdk_iottwinmaker.types.list_tags_for_resource_request
    import aws_sdk_iottwinmaker.types.list_tags_for_resource_response
    import aws_sdk_iottwinmaker.types.list_workspaces_request
    import aws_sdk_iottwinmaker.types.list_workspaces_response
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.order_by_time
    import aws_sdk_iottwinmaker.types.parent_entity_id
    import aws_sdk_iottwinmaker.types.parent_entity_update_request
    import aws_sdk_iottwinmaker.types.pricing_bundles
    import aws_sdk_iottwinmaker.types.pricing_mode
    import aws_sdk_iottwinmaker.types.property_definitions_request
    import aws_sdk_iottwinmaker.types.property_filters
    import aws_sdk_iottwinmaker.types.property_groups_request
    import aws_sdk_iottwinmaker.types.query_service_max_results
    import aws_sdk_iottwinmaker.types.query_statement
    import aws_sdk_iottwinmaker.types.role_arn
    import aws_sdk_iottwinmaker.types.s3_location
    import aws_sdk_iottwinmaker.types.s3_url
    import aws_sdk_iottwinmaker.types.scene_capabilities
    import aws_sdk_iottwinmaker.types.scene_metadata_map
    import aws_sdk_iottwinmaker.types.selected_property_list
    import aws_sdk_iottwinmaker.types.source_configurations
    import aws_sdk_iottwinmaker.types.source_type
    import aws_sdk_iottwinmaker.types.sync_resource_filters
    import aws_sdk_iottwinmaker.types.sync_source
    import aws_sdk_iottwinmaker.types.tabular_conditions
    import aws_sdk_iottwinmaker.types.tag_key_list
    import aws_sdk_iottwinmaker.types.tag_map
    import aws_sdk_iottwinmaker.types.tag_resource_request
    import aws_sdk_iottwinmaker.types.tag_resource_response
    import aws_sdk_iottwinmaker.types.time
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn
    import aws_sdk_iottwinmaker.types.untag_resource_request
    import aws_sdk_iottwinmaker.types.untag_resource_response
    import aws_sdk_iottwinmaker.types.update_component_type_request
    import aws_sdk_iottwinmaker.types.update_component_type_response
    import aws_sdk_iottwinmaker.types.update_entity_request
    import aws_sdk_iottwinmaker.types.update_entity_response
    import aws_sdk_iottwinmaker.types.update_pricing_plan_request
    import aws_sdk_iottwinmaker.types.update_pricing_plan_response
    import aws_sdk_iottwinmaker.types.update_scene_request
    import aws_sdk_iottwinmaker.types.update_scene_response
    import aws_sdk_iottwinmaker.types.update_workspace_request
    import aws_sdk_iottwinmaker.types.update_workspace_response


class AsyncIoTTwinMakerClientConfig(TypedDict, total=False):
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


class AsyncIoTTwinMakerClient:
    """A client for the ``IoTTwinMaker`` service.

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
        self._config = AsyncIoTTwinMakerClientConfig(
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
        self, config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTTwinMakerClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def batch_put_property_values(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entries: "aws_sdk_iottwinmaker.types.entries.Entries",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.batch_put_property_values_response.BatchPutPropertyValuesResponse":
        """<p>Sets values for multiple time series properties.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the properties to set.</p>
            entries: <p>An object that maps strings to the property value entries to set. Each string in the mapping must be unique to this object.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.batch_put_property_values_request.BatchPutPropertyValuesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.batch_put_property_values_response.BatchPutPropertyValuesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.batch_put_property_values

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.batch_put_property_values.async_batch_put_property_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.batch_put_property_values_request.BatchPutPropertyValuesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_metadata_transfer_job(
        self,
        metadata_transfer_job_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_response.CancelMetadataTransferJobResponse":
        """<p>Cancels the metadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_request.CancelMetadataTransferJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_response.CancelMetadataTransferJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.cancel_metadata_transfer_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.cancel_metadata_transfer_job.async_cancel_metadata_transfer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.cancel_metadata_transfer_job_request.CancelMetadataTransferJobRequest = {}  # type: ignore[typeddict-item]
        input_["metadata_transfer_job_id"] = metadata_transfer_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_component_type(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        is_singleton: Optional["aws_sdk_iottwinmaker.types.boolean.Boolean"] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        property_definitions: Optional[
            "aws_sdk_iottwinmaker.types.property_definitions_request.PropertyDefinitionsRequest"
        ] = None,
        extends_from: Optional[
            "aws_sdk_iottwinmaker.types.extends_from.ExtendsFrom"
        ] = None,
        functions: Optional[
            "aws_sdk_iottwinmaker.types.functions_request.FunctionsRequest"
        ] = None,
        tags: Optional["aws_sdk_iottwinmaker.types.tag_map.TagMap"] = None,
        property_groups: Optional[
            "aws_sdk_iottwinmaker.types.property_groups_request.PropertyGroupsRequest"
        ] = None,
        component_type_name: Optional[
            "aws_sdk_iottwinmaker.types.component_type_name.ComponentTypeName"
        ] = None,
        composite_component_types: Optional[
            "aws_sdk_iottwinmaker.types.composite_component_types_request.CompositeComponentTypesRequest"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_component_type_response.CreateComponentTypeResponse":
        """<p>Creates a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            is_singleton: <p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>
            component_type_id: <p>The ID of the component type.</p>
            description: <p>The description of the component type.</p>
            property_definitions: <p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>
            extends_from: <p>Specifies the parent component type to extend.</p>
            functions: <p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>
            tags: <p>Metadata that you can use to manage the component type.</p>
            property_groups: <p/>
            component_type_name: <p>A friendly name for the component type.</p>
            composite_component_types: <p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_component_type_request.CreateComponentTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_component_type_response.CreateComponentTypeResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_component_type

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_component_type.async_create_component_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_component_type_request.CreateComponentTypeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if is_singleton is not None:
            input_["is_singleton"] = is_singleton
        input_["component_type_id"] = component_type_id
        if description is not None:
            input_["description"] = description
        if property_definitions is not None:
            input_["property_definitions"] = property_definitions
        if extends_from is not None:
            input_["extends_from"] = extends_from
        if functions is not None:
            input_["functions"] = functions
        if tags is not None:
            input_["tags"] = tags
        if property_groups is not None:
            input_["property_groups"] = property_groups
        if component_type_name is not None:
            input_["component_type_name"] = component_type_name
        if composite_component_types is not None:
            input_["composite_component_types"] = composite_component_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_entity(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_name: "aws_sdk_iottwinmaker.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        entity_id: Optional["aws_sdk_iottwinmaker.types.entity_id.EntityId"] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        components: Optional[
            "aws_sdk_iottwinmaker.types.components_map_request.ComponentsMapRequest"
        ] = None,
        composite_components: Optional[
            "aws_sdk_iottwinmaker.types.composite_components_map_request.CompositeComponentsMapRequest"
        ] = None,
        parent_entity_id: Optional[
            "aws_sdk_iottwinmaker.types.parent_entity_id.ParentEntityId"
        ] = None,
        tags: Optional["aws_sdk_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_entity_response.CreateEntityResponse":
        """<p>Creates an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity.</p>
            entity_id: <p>The ID of the entity.</p>
            entity_name: <p>The name of the entity.</p>
            description: <p>The description of the entity.</p>
            components: <p>An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.</p>
            composite_components: <p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>
            parent_entity_id: <p>The ID of the entity's parent entity.</p>
            tags: <p>Metadata that you can use to manage the entity.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_entity_request.CreateEntityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_entity_response.CreateEntityResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_entity

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_entity.async_create_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_entity_request.CreateEntityRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if entity_id is not None:
            input_["entity_id"] = entity_id
        input_["entity_name"] = entity_name
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if composite_components is not None:
            input_["composite_components"] = composite_components
        if parent_entity_id is not None:
            input_["parent_entity_id"] = parent_entity_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_metadata_transfer_job(
        self,
        sources: "aws_sdk_iottwinmaker.types.source_configurations.SourceConfigurations",
        destination: "aws_sdk_iottwinmaker.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        metadata_transfer_job_id: Optional["aws_sdk_iottwinmaker.types.id.Id"] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_metadata_transfer_job_response.CreateMetadataTransferJobResponse":
        """<p>Creates a new metadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>
            description: <p>The metadata transfer job description.</p>
            sources: <p>The metadata transfer job sources.</p>
            destination: <p>The metadata transfer job destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_metadata_transfer_job_request.CreateMetadataTransferJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_metadata_transfer_job_response.CreateMetadataTransferJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_metadata_transfer_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_metadata_transfer_job.async_create_metadata_transfer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_metadata_transfer_job_request.CreateMetadataTransferJobRequest = {}  # type: ignore[typeddict-item]
        if metadata_transfer_job_id is not None:
            input_["metadata_transfer_job_id"] = metadata_transfer_job_id
        if description is not None:
            input_["description"] = description
        input_["sources"] = sources
        input_["destination"] = destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_scene(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        scene_id: "aws_sdk_iottwinmaker.types.id.Id",
        content_location: "aws_sdk_iottwinmaker.types.s3_url.S3Url",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        capabilities: Optional[
            "aws_sdk_iottwinmaker.types.scene_capabilities.SceneCapabilities"
        ] = None,
        tags: Optional["aws_sdk_iottwinmaker.types.tag_map.TagMap"] = None,
        scene_metadata: Optional[
            "aws_sdk_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_scene_response.CreateSceneResponse":
        """<p>Creates a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>
            content_location: <p>The relative path that specifies the location of the content definition file.</p>
            description: <p>The description for this scene.</p>
            capabilities: <p>A list of capabilities that the scene uses to render itself.</p>
            tags: <p>Metadata that you can use to manage the scene.</p>
            scene_metadata: <p>The request metadata.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_scene_request.CreateSceneRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_scene_response.CreateSceneResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_scene

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_scene.async_create_scene(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_scene_request.CreateSceneRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["scene_id"] = scene_id
        input_["content_location"] = content_location
        if description is not None:
            input_["description"] = description
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if tags is not None:
            input_["tags"] = tags
        if scene_metadata is not None:
            input_["scene_metadata"] = scene_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_sync_job(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource",
        sync_role: "aws_sdk_iottwinmaker.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        tags: Optional["aws_sdk_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_sync_job_response.CreateSyncJobResponse":
        """<p>This action creates a SyncJob.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSoource is <code>SITEWISE </code>.</p> </note>
            sync_role: <p>The SyncJob IAM role. This IAM role is used by the SyncJob to read from the syncSource, and create, update, or delete the corresponding resources.</p>
            tags: <p>The SyncJob tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_sync_job_request.CreateSyncJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_sync_job_response.CreateSyncJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_sync_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_sync_job.async_create_sync_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_sync_job_request.CreateSyncJobRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["sync_source"] = sync_source
        input_["sync_role"] = sync_role
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_workspace(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        s3_location: Optional[
            "aws_sdk_iottwinmaker.types.s3_location.S3Location"
        ] = None,
        role: Optional["aws_sdk_iottwinmaker.types.role_arn.RoleArn"] = None,
        tags: Optional["aws_sdk_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iottwinmaker.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a workplace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            description: <p>The description of the workspace.</p>
            s3_location: <p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>
            role: <p>The ARN of the execution role associated with the workspace.</p>
            tags: <p>Metadata that you can use to manage the workspace</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.create_workspace.async_create_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.create_workspace_request.CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if description is not None:
            input_["description"] = description
        if s3_location is not None:
            input_["s3_location"] = s3_location
        if role is not None:
            input_["role"] = role
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_component_type(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.delete_component_type_response.DeleteComponentTypeResponse":
        """<p>Deletes a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            component_type_id: <p>The ID of the component type to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.delete_component_type_request.DeleteComponentTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.delete_component_type_response.DeleteComponentTypeResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_component_type

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_component_type.async_delete_component_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.delete_component_type_request.DeleteComponentTypeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["component_type_id"] = component_type_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_entity(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        is_recursive: Optional["aws_sdk_iottwinmaker.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_iottwinmaker.types.delete_entity_response.DeleteEntityResponse":
        """<p>Deletes an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity to delete.</p>
            entity_id: <p>The ID of the entity to delete.</p>
            is_recursive: <p>A Boolean value that specifies whether the operation deletes child entities.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.delete_entity_request.DeleteEntityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.delete_entity_response.DeleteEntityResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_entity

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_entity.async_delete_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.delete_entity_request.DeleteEntityRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["entity_id"] = entity_id
        if is_recursive is not None:
            input_["is_recursive"] = is_recursive

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_scene(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        scene_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.delete_scene_response.DeleteSceneResponse":
        """<p>Deletes a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            scene_id: <p>The ID of the scene to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.delete_scene_request.DeleteSceneRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.delete_scene_response.DeleteSceneResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_scene

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_scene.async_delete_scene(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.delete_scene_request.DeleteSceneRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["scene_id"] = scene_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_sync_job(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.delete_sync_job_response.DeleteSyncJobResponse":
        """<p>Delete the SyncJob.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.delete_sync_job_request.DeleteSyncJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.delete_sync_job_response.DeleteSyncJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_sync_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_sync_job.async_delete_sync_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.delete_sync_job_request.DeleteSyncJobRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["sync_source"] = sync_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_workspace(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.delete_workspace.async_delete_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.delete_workspace_request.DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def execute_query(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        query_statement: "aws_sdk_iottwinmaker.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.query_service_max_results.QueryServiceMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.execute_query_response.ExecuteQueryResponse":
        """<p>Run queries to access information from your knowledge graph of entities within individual workspaces.</p> <note> <p>The ExecuteQuery action only works with <a href=\"https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html\">Amazon Web Services Java SDK2</a>. ExecuteQuery will not work with any Amazon Web Services Java SDK version &lt; 2.x.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            query_statement: <p>The query statement.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.execute_query_request.ExecuteQueryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.execute_query_response.ExecuteQueryResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.execute_query

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.execute_query.async_execute_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.execute_query_request.ExecuteQueryRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["query_statement"] = query_statement
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

    async def get_component_type(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_component_type_response.GetComponentTypeResponse":
        """<p>Retrieves information about a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            component_type_id: <p>The ID of the component type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_component_type_request.GetComponentTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_component_type_response.GetComponentTypeResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_component_type

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_component_type.async_get_component_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_component_type_request.GetComponentTypeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["component_type_id"] = component_type_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_entity(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_entity_response.GetEntityResponse":
        """<p>Retrieves information about an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            entity_id: <p>The ID of the entity.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_entity_request.GetEntityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_entity_response.GetEntityResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_entity

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_entity.async_get_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_entity_request.GetEntityRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["entity_id"] = entity_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_metadata_transfer_job(
        self,
        metadata_transfer_job_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_metadata_transfer_job_response.GetMetadataTransferJobResponse":
        """<p>Gets a nmetadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_metadata_transfer_job_request.GetMetadataTransferJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_metadata_transfer_job_response.GetMetadataTransferJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_metadata_transfer_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_metadata_transfer_job.async_get_metadata_transfer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_metadata_transfer_job_request.GetMetadataTransferJobRequest = {}  # type: ignore[typeddict-item]
        input_["metadata_transfer_job_id"] = metadata_transfer_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pricing_plan(
        self, *, config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None
    ) -> "aws_sdk_iottwinmaker.types.get_pricing_plan_response.GetPricingPlanResponse":
        """<p>Gets the pricing plan.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_pricing_plan_request.GetPricingPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_pricing_plan_response.GetPricingPlanResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_pricing_plan

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_pricing_plan.async_get_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_pricing_plan_request.GetPricingPlanRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_property_value(
        self,
        selected_properties: "aws_sdk_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        component_name: Optional["aws_sdk_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        entity_id: Optional["aws_sdk_iottwinmaker.types.entity_id.EntityId"] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
        property_group_name: Optional["aws_sdk_iottwinmaker.types.name.Name"] = None,
        tabular_conditions: Optional[
            "aws_sdk_iottwinmaker.types.tabular_conditions.TabularConditions"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_property_value_response.GetPropertyValueResponse":
        """<p>Gets the property values for a component, component type, entity, or workspace.</p> <p>You must specify a value for either <code>componentName</code>, <code>componentTypeId</code>, <code>entityId</code>, or <code>workspaceId</code>.</p>

        Args:
            component_name: <p>The name of the component whose property values the operation returns.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            component_type_id: <p>The ID of the component type whose property values the operation returns.</p>
            entity_id: <p>The ID of the entity whose property values the operation returns.</p>
            selected_properties: <p>The properties whose values the operation returns.</p>
            workspace_id: <p>The ID of the workspace whose values the operation returns.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            property_group_name: <p>The property group name.</p>
            tabular_conditions: <p>The tabular conditions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_property_value_request.GetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_property_value_response.GetPropertyValueResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value.async_get_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_property_value_request.GetPropertyValueRequest = {}  # type: ignore[typeddict-item]
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        if component_type_id is not None:
            input_["component_type_id"] = component_type_id
        if entity_id is not None:
            input_["entity_id"] = entity_id
        input_["selected_properties"] = selected_properties
        input_["workspace_id"] = workspace_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if property_group_name is not None:
            input_["property_group_name"] = property_group_name
        if tabular_conditions is not None:
            input_["tabular_conditions"] = tabular_conditions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_property_value_history(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        selected_properties: "aws_sdk_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        entity_id: Optional["aws_sdk_iottwinmaker.types.entity_id.EntityId"] = None,
        component_name: Optional["aws_sdk_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        property_filters: Optional[
            "aws_sdk_iottwinmaker.types.property_filters.PropertyFilters"
        ] = None,
        start_date_time: Optional[
            "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
        ] = None,
        end_date_time: Optional[
            "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
        ] = None,
        interpolation: Optional[
            "aws_sdk_iottwinmaker.types.interpolation_parameters.InterpolationParameters"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        order_by_time: Optional[
            "aws_sdk_iottwinmaker.types.order_by_time.OrderByTime"
        ] = None,
        start_time: Optional["aws_sdk_iottwinmaker.types.time.Time"] = None,
        end_time: Optional["aws_sdk_iottwinmaker.types.time.Time"] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_property_value_history_response.GetPropertyValueHistoryResponse":
        """<p>Retrieves information about the history of a time series property value for a component, component type, entity, or workspace.</p> <p>You must specify a value for <code>workspaceId</code>. For entity-specific queries, specify values for <code>componentName</code> and <code>entityId</code>. For cross-entity quries, specify a value for <code>componentTypeId</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            entity_id: <p>The ID of the entity.</p>
            component_name: <p>The name of the component.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            component_type_id: <p>The ID of the component type.</p>
            selected_properties: <p>A list of properties whose value histories the request retrieves.</p>
            property_filters: <p>A list of objects that filter the property value history request.</p>
            start_date_time: <p>The date and time of the earliest property value to return.</p>
            end_date_time: <p>The date and time of the latest property value to return.</p>
            interpolation: <p>An object that specifies the interpolation type and the interval over which to interpolate data.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            order_by_time: <p>The time direction to use in the result order.</p>
            start_time: <p>The ISO8601 DateTime of the earliest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href=\"https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html\">PropertyValue</a>.</p>
            end_time: <p>The ISO8601 DateTime of the latest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href=\"https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html\">PropertyValue</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_property_value_history_request.GetPropertyValueHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_property_value_history_response.GetPropertyValueHistoryResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value_history

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value_history.async_get_property_value_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_property_value_history_request.GetPropertyValueHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if entity_id is not None:
            input_["entity_id"] = entity_id
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        if component_type_id is not None:
            input_["component_type_id"] = component_type_id
        input_["selected_properties"] = selected_properties
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if start_date_time is not None:
            input_["start_date_time"] = start_date_time
        if end_date_time is not None:
            input_["end_date_time"] = end_date_time
        if interpolation is not None:
            input_["interpolation"] = interpolation
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if order_by_time is not None:
            input_["order_by_time"] = order_by_time
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_scene(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        scene_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_scene_response.GetSceneResponse":
        """<p>Retrieves information about a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_scene_request.GetSceneRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_scene_response.GetSceneResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_scene

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_scene.async_get_scene(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_scene_request.GetSceneRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["scene_id"] = scene_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sync_job(
        self,
        sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        workspace_id: Optional["aws_sdk_iottwinmaker.types.id.Id"] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_sync_job_response.GetSyncJobResponse":
        """<p>Gets the SyncJob.</p>

        Args:
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>
            workspace_id: <p>The workspace ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_sync_job_request.GetSyncJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_sync_job_response.GetSyncJobResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_sync_job

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_sync_job.async_get_sync_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_sync_job_request.GetSyncJobRequest = {}  # type: ignore[typeddict-item]
        input_["sync_source"] = sync_source
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workspace(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id_or_arn.IdOrArn",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.get_workspace_response.GetWorkspaceResponse":
        """<p>Retrieves information about a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.get_workspace_request.GetWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.get_workspace_response.GetWorkspaceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.get_workspace.async_get_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.get_workspace_request.GetWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_components(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        component_path: Optional[
            "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_components_response.ListComponentsResponse":
        """<p>This API lists the components of an entity.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            entity_id: <p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            max_results: <p>The maximum number of results returned at one time. The default is 25.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_components_response.ListComponentsResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_components

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_components_request.ListComponentsRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["entity_id"] = entity_id
        if component_path is not None:
            input_["component_path"] = component_path
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

    async def list_component_types(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        filters: Optional[
            "aws_sdk_iottwinmaker.types.list_component_types_filters.ListComponentTypesFilters"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_component_types_response.ListComponentTypesResponse":
        """<p>Lists all component types in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            filters: <p>A list of objects that filter the request.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_component_types_request.ListComponentTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_component_types_response.ListComponentTypesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_component_types

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_component_types.async_list_component_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_component_types_request.ListComponentTypesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_entities(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        filters: Optional[
            "aws_sdk_iottwinmaker.types.list_entities_filters.ListEntitiesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_entities_response.ListEntitiesResponse":
        """<p>Lists all entities in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            filters: <p>A list of objects that filter the request.</p> <note> <p>Only one object is accepted as a valid input.</p> </note>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_entities_request.ListEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_entities_response.ListEntitiesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_entities

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_entities.async_list_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_entities_request.ListEntitiesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_metadata_transfer_jobs(
        self,
        source_type: "aws_sdk_iottwinmaker.types.source_type.SourceType",
        destination_type: "aws_sdk_iottwinmaker.types.destination_type.DestinationType",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        filters: Optional[
            "aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters.ListMetadataTransferJobsFilters"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_response.ListMetadataTransferJobsResponse":
        """<p>Lists the metadata transfer jobs.</p>

        Args:
            source_type: <p>The metadata transfer job's source type.</p>
            destination_type: <p>The metadata transfer job's destination type.</p>
            filters: <p>An object that filters metadata transfer jobs.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_request.ListMetadataTransferJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_response.ListMetadataTransferJobsResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_metadata_transfer_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_metadata_transfer_jobs.async_list_metadata_transfer_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_request.ListMetadataTransferJobsRequest = {}  # type: ignore[typeddict-item]
        input_["source_type"] = source_type
        input_["destination_type"] = destination_type
        if filters is not None:
            input_["filters"] = filters
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

    async def list_properties(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        component_name: Optional["aws_sdk_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_properties_response.ListPropertiesResponse":
        """<p>This API lists the properties of a component.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            component_name: <p>The name of the component whose properties are returned by the operation.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            entity_id: <p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>
            max_results: <p>The maximum number of results returned at one time. The default is 25.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_properties_request.ListPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_properties_response.ListPropertiesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_properties

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_properties.async_list_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_properties_request.ListPropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        input_["entity_id"] = entity_id
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

    async def list_scenes(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_scenes_response.ListScenesResponse":
        """<p>Lists all scenes in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scenes.</p>
            max_results: <p>Specifies the maximum number of results to display.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_scenes_request.ListScenesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_scenes_response.ListScenesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_scenes

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_scenes.async_list_scenes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_scenes_request.ListScenesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
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

    async def list_sync_jobs(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_sync_jobs_response.ListSyncJobsResponse":
        """<p>List all SyncJobs.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the sync job.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p> <p>Valid Range: Minimum value of 0. Maximum value of 200.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_sync_jobs_request.ListSyncJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_sync_jobs_response.ListSyncJobsResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_jobs.async_list_sync_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_sync_jobs_request.ListSyncJobsRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
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

    async def list_sync_resources(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        filters: Optional[
            "aws_sdk_iottwinmaker.types.sync_resource_filters.SyncResourceFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_sync_resources_response.ListSyncResourcesResponse":
        """<p>Lists the sync resources.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the sync job.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>
            filters: <p>A list of objects that filter the request.</p> <p>The following filter combinations are supported:</p> <ul> <li> <p>Filter with state</p> </li> <li> <p>Filter with ResourceType and ResourceId</p> </li> <li> <p>Filter with ResourceType and ExternalId</p> </li> </ul>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p> <p>Valid Range: Minimum value of 0. Maximum value of 200.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_sync_resources_request.ListSyncResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_sync_resources_response.ListSyncResourcesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_resources

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_resources.async_list_sync_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_sync_resources_request.ListSyncResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["sync_source"] = sync_source
        if filters is not None:
            input_["filters"] = filters
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
        resource_arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
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

    async def list_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iottwinmaker.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iottwinmaker.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Retrieves information about workspaces in the current account.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_workspaces

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.list_workspaces.async_list_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.list_workspaces_request.ListWorkspacesRequest = {}  # type: ignore[typeddict-item]
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

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        tags: "aws_sdk_iottwinmaker.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>Metadata to add to this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        tag_keys: "aws_sdk_iottwinmaker.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
    ) -> "aws_sdk_iottwinmaker.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of tag key names to remove from the resource. You don't specify the value. Both the key and its associated value are removed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_component_type(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        is_singleton: Optional["aws_sdk_iottwinmaker.types.boolean.Boolean"] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        property_definitions: Optional[
            "aws_sdk_iottwinmaker.types.property_definitions_request.PropertyDefinitionsRequest"
        ] = None,
        extends_from: Optional[
            "aws_sdk_iottwinmaker.types.extends_from.ExtendsFrom"
        ] = None,
        functions: Optional[
            "aws_sdk_iottwinmaker.types.functions_request.FunctionsRequest"
        ] = None,
        property_groups: Optional[
            "aws_sdk_iottwinmaker.types.property_groups_request.PropertyGroupsRequest"
        ] = None,
        component_type_name: Optional[
            "aws_sdk_iottwinmaker.types.component_type_name.ComponentTypeName"
        ] = None,
        composite_component_types: Optional[
            "aws_sdk_iottwinmaker.types.composite_component_types_request.CompositeComponentTypesRequest"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.update_component_type_response.UpdateComponentTypeResponse":
        """<p>Updates information in a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            is_singleton: <p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>
            component_type_id: <p>The ID of the component type.</p>
            description: <p>The description of the component type.</p>
            property_definitions: <p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>
            extends_from: <p>Specifies the component type that this component type extends.</p>
            functions: <p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>
            property_groups: <p>The property groups.</p>
            component_type_name: <p>The component type name.</p>
            composite_component_types: <p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.update_component_type_request.UpdateComponentTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.update_component_type_response.UpdateComponentTypeResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_component_type

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_component_type.async_update_component_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.update_component_type_request.UpdateComponentTypeRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if is_singleton is not None:
            input_["is_singleton"] = is_singleton
        input_["component_type_id"] = component_type_id
        if description is not None:
            input_["description"] = description
        if property_definitions is not None:
            input_["property_definitions"] = property_definitions
        if extends_from is not None:
            input_["extends_from"] = extends_from
        if functions is not None:
            input_["functions"] = functions
        if property_groups is not None:
            input_["property_groups"] = property_groups
        if component_type_name is not None:
            input_["component_type_name"] = component_type_name
        if composite_component_types is not None:
            input_["composite_component_types"] = composite_component_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_entity(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        entity_name: Optional[
            "aws_sdk_iottwinmaker.types.entity_name.EntityName"
        ] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        component_updates: Optional[
            "aws_sdk_iottwinmaker.types.component_updates_map_request.ComponentUpdatesMapRequest"
        ] = None,
        composite_component_updates: Optional[
            "aws_sdk_iottwinmaker.types.composite_component_updates_map_request.CompositeComponentUpdatesMapRequest"
        ] = None,
        parent_entity_update: Optional[
            "aws_sdk_iottwinmaker.types.parent_entity_update_request.ParentEntityUpdateRequest"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.update_entity_response.UpdateEntityResponse":
        """<p>Updates an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity.</p>
            entity_id: <p>The ID of the entity.</p>
            entity_name: <p>The name of the entity.</p>
            description: <p>The description of the entity.</p>
            component_updates: <p>An object that maps strings to the component updates in the request. Each string in the mapping must be unique to this object.</p>
            composite_component_updates: <p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>
            parent_entity_update: <p>An object that describes the update request for a parent entity.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.update_entity_request.UpdateEntityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.update_entity_response.UpdateEntityResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_entity

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_entity.async_update_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.update_entity_request.UpdateEntityRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["entity_id"] = entity_id
        if entity_name is not None:
            input_["entity_name"] = entity_name
        if description is not None:
            input_["description"] = description
        if component_updates is not None:
            input_["component_updates"] = component_updates
        if composite_component_updates is not None:
            input_["composite_component_updates"] = composite_component_updates
        if parent_entity_update is not None:
            input_["parent_entity_update"] = parent_entity_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pricing_plan(
        self,
        pricing_mode: "aws_sdk_iottwinmaker.types.pricing_mode.PricingMode",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        bundle_names: Optional[
            "aws_sdk_iottwinmaker.types.pricing_bundles.PricingBundles"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.update_pricing_plan_response.UpdatePricingPlanResponse":
        """<p>Update the pricing plan.</p>

        Args:
            pricing_mode: <p>The pricing mode.</p>
            bundle_names: <p>The bundle names.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.update_pricing_plan_request.UpdatePricingPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.update_pricing_plan_response.UpdatePricingPlanResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_pricing_plan

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_pricing_plan.async_update_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.update_pricing_plan_request.UpdatePricingPlanRequest = {}  # type: ignore[typeddict-item]
        input_["pricing_mode"] = pricing_mode
        if bundle_names is not None:
            input_["bundle_names"] = bundle_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_scene(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        scene_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        content_location: Optional["aws_sdk_iottwinmaker.types.s3_url.S3Url"] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        capabilities: Optional[
            "aws_sdk_iottwinmaker.types.scene_capabilities.SceneCapabilities"
        ] = None,
        scene_metadata: Optional[
            "aws_sdk_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.update_scene_response.UpdateSceneResponse":
        """<p>Updates a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>
            content_location: <p>The relative path that specifies the location of the content definition file.</p>
            description: <p>The description of this scene.</p>
            capabilities: <p>A list of capabilities that the scene uses to render.</p>
            scene_metadata: <p>The scene metadata.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.update_scene_request.UpdateSceneRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.update_scene_response.UpdateSceneResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_scene

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_scene.async_update_scene(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.update_scene_request.UpdateSceneRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["scene_id"] = scene_id
        if content_location is not None:
            input_["content_location"] = content_location
        if description is not None:
            input_["description"] = description
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if scene_metadata is not None:
            input_["scene_metadata"] = scene_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_workspace(
        self,
        workspace_id: "aws_sdk_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[AsyncIoTTwinMakerClientConfig] = None,
        description: Optional[
            "aws_sdk_iottwinmaker.types.description.Description"
        ] = None,
        role: Optional["aws_sdk_iottwinmaker.types.role_arn.RoleArn"] = None,
        s3_location: Optional[
            "aws_sdk_iottwinmaker.types.s3_location.S3Location"
        ] = None,
    ) -> "aws_sdk_iottwinmaker.types.update_workspace_response.UpdateWorkspaceResponse":
        """<p>Updates a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            description: <p>The description of the workspace.</p>
            role: <p>The ARN of the execution role associated with the workspace.</p>
            s3_location: <p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iottwinmaker.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iottwinmaker.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_iottwinmaker._operations.aws_io_t_twin_maker.update_workspace.async_update_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iottwinmaker.types.update_workspace_request.UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        if description is not None:
            input_["description"] = description
        if role is not None:
            input_["role"] = role
        if s3_location is not None:
            input_["s3_location"] = s3_location

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
