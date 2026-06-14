from __future__ import annotations

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
    import aws_sdk_omics.types.annotation_store_item
    import aws_sdk_omics.types.create_annotation_store_request
    import aws_sdk_omics.types.create_annotation_store_response
    import aws_sdk_omics.types.delete_annotation_store_request
    import aws_sdk_omics.types.delete_annotation_store_response
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.get_annotation_store_request
    import aws_sdk_omics.types.get_annotation_store_response
    import aws_sdk_omics.types.id_list
    import aws_sdk_omics.types.list_annotation_stores_filter
    import aws_sdk_omics.types.list_annotation_stores_request
    import aws_sdk_omics.types.list_annotation_stores_response
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.store_format
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.store_options
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.update_annotation_store_request
    import aws_sdk_omics.types.update_annotation_store_response
    import aws_sdk_omics.types.version_name
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class AnnotationStore:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        store_format: "aws_sdk_omics.types.store_format.StoreFormat",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        reference: Optional["aws_sdk_omics.types.reference_item.ReferenceItem"] = None,
        name: Optional["aws_sdk_omics.types.store_name.StoreName"] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        version_name: Optional["aws_sdk_omics.types.version_name.VersionName"] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
        store_options: Optional[
            "aws_sdk_omics.types.store_options.StoreOptions"
        ] = None,
    ) -> "aws_sdk_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates an annotation store.</p>

        Args:
            reference: <p>The genome reference for the store's annotations.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            store_format: <p>The annotation file format of the store.</p>
            store_options: <p>File parsing options for the annotation store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_annotation_store

            output, http_response = (
                aws_sdk_omics._operations.omics.create_annotation_store.create_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
        if reference is not None:
            input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if version_name is not None:
            input_["version_name"] = version_name
        if sse_config is not None:
            input_["sse_config"] = sse_config
        input_["store_format"] = store_format
        if store_options is not None:
            input_["store_options"] = store_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self, name: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.get_annotation_store_response.GetAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation store.</p>

        Args:
            name: <p>The store's name.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_annotation_store_request.GetAnnotationStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_annotation_store_response.GetAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_annotation_store

            output, http_response = (
                aws_sdk_omics._operations.omics.get_annotation_store.get_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_annotation_store_request.GetAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates an annotation store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_annotation_store

            output, http_response = (
                aws_sdk_omics._operations.omics.update_annotation_store.update_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes an annotation store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_annotation_store

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_annotation_store.delete_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
        ids: Optional["aws_sdk_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation stores.</p>

        Args:
            ids: <p>IDs of stores to list.</p>
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_annotation_stores

            output, http_response = (
                aws_sdk_omics._operations.omics.list_annotation_stores.list_annotation_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest = {}  # type: ignore[typeddict-item]
        if ids is not None:
            input_["ids"] = ids
        if max_results is not None:
            input_["max_results"] = max_results
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


class AsyncAnnotationStore:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        store_format: "aws_sdk_omics.types.store_format.StoreFormat",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        reference: Optional["aws_sdk_omics.types.reference_item.ReferenceItem"] = None,
        name: Optional["aws_sdk_omics.types.store_name.StoreName"] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        version_name: Optional["aws_sdk_omics.types.version_name.VersionName"] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
        store_options: Optional[
            "aws_sdk_omics.types.store_options.StoreOptions"
        ] = None,
    ) -> "aws_sdk_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates an annotation store.</p>

        Args:
            reference: <p>The genome reference for the store's annotations.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            store_format: <p>The annotation file format of the store.</p>
            store_options: <p>File parsing options for the annotation store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_annotation_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_annotation_store.async_create_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
        if reference is not None:
            input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if version_name is not None:
            input_["version_name"] = version_name
        if sse_config is not None:
            input_["sse_config"] = sse_config
        input_["store_format"] = store_format
        if store_options is not None:
            input_["store_options"] = store_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.get_annotation_store_response.GetAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation store.</p>

        Args:
            name: <p>The store's name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_annotation_store_request.GetAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_annotation_store_response.GetAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_annotation_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_annotation_store.async_get_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_annotation_store_request.GetAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates an annotation store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_annotation_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.update_annotation_store.async_update_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes an annotation store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_annotation_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_annotation_store.async_delete_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
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
        ids: Optional["aws_sdk_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse":
        r"""<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html\"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation stores.</p>

        Args:
            ids: <p>IDs of stores to list.</p>
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_annotation_stores

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_annotation_stores.async_list_annotation_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest = {}  # type: ignore[typeddict-item]
        if ids is not None:
            input_["ids"] = ids
        if max_results is not None:
            input_["max_results"] = max_results
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
