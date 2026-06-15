"""Generated from Smithy shape ``com.amazonaws.directconnect#OvertureService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_direct_connect._auth._signers
import aws_sdk_direct_connect._auth._sigv4
from aws_sdk_direct_connect._auth._identity import Credentials
from aws_sdk_direct_connect._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_direct_connect._auth._zapros_handler import AuthMiddleware
from aws_sdk_direct_connect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_request
    import aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_result
    import aws_sdk_direct_connect.types.agreement_name
    import aws_sdk_direct_connect.types.allocate_connection_on_interconnect_request
    import aws_sdk_direct_connect.types.allocate_hosted_connection_request
    import aws_sdk_direct_connect.types.allocate_private_virtual_interface_request
    import aws_sdk_direct_connect.types.allocate_public_virtual_interface_request
    import aws_sdk_direct_connect.types.allocate_transit_virtual_interface_request
    import aws_sdk_direct_connect.types.allocate_transit_virtual_interface_result
    import aws_sdk_direct_connect.types.asn
    import aws_sdk_direct_connect.types.associate_connection_with_lag_request
    import aws_sdk_direct_connect.types.associate_hosted_connection_request
    import aws_sdk_direct_connect.types.associate_mac_sec_key_request
    import aws_sdk_direct_connect.types.associate_mac_sec_key_response
    import aws_sdk_direct_connect.types.associate_virtual_interface_request
    import aws_sdk_direct_connect.types.associated_gateway_id
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.bgp_peer_id
    import aws_sdk_direct_connect.types.bgp_peer_id_list
    import aws_sdk_direct_connect.types.cak
    import aws_sdk_direct_connect.types.ckn
    import aws_sdk_direct_connect.types.confirm_connection_request
    import aws_sdk_direct_connect.types.confirm_connection_response
    import aws_sdk_direct_connect.types.confirm_customer_agreement_request
    import aws_sdk_direct_connect.types.confirm_customer_agreement_response
    import aws_sdk_direct_connect.types.confirm_private_virtual_interface_request
    import aws_sdk_direct_connect.types.confirm_private_virtual_interface_response
    import aws_sdk_direct_connect.types.confirm_public_virtual_interface_request
    import aws_sdk_direct_connect.types.confirm_public_virtual_interface_response
    import aws_sdk_direct_connect.types.confirm_transit_virtual_interface_request
    import aws_sdk_direct_connect.types.confirm_transit_virtual_interface_response
    import aws_sdk_direct_connect.types.connection
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.connection_name
    import aws_sdk_direct_connect.types.connections
    import aws_sdk_direct_connect.types.count
    import aws_sdk_direct_connect.types.create_bgp_peer_request
    import aws_sdk_direct_connect.types.create_bgp_peer_response
    import aws_sdk_direct_connect.types.create_connection_request
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_request
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_result
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_association_request
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_association_result
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_request
    import aws_sdk_direct_connect.types.create_direct_connect_gateway_result
    import aws_sdk_direct_connect.types.create_interconnect_request
    import aws_sdk_direct_connect.types.create_lag_request
    import aws_sdk_direct_connect.types.create_private_virtual_interface_request
    import aws_sdk_direct_connect.types.create_public_virtual_interface_request
    import aws_sdk_direct_connect.types.create_transit_virtual_interface_request
    import aws_sdk_direct_connect.types.create_transit_virtual_interface_result
    import aws_sdk_direct_connect.types.customer_address
    import aws_sdk_direct_connect.types.delete_bgp_peer_request
    import aws_sdk_direct_connect.types.delete_bgp_peer_response
    import aws_sdk_direct_connect.types.delete_connection_request
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_request
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_result
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_request
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_result
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_request
    import aws_sdk_direct_connect.types.delete_direct_connect_gateway_result
    import aws_sdk_direct_connect.types.delete_interconnect_request
    import aws_sdk_direct_connect.types.delete_interconnect_response
    import aws_sdk_direct_connect.types.delete_lag_request
    import aws_sdk_direct_connect.types.delete_virtual_interface_request
    import aws_sdk_direct_connect.types.delete_virtual_interface_response
    import aws_sdk_direct_connect.types.describe_connection_loa_request
    import aws_sdk_direct_connect.types.describe_connection_loa_response
    import aws_sdk_direct_connect.types.describe_connections_on_interconnect_request
    import aws_sdk_direct_connect.types.describe_connections_request
    import aws_sdk_direct_connect.types.describe_customer_metadata_response
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_request
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_result
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_request
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_result
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_request
    import aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_result
    import aws_sdk_direct_connect.types.describe_direct_connect_gateways_request
    import aws_sdk_direct_connect.types.describe_direct_connect_gateways_result
    import aws_sdk_direct_connect.types.describe_hosted_connections_request
    import aws_sdk_direct_connect.types.describe_interconnect_loa_request
    import aws_sdk_direct_connect.types.describe_interconnect_loa_response
    import aws_sdk_direct_connect.types.describe_interconnects_request
    import aws_sdk_direct_connect.types.describe_lags_request
    import aws_sdk_direct_connect.types.describe_loa_request
    import aws_sdk_direct_connect.types.describe_router_configuration_request
    import aws_sdk_direct_connect.types.describe_router_configuration_response
    import aws_sdk_direct_connect.types.describe_tags_request
    import aws_sdk_direct_connect.types.describe_tags_response
    import aws_sdk_direct_connect.types.describe_virtual_interfaces_request
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_id
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.direct_connect_gateway_name
    import aws_sdk_direct_connect.types.disassociate_connection_from_lag_request
    import aws_sdk_direct_connect.types.disassociate_mac_sec_key_request
    import aws_sdk_direct_connect.types.disassociate_mac_sec_key_response
    import aws_sdk_direct_connect.types.enable_site_link
    import aws_sdk_direct_connect.types.encryption_mode
    import aws_sdk_direct_connect.types.failure_test_history_status
    import aws_sdk_direct_connect.types.gateway_id_to_associate
    import aws_sdk_direct_connect.types.interconnect
    import aws_sdk_direct_connect.types.interconnect_id
    import aws_sdk_direct_connect.types.interconnect_name
    import aws_sdk_direct_connect.types.interconnects
    import aws_sdk_direct_connect.types.lag
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.lag_name
    import aws_sdk_direct_connect.types.lags
    import aws_sdk_direct_connect.types.list_virtual_interface_test_history_request
    import aws_sdk_direct_connect.types.list_virtual_interface_test_history_response
    import aws_sdk_direct_connect.types.loa
    import aws_sdk_direct_connect.types.loa_content_type
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.locations
    import aws_sdk_direct_connect.types.long_asn
    import aws_sdk_direct_connect.types.max_result_set_size
    import aws_sdk_direct_connect.types.mtu
    import aws_sdk_direct_connect.types.new_bgp_peer
    import aws_sdk_direct_connect.types.new_private_virtual_interface
    import aws_sdk_direct_connect.types.new_private_virtual_interface_allocation
    import aws_sdk_direct_connect.types.new_public_virtual_interface
    import aws_sdk_direct_connect.types.new_public_virtual_interface_allocation
    import aws_sdk_direct_connect.types.new_transit_virtual_interface
    import aws_sdk_direct_connect.types.new_transit_virtual_interface_allocation
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.pagination_token
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.request_mac_sec
    import aws_sdk_direct_connect.types.resource_arn
    import aws_sdk_direct_connect.types.resource_arn_list
    import aws_sdk_direct_connect.types.route_filter_prefix_list
    import aws_sdk_direct_connect.types.router_type_identifier
    import aws_sdk_direct_connect.types.secret_arn
    import aws_sdk_direct_connect.types.start_bgp_failover_test_request
    import aws_sdk_direct_connect.types.start_bgp_failover_test_response
    import aws_sdk_direct_connect.types.stop_bgp_failover_test_request
    import aws_sdk_direct_connect.types.stop_bgp_failover_test_response
    import aws_sdk_direct_connect.types.tag_key_list
    import aws_sdk_direct_connect.types.tag_list
    import aws_sdk_direct_connect.types.tag_resource_request
    import aws_sdk_direct_connect.types.tag_resource_response
    import aws_sdk_direct_connect.types.test_duration
    import aws_sdk_direct_connect.types.test_id
    import aws_sdk_direct_connect.types.untag_resource_request
    import aws_sdk_direct_connect.types.untag_resource_response
    import aws_sdk_direct_connect.types.update_connection_request
    import aws_sdk_direct_connect.types.update_direct_connect_gateway_association_request
    import aws_sdk_direct_connect.types.update_direct_connect_gateway_association_result
    import aws_sdk_direct_connect.types.update_direct_connect_gateway_request
    import aws_sdk_direct_connect.types.update_direct_connect_gateway_response
    import aws_sdk_direct_connect.types.update_lag_request
    import aws_sdk_direct_connect.types.update_virtual_interface_attributes_request
    import aws_sdk_direct_connect.types.virtual_gateway_id
    import aws_sdk_direct_connect.types.virtual_gateways
    import aws_sdk_direct_connect.types.virtual_interface
    import aws_sdk_direct_connect.types.virtual_interface_id
    import aws_sdk_direct_connect.types.virtual_interface_name
    import aws_sdk_direct_connect.types.virtual_interfaces
    import aws_sdk_direct_connect.types.vlan


class AsyncDirectConnectClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncDirectConnectClient:
    """A client for the ``DirectConnect`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncDirectConnectClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDirectConnectClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def accept_direct_connect_gateway_association_proposal(
        self,
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        proposal_id: "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId",
        associated_gateway_owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        override_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_result.AcceptDirectConnectGatewayAssociationProposalResult":
        r"""<p>Accepts a proposal request to attach a virtual private gateway or transit gateway to a Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            proposal_id: <p>The ID of the request proposal.</p>
            associated_gateway_owner_account: <p>The ID of the Amazon Web Services account that owns the virtual private gateway or transit gateway.</p>
            override_allowed_prefixes_to_direct_connect_gateway: <p>Overrides the Amazon VPC prefixes advertised to the Direct Connect gateway.</p> <p>For information about how to set the prefixes, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes\">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_request.AcceptDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_result.AcceptDirectConnectGatewayAssociationProposalResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.accept_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.accept_direct_connect_gateway_association_proposal.async_accept_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.accept_direct_connect_gateway_association_proposal_request.AcceptDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        input_["proposal_id"] = proposal_id
        input_["associated_gateway_owner_account"] = associated_gateway_owner_account
        if override_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["override_allowed_prefixes_to_direct_connect_gateway"] = (
                override_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_connection_on_interconnect(
        self,
        bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "aws_sdk_direct_connect.types.connection_name.ConnectionName",
        owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId",
        vlan: "aws_sdk_direct_connect.types.vlan.VLAN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<note> <p>Deprecated. Use <a>AllocateHostedConnection</a> instead.</p> </note> <p>Creates a hosted connection on an interconnect.</p> <p>Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            bandwidth: <p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.</p>
            connection_name: <p>The name of the provisioned connection.</p>
            owner_account: <p>The ID of the Amazon Web Services account of the customer for whom the connection will be provisioned.</p>
            interconnect_id: <p>The ID of the interconnect on which the connection will be provisioned.</p>
            vlan: <p>The dedicated VLAN provisioned to the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.allocate_connection_on_interconnect_request.AllocateConnectionOnInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.allocate_connection_on_interconnect

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.allocate_connection_on_interconnect.async_allocate_connection_on_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.allocate_connection_on_interconnect_request.AllocateConnectionOnInterconnectRequest = {}  # type: ignore[typeddict-item]
        input_["bandwidth"] = bandwidth
        input_["connection_name"] = connection_name
        input_["owner_account"] = owner_account
        input_["interconnect_id"] = interconnect_id
        input_["vlan"] = vlan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_hosted_connection(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "aws_sdk_direct_connect.types.connection_name.ConnectionName",
        vlan: "aws_sdk_direct_connect.types.vlan.VLAN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        tags: Optional["aws_sdk_direct_connect.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Creates a hosted connection on the specified interconnect or a link aggregation group (LAG) of interconnects.</p> <p>Allocates a VLAN number and a specified amount of capacity (bandwidth) for use by a hosted connection on the specified interconnect or LAG of interconnects. Amazon Web Services polices the hosted connection for the specified capacity and the Direct Connect Partner must also police the hosted connection for the specified capacity.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the interconnect or LAG.</p>
            owner_account: <p>The ID of the Amazon Web Services account ID of the customer for the connection.</p>
            bandwidth: <p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps, and 25Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps, 10Gbps, or 25Gbps hosted connection. </p>
            connection_name: <p>The name of the hosted connection.</p>
            vlan: <p>The dedicated VLAN provisioned to the hosted connection.</p>
            tags: <p>The tags associated with the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.allocate_hosted_connection_request.AllocateHostedConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.allocate_hosted_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.allocate_hosted_connection.async_allocate_hosted_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.allocate_hosted_connection_request.AllocateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["owner_account"] = owner_account
        input_["bandwidth"] = bandwidth
        input_["connection_name"] = connection_name
        input_["vlan"] = vlan
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_private_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        new_private_virtual_interface_allocation: "aws_sdk_direct_connect.types.new_private_virtual_interface_allocation.NewPrivateVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Provisions a private virtual interface to be owned by the specified Amazon Web Services account.</p> <p>Virtual interfaces created using this action must be confirmed by the owner using <a>ConfirmPrivateVirtualInterface</a>. Until then, the virtual interface is in the <code>Confirming</code> state and is not available to handle traffic.</p>

        Args:
            connection_id: <p>The ID of the connection on which the private virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the virtual private interface.</p>
            new_private_virtual_interface_allocation: <p>Information about the private virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.allocate_private_virtual_interface_request.AllocatePrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.allocate_private_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.allocate_private_virtual_interface.async_allocate_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.allocate_private_virtual_interface_request.AllocatePrivateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["owner_account"] = owner_account
        input_["new_private_virtual_interface_allocation"] = (
            new_private_virtual_interface_allocation
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_public_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        new_public_virtual_interface_allocation: "aws_sdk_direct_connect.types.new_public_virtual_interface_allocation.NewPublicVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Provisions a public virtual interface to be owned by the specified Amazon Web Services account.</p> <p>The owner of a connection calls this function to provision a public virtual interface to be owned by the specified Amazon Web Services account.</p> <p>Virtual interfaces created using this function must be confirmed by the owner using <a>ConfirmPublicVirtualInterface</a>. Until this step has been completed, the virtual interface is in the <code>confirming</code> state and is not available to handle traffic.</p> <p>When creating an IPv6 public virtual interface, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.</p>

        Args:
            connection_id: <p>The ID of the connection on which the public virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the public virtual interface.</p>
            new_public_virtual_interface_allocation: <p>Information about the public virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.allocate_public_virtual_interface_request.AllocatePublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.allocate_public_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.allocate_public_virtual_interface.async_allocate_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.allocate_public_virtual_interface_request.AllocatePublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["owner_account"] = owner_account
        input_["new_public_virtual_interface_allocation"] = (
            new_public_virtual_interface_allocation
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_transit_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        new_transit_virtual_interface_allocation: "aws_sdk_direct_connect.types.new_transit_virtual_interface_allocation.NewTransitVirtualInterfaceAllocation",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.allocate_transit_virtual_interface_result.AllocateTransitVirtualInterfaceResult":
        """<p>Provisions a transit virtual interface to be owned by the specified Amazon Web Services account. Use this type of interface to connect a transit gateway to your Direct Connect gateway.</p> <p>The owner of a connection provisions a transit virtual interface to be owned by the specified Amazon Web Services account.</p> <p>After you create a transit virtual interface, it must be confirmed by the owner using <a>ConfirmTransitVirtualInterface</a>. Until this step has been completed, the transit virtual interface is in the <code>requested</code> state and is not available to handle traffic.</p>

        Args:
            connection_id: <p>The ID of the connection on which the transit virtual interface is provisioned.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the transit virtual interface.</p>
            new_transit_virtual_interface_allocation: <p>Information about the transit virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.allocate_transit_virtual_interface_request.AllocateTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.allocate_transit_virtual_interface_result.AllocateTransitVirtualInterfaceResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.allocate_transit_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.allocate_transit_virtual_interface.async_allocate_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.allocate_transit_virtual_interface_request.AllocateTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["owner_account"] = owner_account
        input_["new_transit_virtual_interface_allocation"] = (
            new_transit_virtual_interface_allocation
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_connection_with_lag(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        lag_id: "aws_sdk_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to Amazon Web Services is interrupted). The connection must be hosted on the same Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can re-associate a connection that's currently associated with a different LAG; however, if removing the connection would cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.</p> <p>Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.</p> <p>For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            lag_id: <p>The ID of the LAG with which to associate the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.associate_connection_with_lag_request.AssociateConnectionWithLagRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.associate_connection_with_lag

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.associate_connection_with_lag.async_associate_connection_with_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.associate_connection_with_lag_request.AssociateConnectionWithLagRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["lag_id"] = lag_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_hosted_connection(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        parent_connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection's connectivity to Amazon Web Services as it is being migrated.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the hosted connection.</p>
            parent_connection_id: <p>The ID of the interconnect or the LAG.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.associate_hosted_connection_request.AssociateHostedConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.associate_hosted_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.associate_hosted_connection.async_associate_hosted_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.associate_hosted_connection_request.AssociateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["parent_connection_id"] = parent_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_mac_sec_key(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        secret_arn: Optional[
            "aws_sdk_direct_connect.types.secret_arn.SecretARN"
        ] = None,
        ckn: Optional["aws_sdk_direct_connect.types.ckn.Ckn"] = None,
        cak: Optional["aws_sdk_direct_connect.types.cak.Cak"] = None,
    ) -> "aws_sdk_direct_connect.types.associate_mac_sec_key_response.AssociateMacSecKeyResponse":
        r"""<p>Associates a MAC Security (MACsec) Connection Key Name (CKN)/ Connectivity Association Key (CAK) pair with a Direct Connect connection.</p> <p>You must supply either the <code>secretARN,</code> or the CKN/CAK (<code>ckn</code> and <code>cak</code>) pair in the request.</p> <p>For information about MAC Security (MACsec) key considerations, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-key-consideration\">MACsec pre-shared CKN/CAK key considerations </a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>
            secret_arn: <p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the connection.</p> <p>You can use <a>DescribeConnections</a> or <a>DescribeLags</a> to retrieve the MAC Security (MACsec) secret key.</p> <p>If you use this request parameter, you do not use the <code>ckn</code> and <code>cak</code> request parameters.</p>
            ckn: <p>The MAC Security (MACsec) CKN to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>cak</code> request parameter and not use the <code>secretARN</code> request parameter.</p>
            cak: <p>The MAC Security (MACsec) CAK to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>ckn</code> request parameter and not use the <code>secretARN</code> request parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.associate_mac_sec_key_request.AssociateMacSecKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.associate_mac_sec_key_response.AssociateMacSecKeyResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.associate_mac_sec_key

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.associate_mac_sec_key.async_associate_mac_sec_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.associate_mac_sec_key_request.AssociateMacSecKeyRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if ckn is not None:
            input_["ckn"] = ckn
        if cak is not None:
            input_["cak"] = cak

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_virtual_interface(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to Amazon Web Services is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.</p> <p>Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using <a>AssociateHostedConnection</a>.</p> <p>To reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG for the association.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            connection_id: <p>The ID of the LAG or connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.associate_virtual_interface_request.AssociateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.associate_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.associate_virtual_interface.async_associate_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.associate_virtual_interface_request.AssociateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_connection(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.confirm_connection_response.ConfirmConnectionResponse":
        """<p>Confirms the creation of the specified hosted connection on an interconnect.</p> <p>Upon creation, the hosted connection is initially in the <code>Ordering</code> state, and remains in this state until the owner confirms creation of the hosted connection.</p>

        Args:
            connection_id: <p>The ID of the hosted connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.confirm_connection_request.ConfirmConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.confirm_connection_response.ConfirmConnectionResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.confirm_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.confirm_connection.async_confirm_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.confirm_connection_request.ConfirmConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_customer_agreement(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        agreement_name: Optional[
            "aws_sdk_direct_connect.types.agreement_name.AgreementName"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.confirm_customer_agreement_response.ConfirmCustomerAgreementResponse":
        """<p> The confirmation of the terms of agreement when creating the connection/link aggregation group (LAG). </p>

        Args:
            agreement_name: <p> The name of the customer agreement. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.confirm_customer_agreement_request.ConfirmCustomerAgreementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.confirm_customer_agreement_response.ConfirmCustomerAgreementResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.confirm_customer_agreement

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.confirm_customer_agreement.async_confirm_customer_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.confirm_customer_agreement_request.ConfirmCustomerAgreementRequest = {}  # type: ignore[typeddict-item]
        if agreement_name is not None:
            input_["agreement_name"] = agreement_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_private_virtual_interface(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_gateway_id: Optional[
            "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.confirm_private_virtual_interface_response.ConfirmPrivateVirtualInterfaceResponse":
        """<p>Accepts ownership of a private virtual interface created by another Amazon Web Services account.</p> <p>After the virtual interface owner makes this call, the virtual interface is created and attached to the specified virtual private gateway or Direct Connect gateway, and is made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.confirm_private_virtual_interface_request.ConfirmPrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.confirm_private_virtual_interface_response.ConfirmPrivateVirtualInterfaceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.confirm_private_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.confirm_private_virtual_interface.async_confirm_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.confirm_private_virtual_interface_request.ConfirmPrivateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_public_virtual_interface(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.confirm_public_virtual_interface_response.ConfirmPublicVirtualInterfaceResponse":
        """<p>Accepts ownership of a public virtual interface created by another Amazon Web Services account.</p> <p>After the virtual interface owner makes this call, the specified virtual interface is created and made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.confirm_public_virtual_interface_request.ConfirmPublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.confirm_public_virtual_interface_response.ConfirmPublicVirtualInterfaceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.confirm_public_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.confirm_public_virtual_interface.async_confirm_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.confirm_public_virtual_interface_request.ConfirmPublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_transit_virtual_interface(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.confirm_transit_virtual_interface_response.ConfirmTransitVirtualInterfaceResponse":
        """<p>Accepts ownership of a transit virtual interface created by another Amazon Web Services account.</p> <p> After the owner of the transit virtual interface makes this call, the specified transit virtual interface is created and made available to handle traffic.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.confirm_transit_virtual_interface_request.ConfirmTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.confirm_transit_virtual_interface_response.ConfirmTransitVirtualInterfaceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.confirm_transit_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.confirm_transit_virtual_interface.async_confirm_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.confirm_transit_virtual_interface_request.ConfirmTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_bgp_peer(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_interface_id: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        new_bgp_peer: Optional[
            "aws_sdk_direct_connect.types.new_bgp_peer.NewBGPPeer"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.create_bgp_peer_response.CreateBGPPeerResponse":
        r"""<p>Creates a BGP peer on the specified virtual interface.</p> <p>You must create a BGP peer for the corresponding address family (IPv4/IPv6) in order to access Amazon Web Services resources that also use that address family.</p> <p>If logical redundancy is not supported by the connection, interconnect, or LAG, the BGP peer cannot be in the same address family as an existing BGP peer on the virtual interface.</p> <p>When creating a IPv6 BGP peer, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.</p> <important> <p>If you let Amazon Web Services auto-assign IPv4 addresses, a /30 CIDR will be allocated from 169.254.0.0/16. Amazon Web Services does not recommend this option if you intend to use the customer router peer IP address as the source and destination for traffic. Instead you should use RFC 1918 or other addressing, and specify the address yourself. For more information about RFC 1918 see <a href=\"https://datatracker.ietf.org/doc/html/rfc1918\"> Address Allocation for Private Internets</a>.</p> </important> <p>For a public virtual interface, the Autonomous System Number (ASN) must be private or already on the allow list for the virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            new_bgp_peer: <p>Information about the BGP peer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_bgp_peer_request.CreateBGPPeerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.create_bgp_peer_response.CreateBGPPeerResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_bgp_peer

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_bgp_peer.async_create_bgp_peer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_bgp_peer_request.CreateBGPPeerRequest = {}  # type: ignore[typeddict-item]
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if new_bgp_peer is not None:
            input_["new_bgp_peer"] = new_bgp_peer

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_connection(
        self,
        location: "aws_sdk_direct_connect.types.location_code.LocationCode",
        bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth",
        connection_name: "aws_sdk_direct_connect.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["aws_sdk_direct_connect.types.lag_id.LagId"] = None,
        tags: Optional["aws_sdk_direct_connect.types.tag_list.TagList"] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        r"""<p>Creates a connection between a customer network and a specific Direct Connect location.</p> <p>A connection links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router.</p> <p>To find the locations for your Region, use <a>DescribeLocations</a>.</p> <p>You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.</p>

        Args:
            location: <p>The location of the connection.</p>
            bandwidth: <p>The bandwidth of the connection.</p>
            connection_name: <p>The name of the connection.</p>
            lag_id: <p>The ID of the LAG.</p>
            tags: <p>The tags to associate with the lag.</p>
            provider_name: <p>The name of the service provider associated with the requested connection.</p>
            request_mac_sec: <p>Indicates whether you want the connection to support MAC Security (MACsec).</p> <p>MAC Security (MACsec) is unavailable on hosted connections. For information about MAC Security (MACsec) prerequisites, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACSec.html\">MAC Security in Direct Connect</a> in the <i>Direct Connect User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_connection_request.CreateConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["location"] = location
        input_["bandwidth"] = bandwidth
        input_["connection_name"] = connection_name
        if lag_id is not None:
            input_["lag_id"] = lag_id
        if tags is not None:
            input_["tags"] = tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_direct_connect_gateway(
        self,
        direct_connect_gateway_name: "aws_sdk_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        tags: Optional["aws_sdk_direct_connect.types.tag_list.TagList"] = None,
        amazon_side_asn: Optional[
            "aws_sdk_direct_connect.types.long_asn.LongAsn"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.create_direct_connect_gateway_result.CreateDirectConnectGatewayResult":
        """<p>Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any Amazon Web Services Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different Amazon Web Services Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.</p>

        Args:
            direct_connect_gateway_name: <p>The name of the Direct Connect gateway.</p>
            tags: <p>The key-value pair tags associated with the request.</p>
            amazon_side_asn: <p>The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_direct_connect_gateway_request.CreateDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.create_direct_connect_gateway_result.CreateDirectConnectGatewayResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway.async_create_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_direct_connect_gateway_request.CreateDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_name"] = direct_connect_gateway_name
        if tags is not None:
            input_["tags"] = tags
        if amazon_side_asn is not None:
            input_["amazon_side_asn"] = amazon_side_asn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_direct_connect_gateway_association(
        self,
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        gateway_id: Optional[
            "aws_sdk_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate"
        ] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        virtual_gateway_id: Optional[
            "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.create_direct_connect_gateway_association_result.CreateDirectConnectGatewayAssociationResult":
        r"""<p>Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway</p> <p>This parameter is required when you create an association to a transit gateway.</p> <p>For information about how to set the prefixes, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes\">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_direct_connect_gateway_association_request.CreateDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.create_direct_connect_gateway_association_result.CreateDirectConnectGatewayAssociationResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway_association.async_create_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_direct_connect_gateway_association_request.CreateDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if gateway_id is not None:
            input_["gateway_id"] = gateway_id
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_direct_connect_gateway_association_proposal(
        self,
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        direct_connect_gateway_owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount",
        gateway_id: "aws_sdk_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        remove_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_result.CreateDirectConnectGatewayAssociationProposalResult":
        """<p>Creates a proposal to associate the specified virtual private gateway or transit gateway with the specified Direct Connect gateway.</p> <p>You can associate a Direct Connect gateway and virtual private gateway or transit gateway that is owned by any Amazon Web Services account. </p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            direct_connect_gateway_owner_account: <p>The ID of the Amazon Web Services account that owns the Direct Connect gateway.</p>
            gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>
            remove_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_request.CreateDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_result.CreateDirectConnectGatewayAssociationProposalResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_direct_connect_gateway_association_proposal.async_create_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_direct_connect_gateway_association_proposal_request.CreateDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        input_["direct_connect_gateway_owner_account"] = (
            direct_connect_gateway_owner_account
        )
        input_["gateway_id"] = gateway_id
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if remove_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["remove_allowed_prefixes_to_direct_connect_gateway"] = (
                remove_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_interconnect(
        self,
        interconnect_name: "aws_sdk_direct_connect.types.interconnect_name.InterconnectName",
        bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth",
        location: "aws_sdk_direct_connect.types.location_code.LocationCode",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["aws_sdk_direct_connect.types.lag_id.LagId"] = None,
        tags: Optional["aws_sdk_direct_connect.types.tag_list.TagList"] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.interconnect.Interconnect":
        """<p>Creates an interconnect between an Direct Connect Partner's network and a specific Direct Connect location.</p> <p>An interconnect is a connection that is capable of hosting other connections. The Direct Connect Partner can use an interconnect to provide Direct Connect hosted connections to customers through their own network services. Like a standard connection, an interconnect links the partner's network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an Direct Connect router.</p> <p>You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect is created.</p> <p>For each end customer, the Direct Connect Partner provisions a connection on their interconnect by calling <a>AllocateHostedConnection</a>. The end customer can then connect to Amazon Web Services resources by creating a virtual interface on their connection, using the VLAN assigned to them by the Direct Connect Partner.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_name: <p>The name of the interconnect.</p>
            bandwidth: <p>The port bandwidth, in Gbps. The possible values are 1, 10, and 100.</p>
            location: <p>The location of the interconnect.</p>
            lag_id: <p>The ID of the LAG.</p>
            tags: <p>The tags to associate with the interconnect.</p>
            provider_name: <p>The name of the service provider associated with the interconnect.</p>
            request_mac_sec: <p>Indicates whether you want the interconnect to support MAC Security (MACsec).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_interconnect_request.CreateInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.interconnect.Interconnect"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_interconnect

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_interconnect.async_create_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_interconnect_request.CreateInterconnectRequest = {}  # type: ignore[typeddict-item]
        input_["interconnect_name"] = interconnect_name
        input_["bandwidth"] = bandwidth
        input_["location"] = location
        if lag_id is not None:
            input_["lag_id"] = lag_id
        if tags is not None:
            input_["tags"] = tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_lag(
        self,
        number_of_connections: "aws_sdk_direct_connect.types.count.Count",
        location: "aws_sdk_direct_connect.types.location_code.LocationCode",
        connections_bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth",
        lag_name: "aws_sdk_direct_connect.types.lag_name.LagName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "aws_sdk_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        tags: Optional["aws_sdk_direct_connect.types.tag_list.TagList"] = None,
        child_connection_tags: Optional[
            "aws_sdk_direct_connect.types.tag_list.TagList"
        ] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        request_mac_sec: Optional[
            "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.lag.Lag":
        r"""<p>Creates a link aggregation group (LAG) with the specified number of bundled physical dedicated connections between the customer network and a specific Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.</p> <p>All connections in a LAG must use the same bandwidth (either 1Gbps, 10Gbps, 100Gbps, or 400Gbps) and must terminate at the same Direct Connect endpoint.</p> <p>You can have up to 10 dedicated connections per location. Regardless of this limit, if you request more connections for the LAG than Direct Connect can allocate on a single endpoint, no LAG is created..</p> <p>You can specify an existing physical dedicated connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical dedicated connection, and re-establishes them as a member of the LAG. The LAG will be created on the same Direct Connect endpoint to which the dedicated connection terminates. Any virtual interfaces associated with the dedicated connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.</p> <p>If the Amazon Web Services account used to create a LAG is a registered Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.</p>

        Args:
            number_of_connections: <p>The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.</p>
            location: <p>The location for the LAG.</p>
            connections_bandwidth: <p>The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps. </p>
            lag_name: <p>The name of the LAG.</p>
            connection_id: <p>The ID of an existing dedicated connection to migrate to the LAG.</p>
            tags: <p>The tags to associate with the LAG.</p>
            child_connection_tags: <p>The tags to associate with the automtically created LAGs.</p>
            provider_name: <p>The name of the service provider associated with the LAG.</p>
            request_mac_sec: <p>Indicates whether the connection will support MAC Security (MACsec).</p> <note> <p>All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites\">MACsec prerequisties</a> in the <i>Direct Connect User Guide</i>.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_lag_request.CreateLagRequest]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.lag.Lag"]:
            import aws_sdk_direct_connect._operations.overture_service.create_lag

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_lag.async_create_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_lag_request.CreateLagRequest = {}  # type: ignore[typeddict-item]
        input_["number_of_connections"] = number_of_connections
        input_["location"] = location
        input_["connections_bandwidth"] = connections_bandwidth
        input_["lag_name"] = lag_name
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if tags is not None:
            input_["tags"] = tags
        if child_connection_tags is not None:
            input_["child_connection_tags"] = child_connection_tags
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if request_mac_sec is not None:
            input_["request_mac_sec"] = request_mac_sec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_private_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        new_private_virtual_interface: "aws_sdk_direct_connect.types.new_private_virtual_interface.NewPrivateVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Creates a private virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A private virtual interface can be connected to either a Direct Connect gateway or a Virtual Private Gateway (VGW). Connecting the private virtual interface to a Direct Connect gateway enables the possibility for connecting to multiple VPCs, including VPCs in different Amazon Web Services Regions. Connecting the private virtual interface to a VGW only provides access to a single VPC within the same Region.</p> <p>Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_private_virtual_interface: <p>Information about the private virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_private_virtual_interface_request.CreatePrivateVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_private_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_private_virtual_interface.async_create_private_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_private_virtual_interface_request.CreatePrivateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["new_private_virtual_interface"] = new_private_virtual_interface

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_public_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        new_public_virtual_interface: "aws_sdk_direct_connect.types.new_public_virtual_interface.NewPublicVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Creates a public virtual interface. A virtual interface is the VLAN that transports Direct Connect traffic. A public virtual interface supports sending traffic to public services of Amazon Web Services such as Amazon S3.</p> <p>When creating an IPv6 public virtual interface (<code>addressFamily</code> is <code>ipv6</code>), leave the <code>customer</code> and <code>amazon</code> address fields blank to use auto-assigned IPv6 space. Custom IPv6 addresses are not supported.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_public_virtual_interface: <p>Information about the public virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_public_virtual_interface_request.CreatePublicVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_public_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_public_virtual_interface.async_create_public_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_public_virtual_interface_request.CreatePublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["new_public_virtual_interface"] = new_public_virtual_interface

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_transit_virtual_interface(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        new_transit_virtual_interface: "aws_sdk_direct_connect.types.new_transit_virtual_interface.NewTransitVirtualInterface",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.create_transit_virtual_interface_result.CreateTransitVirtualInterfaceResult":
        """<p>Creates a transit virtual interface. A transit virtual interface should be used to access one or more transit gateways associated with Direct Connect gateways. A transit virtual interface enables the connection of multiple VPCs attached to a transit gateway to a Direct Connect gateway.</p> <important> <p>If you associate your transit gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the transit gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both your the transit gateway and Direct Connect gateway, the association request fails.</p> </important> <p>A jumbo MTU value must be either 1500 or 8500. No other values will be accepted. Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            new_transit_virtual_interface: <p>Information about the transit virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.create_transit_virtual_interface_request.CreateTransitVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.create_transit_virtual_interface_result.CreateTransitVirtualInterfaceResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.create_transit_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.create_transit_virtual_interface.async_create_transit_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.create_transit_virtual_interface_request.CreateTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["new_transit_virtual_interface"] = new_transit_virtual_interface

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_bgp_peer(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        virtual_interface_id: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        asn: Optional["aws_sdk_direct_connect.types.asn.ASN"] = None,
        asn_long: Optional["aws_sdk_direct_connect.types.long_asn.LongAsn"] = None,
        customer_address: Optional[
            "aws_sdk_direct_connect.types.customer_address.CustomerAddress"
        ] = None,
        bgp_peer_id: Optional[
            "aws_sdk_direct_connect.types.bgp_peer_id.BGPPeerId"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.delete_bgp_peer_response.DeleteBGPPeerResponse":
        """<p>Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.</p> <p>You cannot delete the last BGP peer from a virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            asn: <p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>
            asn_long: <p>The long ASN for the BGP peer to be deleted from a Direct Connect virtual interface. The valid range is from 1 to 4294967294 for BGP configuration. </p> <note> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> <ul> <li> <p>The <code>asnLong</code> attribute accepts both ASN and long ASN ranges.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul> </note>
            customer_address: <p>The IP address assigned to the customer interface.</p>
            bgp_peer_id: <p>The ID of the BGP peer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_bgp_peer_request.DeleteBGPPeerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_bgp_peer_response.DeleteBGPPeerResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_bgp_peer

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_bgp_peer.async_delete_bgp_peer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_bgp_peer_request.DeleteBGPPeerRequest = {}  # type: ignore[typeddict-item]
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if asn is not None:
            input_["asn"] = asn
        if asn_long is not None:
            input_["asn_long"] = asn_long
        if customer_address is not None:
            input_["customer_address"] = customer_address
        if bgp_peer_id is not None:
            input_["bgp_peer_id"] = bgp_peer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_connection(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Deletes the specified connection.</p> <p>Deleting a connection only stops the Direct Connect port hour and data transfer charges. If you are partnering with any third parties to connect with the Direct Connect location, you must cancel your service with them separately.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_connection_request.DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_direct_connect_gateway(
        self,
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.delete_direct_connect_gateway_result.DeleteDirectConnectGatewayResult":
        """<p>Deletes the specified Direct Connect gateway. You must first delete all virtual interfaces that are attached to the Direct Connect gateway and disassociate all virtual private gateways associated with the Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_direct_connect_gateway_request.DeleteDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_direct_connect_gateway_result.DeleteDirectConnectGatewayResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway.async_delete_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_direct_connect_gateway_request.DeleteDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_direct_connect_gateway_association(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        virtual_gateway_id: Optional[
            "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_result.DeleteDirectConnectGatewayAssociationResult":
        """<p>Deletes the association between the specified Direct Connect gateway and virtual private gateway.</p> <p>We recommend that you specify the <code>associationID</code> to delete the association. Alternatively, if you own virtual gateway and a Direct Connect gateway association, you can specify the <code>virtualGatewayId</code> and <code>directConnectGatewayId</code> to delete an association.</p>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_request.DeleteDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_result.DeleteDirectConnectGatewayAssociationResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway_association.async_delete_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_request.DeleteDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
        if association_id is not None:
            input_["association_id"] = association_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_direct_connect_gateway_association_proposal(
        self,
        proposal_id: "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_result.DeleteDirectConnectGatewayAssociationProposalResult":
        """<p>Deletes the association proposal request between the specified Direct Connect gateway and virtual private gateway or transit gateway.</p>

        Args:
            proposal_id: <p>The ID of the proposal.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_request.DeleteDirectConnectGatewayAssociationProposalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_result.DeleteDirectConnectGatewayAssociationProposalResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway_association_proposal

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_direct_connect_gateway_association_proposal.async_delete_direct_connect_gateway_association_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_direct_connect_gateway_association_proposal_request.DeleteDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
        input_["proposal_id"] = proposal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_interconnect(
        self,
        interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.delete_interconnect_response.DeleteInterconnectResponse":
        """<p>Deletes the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_interconnect_request.DeleteInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_interconnect_response.DeleteInterconnectResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_interconnect

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_interconnect.async_delete_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_interconnect_request.DeleteInterconnectRequest = {}  # type: ignore[typeddict-item]
        input_["interconnect_id"] = interconnect_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_lag(
        self,
        lag_id: "aws_sdk_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.lag.Lag":
        """<p>Deletes the specified link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.</p>

        Args:
            lag_id: <p>The ID of the LAG.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_lag_request.DeleteLagRequest]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.lag.Lag"]:
            import aws_sdk_direct_connect._operations.overture_service.delete_lag

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_lag.async_delete_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_lag_request.DeleteLagRequest = {}  # type: ignore[typeddict-item]
        input_["lag_id"] = lag_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_virtual_interface(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.delete_virtual_interface_response.DeleteVirtualInterfaceResponse":
        """<p>Deletes a virtual interface.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.delete_virtual_interface_request.DeleteVirtualInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.delete_virtual_interface_response.DeleteVirtualInterfaceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.delete_virtual_interface

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.delete_virtual_interface.async_delete_virtual_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.delete_virtual_interface_request.DeleteVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_connection_loa(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "aws_sdk_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_connection_loa_response.DescribeConnectionLoaResponse":
        r"""<note> <p>Deprecated. Use <a>DescribeLoa</a> instead.</p> </note> <p>Gets the LOA-CFA for a connection.</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html\">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            provider_name: <p>The name of the APN partner or service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_connection_loa_request.DescribeConnectionLoaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_connection_loa_response.DescribeConnectionLoaResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_connection_loa

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_connection_loa.async_describe_connection_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_connection_loa_request.DescribeConnectionLoaRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_connections(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "aws_sdk_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.connections.Connections":
        """<p>Displays the specified connection or all connections in this Region.</p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_connections_request.DescribeConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connections.Connections"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_connections

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_connections.async_describe_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_connections_request.DescribeConnectionsRequest = {}  # type: ignore[typeddict-item]
        if connection_id is not None:
            input_["connection_id"] = connection_id
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

    async def describe_connections_on_interconnect(
        self,
        interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connections.Connections":
        """<note> <p>Deprecated. Use <a>DescribeHostedConnections</a> instead.</p> </note> <p>Lists the connections that have been provisioned on the specified interconnect.</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_connections_on_interconnect_request.DescribeConnectionsOnInterconnectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connections.Connections"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_connections_on_interconnect

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_connections_on_interconnect.async_describe_connections_on_interconnect(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_connections_on_interconnect_request.DescribeConnectionsOnInterconnectRequest = {}  # type: ignore[typeddict-item]
        input_["interconnect_id"] = interconnect_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_customer_metadata(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "aws_sdk_direct_connect.types.describe_customer_metadata_response.DescribeCustomerMetadataResponse":
        """<p>Get and view a list of customer agreements, along with their signed status and whether the customer is an NNIPartner, NNIPartnerV2, or a nonPartner. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_customer_metadata_response.DescribeCustomerMetadataResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_customer_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_customer_metadata.async_describe_customer_metadata(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_direct_connect_gateway_association_proposals(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        proposal_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
        ] = None,
        associated_gateway_id: Optional[
            "aws_sdk_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_result.DescribeDirectConnectGatewayAssociationProposalsResult":
        """<p>Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway. </p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            proposal_id: <p>The ID of the proposal.</p>
            associated_gateway_id: <p>The ID of the associated gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_request.DescribeDirectConnectGatewayAssociationProposalsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_result.DescribeDirectConnectGatewayAssociationProposalsResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_association_proposals

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_association_proposals.async_describe_direct_connect_gateway_association_proposals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_direct_connect_gateway_association_proposals_request.DescribeDirectConnectGatewayAssociationProposalsRequest = {}  # type: ignore[typeddict-item]
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if proposal_id is not None:
            input_["proposal_id"] = proposal_id
        if associated_gateway_id is not None:
            input_["associated_gateway_id"] = associated_gateway_id
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

    async def describe_direct_connect_gateway_associations(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        associated_gateway_id: Optional[
            "aws_sdk_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
        ] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
        virtual_gateway_id: Optional[
            "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_result.DescribeDirectConnectGatewayAssociationsResult":
        """<p>Lists the associations between your Direct Connect gateways and virtual private gateways and transit gateways. You must specify one of the following:</p> <ul> <li> <p>A Direct Connect gateway</p> <p>The response contains all virtual private gateways and transit gateways associated with the Direct Connect gateway.</p> </li> <li> <p>A virtual private gateway</p> <p>The response contains the Direct Connect gateway.</p> </li> <li> <p>A transit gateway</p> <p>The response contains the Direct Connect gateway.</p> </li> <li> <p>A Direct Connect gateway and a virtual private gateway</p> <p>The response contains the association between the Direct Connect gateway and virtual private gateway.</p> </li> <li> <p>A Direct Connect gateway and a transit gateway</p> <p>The response contains the association between the Direct Connect gateway and transit gateway.</p> </li> <li> <p>A Direct Connect gateway and a virtual private gateway</p> <p>The response contains the association between the Direct Connect gateway and virtual private gateway.</p> </li> <li> <p>A Direct Connect gateway association to a Cloud WAN core network</p> <p>The response contains the Cloud WAN core network ID that the Direct Connect gateway is associated to.</p> </li> </ul>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            associated_gateway_id: <p>The ID of the associated gateway.</p>
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>
            virtual_gateway_id: <p>The ID of the virtual private gateway or transit gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_request.DescribeDirectConnectGatewayAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_result.DescribeDirectConnectGatewayAssociationsResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_associations

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_associations.async_describe_direct_connect_gateway_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_direct_connect_gateway_associations_request.DescribeDirectConnectGatewayAssociationsRequest = {}  # type: ignore[typeddict-item]
        if association_id is not None:
            input_["association_id"] = association_id
        if associated_gateway_id is not None:
            input_["associated_gateway_id"] = associated_gateway_id
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if virtual_gateway_id is not None:
            input_["virtual_gateway_id"] = virtual_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_direct_connect_gateway_attachments(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        virtual_interface_id: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_result.DescribeDirectConnectGatewayAttachmentsResult":
        """<p>Lists the attachments between your Direct Connect gateways and virtual interfaces. You must specify a Direct Connect gateway, a virtual interface, or both. If you specify a Direct Connect gateway, the response contains all virtual interfaces attached to the Direct Connect gateway. If you specify a virtual interface, the response contains all Direct Connect gateways attached to the virtual interface. If you specify both, the response contains the attachment between the Direct Connect gateway and the virtual interface.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_request.DescribeDirectConnectGatewayAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_result.DescribeDirectConnectGatewayAttachmentsResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_attachments

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateway_attachments.async_describe_direct_connect_gateway_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_direct_connect_gateway_attachments_request.DescribeDirectConnectGatewayAttachmentsRequest = {}  # type: ignore[typeddict-item]
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
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

    async def describe_direct_connect_gateways(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        direct_connect_gateway_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_direct_connect_gateways_result.DescribeDirectConnectGatewaysResult":
        """<p>Lists all your Direct Connect gateways or only the specified Direct Connect gateway. Deleted Direct Connect gateways are not returned.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token provided in the previous call to retrieve the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_direct_connect_gateways_request.DescribeDirectConnectGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_direct_connect_gateways_result.DescribeDirectConnectGatewaysResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_direct_connect_gateways.async_describe_direct_connect_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_direct_connect_gateways_request.DescribeDirectConnectGatewaysRequest = {}  # type: ignore[typeddict-item]
        if direct_connect_gateway_id is not None:
            input_["direct_connect_gateway_id"] = direct_connect_gateway_id
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

    async def describe_hosted_connections(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.connections.Connections":
        """<p>Lists the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG).</p> <note> <p>Intended for use by Direct Connect Partners only.</p> </note>

        Args:
            connection_id: <p>The ID of the interconnect or LAG.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_hosted_connections_request.DescribeHostedConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connections.Connections"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_hosted_connections

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_hosted_connections.async_describe_hosted_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_hosted_connections_request.DescribeHostedConnectionsRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
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

    async def describe_interconnect_loa(
        self,
        interconnect_id: "aws_sdk_direct_connect.types.interconnect_id.InterconnectId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "aws_sdk_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_interconnect_loa_response.DescribeInterconnectLoaResponse":
        r"""<note> <p>Deprecated. Use <a>DescribeLoa</a> instead.</p> </note> <p>Gets the LOA-CFA for the specified interconnect.</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html\">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
            provider_name: <p>The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_interconnect_loa_request.DescribeInterconnectLoaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_interconnect_loa_response.DescribeInterconnectLoaResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_interconnect_loa

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_interconnect_loa.async_describe_interconnect_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_interconnect_loa_request.DescribeInterconnectLoaRequest = {}  # type: ignore[typeddict-item]
        input_["interconnect_id"] = interconnect_id
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_interconnects(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        interconnect_id: Optional[
            "aws_sdk_direct_connect.types.interconnect_id.InterconnectId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.interconnects.Interconnects":
        """<p>Lists the interconnects owned by the Amazon Web Services account or only the specified interconnect.</p>

        Args:
            interconnect_id: <p>The ID of the interconnect.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_interconnects_request.DescribeInterconnectsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.interconnects.Interconnects"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_interconnects

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_interconnects.async_describe_interconnects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_interconnects_request.DescribeInterconnectsRequest = {}  # type: ignore[typeddict-item]
        if interconnect_id is not None:
            input_["interconnect_id"] = interconnect_id
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

    async def describe_lags(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_id: Optional["aws_sdk_direct_connect.types.lag_id.LagId"] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.lags.Lags":
        """<p>Describes all your link aggregation groups (LAG) or the specified LAG.</p>

        Args:
            lag_id: <p>The ID of the LAG.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_lags_request.DescribeLagsRequest]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.lags.Lags"]:
            import aws_sdk_direct_connect._operations.overture_service.describe_lags

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_lags.async_describe_lags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_lags_request.DescribeLagsRequest = {}  # type: ignore[typeddict-item]
        if lag_id is not None:
            input_["lag_id"] = lag_id
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

    async def describe_loa(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        provider_name: Optional[
            "aws_sdk_direct_connect.types.provider_name.ProviderName"
        ] = None,
        loa_content_type: Optional[
            "aws_sdk_direct_connect.types.loa_content_type.LoaContentType"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.loa.Loa":
        r"""<p>Gets the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).</p> <p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to Amazon Web Services at the colocation facility. For more information, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html\">Requesting Cross Connects at Direct Connect Locations</a> in the <i>Direct Connect User Guide</i>.</p>

        Args:
            connection_id: <p>The ID of a connection, LAG, or interconnect.</p>
            provider_name: <p>The name of the service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>
            loa_content_type: <p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_loa_request.DescribeLoaRequest]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.loa.Loa"]:
            import aws_sdk_direct_connect._operations.overture_service.describe_loa

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_loa.async_describe_loa(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_loa_request.DescribeLoaRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if loa_content_type is not None:
            input_["loa_content_type"] = loa_content_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_locations(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "aws_sdk_direct_connect.types.locations.Locations":
        """<p>Lists the Direct Connect locations in the current Amazon Web Services Region. These are the locations that can be selected when calling <a>CreateConnection</a> or <a>CreateInterconnect</a>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.locations.Locations"]:
            import aws_sdk_direct_connect._operations.overture_service.describe_locations

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_locations.async_describe_locations(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_router_configuration(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        router_type_identifier: Optional[
            "aws_sdk_direct_connect.types.router_type_identifier.RouterTypeIdentifier"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.describe_router_configuration_response.DescribeRouterConfigurationResponse":
        """<p> Details about the router. </p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            router_type_identifier: <p>Identifies the router by a combination of vendor, platform, and software version. For example, <code>CiscoSystemsInc-2900SeriesRouters-IOS124</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_router_configuration_request.DescribeRouterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_router_configuration_response.DescribeRouterConfigurationResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_router_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_router_configuration.async_describe_router_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_router_configuration_request.DescribeRouterConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        if router_type_identifier is not None:
            input_["router_type_identifier"] = router_type_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_tags(
        self,
        resource_arns: "aws_sdk_direct_connect.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.describe_tags_response.DescribeTagsResponse":
        """<p>Describes the tags associated with the specified Direct Connect resources.</p>

        Args:
            resource_arns: <p>The Amazon Resource Names (ARNs) of the resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_tags_request.DescribeTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.describe_tags_response.DescribeTagsResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_tags

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_tags_request.DescribeTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arns"] = resource_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_virtual_gateways(
        self, *, config_overrides: Optional[AsyncDirectConnectClientConfig] = None
    ) -> "aws_sdk_direct_connect.types.virtual_gateways.VirtualGateways":
        r"""<note> <p>Deprecated. Use <code>DescribeVpnGateways</code> instead. See <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html\">DescribeVPNGateways</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </note> <p>Lists the virtual private gateways owned by the Amazon Web Services account.</p> <p>You can create one or more Direct Connect private virtual interfaces linked to a virtual private gateway.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_gateways.VirtualGateways"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_virtual_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_virtual_gateways.async_describe_virtual_gateways(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_virtual_interfaces(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_id: Optional[
            "aws_sdk_direct_connect.types.connection_id.ConnectionId"
        ] = None,
        virtual_interface_id: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interfaces.VirtualInterfaces":
        """<p>Displays all virtual interfaces for an Amazon Web Services account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.</p> <p>A virtual interface (VLAN) transmits the traffic between the Direct Connect location and the customer network.</p> <ul> <li> <p>If you're using an <code>asn</code>, the response includes ASN value in both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you're using <code>asnLong</code>, the response returns a value of <code>0</code> (zero) for the <code>asn</code> attribute because it exceeds the highest ASN value of 2,147,483,647 that it can support</p> </li> </ul>

        Args:
            connection_id: <p>The ID of the connection.</p>
            virtual_interface_id: <p>The ID of the virtual interface.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.describe_virtual_interfaces_request.DescribeVirtualInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interfaces.VirtualInterfaces"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.describe_virtual_interfaces

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.describe_virtual_interfaces.async_describe_virtual_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.describe_virtual_interfaces_request.DescribeVirtualInterfacesRequest = {}  # type: ignore[typeddict-item]
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
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

    async def disassociate_connection_from_lag(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        lag_id: "aws_sdk_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the <a>DeleteConnection</a> request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an Direct Connect Partner is automatically converted to an interconnect.</p> <p>If disassociating the connection would cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it's the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections. </p>

        Args:
            connection_id: <p>The ID of the connection.</p>
            lag_id: <p>The ID of the LAG.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.disassociate_connection_from_lag_request.DisassociateConnectionFromLagRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.disassociate_connection_from_lag

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.disassociate_connection_from_lag.async_disassociate_connection_from_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.disassociate_connection_from_lag_request.DisassociateConnectionFromLagRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["lag_id"] = lag_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_mac_sec_key(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        secret_arn: "aws_sdk_direct_connect.types.secret_arn.SecretARN",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.disassociate_mac_sec_key_response.DisassociateMacSecKeyResponse":
        """<p>Removes the association between a MAC Security (MACsec) security key and a Direct Connect connection.</p>

        Args:
            connection_id: <p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>
            secret_arn: <p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.</p> <p>You can use <a>DescribeConnections</a> to retrieve the ARN of the MAC Security (MACsec) secret key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.disassociate_mac_sec_key_request.DisassociateMacSecKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.disassociate_mac_sec_key_response.DisassociateMacSecKeyResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.disassociate_mac_sec_key

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.disassociate_mac_sec_key.async_disassociate_mac_sec_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.disassociate_mac_sec_key_request.DisassociateMacSecKeyRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        input_["secret_arn"] = secret_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_virtual_interface_test_history(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        test_id: Optional["aws_sdk_direct_connect.types.test_id.TestId"] = None,
        virtual_interface_id: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
        ] = None,
        bgp_peers: Optional[
            "aws_sdk_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"
        ] = None,
        status: Optional[
            "aws_sdk_direct_connect.types.failure_test_history_status.FailureTestHistoryStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.list_virtual_interface_test_history_response.ListVirtualInterfaceTestHistoryResponse":
        """<p>Lists the virtual interface failover test history.</p>

        Args:
            test_id: <p>The ID of the virtual interface failover test.</p>
            virtual_interface_id: <p>The ID of the virtual interface that was tested.</p>
            bgp_peers: <p>The BGP peers that were placed in the DOWN state during the virtual interface failover test.</p>
            status: <p>The status of the virtual interface failover test.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.list_virtual_interface_test_history_request.ListVirtualInterfaceTestHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.list_virtual_interface_test_history_response.ListVirtualInterfaceTestHistoryResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.list_virtual_interface_test_history

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.list_virtual_interface_test_history.async_list_virtual_interface_test_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.list_virtual_interface_test_history_request.ListVirtualInterfaceTestHistoryRequest = {}  # type: ignore[typeddict-item]
        if test_id is not None:
            input_["test_id"] = test_id
        if virtual_interface_id is not None:
            input_["virtual_interface_id"] = virtual_interface_id
        if bgp_peers is not None:
            input_["bgp_peers"] = bgp_peers
        if status is not None:
            input_["status"] = status
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

    async def start_bgp_failover_test(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        bgp_peers: Optional[
            "aws_sdk_direct_connect.types.bgp_peer_id_list.BGPPeerIdList"
        ] = None,
        test_duration_in_minutes: Optional[
            "aws_sdk_direct_connect.types.test_duration.TestDuration"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.start_bgp_failover_test_response.StartBgpFailoverTestResponse":
        r"""<p>Starts the virtual interface failover test that verifies your configuration meets your resiliency requirements by placing the BGP peering session in the DOWN state. You can then send traffic to verify that there are no outages.</p> <p>You can run the test on public, private, transit, and hosted virtual interfaces.</p> <p>You can use <a href=\"https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html\">ListVirtualInterfaceTestHistory</a> to view the virtual interface test history.</p> <p>If you need to stop the test before the test interval completes, use <a href=\"https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html\">StopBgpFailoverTest</a>.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface you want to test.</p>
            bgp_peers: <p>The BGP peers to place in the DOWN state.</p>
            test_duration_in_minutes: <p>The time in minutes that the virtual interface failover test will last.</p> <p>Maximum value: 4,320 minutes (72 hours).</p> <p>Default: 180 minutes (3 hours).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.start_bgp_failover_test_request.StartBgpFailoverTestRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.start_bgp_failover_test_response.StartBgpFailoverTestResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.start_bgp_failover_test

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.start_bgp_failover_test.async_start_bgp_failover_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.start_bgp_failover_test_request.StartBgpFailoverTestRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        if bgp_peers is not None:
            input_["bgp_peers"] = bgp_peers
        if test_duration_in_minutes is not None:
            input_["test_duration_in_minutes"] = test_duration_in_minutes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_bgp_failover_test(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.stop_bgp_failover_test_response.StopBgpFailoverTestResponse":
        """<p>Stops the virtual interface failover test.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual interface you no longer want to test.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.stop_bgp_failover_test_request.StopBgpFailoverTestRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.stop_bgp_failover_test_response.StopBgpFailoverTestResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.stop_bgp_failover_test

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.stop_bgp_failover_test.async_stop_bgp_failover_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.stop_bgp_failover_test_request.StopBgpFailoverTestRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_direct_connect.types.resource_arn.ResourceArn",
        tags: "aws_sdk_direct_connect.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified Direct Connect resource. Each resource can have a maximum of 50 tags.</p> <p>Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_direct_connect.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_direct_connect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Direct Connect resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys of the tags to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_connection(
        self,
        connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        connection_name: Optional[
            "aws_sdk_direct_connect.types.connection_name.ConnectionName"
        ] = None,
        encryption_mode: Optional[
            "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.connection.Connection":
        """<p>Updates the Direct Connect connection configuration.</p> <p>You can update the following parameters for a connection:</p> <ul> <li> <p>The connection name</p> </li> <li> <p>The connection's MAC Security (MACsec) encryption mode.</p> </li> </ul>

        Args:
            connection_id: <p>The ID of the connection.</p> <p>You can use <a>DescribeConnections</a> to retrieve the connection ID.</p>
            connection_name: <p>The name of the connection.</p>
            encryption_mode: <p>The connection MAC Security (MACsec) encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.connection.Connection"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.update_connection

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.update_connection_request.UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id
        if connection_name is not None:
            input_["connection_name"] = connection_name
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_direct_connect_gateway(
        self,
        direct_connect_gateway_id: "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId",
        new_direct_connect_gateway_name: "aws_sdk_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
    ) -> "aws_sdk_direct_connect.types.update_direct_connect_gateway_response.UpdateDirectConnectGatewayResponse":
        """<p>Updates the name of a current Direct Connect gateway.</p>

        Args:
            direct_connect_gateway_id: <p>The ID of the Direct Connect gateway to update.</p>
            new_direct_connect_gateway_name: <p>The new name for the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.update_direct_connect_gateway_request.UpdateDirectConnectGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.update_direct_connect_gateway_response.UpdateDirectConnectGatewayResponse"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.update_direct_connect_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.update_direct_connect_gateway.async_update_direct_connect_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.update_direct_connect_gateway_request.UpdateDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["direct_connect_gateway_id"] = direct_connect_gateway_id
        input_["new_direct_connect_gateway_name"] = new_direct_connect_gateway_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_direct_connect_gateway_association(
        self,
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        association_id: Optional[
            "aws_sdk_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
        ] = None,
        add_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
        remove_allowed_prefixes_to_direct_connect_gateway: Optional[
            "aws_sdk_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.update_direct_connect_gateway_association_result.UpdateDirectConnectGatewayAssociationResult":
        """<p>Updates the specified attributes of the Direct Connect gateway association.</p> <p>Add or remove prefixes from the association.</p>

        Args:
            association_id: <p>The ID of the Direct Connect gateway association.</p>
            add_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>
            remove_allowed_prefixes_to_direct_connect_gateway: <p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.update_direct_connect_gateway_association_request.UpdateDirectConnectGatewayAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.update_direct_connect_gateway_association_result.UpdateDirectConnectGatewayAssociationResult"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.update_direct_connect_gateway_association

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.update_direct_connect_gateway_association.async_update_direct_connect_gateway_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.update_direct_connect_gateway_association_request.UpdateDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
        if association_id is not None:
            input_["association_id"] = association_id
        if add_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["add_allowed_prefixes_to_direct_connect_gateway"] = (
                add_allowed_prefixes_to_direct_connect_gateway
            )
        if remove_allowed_prefixes_to_direct_connect_gateway is not None:
            input_["remove_allowed_prefixes_to_direct_connect_gateway"] = (
                remove_allowed_prefixes_to_direct_connect_gateway
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_lag(
        self,
        lag_id: "aws_sdk_direct_connect.types.lag_id.LagId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        lag_name: Optional["aws_sdk_direct_connect.types.lag_name.LagName"] = None,
        minimum_links: Optional["aws_sdk_direct_connect.types.count.Count"] = None,
        encryption_mode: Optional[
            "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.lag.Lag":
        """<p>Updates the attributes of the specified link aggregation group (LAG).</p> <p>You can update the following LAG attributes:</p> <ul> <li> <p>The name of the LAG.</p> </li> <li> <p>The value for the minimum number of connections that must be operational for the LAG itself to be operational. </p> </li> <li> <p>The LAG's MACsec encryption mode.</p> <p>Amazon Web Services assigns this value to each connection which is part of the LAG.</p> </li> <li> <p>The tags</p> </li> </ul> <note> <p>If you adjust the threshold value for the minimum number of operational connections, ensure that the new value does not cause the LAG to fall below the threshold and become non-operational.</p> </note>

        Args:
            lag_id: <p>The ID of the LAG.</p>
            lag_name: <p>The name of the LAG.</p>
            minimum_links: <p>The minimum number of physical connections that must be operational for the LAG itself to be operational.</p>
            encryption_mode: <p>The LAG MAC Security (MACsec) encryption mode.</p> <p>Amazon Web Services applies the value to all connections which are part of the LAG.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.update_lag_request.UpdateLagRequest]",
        ) -> AsyncOperationResponse["aws_sdk_direct_connect.types.lag.Lag"]:
            import aws_sdk_direct_connect._operations.overture_service.update_lag

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.update_lag.async_update_lag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.update_lag_request.UpdateLagRequest = {}  # type: ignore[typeddict-item]
        input_["lag_id"] = lag_id
        if lag_name is not None:
            input_["lag_name"] = lag_name
        if minimum_links is not None:
            input_["minimum_links"] = minimum_links
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_virtual_interface_attributes(
        self,
        virtual_interface_id: "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId",
        *,
        config_overrides: Optional[AsyncDirectConnectClientConfig] = None,
        mtu: Optional["aws_sdk_direct_connect.types.mtu.MTU"] = None,
        enable_site_link: Optional[
            "aws_sdk_direct_connect.types.enable_site_link.EnableSiteLink"
        ] = None,
        virtual_interface_name: Optional[
            "aws_sdk_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
        ] = None,
    ) -> "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface":
        """<p>Updates the specified attributes of the specified virtual private interface.</p> <p>Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call <a>DescribeConnections</a>. To check whether your virtual interface supports jumbo frames, call <a>DescribeVirtualInterfaces</a>.</p>

        Args:
            virtual_interface_id: <p>The ID of the virtual private interface.</p>
            mtu: <p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>
            enable_site_link: <p>Indicates whether to enable or disable SiteLink.</p>
            virtual_interface_name: <p>The name of the virtual private interface.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_direct_connect.types.update_virtual_interface_attributes_request.UpdateVirtualInterfaceAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
        ]:
            import aws_sdk_direct_connect._operations.overture_service.update_virtual_interface_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_direct_connect._operations.overture_service.update_virtual_interface_attributes.async_update_virtual_interface_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_direct_connect.types.update_virtual_interface_attributes_request.UpdateVirtualInterfaceAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["virtual_interface_id"] = virtual_interface_id
        if mtu is not None:
            input_["mtu"] = mtu
        if enable_site_link is not None:
            input_["enable_site_link"] = enable_site_link
        if virtual_interface_name is not None:
            input_["virtual_interface_name"] = virtual_interface_name

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
