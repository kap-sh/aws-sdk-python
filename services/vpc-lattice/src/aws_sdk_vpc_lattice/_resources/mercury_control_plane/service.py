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
    import aws_sdk_vpc_lattice.types.certificate_arn
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_service_request
    import aws_sdk_vpc_lattice.types.create_service_response
    import aws_sdk_vpc_lattice.types.delete_service_request
    import aws_sdk_vpc_lattice.types.delete_service_response
    import aws_sdk_vpc_lattice.types.get_service_request
    import aws_sdk_vpc_lattice.types.get_service_response
    import aws_sdk_vpc_lattice.types.list_services_request
    import aws_sdk_vpc_lattice.types.list_services_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.service_name
    import aws_sdk_vpc_lattice.types.service_summary
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_service_request
    import aws_sdk_vpc_lattice.types.update_service_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Service:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_vpc_lattice.types.service_name.ServiceName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        custom_domain_name: Optional[
            "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
        ] = None,
        certificate_arn: Optional[
            "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_response.CreateServiceResponse":
        r"""<p>Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html\">Services</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            tags: <p>The tags for the service.</p>
            custom_domain_name: <p>The custom domain name of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_response.CreateServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_request.CreateServiceRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_response.GetServiceResponse":
        """<p>Retrieves information about the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_response.GetServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_request.GetServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        certificate_arn: Optional[
            "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_response.UpdateServiceResponse":
        """<p>Updates the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_response.UpdateServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_request.UpdateServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_response.DeleteServiceResponse":
        r"""<p>Deletes a service. A service can't be deleted if it's associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service\">Delete a service</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_response.DeleteServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_request.DeleteServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier

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
    ) -> "aws_sdk_vpc_lattice.types.list_services_response.ListServicesResponse":
        """<p>Lists the services owned by the caller account or shared with the caller account.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_services_response.ListServicesResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_services

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_services_request.ListServicesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncService:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_vpc_lattice.types.service_name.ServiceName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        custom_domain_name: Optional[
            "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
        ] = None,
        certificate_arn: Optional[
            "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_response.CreateServiceResponse":
        r"""<p>Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html\">Services</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            tags: <p>The tags for the service.</p>
            custom_domain_name: <p>The custom domain name of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_service_request.CreateServiceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_response.CreateServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_request.CreateServiceRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_response.GetServiceResponse":
        """<p>Retrieves information about the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_service_request.GetServiceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_response.GetServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_request.GetServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        certificate_arn: Optional[
            "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["aws_sdk_vpc_lattice.types.auth_type.AuthType"] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_response.UpdateServiceResponse":
        """<p>Updates the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_service_request.UpdateServiceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_response.UpdateServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_request.UpdateServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_response.DeleteServiceResponse":
        r"""<p>Deletes a service. A service can't be deleted if it's associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service\">Delete a service</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_service_request.DeleteServiceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_response.DeleteServiceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_request.DeleteServiceRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier

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
    ) -> "aws_sdk_vpc_lattice.types.list_services_response.ListServicesResponse":
        """<p>Lists the services owned by the caller account or shared with the caller account.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_services_request.ListServicesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_services_response.ListServicesResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_services

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_services_request.ListServicesRequest = {}  # type: ignore[typeddict-item]
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
