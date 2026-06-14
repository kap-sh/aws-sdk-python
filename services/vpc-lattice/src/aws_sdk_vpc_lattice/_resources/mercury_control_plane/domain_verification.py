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
    import aws_sdk_vpc_lattice.types.delete_domain_verification_request
    import aws_sdk_vpc_lattice.types.delete_domain_verification_response
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.domain_verification_identifier
    import aws_sdk_vpc_lattice.types.domain_verification_summary
    import aws_sdk_vpc_lattice.types.get_domain_verification_request
    import aws_sdk_vpc_lattice.types.get_domain_verification_response
    import aws_sdk_vpc_lattice.types.list_domain_verifications_request
    import aws_sdk_vpc_lattice.types.list_domain_verifications_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.start_domain_verification_request
    import aws_sdk_vpc_lattice.types.start_domain_verification_response
    import aws_sdk_vpc_lattice.types.tag_map
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class DomainVerification:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        domain_name: "aws_sdk_vpc_lattice.types.domain_name.DomainName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse":
        """<p> Starts the domain verification process for a custom domain name. </p>

        Args:
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>
            domain_name: <p> The domain name to verify ownership for. </p>
            tags: <p> The tags for the domain verification. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.start_domain_verification

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.start_domain_verification.start_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["domain_name"] = domain_name
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
        domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse":
        """<p> Retrieves information about a domain verification.ß </p>

        Args:
            domain_verification_identifier: <p> The ID or ARN of the domain verification to retrieve. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_domain_verification

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_domain_verification.get_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["domain_verification_identifier"] = domain_verification_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse":
        """<p> Deletes the specified domain verification. </p>

        Args:
            domain_verification_identifier: <p> The ID of the domain verification to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_domain_verification

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_domain_verification.delete_domain_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["domain_verification_identifier"] = domain_verification_identifier

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
    ) -> "aws_sdk_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse":
        """<p> Lists the domain verifications. </p>

        Args:
            max_results: <p> The maximum number of results to return. </p>
            next_token: <p> A pagination token for the next page of results. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_domain_verifications

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_domain_verifications.list_domain_verifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncDomainVerification:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        domain_name: "aws_sdk_vpc_lattice.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse":
        """<p> Starts the domain verification process for a custom domain name. </p>

        Args:
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>
            domain_name: <p> The domain name to verify ownership for. </p>
            tags: <p> The tags for the domain verification. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.start_domain_verification_response.StartDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.start_domain_verification

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.start_domain_verification.async_start_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.start_domain_verification_request.StartDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["domain_name"] = domain_name
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
        domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse":
        """<p> Retrieves information about a domain verification.ß </p>

        Args:
            domain_verification_identifier: <p> The ID or ARN of the domain verification to retrieve. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_domain_verification_response.GetDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_domain_verification

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_domain_verification.async_get_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_domain_verification_request.GetDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["domain_verification_identifier"] = domain_verification_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse":
        """<p> Deletes the specified domain verification. </p>

        Args:
            domain_verification_identifier: <p> The ID of the domain verification to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_domain_verification_response.DeleteDomainVerificationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_domain_verification

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_domain_verification.async_delete_domain_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_domain_verification_request.DeleteDomainVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["domain_verification_identifier"] = domain_verification_identifier

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
    ) -> "aws_sdk_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse":
        """<p> Lists the domain verifications. </p>

        Args:
            max_results: <p> The maximum number of results to return. </p>
            next_token: <p> A pagination token for the next page of results. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_domain_verifications_response.ListDomainVerificationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_domain_verifications

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_domain_verifications.async_list_domain_verifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_domain_verifications_request.ListDomainVerificationsRequest = {}  # type: ignore[typeddict-item]
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
