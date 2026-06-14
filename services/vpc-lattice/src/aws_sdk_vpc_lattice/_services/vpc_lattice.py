"""Generated from Smithy shape ``com.amazonaws.vpclattice#MercuryControlPlane``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._auth._identity import Credentials
from aws_sdk_vpc_lattice._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_vpc_lattice._auth._zapros_handler import AuthMiddleware
from aws_sdk_vpc_lattice._pagination import resolve_path as _resolve_path
from aws_sdk_vpc_lattice._resources.mercury_control_plane.access_log_subscription import (
    AccessLogSubscription,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.domain_verification import (
    DomainVerification,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.listener import Listener
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_configuration import (
    ResourceConfiguration,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_endpoint_association import (
    ResourceEndpointAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.resource_gateway import (
    ResourceGateway,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.rule import Rule
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service import Service
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_load_balancer_association import (
    ServiceLoadBalancerAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network import (
    ServiceNetwork,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_resource_association import (
    ServiceNetworkResourceAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_service_association import (
    ServiceNetworkServiceAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.service_network_vpc_association import (
    ServiceNetworkVpcAssociation,
)
from aws_sdk_vpc_lattice._resources.mercury_control_plane.target_group import (
    TargetGroup,
)
from aws_sdk_vpc_lattice._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class VPCLatticeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class VPCLatticeClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = VPCLatticeClientConfig(
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
        # resources
        self.access_log_subscription = AccessLogSubscription(self)
        self.domain_verification = DomainVerification(self)
        self.listener = Listener(self)
        self.resource_configuration = ResourceConfiguration(self)
        self.resource_endpoint_association = ResourceEndpointAssociation(self)
        self.resource_gateway = ResourceGateway(self)
        self.rule = Rule(self)
        self.service = Service(self)
        self.service_load_balancer_association = ServiceLoadBalancerAssociation(self)
        self.service_network = ServiceNetwork(self)
        self.service_network_resource_association = ServiceNetworkResourceAssociation(
            self
        )
        self.service_network_service_association = ServiceNetworkServiceAssociation(
            self
        )
        self.service_network_vpc_association = ServiceNetworkVpcAssociation(self)
        self.target_group = TargetGroup(self)

    def operation_options(
        self, config_overrides: Optional[VPCLatticeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: VPCLatticeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_update_rule(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rules: "aws_sdk_vpc_lattice.types.rule_update_list.RuleUpdateList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse":
        """<p>Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority.</p> <p> <b>Required permissions:</b> <code>vpc-lattice:UpdateRule</code> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_service-with-iam.html\">How Amazon VPC Lattice works with IAM</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rules: <p>The rules for the specified listener.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.batch_update_rule_response.BatchUpdateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.batch_update_rule

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.batch_update_rule.batch_update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.batch_update_rule_request.BatchUpdateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rules"] = rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> (
        "aws_sdk_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse"
    ):
        """<p>Deletes the specified auth policy. If an auth is set to <code>AWS_IAM</code> and the auth policy is deleted, all requests are denied. If you are trying to remove the auth policy completely, you must set the auth type to <code>NONE</code>. If auth is enabled on the resource, but no auth policy is set, all requests are denied.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_auth_policy_response.DeleteAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_auth_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_auth_policy.delete_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_auth_policy_request.DeleteAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the specified resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse":
        """<p>Retrieves information about the auth policy for the specified service or service network.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_auth_policy_response.GetAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_auth_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_auth_policy.get_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_auth_policy_request.GetAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves information about the specified resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the service network or service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_response.ListServiceNetworkVpcEndpointAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_endpoint_associations.list_service_network_vpc_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_vpc_endpoint_associations_request.ListServiceNetworkVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_identifier"] = service_network_identifier
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

    def iter_list_service_network_vpc_endpoint_associations(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_vpc_lattice.types.service_network_endpoint_association.ServiceNetworkEndpointAssociation]":
        _token = next_token
        while True:
            _response = self.list_service_network_vpc_endpoint_associations(
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_auth_policy(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        policy: "aws_sdk_vpc_lattice.types.auth_policy_string.AuthPolicyString",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse":
        """<p>Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html\">Auth policies</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.put_auth_policy_response.PutAuthPolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.put_auth_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.put_auth_policy.put_auth_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.put_auth_policy_request.PutAuthPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifier"] = resource_identifier
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn",
        policy: "aws_sdk_vpc_lattice.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based permission policy to a service or service network. The policy must contain the same actions and condition statements as the Amazon Web Services Resource Access Manager permission for sharing services and service networks.</p>

        Args:
            resource_arn: <p>The ID or ARN of the service network or service for which the policy is created.</p>
            policy: <p>An IAM policy. The policy string in JSON must not contain newlines or blank lines.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.put_resource_policy

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        tags: "aws_sdk_vpc_lattice.types.tag_map.TagMap",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.tag_resource

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn",
        tag_keys: "aws_sdk_vpc_lattice.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys of the tags to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.untag_resource

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
