from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_request
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_response
    import aws_sdk_mediaconnect.types.create_router_network_interface_request
    import aws_sdk_mediaconnect.types.create_router_network_interface_response
    import aws_sdk_mediaconnect.types.delete_router_network_interface_request
    import aws_sdk_mediaconnect.types.delete_router_network_interface_response
    import aws_sdk_mediaconnect.types.get_router_network_interface_request
    import aws_sdk_mediaconnect.types.get_router_network_interface_response
    import aws_sdk_mediaconnect.types.list_router_network_interfaces_request
    import aws_sdk_mediaconnect.types.list_router_network_interfaces_response
    import aws_sdk_mediaconnect.types.listed_router_network_interface
    import aws_sdk_mediaconnect.types.router_network_interface_arn
    import aws_sdk_mediaconnect.types.router_network_interface_arn_list
    import aws_sdk_mediaconnect.types.router_network_interface_configuration
    import aws_sdk_mediaconnect.types.router_network_interface_filter_list
    import aws_sdk_mediaconnect.types.update_router_network_interface_request
    import aws_sdk_mediaconnect.types.update_router_network_interface_response
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterNetworkInterfaceResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse":
        """<p>Creates a new router network interface in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router network interface.</p>
            configuration: <p>The configuration settings for the router network interface.</p>
            region_name: <p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router network interface.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.router_network_interface_service_quota_exceeded_exception.RouterNetworkInterfaceServiceQuotaExceededException: <p>The request to create a new router network interface would exceed the service quotas (limits) set for the account. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_network_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.create_router_network_interface.create_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configuration"] = configuration
        if region_name is not None:
            input_["region_name"] = region_name
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about a specific router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_network_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.get_router_network_interface.get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse":
        """<p>Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>
            name: <p>The updated name for the router network interface.</p>
            configuration: <p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_network_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_router_network_interface.update_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse":
        """<p>Deletes a router network interface from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_network_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.delete_router_network_interface.delete_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse":
        """<p>Retrieves a list of router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router network interfaces to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router network interfaces.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_network_interfaces

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_router_network_interfaces.list_router_network_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_router_network_interface(
        self,
        arns: "aws_sdk_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_network_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.batch_get_router_network_interface.batch_get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRouterNetworkInterfaceResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse":
        """<p>Creates a new router network interface in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router network interface.</p>
            configuration: <p>The configuration settings for the router network interface.</p>
            region_name: <p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router network interface.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.router_network_interface_service_quota_exceeded_exception.RouterNetworkInterfaceServiceQuotaExceededException: <p>The request to create a new router network interface would exceed the service quotas (limits) set for the account. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.create_router_network_interface.async_create_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configuration"] = configuration
        if region_name is not None:
            input_["region_name"] = region_name
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about a specific router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.get_router_network_interface.async_get_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse":
        """<p>Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>
            name: <p>The updated name for the router network interface.</p>
            configuration: <p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_router_network_interface.async_update_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse":
        """<p>Deletes a router network interface from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.delete_router_network_interface.async_delete_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse":
        """<p>Retrieves a list of router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router network interfaces to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router network interfaces.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_network_interfaces

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_router_network_interfaces.async_list_router_network_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_router_network_interface(
        self,
        arns: "aws_sdk_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.batch_get_router_network_interface.async_batch_get_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
