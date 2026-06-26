from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_route53globalresolver._auth._signers
import aws_sdk_route53globalresolver._auth._sigv4
from aws_sdk_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.associate_hosted_zone_input
    import aws_sdk_route53globalresolver.types.associate_hosted_zone_output
    import aws_sdk_route53globalresolver.types.get_hosted_zone_association_input
    import aws_sdk_route53globalresolver.types.get_hosted_zone_association_output
    import aws_sdk_route53globalresolver.types.hosted_zone_association_summary
    import aws_sdk_route53globalresolver.types.hosted_zone_id
    import aws_sdk_route53globalresolver.types.list_hosted_zone_associations_input
    import aws_sdk_route53globalresolver.types.list_hosted_zone_associations_output
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.update_hosted_zone_association_input
    import aws_sdk_route53globalresolver.types.update_hosted_zone_association_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class HostedZoneAssociation:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput":
        """<p>Associates a Route 53 private hosted zone with a Route 53 Global Resolver resource. This allows the resolver to resolve DNS queries for the private hosted zone from anywhere globally.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to associate with the Route 53 Global Resolver resource.</p>
            resource_arn: <p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone will be associated to.</p>
            name: <p>Name for the private hosted zone association.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone.associate_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_id"] = hosted_zone_id
        input_["resource_arn"] = resource_arn
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        hosted_zone_association_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput":
        """<p>Retrieves information about a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>ID of the private hosted zone association.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association.get_hosted_zone_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_association_id"] = hosted_zone_association_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        hosted_zone_association_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput":
        """<p>Updates the configuration of a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>The ID of the private hosted zone association.</p>
            name: <p>The name you want to update the hosted zone association to.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association.update_hosted_zone_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_association_id"] = hosted_zone_association_id
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput":
        """<p>Lists all hosted zone associations for a Route 53 Global Resolver resource with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            resource_arn: <p>Amazon Resource Name (ARN) of the DNS view.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations.list_hosted_zone_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncHostedZoneAssociation:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput":
        """<p>Associates a Route 53 private hosted zone with a Route 53 Global Resolver resource. This allows the resolver to resolve DNS queries for the private hosted zone from anywhere globally.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to associate with the Route 53 Global Resolver resource.</p>
            resource_arn: <p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone will be associated to.</p>
            name: <p>Name for the private hosted zone association.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.associate_hosted_zone_output.AssociateHostedZoneOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.associate_hosted_zone.async_associate_hosted_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.associate_hosted_zone_input.AssociateHostedZoneInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_id"] = hosted_zone_id
        input_["resource_arn"] = resource_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        hosted_zone_association_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput":
        """<p>Retrieves information about a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>ID of the private hosted zone association.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_hosted_zone_association_output.GetHostedZoneAssociationOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_hosted_zone_association.async_get_hosted_zone_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_hosted_zone_association_input.GetHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_association_id"] = hosted_zone_association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        hosted_zone_association_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput":
        """<p>Updates the configuration of a hosted zone association.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_association_id: <p>The ID of the private hosted zone association.</p>
            name: <p>The name you want to update the hosted zone association to.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_hosted_zone_association_output.UpdateHostedZoneAssociationOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_hosted_zone_association.async_update_hosted_zone_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_hosted_zone_association_input.UpdateHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_association_id"] = hosted_zone_association_id
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput":
        """<p>Lists all hosted zone associations for a Route 53 Global Resolver resource with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            resource_arn: <p>Amazon Resource Name (ARN) of the DNS view.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_hosted_zone_associations_output.ListHostedZoneAssociationsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_hosted_zone_associations.async_list_hosted_zone_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_hosted_zone_associations_input.ListHostedZoneAssociationsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
