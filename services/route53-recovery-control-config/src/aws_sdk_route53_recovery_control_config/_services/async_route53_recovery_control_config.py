"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#Route53RecoveryControlConfig``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_route53_recovery_control_config._auth._signers
import aws_sdk_route53_recovery_control_config._auth._sigv4
from aws_sdk_route53_recovery_control_config._auth._identity import Credentials
from aws_sdk_route53_recovery_control_config._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_route53_recovery_control_config._auth._zapros_handler import AuthMiddleware
from aws_sdk_route53_recovery_control_config._pagination import (
    resolve_path as _resolve_path,
)
from aws_sdk_route53_recovery_control_config._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__list_of__string
    import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string
    import aws_sdk_route53_recovery_control_config.types.__string_max36_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.assertion_rule_update
    import aws_sdk_route53_recovery_control_config.types.cluster
    import aws_sdk_route53_recovery_control_config.types.control_panel
    import aws_sdk_route53_recovery_control_config.types.create_cluster_request
    import aws_sdk_route53_recovery_control_config.types.create_cluster_response
    import aws_sdk_route53_recovery_control_config.types.create_control_panel_request
    import aws_sdk_route53_recovery_control_config.types.create_control_panel_response
    import aws_sdk_route53_recovery_control_config.types.create_routing_control_request
    import aws_sdk_route53_recovery_control_config.types.create_routing_control_response
    import aws_sdk_route53_recovery_control_config.types.create_safety_rule_request
    import aws_sdk_route53_recovery_control_config.types.create_safety_rule_response
    import aws_sdk_route53_recovery_control_config.types.delete_cluster_request
    import aws_sdk_route53_recovery_control_config.types.delete_cluster_response
    import aws_sdk_route53_recovery_control_config.types.delete_control_panel_request
    import aws_sdk_route53_recovery_control_config.types.delete_control_panel_response
    import aws_sdk_route53_recovery_control_config.types.delete_routing_control_request
    import aws_sdk_route53_recovery_control_config.types.delete_routing_control_response
    import aws_sdk_route53_recovery_control_config.types.delete_safety_rule_request
    import aws_sdk_route53_recovery_control_config.types.delete_safety_rule_response
    import aws_sdk_route53_recovery_control_config.types.describe_cluster_request
    import aws_sdk_route53_recovery_control_config.types.describe_cluster_response
    import aws_sdk_route53_recovery_control_config.types.describe_control_panel_request
    import aws_sdk_route53_recovery_control_config.types.describe_control_panel_response
    import aws_sdk_route53_recovery_control_config.types.describe_routing_control_request
    import aws_sdk_route53_recovery_control_config.types.describe_routing_control_response
    import aws_sdk_route53_recovery_control_config.types.describe_safety_rule_request
    import aws_sdk_route53_recovery_control_config.types.describe_safety_rule_response
    import aws_sdk_route53_recovery_control_config.types.gating_rule_update
    import aws_sdk_route53_recovery_control_config.types.get_resource_policy_request
    import aws_sdk_route53_recovery_control_config.types.get_resource_policy_response
    import aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_request
    import aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_response
    import aws_sdk_route53_recovery_control_config.types.list_clusters_request
    import aws_sdk_route53_recovery_control_config.types.list_clusters_response
    import aws_sdk_route53_recovery_control_config.types.list_control_panels_request
    import aws_sdk_route53_recovery_control_config.types.list_control_panels_response
    import aws_sdk_route53_recovery_control_config.types.list_routing_controls_request
    import aws_sdk_route53_recovery_control_config.types.list_routing_controls_response
    import aws_sdk_route53_recovery_control_config.types.list_safety_rules_request
    import aws_sdk_route53_recovery_control_config.types.list_safety_rules_response
    import aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_request
    import aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_response
    import aws_sdk_route53_recovery_control_config.types.max_results
    import aws_sdk_route53_recovery_control_config.types.network_type
    import aws_sdk_route53_recovery_control_config.types.new_assertion_rule
    import aws_sdk_route53_recovery_control_config.types.new_gating_rule
    import aws_sdk_route53_recovery_control_config.types.routing_control
    import aws_sdk_route53_recovery_control_config.types.rule
    import aws_sdk_route53_recovery_control_config.types.tag_resource_request
    import aws_sdk_route53_recovery_control_config.types.tag_resource_response
    import aws_sdk_route53_recovery_control_config.types.untag_resource_request
    import aws_sdk_route53_recovery_control_config.types.untag_resource_response
    import aws_sdk_route53_recovery_control_config.types.update_cluster_request
    import aws_sdk_route53_recovery_control_config.types.update_cluster_response
    import aws_sdk_route53_recovery_control_config.types.update_control_panel_request
    import aws_sdk_route53_recovery_control_config.types.update_control_panel_response
    import aws_sdk_route53_recovery_control_config.types.update_routing_control_request
    import aws_sdk_route53_recovery_control_config.types.update_routing_control_response
    import aws_sdk_route53_recovery_control_config.types.update_safety_rule_request
    import aws_sdk_route53_recovery_control_config.types.update_safety_rule_response


class AsyncRoute53RecoveryControlConfigClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncRoute53RecoveryControlConfigClient:
    """A client for the ``Route53RecoveryControlConfig`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_dual_stack: bool | None = None,
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncRoute53RecoveryControlConfigClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53RecoveryControlConfigClientConfig = (
            config_overrides or {}
        )
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_cluster(
        self,
        cluster_name: "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        tags: Optional[
            "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
        network_type: Optional[
            "aws_sdk_route53_recovery_control_config.types.network_type.NetworkType"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.create_cluster_response.CreateClusterResponse":
        """<p>Create a new cluster. A cluster is a set of redundant Regional endpoints against which you can run API calls to update or get the state of one or more routing controls. Each cluster has a name, status, Amazon Resource Name (ARN), and an array of the five cluster endpoints (one for each supported Amazon Web Services Region) that you can use with API calls to the cluster data plane.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_name: <p>The name of the cluster.</p>
            tags: <p>The tags associated with the cluster.</p>
            network_type: <p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.create_cluster_response.CreateClusterResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.create_cluster_request.CreateClusterRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_control_panel(
        self,
        cluster_arn: "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09",
        control_panel_name: "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        tags: Optional[
            "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.create_control_panel_response.CreateControlPanelResponse":
        """<p>Creates a new control panel. A control panel represents a group of routing controls that can be changed together in a single transaction. You can use a control panel to centrally view the operational status of applications across your organization, and trigger multi-app failovers in a single transaction, for example, to fail over an Availability Zone or Amazon Web Services Region.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster for the control panel.</p>
            control_panel_name: <p>The name of the control panel.</p>
            tags: <p>The tags associated with the control panel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.create_control_panel_request.CreateControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.create_control_panel_response.CreateControlPanelResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_control_panel

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_control_panel.async_create_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.create_control_panel_request.CreateControlPanelRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["cluster_arn"] = cluster_arn
        input_["control_panel_name"] = control_panel_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_routing_control(
        self,
        cluster_arn: "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09",
        routing_control_name: "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        client_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        control_panel_arn: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.create_routing_control_response.CreateRoutingControlResponse":
        """<p>Creates a new routing control.</p> <p>A routing control has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control traffic routing.</p> <p>To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster that includes the routing control.</p>
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel that includes the routing control.</p>
            routing_control_name: <p>The name of the routing control.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.create_routing_control_request.CreateRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.create_routing_control_response.CreateRoutingControlResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_routing_control

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_routing_control.async_create_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.create_routing_control_request.CreateRoutingControlRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["cluster_arn"] = cluster_arn
        if control_panel_arn is not None:
            input_["control_panel_arn"] = control_panel_arn
        input_["routing_control_name"] = routing_control_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_safety_rule(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        assertion_rule: Optional[
            "aws_sdk_route53_recovery_control_config.types.new_assertion_rule.NewAssertionRule"
        ] = None,
        client_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
        ] = None,
        gating_rule: Optional[
            "aws_sdk_route53_recovery_control_config.types.new_gating_rule.NewGatingRule"
        ] = None,
        tags: Optional[
            "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.create_safety_rule_response.CreateSafetyRuleResponse":
        """<p>Creates a safety rule in a control panel. Safety rules let you add safeguards around changing routing control states, and for enabling and disabling routing controls, to help prevent unexpected outcomes.</p> <p>There are two types of safety rules: assertion rules and gating rules.</p> <p>Assertion rule: An assertion rule enforces that, when you change a routing control state, that a certain criteria is met. For example, the criteria might be that at least one routing control state is On after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.</p> <p>Gating rule: A gating rule lets you configure a gating routing control as an overall \"on/off\" switch for a group of routing controls. Or, you can configure more complex gating scenarios, for example by configuring multiple gating routing controls.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.safety-rules.html\">Safety rules</a> in the Amazon Route 53 Application Recovery Controller Developer Guide.</p>

        Args:
            assertion_rule: <p>The assertion rule requested.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>
            gating_rule: <p>The gating rule requested.</p>
            tags: <p>The tags associated with the safety rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.create_safety_rule_request.CreateSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.create_safety_rule_response.CreateSafetyRuleResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_safety_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.create_safety_rule.async_create_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.create_safety_rule_request.CreateSafetyRuleRequest = {}  # type: ignore[typeddict-item]
        if assertion_rule is not None:
            input_["assertion_rule"] = assertion_rule
        if client_token is not None:
            input_["client_token"] = client_token
        if gating_rule is not None:
            input_["gating_rule"] = gating_rule
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cluster(
        self,
        cluster_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Delete a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster that you're deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.delete_cluster_request.DeleteClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_arn"] = cluster_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_control_panel(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.delete_control_panel_response.DeleteControlPanelResponse":
        """<p>Deletes a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.delete_control_panel_request.DeleteControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.delete_control_panel_response.DeleteControlPanelResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_control_panel

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_control_panel.async_delete_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.delete_control_panel_request.DeleteControlPanelRequest = {}  # type: ignore[typeddict-item]
        input_["control_panel_arn"] = control_panel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_routing_control(
        self,
        routing_control_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.delete_routing_control_response.DeleteRoutingControlResponse":
        """<p>Deletes a routing control.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control that you're deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.delete_routing_control_request.DeleteRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.delete_routing_control_response.DeleteRoutingControlResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_routing_control

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_routing_control.async_delete_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.delete_routing_control_request.DeleteRoutingControlRequest = {}  # type: ignore[typeddict-item]
        input_["routing_control_arn"] = routing_control_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_safety_rule(
        self,
        safety_rule_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.delete_safety_rule_response.DeleteSafetyRuleResponse":
        """<p>Deletes a safety rule.</p>/&gt;

        Args:
            safety_rule_arn: <p>The ARN of the safety rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.delete_safety_rule_request.DeleteSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.delete_safety_rule_response.DeleteSafetyRuleResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_safety_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.delete_safety_rule.async_delete_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.delete_safety_rule_request.DeleteSafetyRuleRequest = {}  # type: ignore[typeddict-item]
        input_["safety_rule_arn"] = safety_rule_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_cluster(
        self,
        cluster_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.describe_cluster_response.DescribeClusterResponse":
        """<p>Display the details about a cluster. The response includes the cluster name, endpoints, status, and Amazon Resource Name (ARN).</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_cluster.async_describe_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.describe_cluster_request.DescribeClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_arn"] = cluster_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_control_panel(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.describe_control_panel_response.DescribeControlPanelResponse":
        """<p>Displays details about a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.describe_control_panel_request.DescribeControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.describe_control_panel_response.DescribeControlPanelResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_control_panel

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_control_panel.async_describe_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.describe_control_panel_request.DescribeControlPanelRequest = {}  # type: ignore[typeddict-item]
        input_["control_panel_arn"] = control_panel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_routing_control(
        self,
        routing_control_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.describe_routing_control_response.DescribeRoutingControlResponse":
        """<p>Displays details about a routing control. A routing control has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control routing.</p> <p>To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.describe_routing_control_request.DescribeRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.describe_routing_control_response.DescribeRoutingControlResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_routing_control

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_routing_control.async_describe_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.describe_routing_control_request.DescribeRoutingControlRequest = {}  # type: ignore[typeddict-item]
        input_["routing_control_arn"] = routing_control_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_safety_rule(
        self,
        safety_rule_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.describe_safety_rule_response.DescribeSafetyRuleResponse":
        """<p>Returns information about a safety rule.</p>

        Args:
            safety_rule_arn: <p>The ARN of the safety rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.describe_safety_rule_request.DescribeSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.describe_safety_rule_response.DescribeSafetyRuleResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_safety_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.describe_safety_rule.async_describe_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.describe_safety_rule_request.DescribeSafetyRuleRequest = {}  # type: ignore[typeddict-item]
        input_["safety_rule_arn"] = safety_rule_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Get information about the resource policy for a cluster.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_associated_route53_health_checks(
        self,
        routing_control_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_response.ListAssociatedRoute53HealthChecksResponse":
        """<p>Returns an array of all Amazon Route 53 health checks associated with a specific routing control.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_request.ListAssociatedRoute53HealthChecksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_response.ListAssociatedRoute53HealthChecksResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_associated_route53_health_checks

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_associated_route53_health_checks.async_list_associated_route53_health_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_associated_route53_health_checks_request.ListAssociatedRoute53HealthChecksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["routing_control_arn"] = routing_control_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_associated_route53_health_checks(
        self,
        routing_control_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_control_config.types.__string_max36_pattern_s.__stringMax36PatternS]":
        _token = next_token
        while True:
            _response = await self.list_associated_route53_health_checks(
                routing_control_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_check_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_clusters_response.ListClustersResponse":
        """<p>Returns an array of all the clusters in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_clusters_response.ListClustersResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_clusters

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_clusters_request.ListClustersRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_control_config.types.cluster.Cluster]":
        _token = next_token
        while True:
            _response = await self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_control_panels(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        cluster_arn: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_control_panels_response.ListControlPanelsResponse":
        """<p>Returns an array of control panels in an account or in a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of a cluster.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_control_panels_request.ListControlPanelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_control_panels_response.ListControlPanelsResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_control_panels

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_control_panels.async_list_control_panels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_control_panels_request.ListControlPanelsRequest = {}  # type: ignore[typeddict-item]
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
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

    async def iter_list_control_panels(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        cluster_arn: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_control_config.types.control_panel.ControlPanel]":
        _token = next_token
        while True:
            _response = await self.list_control_panels(
                config_overrides=config_overrides,
                cluster_arn=cluster_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("control_panels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_routing_controls(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_routing_controls_response.ListRoutingControlsResponse":
        """<p>Returns an array of routing controls for a control panel. A routing control is an Amazon Route 53 Application Recovery Controller construct that has one of two states: ON and OFF. You can map the routing control state to the state of an Amazon Route 53 health check, which can be used to control routing.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_routing_controls_request.ListRoutingControlsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_routing_controls_response.ListRoutingControlsResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_routing_controls

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_routing_controls.async_list_routing_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_routing_controls_request.ListRoutingControlsRequest = {}  # type: ignore[typeddict-item]
        input_["control_panel_arn"] = control_panel_arn
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

    async def iter_list_routing_controls(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_control_config.types.routing_control.RoutingControl]":
        _token = next_token
        while True:
            _response = await self.list_routing_controls(
                control_panel_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("routing_controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_safety_rules(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_safety_rules_response.ListSafetyRulesResponse":
        """<p>List the safety rules (the assertion rules and gating rules) that you've defined for the routing controls in a control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_safety_rules_request.ListSafetyRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_safety_rules_response.ListSafetyRulesResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_safety_rules

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_safety_rules.async_list_safety_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_safety_rules_request.ListSafetyRulesRequest = {}  # type: ignore[typeddict-item]
        input_["control_panel_arn"] = control_panel_arn
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

    async def iter_list_safety_rules(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_control_config.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_control_config.types.rule.Rule]":
        _token = next_token
        while True:
            _response = await self.list_safety_rules(
                control_panel_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("safety_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        tags: "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>
            tags: <p>The tags associated with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string",
        tag_keys: "aws_sdk_route53_recovery_control_config.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>
            tag_keys: <p>Keys for the tags to be removed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_cluster(
        self,
        cluster_arn: "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09",
        network_type: "aws_sdk_route53_recovery_control_config.types.network_type.NetworkType",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates an existing cluster. You can only update the network type of a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            network_type: <p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.update_cluster_request.UpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_arn"] = cluster_arn
        input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_control_panel(
        self,
        control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09",
        control_panel_name: "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.update_control_panel_response.UpdateControlPanelResponse":
        """<p>Updates a control panel. The only update you can make to a control panel is to change the name of the control panel.</p>

        Args:
            control_panel_arn: <p>The Amazon Resource Name (ARN) of the control panel.</p>
            control_panel_name: <p>The name of the control panel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.update_control_panel_request.UpdateControlPanelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.update_control_panel_response.UpdateControlPanelResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_control_panel

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_control_panel.async_update_control_panel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.update_control_panel_request.UpdateControlPanelRequest = {}  # type: ignore[typeddict-item]
        input_["control_panel_arn"] = control_panel_arn
        input_["control_panel_name"] = control_panel_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_routing_control(
        self,
        routing_control_arn: "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09",
        routing_control_name: "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS",
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.update_routing_control_response.UpdateRoutingControlResponse":
        """<p>Updates a routing control. You can only update the name of the routing control. To get or update the routing control state, see the Recovery Cluster (data plane) API actions for Amazon Route 53 Application Recovery Controller.</p>

        Args:
            routing_control_arn: <p>The Amazon Resource Name (ARN) of the routing control.</p>
            routing_control_name: <p>The name of the routing control.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.update_routing_control_request.UpdateRoutingControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.update_routing_control_response.UpdateRoutingControlResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_routing_control

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_routing_control.async_update_routing_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.update_routing_control_request.UpdateRoutingControlRequest = {}  # type: ignore[typeddict-item]
        input_["routing_control_arn"] = routing_control_arn
        input_["routing_control_name"] = routing_control_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_safety_rule(
        self,
        *,
        config_overrides: Optional[
            AsyncRoute53RecoveryControlConfigClientConfig
        ] = None,
        assertion_rule_update: Optional[
            "aws_sdk_route53_recovery_control_config.types.assertion_rule_update.AssertionRuleUpdate"
        ] = None,
        gating_rule_update: Optional[
            "aws_sdk_route53_recovery_control_config.types.gating_rule_update.GatingRuleUpdate"
        ] = None,
    ) -> "aws_sdk_route53_recovery_control_config.types.update_safety_rule_response.UpdateSafetyRuleResponse":
        """<p>Update a safety rule (an assertion rule or gating rule). You can only update the name and the waiting period for a safety rule. To make other updates, delete the safety rule and create a new one.</p>

        Args:
            assertion_rule_update: <p>The assertion rule to update.</p>
            gating_rule_update: <p>The gating rule to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_control_config.types.update_safety_rule_request.UpdateSafetyRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_control_config.types.update_safety_rule_response.UpdateSafetyRuleResponse"
        ]:
            import aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_safety_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_control_config._operations.route53_recovery_control_config.update_safety_rule.async_update_safety_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_control_config.types.update_safety_rule_request.UpdateSafetyRuleRequest = {}  # type: ignore[typeddict-item]
        if assertion_rule_update is not None:
            input_["assertion_rule_update"] = assertion_rule_update
        if gating_rule_update is not None:
            input_["gating_rule_update"] = gating_rule_update

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
