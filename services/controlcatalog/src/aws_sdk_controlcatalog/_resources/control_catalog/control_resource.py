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
    import aws_sdk_controlcatalog.types.control_arn
    import aws_sdk_controlcatalog.types.control_filter
    import aws_sdk_controlcatalog.types.control_summary
    import aws_sdk_controlcatalog.types.get_control_request
    import aws_sdk_controlcatalog.types.get_control_response
    import aws_sdk_controlcatalog.types.list_controls_request
    import aws_sdk_controlcatalog.types.list_controls_response
    import aws_sdk_controlcatalog.types.max_list_controls_results
    import aws_sdk_controlcatalog.types.pagination_token
    from aws_sdk_controlcatalog._services.async_control_catalog import (
        AsyncControlCatalogClient,
        AsyncControlCatalogClientConfig,
    )
    from aws_sdk_controlcatalog._services.control_catalog import (
        ControlCatalogClient,
        ControlCatalogClientConfig,
    )


class ControlResource:
    def __init__(self, service: ControlCatalogClient) -> None:
        self._service = service

    def read(
        self,
        control_arn: "aws_sdk_controlcatalog.types.control_arn.ControlArn",
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
    ) -> "aws_sdk_controlcatalog.types.get_control_response.GetControlResponse":
        """<p>Returns details about a specific control, most notably a list of Amazon Web Services Regions where this control is supported. Input a value for the <i>ControlArn</i> parameter, in ARN form. <code>GetControl</code> accepts <i>controltower</i> or <i>controlcatalog</i> control ARNs as input. Returns a <i>controlcatalog</i> ARN format.</p> <p>In the API response, controls that have the value <code>GLOBAL</code> in the <code>Scope</code> field do not show the <code>DeployableRegions</code> field, because it does not apply. Controls that have the value <code>REGIONAL</code> in the <code>Scope</code> field return a value for the <code>DeployableRegions</code> field, as shown in the example.</p>

        Args:
            control_arn: <p>The Amazon Resource Name (ARN) of the control. It has one of the following formats:</p> <p> <i>Global format</i> </p> <p> <code>arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}</code> </p> <p> <i>Or Regional format</i> </p> <p> <code>arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}</code> </p> <p>Here is a more general pattern that covers Amazon Web Services Control Tower and Control Catalog ARNs:</p> <p> <code>^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controlcatalog.types.get_control_request.GetControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_controlcatalog.types.get_control_response.GetControlResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.get_control

            output, http_response = (
                aws_sdk_controlcatalog._operations.control_catalog.get_control.get_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controlcatalog.types.get_control_request.GetControlRequest = {}  # type: ignore[typeddict-item]
        input["control_arn"] = control_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_controls_results.MaxListControlsResults"
        ] = None,
        filter: Optional[
            "aws_sdk_controlcatalog.types.control_filter.ControlFilter"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_controls_response.ListControlsResponse":
        """<p>Returns a paginated list of all available controls in the Control Catalog library. Allows you to discover available controls. The list of controls is given as structures of type <i>controlSummary</i>. The ARN is returned in the global <i>controlcatalog</i> format, as shown in the examples.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            filter: <p>An optional filter that narrows the results to controls with specific implementation types or identifiers. If you don't provide a filter, the operation returns all available controls.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controlcatalog.types.list_controls_request.ListControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_controlcatalog.types.list_controls_response.ListControlsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_controls

            output, http_response = (
                aws_sdk_controlcatalog._operations.control_catalog.list_controls.list_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controlcatalog.types.list_controls_request.ListControlsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filter is not None:
            input["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncControlResource:
    def __init__(self, service: AsyncControlCatalogClient) -> None:
        self._service = service

    async def read(
        self,
        control_arn: "aws_sdk_controlcatalog.types.control_arn.ControlArn",
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
    ) -> "aws_sdk_controlcatalog.types.get_control_response.GetControlResponse":
        """<p>Returns details about a specific control, most notably a list of Amazon Web Services Regions where this control is supported. Input a value for the <i>ControlArn</i> parameter, in ARN form. <code>GetControl</code> accepts <i>controltower</i> or <i>controlcatalog</i> control ARNs as input. Returns a <i>controlcatalog</i> ARN format.</p> <p>In the API response, controls that have the value <code>GLOBAL</code> in the <code>Scope</code> field do not show the <code>DeployableRegions</code> field, because it does not apply. Controls that have the value <code>REGIONAL</code> in the <code>Scope</code> field return a value for the <code>DeployableRegions</code> field, as shown in the example.</p>

        Args:
            control_arn: <p>The Amazon Resource Name (ARN) of the control. It has one of the following formats:</p> <p> <i>Global format</i> </p> <p> <code>arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}</code> </p> <p> <i>Or Regional format</i> </p> <p> <code>arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}</code> </p> <p>Here is a more general pattern that covers Amazon Web Services Control Tower and Control Catalog ARNs:</p> <p> <code>^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$</code> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controlcatalog.types.get_control_request.GetControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controlcatalog.types.get_control_response.GetControlResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.get_control

            (
                output,
                http_response,
            ) = await aws_sdk_controlcatalog._operations.control_catalog.get_control.async_get_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controlcatalog.types.get_control_request.GetControlRequest = {}  # type: ignore[typeddict-item]
        input["control_arn"] = control_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_controls_results.MaxListControlsResults"
        ] = None,
        filter: Optional[
            "aws_sdk_controlcatalog.types.control_filter.ControlFilter"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_controls_response.ListControlsResponse":
        """<p>Returns a paginated list of all available controls in the Control Catalog library. Allows you to discover available controls. The list of controls is given as structures of type <i>controlSummary</i>. The ARN is returned in the global <i>controlcatalog</i> format, as shown in the examples.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            filter: <p>An optional filter that narrows the results to controls with specific implementation types or identifiers. If you don't provide a filter, the operation returns all available controls.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controlcatalog.types.list_controls_request.ListControlsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controlcatalog.types.list_controls_response.ListControlsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_controls

            (
                output,
                http_response,
            ) = await aws_sdk_controlcatalog._operations.control_catalog.list_controls.async_list_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controlcatalog.types.list_controls_request.ListControlsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filter is not None:
            input["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
