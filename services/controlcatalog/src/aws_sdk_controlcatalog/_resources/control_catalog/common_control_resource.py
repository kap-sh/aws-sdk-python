from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_controlcatalog._auth._signers
import aws_sdk_controlcatalog._auth._sigv4
from aws_sdk_controlcatalog._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.common_control_filter
    import aws_sdk_controlcatalog.types.common_control_summary
    import aws_sdk_controlcatalog.types.list_common_controls_request
    import aws_sdk_controlcatalog.types.list_common_controls_response
    import aws_sdk_controlcatalog.types.max_list_common_controls_results
    import aws_sdk_controlcatalog.types.pagination_token
    from aws_sdk_controlcatalog._services.async_control_catalog import (
        AsyncControlCatalogClient,
        AsyncControlCatalogClientConfig,
    )
    from aws_sdk_controlcatalog._services.control_catalog import (
        ControlCatalogClient,
        ControlCatalogClientConfig,
    )


class CommonControlResource:
    def __init__(self, service: ControlCatalogClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "aws_sdk_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse":
        """<p>Returns a paginated list of common controls from the Amazon Web Services Control Catalog.</p> <p>You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            common_control_filter: <p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_common_controls

            output, http_response = (
                aws_sdk_controlcatalog._operations.control_catalog.list_common_controls.list_common_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if common_control_filter is not None:
            input_["common_control_filter"] = common_control_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCommonControlResource:
    def __init__(self, service: AsyncControlCatalogClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "aws_sdk_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse":
        """<p>Returns a paginated list of common controls from the Amazon Web Services Control Catalog.</p> <p>You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            common_control_filter: <p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_common_controls

            (
                output,
                http_response,
            ) = await aws_sdk_controlcatalog._operations.control_catalog.list_common_controls.async_list_common_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if common_control_filter is not None:
            input_["common_control_filter"] = common_control_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
