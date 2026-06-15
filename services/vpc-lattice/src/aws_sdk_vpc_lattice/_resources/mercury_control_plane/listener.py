from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_listener_request
    import aws_sdk_vpc_lattice.types.create_listener_response
    import aws_sdk_vpc_lattice.types.delete_listener_request
    import aws_sdk_vpc_lattice.types.delete_listener_response
    import aws_sdk_vpc_lattice.types.get_listener_request
    import aws_sdk_vpc_lattice.types.get_listener_response
    import aws_sdk_vpc_lattice.types.list_listeners_request
    import aws_sdk_vpc_lattice.types.list_listeners_response
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.listener_name
    import aws_sdk_vpc_lattice.types.listener_protocol
    import aws_sdk_vpc_lattice.types.listener_summary
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.port
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_listener_request
    import aws_sdk_vpc_lattice.types.update_listener_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Listener:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        name: "aws_sdk_vpc_lattice.types.listener_name.ListenerName",
        protocol: "aws_sdk_vpc_lattice.types.listener_protocol.ListenerProtocol",
        default_action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port: Optional["aws_sdk_vpc_lattice.types.port.Port"] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_listener_response.CreateListenerResponse":
        r"""<p>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html\">Listeners</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            name: <p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            protocol: <p>The listener protocol.</p>
            port: <p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>
            default_action: <p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the listener.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_listener_request.CreateListenerRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_listener_response.CreateListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_listener

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_listener.create_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_listener_request.CreateListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["name"] = name
        input_["protocol"] = protocol
        if port is not None:
            input_["port"] = port
        input_["default_action"] = default_action
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_listener_response.GetListenerResponse":
        """<p>Retrieves information about the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_listener_request.GetListenerRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_listener_response.GetListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_listener

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_listener.get_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_listener_request.GetListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        default_action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_listener_response.UpdateListenerResponse":
        """<p>Updates the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            default_action: <p>The action for the default rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_listener_request.UpdateListenerRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_listener_response.UpdateListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_listener

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_listener.update_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_listener_request.UpdateListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["default_action"] = default_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_listener_response.DeleteListenerResponse":
        """<p>Deletes the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_listener_request.DeleteListenerRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_listener_response.DeleteListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_listener

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_listener.delete_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_listener_request.DeleteListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_listeners_response.ListListenersResponse":
        """<p>Lists the listeners for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_listeners_request.ListListenersRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_listeners_response.ListListenersResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_listeners

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_listeners.list_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_listeners_request.ListListenersRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
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


class AsyncListener:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        name: "aws_sdk_vpc_lattice.types.listener_name.ListenerName",
        protocol: "aws_sdk_vpc_lattice.types.listener_protocol.ListenerProtocol",
        default_action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        port: Optional["aws_sdk_vpc_lattice.types.port.Port"] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_listener_response.CreateListenerResponse":
        r"""<p>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html\">Listeners</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            name: <p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            protocol: <p>The listener protocol.</p>
            port: <p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>
            default_action: <p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the listener.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_listener_request.CreateListenerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_listener_response.CreateListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_listener

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_listener.async_create_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_listener_request.CreateListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["name"] = name
        input_["protocol"] = protocol
        if port is not None:
            input_["port"] = port
        input_["default_action"] = default_action
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_listener_response.GetListenerResponse":
        """<p>Retrieves information about the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_listener_request.GetListenerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_listener_response.GetListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_listener

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_listener.async_get_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_listener_request.GetListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        default_action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_listener_response.UpdateListenerResponse":
        """<p>Updates the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            default_action: <p>The action for the default rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_listener_request.UpdateListenerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_listener_response.UpdateListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_listener

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_listener.async_update_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_listener_request.UpdateListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["default_action"] = default_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_listener_response.DeleteListenerResponse":
        """<p>Deletes the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_listener_request.DeleteListenerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_listener_response.DeleteListenerResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_listener

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_listener.async_delete_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_listener_request.DeleteListenerRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_listeners_response.ListListenersResponse":
        """<p>Lists the listeners for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_listeners_request.ListListenersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_listeners_response.ListListenersResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_listeners

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_listeners.async_list_listeners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_listeners_request.ListListenersRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
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
