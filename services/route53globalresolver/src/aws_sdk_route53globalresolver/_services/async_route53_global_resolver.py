"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EC2DNSGlobalResolverCustomerAPI``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_route53globalresolver._auth._signers
import aws_sdk_route53globalresolver._auth._sigv4
from aws_sdk_route53globalresolver._auth._identity import Credentials
from aws_sdk_route53globalresolver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_route53globalresolver._auth._zapros_handler import AuthMiddleware
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_source import (
    AsyncAccessSource,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.access_token import (
    AsyncAccessToken,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.dns_view import (
    AsyncDNSView,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_domain_list import (
    AsyncFirewallDomainList,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.firewall_rule import (
    AsyncFirewallRule,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.global_resolver import (
    AsyncGlobalResolver,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.hosted_zone_association import (
    AsyncHostedZoneAssociation,
)
from aws_sdk_route53globalresolver._resources.ec2_dns_global_resolver_customer_api.managed_firewall_domain_list import (
    AsyncManagedFirewallDomainList,
)
from aws_sdk_route53globalresolver._services._aws_config import aaws_config
from aws_sdk_route53globalresolver._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.disassociate_hosted_zone_input
    import aws_sdk_route53globalresolver.types.disassociate_hosted_zone_output
    import aws_sdk_route53globalresolver.types.hosted_zone_id
    import aws_sdk_route53globalresolver.types.list_tags_for_resource_request
    import aws_sdk_route53globalresolver.types.list_tags_for_resource_response
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.tag_keys
    import aws_sdk_route53globalresolver.types.tag_resource_request
    import aws_sdk_route53globalresolver.types.tag_resource_response
    import aws_sdk_route53globalresolver.types.tags
    import aws_sdk_route53globalresolver.types.untag_resource_request
    import aws_sdk_route53globalresolver.types.untag_resource_response


class AsyncRoute53GlobalResolverClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncRoute53GlobalResolverClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncRoute53GlobalResolverClientConfig(
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
        self.access_source = AsyncAccessSource(self)
        self.access_token = AsyncAccessToken(self)
        self.dns_view = AsyncDNSView(self)
        self.firewall_domain_list = AsyncFirewallDomainList(self)
        self.firewall_rule = AsyncFirewallRule(self)
        self.global_resolver = AsyncGlobalResolver(self)
        self.hosted_zone_association = AsyncHostedZoneAssociation(self)
        self.managed_firewall_domain_list = AsyncManagedFirewallDomainList(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53GlobalResolverClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def disassociate_hosted_zone(
        self,
        hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId",
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput":
        """<p>Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            hosted_zone_id: <p>The ID of the Route 53 private hosted zone to disassociate.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource to disassociate the hosted zone from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.disassociate_hosted_zone_output.DisassociateHostedZoneOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disassociate_hosted_zone.async_disassociate_hosted_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.disassociate_hosted_zone_input.DisassociateHostedZoneInput = {}  # type: ignore[typeddict-item]
        input_["hosted_zone_id"] = hosted_zone_id
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        tags: "aws_sdk_route53globalresolver.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds or updates tags for a Route 53 Global Resolver resource. Tags are key-value pairs that help you organize and identify your resources.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to be tagged.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_route53globalresolver.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a Route 53 Global Resolver resource.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys associated with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
