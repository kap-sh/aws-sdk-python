from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_deadline._auth._signers
import aws_sdk_deadline._auth._sigv4
from aws_sdk_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.create_license_endpoint_request
    import aws_sdk_deadline.types.create_license_endpoint_response
    import aws_sdk_deadline.types.delete_license_endpoint_request
    import aws_sdk_deadline.types.delete_license_endpoint_response
    import aws_sdk_deadline.types.delete_metered_product_request
    import aws_sdk_deadline.types.delete_metered_product_response
    import aws_sdk_deadline.types.get_license_endpoint_request
    import aws_sdk_deadline.types.get_license_endpoint_response
    import aws_sdk_deadline.types.license_endpoint_id
    import aws_sdk_deadline.types.license_endpoint_summary
    import aws_sdk_deadline.types.list_license_endpoints_request
    import aws_sdk_deadline.types.list_license_endpoints_response
    import aws_sdk_deadline.types.list_metered_products_request
    import aws_sdk_deadline.types.list_metered_products_response
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.metered_product_id
    import aws_sdk_deadline.types.metered_product_summary
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.put_metered_product_request
    import aws_sdk_deadline.types.put_metered_product_response
    import aws_sdk_deadline.types.security_group_id_list
    import aws_sdk_deadline.types.subnet_id_list
    import aws_sdk_deadline.types.tags
    import aws_sdk_deadline.types.vpc_id
    from aws_sdk_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from aws_sdk_deadline._services.deadline import deadlineClient, deadlineClientConfig


class LicenseEndpointResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "aws_sdk_deadline.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_deadline.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_deadline.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse":
        """<p>Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            vpc_id: <p>The VPC (virtual private cloud) ID to use with the license endpoint.</p>
            subnet_ids: <p>The subnet IDs.</p>
            security_group_ids: <p>The security group IDs.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_license_endpoint

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_license_endpoint.create_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        input_["security_group_ids"] = security_group_ids
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
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse":
        """<p>Gets a licence endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_license_endpoint

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_license_endpoint.get_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse":
        """<p>Deletes a license endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID of the license endpoint to delete.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_license_endpoint

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_license_endpoint.delete_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse":
        """<p>Lists license endpoints.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_license_endpoints

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_license_endpoints.list_license_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_metered_product(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse":
        """<p>Deletes a metered product.</p>

        Args:
            license_endpoint_id: <p>The ID of the license endpoint from which to remove the metered product.</p>
            product_id: <p>The product ID to remove from the license endpoint.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_metered_product

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_metered_product.delete_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        input_["product_id"] = product_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_metered_products(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_metered_products_response.ListMeteredProductsResponse":
        """<p>Lists metered products.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to include on the list of metered products.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_metered_products_request.ListMeteredProductsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_metered_products

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_metered_products.list_metered_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_metered_products_request.ListMeteredProductsRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_metered_product(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> (
        "aws_sdk_deadline.types.put_metered_product_response.PutMeteredProductResponse"
    ):
        """<p>Adds a metered product.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to add to the metered product.</p>
            product_id: <p>The product ID to add to the metered product.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.put_metered_product_request.PutMeteredProductRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.put_metered_product_response.PutMeteredProductResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.put_metered_product

            output, http_response = (
                aws_sdk_deadline._operations.deadline.put_metered_product.put_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.put_metered_product_request.PutMeteredProductRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        input_["product_id"] = product_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLicenseEndpointResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "aws_sdk_deadline.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_deadline.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_deadline.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse":
        """<p>Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            vpc_id: <p>The VPC (virtual private cloud) ID to use with the license endpoint.</p>
            subnet_ids: <p>The subnet IDs.</p>
            security_group_ids: <p>The security group IDs.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_license_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.create_license_endpoint.async_create_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        input_["security_group_ids"] = security_group_ids
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
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse":
        """<p>Gets a licence endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_license_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_license_endpoint.async_get_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse":
        """<p>Deletes a license endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID of the license endpoint to delete.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_license_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_license_endpoint.async_delete_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse":
        """<p>Lists license endpoints.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_license_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_license_endpoints.async_list_license_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_metered_product(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse":
        """<p>Deletes a metered product.</p>

        Args:
            license_endpoint_id: <p>The ID of the license endpoint from which to remove the metered product.</p>
            product_id: <p>The product ID to remove from the license endpoint.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_metered_product

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_metered_product.async_delete_metered_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        input_["product_id"] = product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_metered_products(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_metered_products_response.ListMeteredProductsResponse":
        """<p>Lists metered products.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to include on the list of metered products.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_metered_products_request.ListMeteredProductsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_metered_products

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_metered_products.async_list_metered_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_metered_products_request.ListMeteredProductsRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_metered_product(
        self,
        license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> (
        "aws_sdk_deadline.types.put_metered_product_response.PutMeteredProductResponse"
    ):
        """<p>Adds a metered product.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to add to the metered product.</p>
            product_id: <p>The product ID to add to the metered product.</p>

        Raises:
            aws_sdk_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            aws_sdk_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            aws_sdk_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            aws_sdk_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            aws_sdk_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            aws_sdk_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.put_metered_product_request.PutMeteredProductRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.put_metered_product_response.PutMeteredProductResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.put_metered_product

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.put_metered_product.async_put_metered_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.put_metered_product_request.PutMeteredProductRequest = {}  # type: ignore[typeddict-item]
        input_["license_endpoint_id"] = license_endpoint_id
        input_["product_id"] = product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
