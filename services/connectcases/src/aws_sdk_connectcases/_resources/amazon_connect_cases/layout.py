from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_connectcases._auth._signers
import aws_sdk_connectcases._auth._sigv4
from aws_sdk_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.create_layout_request
    import aws_sdk_connectcases.types.create_layout_response
    import aws_sdk_connectcases.types.delete_layout_request
    import aws_sdk_connectcases.types.delete_layout_response
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.get_layout_request
    import aws_sdk_connectcases.types.get_layout_response
    import aws_sdk_connectcases.types.layout_content
    import aws_sdk_connectcases.types.layout_id
    import aws_sdk_connectcases.types.layout_name
    import aws_sdk_connectcases.types.list_layouts_request
    import aws_sdk_connectcases.types.list_layouts_response
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.update_layout_request
    import aws_sdk_connectcases.types.update_layout_response
    from aws_sdk_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from aws_sdk_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Layout:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        name: "aws_sdk_connectcases.types.layout_name.LayoutName",
        content: "aws_sdk_connectcases.types.layout_content.LayoutContent",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.create_layout_response.CreateLayoutResponse":
        """<p>Creates a layout in the Cases domain. Layouts define the following configuration in the top section and More Info tab of the Cases user interface:</p> <ul> <li> <p>Fields to display to the users</p> </li> <li> <p>Field ordering</p> </li> </ul> <note> <p>Title and Status fields cannot be part of layouts since they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the layout. It must be unique for the Cases domain.</p>
            content: <p>Information about which fields will be present in the layout, and information about the order of the fields.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.create_layout_request.CreateLayoutRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.create_layout_response.CreateLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_layout

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.create_layout.create_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.create_layout_request.CreateLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        input_["content"] = content

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_layout_response.GetLayoutResponse":
        """<p>Returns the details for the requested layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.get_layout_request.GetLayoutRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.get_layout_response.GetLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_layout

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.get_layout.get_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.get_layout_request.GetLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        name: Optional["aws_sdk_connectcases.types.layout_name.LayoutName"] = None,
        content: Optional[
            "aws_sdk_connectcases.types.layout_content.LayoutContent"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_layout_response.UpdateLayoutResponse":
        """<p>Updates the attributes of an existing layout.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p> <p>A <code>ValidationException</code> is returned when you add non-existent <code>fieldIds</code> to a layout.</p> <note> <p>Title and Status fields cannot be part of layouts because they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>
            name: <p>The name of the layout. It must be unique per domain.</p>
            content: <p>Information about which fields will be present in the layout, the order of the fields.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.update_layout_request.UpdateLayoutRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.update_layout_response.UpdateLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_layout

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.update_layout.update_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.update_layout_request.UpdateLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_layout_response.DeleteLayoutResponse":
        """<p>Deletes a layout from a cases template. You can delete up to 100 layouts per domain.</p> <p>After a layout is deleted:</p> <ul> <li> <p>You can still retrieve the layout by calling <code>GetLayout</code>.</p> </li> <li> <p>You cannot update a deleted layout by calling <code>UpdateLayout</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted layouts are not included in the <code>ListLayouts</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.delete_layout_request.DeleteLayoutRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.delete_layout_response.DeleteLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_layout

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.delete_layout.delete_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.delete_layout_request.DeleteLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_layouts_response.ListLayoutsResponse":
        """<p>Lists all layouts in the given cases domain. Each list item is a condensed summary object of the layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.list_layouts_request.ListLayoutsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.list_layouts_response.ListLayoutsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_layouts

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.list_layouts.list_layouts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.list_layouts_request.ListLayoutsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLayout:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        name: "aws_sdk_connectcases.types.layout_name.LayoutName",
        content: "aws_sdk_connectcases.types.layout_content.LayoutContent",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.create_layout_response.CreateLayoutResponse":
        """<p>Creates a layout in the Cases domain. Layouts define the following configuration in the top section and More Info tab of the Cases user interface:</p> <ul> <li> <p>Fields to display to the users</p> </li> <li> <p>Field ordering</p> </li> </ul> <note> <p>Title and Status fields cannot be part of layouts since they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the layout. It must be unique for the Cases domain.</p>
            content: <p>Information about which fields will be present in the layout, and information about the order of the fields.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.create_layout_request.CreateLayoutRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.create_layout_response.CreateLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_layout

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.create_layout.async_create_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.create_layout_request.CreateLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_layout_response.GetLayoutResponse":
        """<p>Returns the details for the requested layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.get_layout_request.GetLayoutRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.get_layout_response.GetLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_layout

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.get_layout.async_get_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.get_layout_request.GetLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["aws_sdk_connectcases.types.layout_name.LayoutName"] = None,
        content: Optional[
            "aws_sdk_connectcases.types.layout_content.LayoutContent"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_layout_response.UpdateLayoutResponse":
        """<p>Updates the attributes of an existing layout.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p> <p>A <code>ValidationException</code> is returned when you add non-existent <code>fieldIds</code> to a layout.</p> <note> <p>Title and Status fields cannot be part of layouts because they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>
            name: <p>The name of the layout. It must be unique per domain.</p>
            content: <p>Information about which fields will be present in the layout, the order of the fields.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.update_layout_request.UpdateLayoutRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.update_layout_response.UpdateLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_layout

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.update_layout.async_update_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.update_layout_request.UpdateLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_layout_response.DeleteLayoutResponse":
        """<p>Deletes a layout from a cases template. You can delete up to 100 layouts per domain.</p> <p>After a layout is deleted:</p> <ul> <li> <p>You can still retrieve the layout by calling <code>GetLayout</code>.</p> </li> <li> <p>You cannot update a deleted layout by calling <code>UpdateLayout</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted layouts are not included in the <code>ListLayouts</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.delete_layout_request.DeleteLayoutRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.delete_layout_response.DeleteLayoutResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_layout

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.delete_layout.async_delete_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.delete_layout_request.DeleteLayoutRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["layout_id"] = layout_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_layouts_response.ListLayoutsResponse":
        """<p>Lists all layouts in the given cases domain. Each list item is a condensed summary object of the layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            aws_sdk_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            aws_sdk_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            aws_sdk_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            aws_sdk_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            aws_sdk_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.list_layouts_request.ListLayoutsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.list_layouts_response.ListLayoutsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_layouts

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.list_layouts.async_list_layouts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.list_layouts_request.ListLayoutsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
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
