from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.create_variant_store_request
    import aws_sdk_omics.types.create_variant_store_response
    import aws_sdk_omics.types.delete_variant_store_request
    import aws_sdk_omics.types.delete_variant_store_response
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.get_variant_store_request
    import aws_sdk_omics.types.get_variant_store_response
    import aws_sdk_omics.types.id_list
    import aws_sdk_omics.types.list_variant_stores_filter
    import aws_sdk_omics.types.list_variant_stores_request
    import aws_sdk_omics.types.list_variant_stores_response
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.update_variant_store_request
    import aws_sdk_omics.types.update_variant_store_response
    import aws_sdk_omics.types.variant_store_item
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class VariantStore:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        reference: "aws_sdk_omics.types.reference_item.ReferenceItem",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["aws_sdk_omics.types.store_name.StoreName"] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
    ) -> "aws_sdk_omics.types.create_variant_store_response.CreateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates a variant store.</p>

        Args:
            reference: <p>The genome reference for the store's variants.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_variant_store_request.CreateVariantStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_variant_store_response.CreateVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_variant_store

            output, http_response = (
                aws_sdk_omics._operations.omics.create_variant_store.create_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_variant_store_request.CreateVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sse_config is not None:
            input_["sse_config"] = sse_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self, name: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.get_variant_store_response.GetVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant store.</p>

        Args:
            name: <p>The store's name.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_variant_store_request.GetVariantStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_variant_store_response.GetVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_variant_store

            output, http_response = (
                aws_sdk_omics._operations.omics.get_variant_store.get_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_variant_store_request.GetVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
    ) -> "aws_sdk_omics.types.update_variant_store_response.UpdateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates a variant store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.update_variant_store_request.UpdateVariantStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.update_variant_store_response.UpdateVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_variant_store

            output, http_response = (
                aws_sdk_omics._operations.omics.update_variant_store.update_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.update_variant_store_request.UpdateVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_omics.types.delete_variant_store_response.DeleteVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes a variant store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_variant_store_request.DeleteVariantStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_variant_store_response.DeleteVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_variant_store

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_variant_store.delete_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_variant_store_request.DeleteVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["aws_sdk_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_variant_stores_response.ListVariantStoresResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant stores.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            ids: <p>A list of store IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_variant_stores_request.ListVariantStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_variant_stores_response.ListVariantStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_variant_stores

            output, http_response = (
                aws_sdk_omics._operations.omics.list_variant_stores.list_variant_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_variant_stores_request.ListVariantStoresRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncVariantStore:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        reference: "aws_sdk_omics.types.reference_item.ReferenceItem",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["aws_sdk_omics.types.store_name.StoreName"] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
    ) -> "aws_sdk_omics.types.create_variant_store_response.CreateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates a variant store.</p>

        Args:
            reference: <p>The genome reference for the store's variants.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_variant_store_request.CreateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_variant_store_response.CreateVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_variant_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_variant_store.async_create_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_variant_store_request.CreateVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sse_config is not None:
            input_["sse_config"] = sse_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.get_variant_store_response.GetVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant store.</p>

        Args:
            name: <p>The store's name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_variant_store_request.GetVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_variant_store_response.GetVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_variant_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_variant_store.async_get_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_variant_store_request.GetVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
    ) -> "aws_sdk_omics.types.update_variant_store_response.UpdateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates a variant store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.update_variant_store_request.UpdateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.update_variant_store_response.UpdateVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_variant_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.update_variant_store.async_update_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.update_variant_store_request.UpdateVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_omics.types.delete_variant_store_response.DeleteVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes a variant store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_variant_store_request.DeleteVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_variant_store_response.DeleteVariantStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_variant_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_variant_store.async_delete_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_variant_store_request.DeleteVariantStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        ids: Optional["aws_sdk_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_variant_stores_response.ListVariantStoresResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant stores.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            ids: <p>A list of store IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_variant_stores_request.ListVariantStoresRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_variant_stores_response.ListVariantStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_variant_stores

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_variant_stores.async_list_variant_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_variant_stores_request.ListVariantStoresRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
