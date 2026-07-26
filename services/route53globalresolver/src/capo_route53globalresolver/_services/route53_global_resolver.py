"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EC2DNSGlobalResolverCustomerAPI``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._auth._identity import Credentials
from capo_route53globalresolver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53globalresolver._auth._zapros_handler import AuthMiddleware
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_source import (
    AccessSource,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_token import (
    AccessToken,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.dns_view import (
    DNSView,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_domain_list import (
    FirewallDomainList,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_rule import (
    FirewallRule,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.global_resolver import (
    GlobalResolver,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.hosted_zone_association import (
    HostedZoneAssociation,
)
from capo_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.managed_firewall_domain_list import (
    ManagedFirewallDomainList,
)
from capo_route53globalresolver._services._aws_config import aws_config
from capo_route53globalresolver._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.disassociate_hosted_zone_input
    import capo_route53globalresolver.types.disassociate_hosted_zone_output
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.list_tags_for_resource_request
    import capo_route53globalresolver.types.list_tags_for_resource_response
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.tag_keys
    import capo_route53globalresolver.types.tag_resource_request
    import capo_route53globalresolver.types.tag_resource_response
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.untag_resource_request
    import capo_route53globalresolver.types.untag_resource_response


class Route53GlobalResolverClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class Route53GlobalResolverClient:
    """A client for the ``Route53GlobalResolver`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = Route53GlobalResolverClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.access_source = AccessSource(self)
        self.access_token = AccessToken(self)
        self.dns_view = DNSView(self)
        self.firewall_domain_list = FirewallDomainList(self)
        self.firewall_rule = FirewallRule(self)
        self.global_resolver = GlobalResolver(self)
        self.hosted_zone_association = HostedZoneAssociation(self)
        self.managed_firewall_domain_list = ManagedFirewallDomainList(self)

    def operation_options(
        self, config_overrides: Optional[Route53GlobalResolverClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Route53GlobalResolverClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def disassociate_hosted_zone(
        self,
        hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput":
        """<p>Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to disassociate.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource to disassociate the hosted zone from.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone.disassociate_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_id"] = hosted_zone_id
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        tags: "capo_route53globalresolver.types.tags.Tags",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a Route 53 Global Resolver resource. Tags are key-value pairs that help you organize and identify your resources.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to be tagged.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        tag_keys: "capo_route53globalresolver.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> (
        "capo_route53globalresolver.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes tags from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys associated with the resource.</p>

        Raises:
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53globalresolver.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
