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
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_service_network_request
    import aws_sdk_vpc_lattice.types.create_service_network_response
    import aws_sdk_vpc_lattice.types.delete_service_network_request
    import aws_sdk_vpc_lattice.types.delete_service_network_response
    import aws_sdk_vpc_lattice.types.get_service_network_request
    import aws_sdk_vpc_lattice.types.get_service_network_response
    import aws_sdk_vpc_lattice.types.list_service_networks_request
    import aws_sdk_vpc_lattice.types.list_service_networks_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.service_network_summary
    import aws_sdk_vpc_lattice.types.sharing_config
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_service_network_request
    import aws_sdk_vpc_lattice.types.update_service_network_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ServiceNetwork:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        sharing_config: Optional[
            "aws_sdk_vpc_lattice.types.sharing_config.SharingConfig"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse":
        r"""<p>Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html\">Service networks</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            tags: <p>The tags for the service network.</p>
            sharing_config: <p>Specify if the service network should be enabled for sharing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network.create_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if tags is not None:
            input_["tags"] = tags
        if sharing_config is not None:
            input_["sharing_config"] = sharing_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse":
        """<p>Retrieves information about the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network.get_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        auth_type: "aws_sdk_vpc_lattice.types.auth_type.AuthType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse":
        """<p>Updates the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network.update_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier
        input_["auth_type"] = auth_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse":
        r"""<p>Deletes a service network. You can only delete the service network if there is no service or VPC associated with it. If you delete a service network, all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions, are also deleted. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#delete-service-network\">Delete a service network</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network.delete_service_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse":
        """<p>Lists the service networks owned by or shared with this account. The account ID in the ARN shows which account owns the service network.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_networks

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_networks.list_service_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest = {}  # type: ignore[typeddict-item]
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


class AsyncServiceNetwork:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        sharing_config: Optional[
            "aws_sdk_vpc_lattice.types.sharing_config.SharingConfig"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse":
        r"""<p>Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html\">Service networks</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            tags: <p>The tags for the service network.</p>
            sharing_config: <p>Specify if the service network should be enabled for sharing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_response.CreateServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network.async_create_service_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_request.CreateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if tags is not None:
            input_["tags"] = tags
        if sharing_config is not None:
            input_["sharing_config"] = sharing_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse":
        """<p>Retrieves information about the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_response.GetServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network.async_get_service_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_request.GetServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        auth_type: "aws_sdk_vpc_lattice.types.auth_type.AuthType",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse":
        """<p>Updates the specified service network.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_network_response.UpdateServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network.async_update_service_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_network_request.UpdateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier
        input_["auth_type"] = auth_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse":
        r"""<p>Deletes a service network. You can only delete the service network if there is no service or VPC associated with it. If you delete a service network, all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions, are also deleted. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#delete-service-network\">Delete a service network</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_response.DeleteServiceNetworkResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network.async_delete_service_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_request.DeleteServiceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse":
        """<p>Lists the service networks owned by or shared with this account. The account ID in the ARN shows which account owns the service network.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_networks_response.ListServiceNetworksResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_networks

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_networks.async_list_service_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_networks_request.ListServiceNetworksRequest = {}  # type: ignore[typeddict-item]
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
