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
    import aws_sdk_omics.types.annotation_store_version_item
    import aws_sdk_omics.types.create_annotation_store_version_request
    import aws_sdk_omics.types.create_annotation_store_version_response
    import aws_sdk_omics.types.delete_annotation_store_versions_request
    import aws_sdk_omics.types.delete_annotation_store_versions_response
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.get_annotation_store_version_request
    import aws_sdk_omics.types.get_annotation_store_version_response
    import aws_sdk_omics.types.list_annotation_store_versions_filter
    import aws_sdk_omics.types.list_annotation_store_versions_request
    import aws_sdk_omics.types.list_annotation_store_versions_response
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.update_annotation_store_version_request
    import aws_sdk_omics.types.update_annotation_store_version_response
    import aws_sdk_omics.types.version_list
    import aws_sdk_omics.types.version_name
    import aws_sdk_omics.types.version_options
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class AnnotationStoreVersion:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_omics.types.store_name.StoreName",
        version_name: "aws_sdk_omics.types.version_name.VersionName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        version_options: Optional[
            "aws_sdk_omics.types.version_options.VersionOptions"
        ] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse":
        """<p> Creates a new version of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store version from which versions are being created. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            description: <p> The description of an annotation store version. </p>
            version_options: <p> The options for an annotation store version. </p>
            tags: <p> Any tags added to annotation store version. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_annotation_store_version

            output, http_response = (
                aws_sdk_omics._operations.omics.create_annotation_store_version.create_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name
        if description is not None:
            input["description"] = description
        if version_options is not None:
            input["version_options"] = version_options
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse":
        """<p> Retrieves the metadata for an annotation store version. </p>

        Args:
            name: <p> The name given to an annotation store version to distinguish it from others. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from others. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_annotation_store_version

            output, http_response = (
                aws_sdk_omics._operations.omics.get_annotation_store_version.get_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
    ) -> "aws_sdk_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse":
        """<p> Updates the description of an annotation store version. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            version_name: <p> The name of an annotation store version. </p>
            description: <p> The description of an annotation store. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_annotation_store_version

            output, http_response = (
                aws_sdk_omics._operations.omics.update_annotation_store_version.update_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse":
        """<p> Lists the versions of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            max_results: <p> The maximum number of annotation store versions to return in one page of results. </p>
            next_token: <p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>
            filter: <p> A filter to apply to the list of annotation store versions. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_annotation_store_versions

            output, http_response = (
                aws_sdk_omics._operations.omics.list_annotation_store_versions.list_annotation_store_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filter is not None:
            input["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_annotation_store_versions(
        self,
        name: str,
        versions: "aws_sdk_omics.types.version_list.VersionList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse":
        """<p> Deletes one or multiple versions of an annotation store. </p>

        Args:
            name: <p> The name of the annotation store from which versions are being deleted. </p>
            versions: <p> The versions of an annotation store to be deleted. </p>
            force: <p> Forces the deletion of an annotation store version when imports are in-progress.. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_annotation_store_versions

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_annotation_store_versions.delete_annotation_store_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["versions"] = versions
        if force is not None:
            input["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAnnotationStoreVersion:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_omics.types.store_name.StoreName",
        version_name: "aws_sdk_omics.types.version_name.VersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
        version_options: Optional[
            "aws_sdk_omics.types.version_options.VersionOptions"
        ] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse":
        """<p> Creates a new version of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store version from which versions are being created. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            description: <p> The description of an annotation store version. </p>
            version_options: <p> The options for an annotation store version. </p>
            tags: <p> Any tags added to annotation store version. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_annotation_store_version

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_annotation_store_version.async_create_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name
        if description is not None:
            input["description"] = description
        if version_options is not None:
            input["version_options"] = version_options
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse":
        """<p> Retrieves the metadata for an annotation store version. </p>

        Args:
            name: <p> The name given to an annotation store version to distinguish it from others. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from others. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_annotation_store_version

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_annotation_store_version.async_get_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["aws_sdk_omics.types.description.Description"] = None,
    ) -> "aws_sdk_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse":
        """<p> Updates the description of an annotation store version. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            version_name: <p> The name of an annotation store version. </p>
            description: <p> The description of an annotation store. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse"
        ]:
            import aws_sdk_omics._operations.omics.update_annotation_store_version

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.update_annotation_store_version.async_update_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["version_name"] = version_name
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "aws_sdk_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse":
        """<p> Lists the versions of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            max_results: <p> The maximum number of annotation store versions to return in one page of results. </p>
            next_token: <p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>
            filter: <p> A filter to apply to the list of annotation store versions. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_annotation_store_versions

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_annotation_store_versions.async_list_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filter is not None:
            input["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_annotation_store_versions(
        self,
        name: str,
        versions: "aws_sdk_omics.types.version_list.VersionList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse":
        """<p> Deletes one or multiple versions of an annotation store. </p>

        Args:
            name: <p> The name of the annotation store from which versions are being deleted. </p>
            versions: <p> The versions of an annotation store to be deleted. </p>
            force: <p> Forces the deletion of an annotation store version when imports are in-progress.. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_annotation_store_versions

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_annotation_store_versions.async_delete_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["versions"] = versions
        if force is not None:
            input["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
