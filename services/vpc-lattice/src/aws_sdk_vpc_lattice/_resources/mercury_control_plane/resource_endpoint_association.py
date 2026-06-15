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
    import aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_request
    import aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_response
    import aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_request
    import aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_summary
    import aws_sdk_vpc_lattice.types.vpc_endpoint_id
    import aws_sdk_vpc_lattice.types.vpc_endpoint_owner
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ResourceEndpointAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def delete(
        self,
        resource_endpoint_association_identifier: "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse":
        """<p>Disassociates the resource configuration from the resource VPC endpoint.</p>

        Args:
            resource_endpoint_association_identifier: <p>The ID or ARN of the association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association.delete_resource_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_endpoint_association_identifier"] = (
            resource_endpoint_association_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "aws_sdk_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "aws_sdk_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse":
        """<p>Lists the associations for the specified VPC endpoint.</p>

        Args:
            resource_configuration_identifier: <p>The ID for the resource configuration associated with the VPC endpoint.</p>
            resource_endpoint_association_identifier: <p>The ID of the association.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint in the association.</p>
            vpc_endpoint_owner: <p>The owner of the VPC endpoint in the association.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations.list_resource_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier
        if resource_endpoint_association_identifier is not None:
            input_["resource_endpoint_association_identifier"] = (
                resource_endpoint_association_identifier
            )
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_owner is not None:
            input_["vpc_endpoint_owner"] = vpc_endpoint_owner
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


class AsyncResourceEndpointAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def delete(
        self,
        resource_endpoint_association_identifier: "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse":
        """<p>Disassociates the resource configuration from the resource VPC endpoint.</p>

        Args:
            resource_endpoint_association_identifier: <p>The ID or ARN of the association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association.async_delete_resource_endpoint_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_endpoint_association_identifier"] = (
            resource_endpoint_association_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "aws_sdk_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "aws_sdk_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse":
        """<p>Lists the associations for the specified VPC endpoint.</p>

        Args:
            resource_configuration_identifier: <p>The ID for the resource configuration associated with the VPC endpoint.</p>
            resource_endpoint_association_identifier: <p>The ID of the association.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint in the association.</p>
            vpc_endpoint_owner: <p>The owner of the VPC endpoint in the association.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations.async_list_resource_endpoint_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier
        if resource_endpoint_association_identifier is not None:
            input_["resource_endpoint_association_identifier"] = (
                resource_endpoint_association_identifier
            )
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_owner is not None:
            input_["vpc_endpoint_owner"] = vpc_endpoint_owner
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
