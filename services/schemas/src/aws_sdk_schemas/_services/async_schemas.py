"""Generated from Smithy shape ``com.amazonaws.schemas#schemas``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_schemas._auth._signers
import aws_sdk_schemas._auth._sigv4
from aws_sdk_schemas._auth._identity import Credentials
from aws_sdk_schemas._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_schemas._auth._zapros_handler import AuthMiddleware
from aws_sdk_schemas._pagination import resolve_path as _resolve_path
from aws_sdk_schemas._services._aws_config import aaws_config
from aws_sdk_schemas._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__boolean
    import aws_sdk_schemas.types.__integer
    import aws_sdk_schemas.types.__list_of__string
    import aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__string_min0_max36
    import aws_sdk_schemas.types.__string_min0_max256
    import aws_sdk_schemas.types.__string_min1_max100000
    import aws_sdk_schemas.types.__string_min20_max1600
    import aws_sdk_schemas.types.create_discoverer_request
    import aws_sdk_schemas.types.create_discoverer_response
    import aws_sdk_schemas.types.create_registry_request
    import aws_sdk_schemas.types.create_registry_response
    import aws_sdk_schemas.types.create_schema_request
    import aws_sdk_schemas.types.create_schema_response
    import aws_sdk_schemas.types.delete_discoverer_request
    import aws_sdk_schemas.types.delete_registry_request
    import aws_sdk_schemas.types.delete_resource_policy_request
    import aws_sdk_schemas.types.delete_schema_request
    import aws_sdk_schemas.types.delete_schema_version_request
    import aws_sdk_schemas.types.describe_code_binding_request
    import aws_sdk_schemas.types.describe_code_binding_response
    import aws_sdk_schemas.types.describe_discoverer_request
    import aws_sdk_schemas.types.describe_discoverer_response
    import aws_sdk_schemas.types.describe_registry_request
    import aws_sdk_schemas.types.describe_registry_response
    import aws_sdk_schemas.types.describe_schema_request
    import aws_sdk_schemas.types.describe_schema_response
    import aws_sdk_schemas.types.discoverer_summary
    import aws_sdk_schemas.types.export_schema_request
    import aws_sdk_schemas.types.export_schema_response
    import aws_sdk_schemas.types.get_code_binding_source_request
    import aws_sdk_schemas.types.get_code_binding_source_response
    import aws_sdk_schemas.types.get_discovered_schema_request
    import aws_sdk_schemas.types.get_discovered_schema_response
    import aws_sdk_schemas.types.get_resource_policy_request
    import aws_sdk_schemas.types.get_resource_policy_response
    import aws_sdk_schemas.types.list_discoverers_request
    import aws_sdk_schemas.types.list_discoverers_response
    import aws_sdk_schemas.types.list_registries_request
    import aws_sdk_schemas.types.list_registries_response
    import aws_sdk_schemas.types.list_schema_versions_request
    import aws_sdk_schemas.types.list_schema_versions_response
    import aws_sdk_schemas.types.list_schemas_request
    import aws_sdk_schemas.types.list_schemas_response
    import aws_sdk_schemas.types.list_tags_for_resource_request
    import aws_sdk_schemas.types.list_tags_for_resource_response
    import aws_sdk_schemas.types.put_code_binding_request
    import aws_sdk_schemas.types.put_code_binding_response
    import aws_sdk_schemas.types.put_resource_policy_request
    import aws_sdk_schemas.types.put_resource_policy_response
    import aws_sdk_schemas.types.registry_summary
    import aws_sdk_schemas.types.schema_summary
    import aws_sdk_schemas.types.schema_version_summary
    import aws_sdk_schemas.types.search_schema_summary
    import aws_sdk_schemas.types.search_schemas_request
    import aws_sdk_schemas.types.search_schemas_response
    import aws_sdk_schemas.types.start_discoverer_request
    import aws_sdk_schemas.types.start_discoverer_response
    import aws_sdk_schemas.types.stop_discoverer_request
    import aws_sdk_schemas.types.stop_discoverer_response
    import aws_sdk_schemas.types.synthesized_json__string
    import aws_sdk_schemas.types.tag_resource_request
    import aws_sdk_schemas.types.tags
    import aws_sdk_schemas.types.type
    import aws_sdk_schemas.types.untag_resource_request
    import aws_sdk_schemas.types.update_discoverer_request
    import aws_sdk_schemas.types.update_discoverer_response
    import aws_sdk_schemas.types.update_registry_request
    import aws_sdk_schemas.types.update_registry_response
    import aws_sdk_schemas.types.update_schema_request
    import aws_sdk_schemas.types.update_schema_response


class AsyncschemasClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncschemasClient:
    """A client for the ``schemas`` service.

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
        self._config = AsyncschemasClientConfig(
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
        self, config_overrides: Optional[AsyncschemasClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncschemasClientConfig = config_overrides or {}
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

    async def create_discoverer(
        self,
        source_arn: "aws_sdk_schemas.types.__string_min20_max1600.__stringMin20Max1600",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        cross_account: Optional["aws_sdk_schemas.types.__boolean.__boolean"] = None,
        tags: Optional["aws_sdk_schemas.types.tags.Tags"] = None,
    ) -> "aws_sdk_schemas.types.create_discoverer_response.CreateDiscovererResponse":
        """<p>Creates a discoverer.</p>

        Args:
            description: <p>A description for the discoverer.</p>
            source_arn: <p>The ARN of the event bus.</p>
            cross_account: <p>Support discovery of schemas in events sent to the bus from another account. (default: true).</p>
            tags: <p>Tags associated with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.create_discoverer_request.CreateDiscovererRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.create_discoverer_response.CreateDiscovererResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.create_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.create_discoverer.async_create_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.create_discoverer_request.CreateDiscovererRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["source_arn"] = source_arn
        if cross_account is not None:
            input_["cross_account"] = cross_account
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_registry(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        tags: Optional["aws_sdk_schemas.types.tags.Tags"] = None,
    ) -> "aws_sdk_schemas.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a registry.</p>

        Args:
            description: <p>A description of the registry to be created.</p>
            registry_name: <p>The name of the registry.</p>
            tags: <p>Tags to associate with the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.create_registry_request.CreateRegistryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.create_registry_response.CreateRegistryResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.create_registry

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.create_registry.async_create_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.create_registry_request.CreateRegistryRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["registry_name"] = registry_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_schema(
        self,
        content: "aws_sdk_schemas.types.__string_min1_max100000.__stringMin1Max100000",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        type: "aws_sdk_schemas.types.type.Type",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        tags: Optional["aws_sdk_schemas.types.tags.Tags"] = None,
    ) -> "aws_sdk_schemas.types.create_schema_response.CreateSchemaResponse":
        """<p>Creates a schema definition.</p> <note><p>Inactive schemas will be deleted after two years.</p></note>

        Args:
            content: <p>The source of the schema definition.</p>
            description: <p>A description of the schema.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            tags: <p>Tags associated with the schema.</p>
            type: <p>The type of schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.create_schema_request.CreateSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.create_schema_response.CreateSchemaResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.create_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.create_schema.async_create_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.create_schema_request.CreateSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["content"] = content
        if description is not None:
            input_["description"] = description
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if tags is not None:
            input_["tags"] = tags
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_discoverer(
        self,
        discoverer_id: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Deletes a discoverer.</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.delete_discoverer_request.DeleteDiscovererRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.delete_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.delete_discoverer.async_delete_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.delete_discoverer_request.DeleteDiscovererRequest = {}  # type: ignore[typeddict-item]
        input_["discoverer_id"] = discoverer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_registry(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Deletes a Registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.delete_registry

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.delete_registry.async_delete_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.delete_registry_request.DeleteRegistryRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        registry_name: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> None:
        """<p>Delete the resource-based policy attached to the specified registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        if registry_name is not None:
            input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_schema(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Delete a schema definition.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.delete_schema_request.DeleteSchemaRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.delete_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.delete_schema.async_delete_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.delete_schema_request.DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_schema_version(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        schema_version: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Delete the schema version definition</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: The version number of the schema
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.delete_schema_version_request.DeleteSchemaVersionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.delete_schema_version

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.delete_schema_version.async_delete_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.delete_schema_version_request.DeleteSchemaVersionRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        input_["schema_version"] = schema_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_code_binding(
        self,
        language: "aws_sdk_schemas.types.__string.__string",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        schema_version: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.describe_code_binding_response.DescribeCodeBindingResponse":
        """<p>Describe the code binding URI.</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.describe_code_binding_request.DescribeCodeBindingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.describe_code_binding_response.DescribeCodeBindingResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.describe_code_binding

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.describe_code_binding.async_describe_code_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.describe_code_binding_request.DescribeCodeBindingRequest = {}  # type: ignore[typeddict-item]
        input_["language"] = language
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_discoverer(
        self,
        discoverer_id: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> (
        "aws_sdk_schemas.types.describe_discoverer_response.DescribeDiscovererResponse"
    ):
        """<p>Describes the discoverer.</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.describe_discoverer_request.DescribeDiscovererRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.describe_discoverer_response.DescribeDiscovererResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.describe_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.describe_discoverer.async_describe_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.describe_discoverer_request.DescribeDiscovererRequest = {}  # type: ignore[typeddict-item]
        input_["discoverer_id"] = discoverer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_registry(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> "aws_sdk_schemas.types.describe_registry_response.DescribeRegistryResponse":
        """<p>Describes the registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.describe_registry_request.DescribeRegistryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.describe_registry_response.DescribeRegistryResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.describe_registry

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.describe_registry.async_describe_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.describe_registry_request.DescribeRegistryRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_schema(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        schema_version: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.describe_schema_response.DescribeSchemaResponse":
        """<p>Retrieve the schema definition.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.describe_schema_request.DescribeSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.describe_schema_response.DescribeSchemaResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.describe_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.describe_schema.async_describe_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.describe_schema_request.DescribeSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_schema(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        type: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        schema_version: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.export_schema_response.ExportSchemaResponse":
        """export_schema

        Args:
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.export_schema_request.ExportSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.export_schema_response.ExportSchemaResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.export_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.export_schema.async_export_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.export_schema_request.ExportSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if schema_version is not None:
            input_["schema_version"] = schema_version
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_code_binding_source(
        self,
        language: "aws_sdk_schemas.types.__string.__string",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        schema_version: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.get_code_binding_source_response.GetCodeBindingSourceResponse":
        """<p>Get the code binding source URI.</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.get_code_binding_source_request.GetCodeBindingSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.get_code_binding_source_response.GetCodeBindingSourceResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.get_code_binding_source

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.get_code_binding_source.async_get_code_binding_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.get_code_binding_source_request.GetCodeBindingSourceRequest = {}  # type: ignore[typeddict-item]
        input_["language"] = language
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_discovered_schema(
        self,
        events: "aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input.__listOfGetDiscoveredSchemaVersionItemInput",
        type: "aws_sdk_schemas.types.type.Type",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> "aws_sdk_schemas.types.get_discovered_schema_response.GetDiscoveredSchemaResponse":
        """<p>Get the discovered schema that was generated based on sampled events.</p>

        Args:
            events: <p>An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events.</p>
            type: <p>The type of event.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.get_discovered_schema_request.GetDiscoveredSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.get_discovered_schema_response.GetDiscoveredSchemaResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.get_discovered_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.get_discovered_schema.async_get_discovered_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.get_discovered_schema_request.GetDiscoveredSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["events"] = events
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        registry_name: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to a given registry.</p>

        Args:
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        if registry_name is not None:
            input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_discoverers(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        discoverer_id_prefix: Optional[
            "aws_sdk_schemas.types.__string.__string"
        ] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        source_arn_prefix: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.list_discoverers_response.ListDiscoverersResponse":
        """<p>List the discoverers.</p>

        Args:
            discoverer_id_prefix: <p>Specifying this limits the results to only those discoverer IDs that start with the specified prefix.</p>
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            source_arn_prefix: <p>Specifying this limits the results to only those ARNs that start with the specified prefix.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.list_discoverers_request.ListDiscoverersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.list_discoverers_response.ListDiscoverersResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.list_discoverers

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.list_discoverers.async_list_discoverers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.list_discoverers_request.ListDiscoverersRequest = {}  # type: ignore[typeddict-item]
        if discoverer_id_prefix is not None:
            input_["discoverer_id_prefix"] = discoverer_id_prefix
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if source_arn_prefix is not None:
            input_["source_arn_prefix"] = source_arn_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_discoverers(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        discoverer_id_prefix: Optional[
            "aws_sdk_schemas.types.__string.__string"
        ] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        source_arn_prefix: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_schemas.types.discoverer_summary.DiscovererSummary]":
        _token = next_token
        while True:
            _response = await self.list_discoverers(
                config_overrides=config_overrides,
                discoverer_id_prefix=discoverer_id_prefix,
                limit=limit,
                next_token=_token,
                source_arn_prefix=source_arn_prefix,
            )
            _page = _resolve_path(_response, ("discoverers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_registries(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        registry_name_prefix: Optional[
            "aws_sdk_schemas.types.__string.__string"
        ] = None,
        scope: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.list_registries_response.ListRegistriesResponse":
        """<p>List the registries.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name_prefix: <p>Specifying this limits the results to only those registry names that start with the specified prefix.</p>
            scope: <p>Can be set to Local or AWS to limit responses to your custom registries, or the ones provided by AWS.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.list_registries_request.ListRegistriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.list_registries_response.ListRegistriesResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.list_registries

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.list_registries.async_list_registries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.list_registries_request.ListRegistriesRequest = {}  # type: ignore[typeddict-item]
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if registry_name_prefix is not None:
            input_["registry_name_prefix"] = registry_name_prefix
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_registries(
        self,
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        registry_name_prefix: Optional[
            "aws_sdk_schemas.types.__string.__string"
        ] = None,
        scope: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_schemas.types.registry_summary.RegistrySummary]":
        _token = next_token
        while True:
            _response = await self.list_registries(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                registry_name_prefix=registry_name_prefix,
                scope=scope,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schemas(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        schema_name_prefix: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.list_schemas_response.ListSchemasResponse":
        """<p>List the schemas.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name_prefix: <p>Specifying this limits the results to only those schema names that start with the specified prefix.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.list_schemas_request.ListSchemasRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.list_schemas_response.ListSchemasResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.list_schemas

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.list_schemas_request.ListSchemasRequest = {}  # type: ignore[typeddict-item]
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        input_["registry_name"] = registry_name
        if schema_name_prefix is not None:
            input_["schema_name_prefix"] = schema_name_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_schemas(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        schema_name_prefix: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_schemas.types.schema_summary.SchemaSummary]":
        _token = next_token
        while True:
            _response = await self.list_schemas(
                registry_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                schema_name_prefix=schema_name_prefix,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schema_versions(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_schemas.types.list_schema_versions_response.ListSchemaVersionsResponse"
    ):
        """<p>Provides a list of the schema versions and related information.</p>

        Args:
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.list_schema_versions_request.ListSchemaVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.list_schema_versions

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.list_schema_versions.async_list_schema_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.list_schema_versions_request.ListSchemaVersionsRequest = {}  # type: ignore[typeddict-item]
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_schema_versions(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_schemas.types.schema_version_summary.SchemaVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_schema_versions(
                registry_name,
                schema_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schema_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> "aws_sdk_schemas.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Get tags for resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_code_binding(
        self,
        language: "aws_sdk_schemas.types.__string.__string",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        schema_version: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse":
        """<p>Put code binding URI</p>

        Args:
            language: <p>The language of the code binding.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            schema_version: <p>Specifying this limits the results to only this schema version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.put_code_binding_request.PutCodeBindingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.put_code_binding

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.put_code_binding.async_put_code_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.put_code_binding_request.PutCodeBindingRequest = {}  # type: ignore[typeddict-item]
        input_["language"] = language
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if schema_version is not None:
            input_["schema_version"] = schema_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        policy: "aws_sdk_schemas.types.synthesized_json__string.SynthesizedJson__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        registry_name: Optional["aws_sdk_schemas.types.__string.__string"] = None,
        revision_id: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>The name of the policy.</p>

        Args:
            policy: <p>The resource-based policy.</p>
            registry_name: <p>The name of the registry.</p>
            revision_id: <p>The revision ID of the policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["policy"] = policy
        if registry_name is not None:
            input_["registry_name"] = registry_name
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_schemas(
        self,
        keywords: "aws_sdk_schemas.types.__string.__string",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> "aws_sdk_schemas.types.search_schemas_response.SearchSchemasResponse":
        """<p>Search the schemas</p>

        Args:
            keywords: <p>Specifying this limits the results to only schemas that include the provided keywords.</p>
            next_token: <p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.search_schemas_request.SearchSchemasRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.search_schemas_response.SearchSchemasResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.search_schemas

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.search_schemas.async_search_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.search_schemas_request.SearchSchemasRequest = {}  # type: ignore[typeddict-item]
        input_["keywords"] = keywords
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_schemas(
        self,
        keywords: "aws_sdk_schemas.types.__string.__string",
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        limit: Optional["aws_sdk_schemas.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_schemas.types.__string.__string"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_schemas.types.search_schema_summary.SearchSchemaSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.search_schemas(
                keywords,
                registry_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_discoverer(
        self,
        discoverer_id: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> "aws_sdk_schemas.types.start_discoverer_response.StartDiscovererResponse":
        """<p>Starts the discoverer</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.start_discoverer_request.StartDiscovererRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.start_discoverer_response.StartDiscovererResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.start_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.start_discoverer.async_start_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.start_discoverer_request.StartDiscovererRequest = {}  # type: ignore[typeddict-item]
        input_["discoverer_id"] = discoverer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_discoverer(
        self,
        discoverer_id: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> "aws_sdk_schemas.types.stop_discoverer_response.StopDiscovererResponse":
        """<p>Stops the discoverer</p>

        Args:
            discoverer_id: <p>The ID of the discoverer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.stop_discoverer_request.StopDiscovererRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.stop_discoverer_response.StopDiscovererResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.stop_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.stop_discoverer.async_stop_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.stop_discoverer_request.StopDiscovererRequest = {}  # type: ignore[typeddict-item]
        input_["discoverer_id"] = discoverer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_schemas.types.__string.__string",
        tags: "aws_sdk_schemas.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Add tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>Tags associated with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_schemas.types.__string.__string",
        tag_keys: "aws_sdk_schemas.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
    ) -> None:
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Keys of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_schemas._operations.schemas.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_discoverer(
        self,
        discoverer_id: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        cross_account: Optional["aws_sdk_schemas.types.__boolean.__boolean"] = None,
    ) -> "aws_sdk_schemas.types.update_discoverer_response.UpdateDiscovererResponse":
        """<p>Updates the discoverer</p>

        Args:
            description: <p>The description of the discoverer to update.</p>
            discoverer_id: <p>The ID of the discoverer.</p>
            cross_account: <p>Support discovery of schemas in events sent to the bus from another account. (default: true)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.update_discoverer_request.UpdateDiscovererRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.update_discoverer_response.UpdateDiscovererResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.update_discoverer

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.update_discoverer.async_update_discoverer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.update_discoverer_request.UpdateDiscovererRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["discoverer_id"] = discoverer_id
        if cross_account is not None:
            input_["cross_account"] = cross_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_registry(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
    ) -> "aws_sdk_schemas.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates a registry.</p>

        Args:
            description: <p>The description of the registry to update.</p>
            registry_name: <p>The name of the registry.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.update_registry_request.UpdateRegistryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.update_registry

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.update_registry.async_update_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.update_registry_request.UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["registry_name"] = registry_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_schema(
        self,
        registry_name: "aws_sdk_schemas.types.__string.__string",
        schema_name: "aws_sdk_schemas.types.__string.__string",
        *,
        config_overrides: Optional[AsyncschemasClientConfig] = None,
        client_token_id: Optional[
            "aws_sdk_schemas.types.__string_min0_max36.__stringMin0Max36"
        ] = None,
        content: Optional[
            "aws_sdk_schemas.types.__string_min1_max100000.__stringMin1Max100000"
        ] = None,
        description: Optional[
            "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
        ] = None,
        type: Optional["aws_sdk_schemas.types.type.Type"] = None,
    ) -> "aws_sdk_schemas.types.update_schema_response.UpdateSchemaResponse":
        """<p>Updates the schema definition</p> <note><p>Inactive schemas will be deleted after two years.</p></note>

        Args:
            client_token_id: <p>The ID of the client token.</p>
            content: <p>The source of the schema definition.</p>
            description: <p>The description of the schema.</p>
            registry_name: <p>The name of the registry.</p>
            schema_name: <p>The name of the schema.</p>
            type: <p>The schema type for the events schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_schemas.types.update_schema_request.UpdateSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_schemas.types.update_schema_response.UpdateSchemaResponse"
        ]:
            import aws_sdk_schemas._operations.schemas.update_schema

            (
                output,
                http_response,
            ) = await aws_sdk_schemas._operations.schemas.update_schema.async_update_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_schemas.types.update_schema_request.UpdateSchemaRequest = {}  # type: ignore[typeddict-item]
        if client_token_id is not None:
            input_["client_token_id"] = client_token_id
        if content is not None:
            input_["content"] = content
        if description is not None:
            input_["description"] = description
        input_["registry_name"] = registry_name
        input_["schema_name"] = schema_name
        if type is not None:
            input_["type"] = type

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
