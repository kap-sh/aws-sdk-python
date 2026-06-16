"""Generated from Smithy shape ``com.amazonaws.vpclattice#MercuryControlPlane``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._auth._identity import Credentials
from aws_sdk_vpc_lattice._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_vpc_lattice._auth._zapros_handler import AuthMiddleware
from aws_sdk_vpc_lattice._pagination import resolve_path as _resolve_path
from aws_sdk_vpc_lattice._resources.mercury_control_plane.access_log_subscription import (
    AsyncAccessLogSubscription,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.domain_verification import (
    AsyncDomainVerification,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.listener import AsyncListener
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_configuration import (
    AsyncResourceConfiguration,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_endpoint_association import (
    AsyncResourceEndpointAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_gateway import (
    AsyncResourceGateway,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.rule import AsyncRule
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service import AsyncService
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_load_balancer_association import (
    AsyncServiceLoadBalancerAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network import (
    AsyncServiceNetwork,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_resource_association import (
    AsyncServiceNetworkResourceAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_service_association import (
    AsyncServiceNetworkServiceAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_vpc_association import (
    AsyncServiceNetworkVpcAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.target_group import (
    AsyncTargetGroup,
)
from aws_sdk_vpc_lattice._services._aws_config import aaws_config
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.arn
    import aws_sdk_vpc_lattice.types.auth_policy_string
    import aws_sdk_vpc_lattice.types.batch_update_rule_request
    import aws_sdk_vpc_lattice.types.batch_update_rule_response
    import aws_sdk_vpc_lattice.types.delete_auth_policy_request
    import aws_sdk_vpc_lattice.types.delete_auth_policy_response
    import aws_sdk_vpc_lattice.types.delete_resource_policy_request
    import aws_sdk_vpc_lattice.types.delete_resource_policy_response
    import aws_sdk_vpc_lattice.types.get_auth_policy_request
    import aws_sdk_vpc_lattice.types.get_auth_policy_response
    import aws_sdk_vpc_lattice.types.get_resource_policy_request
    import aws_sdk_vpc_lattice.types.get_resource_policy_response
    import aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request
    import aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response
    import aws_sdk_vpc_lattice.types.list_tags_for_resource_request
    import aws_sdk_vpc_lattice.types.list_tags_for_resource_response
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.policy_string
    import aws_sdk_vpc_lattice.types.put_auth_policy_request
    import aws_sdk_vpc_lattice.types.put_auth_policy_response
    import aws_sdk_vpc_lattice.types.put_resource_policy_request
    import aws_sdk_vpc_lattice.types.put_resource_policy_response
    import aws_sdk_vpc_lattice.types.resource_arn
    import aws_sdk_vpc_lattice.types.resource_identifier
    import aws_sdk_vpc_lattice.types.rule_update_list
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.service_network_endpoint_association
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.tag_keys
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.tag_resource_request
    import aws_sdk_vpc_lattice.types.tag_resource_response
    import aws_sdk_vpc_lattice.types.untag_resource_request
    import aws_sdk_vpc_lattice.types.untag_resource_response


class AsyncVPCLatticeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncVPCLatticeClient:
    """A client for the ``VPCLattice`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncVPCLatticeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.access_log_subscription = AsyncAccessLogSubscription(self)
        self.domain_verification = AsyncDomainVerification(self)
        self.listener = AsyncListener(self)
        self.resource_configuration = AsyncResourceConfiguration(self)
        self.resource_endpoint_association = AsyncResourceEndpointAssociation(self)
        self.resource_gateway = AsyncResourceGateway(self)
        self.rule = AsyncRule(self)
        self.service = AsyncService(self)
        self.service_load_balancer_association = AsyncServiceLoadBalancerAssociation(
            self
        )
        self.service_network = AsyncServiceNetwork(self)
        self.service_network_resource_association = (
            AsyncServiceNetworkResourceAssociation(self)
        )
        self.service_network_service_association = (
            AsyncServiceNetworkServiceAssociation(self)
        )
        self.service_network_vpc_association = AsyncServiceNetworkVpcAssociation(self)
        self.target_group = AsyncTargetGroup(self)

    def operation_options(
        self, config_overrides: Optional[AsyncVPCLatticeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncVPCLatticeClientConfig = config_overrides or {}
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

    async def batch_update_rule(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rules: "aws_sdk_vpc_lattice.types.rule_update_list.RuleUpdateList",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse":
        r"""<p>Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority.</p> <p> <b>Required permissions:</b> <code>vpc-lattice:UpdateRule</code> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_service-with-iam.html\">How Amazon VPC Lattice works with IAM</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rules: <p>The rules for the specified listener.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.batch_update_rule

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.batch_update_rule.async_batch_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rules"] = rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> (
        "aws_sdk_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse"
    ):
        """<p>Deletes the specified auth policy. If an auth is set to <code>AWS_IAM</code> and the auth policy is deleted, all requests are denied. If you are trying to remove the auth policy completely, you must set the auth type to <code>NONE</code>. If auth is enabled on the resource, but no auth policy is set, all requests are denied.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_auth_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_auth_policy.async_delete_auth_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the specified resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse":
        """<p>Retrieves information about the auth policy for the specified service or service network.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_auth_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_auth_policy.async_get_auth_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves information about the specified resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the service network or service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response.ListServiceNetworkVpcEndpointAssociationsResponse":
        """<p>Lists the associations between a service network and a VPC endpoint.</p>

        Args:
            service_network_identifier: <p>The ID of the service network associated with the VPC endpoint.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response.ListServiceNetworkVpcEndpointAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations.async_list_service_network_vpc_endpoint_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier
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

    async def iter_list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_vpc_lattice.types.service_network_endpoint_association.ServiceNetworkEndpointAssociation]":
        _token = next_token
        while True:
            _response = await self.list_service_network_vpc_endpoint_associations(
                service_network_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        policy: "aws_sdk_vpc_lattice.types.auth_policy_string.AuthPolicyString",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse":
        r"""<p>Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html\">Auth policies</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.put_auth_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.put_auth_policy.async_put_auth_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        policy: "aws_sdk_vpc_lattice.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based permission policy to a service or service network. The policy must contain the same actions and condition statements as the Amazon Web Services Resource Access Manager permission for sharing services and service networks.</p>

        Args:
            resource_arn: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>An IAM policy. The policy string in JSON must not contain newlines or blank lines.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        tags: "aws_sdk_vpc_lattice.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        tag_keys: "aws_sdk_vpc_lattice.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys of the tags to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
