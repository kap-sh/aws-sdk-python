"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Route53RecoveryReadiness``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_route53_recovery_readiness._auth._signers
import aws_sdk_route53_recovery_readiness._auth._sigv4
from aws_sdk_route53_recovery_readiness._auth._identity import Credentials
from aws_sdk_route53_recovery_readiness._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_route53_recovery_readiness._auth._zapros_handler import AuthMiddleware
from aws_sdk_route53_recovery_readiness._pagination import resolve_path as _resolve_path
from aws_sdk_route53_recovery_readiness._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__list_of_resource
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09
    import aws_sdk_route53_recovery_readiness.types.cell_output
    import aws_sdk_route53_recovery_readiness.types.create_cell_request
    import aws_sdk_route53_recovery_readiness.types.create_cell_response
    import aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_request
    import aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_response
    import aws_sdk_route53_recovery_readiness.types.create_readiness_check_request
    import aws_sdk_route53_recovery_readiness.types.create_readiness_check_response
    import aws_sdk_route53_recovery_readiness.types.create_recovery_group_request
    import aws_sdk_route53_recovery_readiness.types.create_recovery_group_response
    import aws_sdk_route53_recovery_readiness.types.create_resource_set_request
    import aws_sdk_route53_recovery_readiness.types.create_resource_set_response
    import aws_sdk_route53_recovery_readiness.types.cross_account_authorization
    import aws_sdk_route53_recovery_readiness.types.delete_cell_request
    import aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_request
    import aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_response
    import aws_sdk_route53_recovery_readiness.types.delete_readiness_check_request
    import aws_sdk_route53_recovery_readiness.types.delete_recovery_group_request
    import aws_sdk_route53_recovery_readiness.types.delete_resource_set_request
    import aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_request
    import aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_response
    import aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_request
    import aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_response
    import aws_sdk_route53_recovery_readiness.types.get_cell_request
    import aws_sdk_route53_recovery_readiness.types.get_cell_response
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_request
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_request
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_response
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_response
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_request
    import aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_response
    import aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request
    import aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response
    import aws_sdk_route53_recovery_readiness.types.get_recovery_group_request
    import aws_sdk_route53_recovery_readiness.types.get_recovery_group_response
    import aws_sdk_route53_recovery_readiness.types.get_resource_set_request
    import aws_sdk_route53_recovery_readiness.types.get_resource_set_response
    import aws_sdk_route53_recovery_readiness.types.list_cells_request
    import aws_sdk_route53_recovery_readiness.types.list_cells_response
    import aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_request
    import aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_response
    import aws_sdk_route53_recovery_readiness.types.list_readiness_checks_request
    import aws_sdk_route53_recovery_readiness.types.list_readiness_checks_response
    import aws_sdk_route53_recovery_readiness.types.list_recovery_groups_request
    import aws_sdk_route53_recovery_readiness.types.list_recovery_groups_response
    import aws_sdk_route53_recovery_readiness.types.list_resource_sets_request
    import aws_sdk_route53_recovery_readiness.types.list_resource_sets_response
    import aws_sdk_route53_recovery_readiness.types.list_rules_output
    import aws_sdk_route53_recovery_readiness.types.list_rules_request
    import aws_sdk_route53_recovery_readiness.types.list_rules_response
    import aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_request
    import aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_response
    import aws_sdk_route53_recovery_readiness.types.max_results
    import aws_sdk_route53_recovery_readiness.types.readiness_check_output
    import aws_sdk_route53_recovery_readiness.types.readiness_check_summary
    import aws_sdk_route53_recovery_readiness.types.recovery_group_output
    import aws_sdk_route53_recovery_readiness.types.resource_result
    import aws_sdk_route53_recovery_readiness.types.resource_set_output
    import aws_sdk_route53_recovery_readiness.types.rule_result
    import aws_sdk_route53_recovery_readiness.types.tag_resource_request
    import aws_sdk_route53_recovery_readiness.types.tag_resource_response
    import aws_sdk_route53_recovery_readiness.types.tags
    import aws_sdk_route53_recovery_readiness.types.untag_resource_request
    import aws_sdk_route53_recovery_readiness.types.update_cell_request
    import aws_sdk_route53_recovery_readiness.types.update_cell_response
    import aws_sdk_route53_recovery_readiness.types.update_readiness_check_request
    import aws_sdk_route53_recovery_readiness.types.update_readiness_check_response
    import aws_sdk_route53_recovery_readiness.types.update_recovery_group_request
    import aws_sdk_route53_recovery_readiness.types.update_recovery_group_response
    import aws_sdk_route53_recovery_readiness.types.update_resource_set_request
    import aws_sdk_route53_recovery_readiness.types.update_resource_set_response


class AsyncRoute53RecoveryReadinessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
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


class AsyncRoute53RecoveryReadinessClient:
    """A client for the ``Route53RecoveryReadiness`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncRoute53RecoveryReadinessClientConfig(
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

    def operation_options(
        self,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53RecoveryReadinessClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def create_cell(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        cells: Optional[
            "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
        tags: Optional["aws_sdk_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.create_cell_response.CreateCellResponse":
        """<p>Creates a cell in an account.</p>

        Args:
            cell_name: <p>The name of the cell to create.</p>
            cells: <p>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Amazon Web Services Regions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.create_cell_request.CreateCellRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.create_cell_response.CreateCellResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_cell

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_cell.async_create_cell(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.create_cell_request.CreateCellRequest = {}  # type: ignore[typeddict-item]
        input_["cell_name"] = cell_name
        if cells is not None:
            input_["cells"] = cells
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_cross_account_authorization(
        self,
        cross_account_authorization: "aws_sdk_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_response.CreateCrossAccountAuthorizationResponse":
        """<p>Creates a cross-account readiness authorization. This lets you authorize another account to work with Route 53 Application Recovery Controller, for example, to check the readiness status of resources in a separate account.</p>

        Args:
            cross_account_authorization: <p>The cross-account authorization.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_request.CreateCrossAccountAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_response.CreateCrossAccountAuthorizationResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_cross_account_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_cross_account_authorization.async_create_cross_account_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.create_cross_account_authorization_request.CreateCrossAccountAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["cross_account_authorization"] = cross_account_authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_readiness_check(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        tags: Optional["aws_sdk_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.create_readiness_check_response.CreateReadinessCheckResponse":
        """<p>Creates a readiness check in an account. A readiness check monitors a resource set in your application, such as a set of Amazon Aurora instances, that Application Recovery Controller is auditing recovery readiness for. The audits run once every minute on every resource that's associated with a readiness check.</p>

        Args:
            readiness_check_name: <p>The name of the readiness check to create.</p>
            resource_set_name: <p>The name of the resource set to check.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.create_readiness_check_request.CreateReadinessCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.create_readiness_check_response.CreateReadinessCheckResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_readiness_check

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_readiness_check.async_create_readiness_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.create_readiness_check_request.CreateReadinessCheckRequest = {}  # type: ignore[typeddict-item]
        input_["readiness_check_name"] = readiness_check_name
        input_["resource_set_name"] = resource_set_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_recovery_group(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        cells: Optional[
            "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
        tags: Optional["aws_sdk_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.create_recovery_group_response.CreateRecoveryGroupResponse":
        """<p>Creates a recovery group in an account. A recovery group corresponds to an application and includes a list of the cells that make up the application.</p>

        Args:
            cells: <p>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</p>
            recovery_group_name: <p>The name of the recovery group to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.create_recovery_group_request.CreateRecoveryGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.create_recovery_group_response.CreateRecoveryGroupResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_recovery_group

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_recovery_group.async_create_recovery_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.create_recovery_group_request.CreateRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
        if cells is not None:
            input_["cells"] = cells
        input_["recovery_group_name"] = recovery_group_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_resource_set(
        self,
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_set_type: "aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09",
        resources: "aws_sdk_route53_recovery_readiness.types.__list_of_resource.__listOfResource",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        tags: Optional["aws_sdk_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.create_resource_set_response.CreateResourceSetResponse":
        """<p>Creates a resource set. A resource set is a set of resources of one type that span multiple cells. You can associate a resource set with a readiness check to monitor the resources for failover readiness.</p>

        Args:
            resource_set_name: <p>The name of the resource set to create.</p>
            resource_set_type: <p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>
            resources: <p>A list of resource objects in the resource set.</p>
            tags: <p>A tag to associate with the parameters for a resource set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.create_resource_set_request.CreateResourceSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.create_resource_set_response.CreateResourceSetResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_resource_set

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.create_resource_set.async_create_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.create_resource_set_request.CreateResourceSetRequest = {}  # type: ignore[typeddict-item]
        input_["resource_set_name"] = resource_set_name
        input_["resource_set_type"] = resource_set_type
        input_["resources"] = resources
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cell(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Delete a cell. When successful, the response code is 204, with no response body.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.delete_cell_request.DeleteCellRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cell

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cell.async_delete_cell(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.delete_cell_request.DeleteCellRequest = {}  # type: ignore[typeddict-item]
        input_["cell_name"] = cell_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cross_account_authorization(
        self,
        cross_account_authorization: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_response.DeleteCrossAccountAuthorizationResponse":
        """<p>Deletes cross account readiness authorization.</p>

        Args:
            cross_account_authorization: <p>The cross-account authorization.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_request.DeleteCrossAccountAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_response.DeleteCrossAccountAuthorizationResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cross_account_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cross_account_authorization.async_delete_cross_account_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.delete_cross_account_authorization_request.DeleteCrossAccountAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["cross_account_authorization"] = cross_account_authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_readiness_check(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.delete_readiness_check_request.DeleteReadinessCheckRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_readiness_check

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_readiness_check.async_delete_readiness_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.delete_readiness_check_request.DeleteReadinessCheckRequest = {}  # type: ignore[typeddict-item]
        input_["readiness_check_name"] = readiness_check_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_recovery_group(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a recovery group.</p>

        Args:
            recovery_group_name: <p>The name of a recovery group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.delete_recovery_group_request.DeleteRecoveryGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_recovery_group

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_recovery_group.async_delete_recovery_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.delete_recovery_group_request.DeleteRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
        input_["recovery_group_name"] = recovery_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_set(
        self,
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a resource set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.delete_resource_set_request.DeleteResourceSetRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_resource_set

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.delete_resource_set.async_delete_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.delete_resource_set_request.DeleteResourceSetRequest = {}  # type: ignore[typeddict-item]
        input_["resource_set_name"] = resource_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_architecture_recommendations(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_response.GetArchitectureRecommendationsResponse":
        """<p>Gets recommendations about architecture designs for improving resiliency for an application, based on a recovery group.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            recovery_group_name: <p>The name of a recovery group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_request.GetArchitectureRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_response.GetArchitectureRecommendationsResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_architecture_recommendations

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_architecture_recommendations.async_get_architecture_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_architecture_recommendations_request.GetArchitectureRecommendationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["recovery_group_name"] = recovery_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cell(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_cell_response.GetCellResponse":
        """<p>Gets information about a cell including cell name, cell Amazon Resource Name (ARN), ARNs of nested cells for this cell, and a list of those cell ARNs with their associated recovery group ARNs.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_cell_request.GetCellRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_cell_response.GetCellResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell.async_get_cell(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_cell_request.GetCellRequest = {}  # type: ignore[typeddict-item]
        input_["cell_name"] = cell_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cell_readiness_summary(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_response.GetCellReadinessSummaryResponse":
        """<p>Gets readiness for a cell. Aggregates the readiness of all the resources that are associated with the cell into a single value.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_request.GetCellReadinessSummaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_response.GetCellReadinessSummaryResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell_readiness_summary

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell_readiness_summary.async_get_cell_readiness_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_cell_readiness_summary_request.GetCellReadinessSummaryRequest = {}  # type: ignore[typeddict-item]
        input_["cell_name"] = cell_name
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

    async def iter_get_cell_readiness_summary(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.readiness_check_summary.ReadinessCheckSummary]":
        _token = next_token
        while True:
            _response = await self.get_cell_readiness_summary(
                cell_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_readiness_check(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_readiness_check_response.GetReadinessCheckResponse":
        """<p>Gets details about a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_readiness_check_request.GetReadinessCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_readiness_check_response.GetReadinessCheckResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check.async_get_readiness_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_readiness_check_request.GetReadinessCheckRequest = {}  # type: ignore[typeddict-item]
        input_["readiness_check_name"] = readiness_check_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_readiness_check_resource_status(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_identifier: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_response.GetReadinessCheckResourceStatusResponse":
        """<p>Gets individual readiness status for a readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in the recovery group, use GetRecoveryGroupReadinessSummary.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            readiness_check_name: <p>Name of a readiness check.</p>
            resource_identifier: <p>The resource identifier, which is the Amazon Resource Name (ARN) or the identifier generated for the resource by Application Recovery Controller (for example, for a DNS target resource).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_request.GetReadinessCheckResourceStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_response.GetReadinessCheckResourceStatusResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_resource_status

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_resource_status.async_get_readiness_check_resource_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_readiness_check_resource_status_request.GetReadinessCheckResourceStatusRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["readiness_check_name"] = readiness_check_name
        input_["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_readiness_check_resource_status(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_identifier: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_route53_recovery_readiness.types.rule_result.RuleResult]"
    ):
        _token = next_token
        while True:
            _response = await self.get_readiness_check_resource_status(
                readiness_check_name,
                resource_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_readiness_check_status(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_response.GetReadinessCheckStatusResponse":
        """<p>Gets the readiness status for an individual readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in a recovery group, use GetRecoveryGroupReadinessSummary.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            readiness_check_name: <p>Name of a readiness check.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_request.GetReadinessCheckStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_response.GetReadinessCheckStatusResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_status

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_status.async_get_readiness_check_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_readiness_check_status_request.GetReadinessCheckStatusRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["readiness_check_name"] = readiness_check_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_readiness_check_status(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.resource_result.ResourceResult]":
        _token = next_token
        while True:
            _response = await self.get_readiness_check_status(
                readiness_check_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_recovery_group(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_recovery_group_response.GetRecoveryGroupResponse":
        """<p>Gets details about a recovery group, including a list of the cells that are included in it.</p>

        Args:
            recovery_group_name: <p>The name of a recovery group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_recovery_group_request.GetRecoveryGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_recovery_group_response.GetRecoveryGroupResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group.async_get_recovery_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_recovery_group_request.GetRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
        input_["recovery_group_name"] = recovery_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_recovery_group_readiness_summary(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response.GetRecoveryGroupReadinessSummaryResponse":
        """<p>Displays a summary of information about a recovery group's readiness status. Includes the readiness checks for resources in the recovery group and the readiness status of each one.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            recovery_group_name: <p>The name of a recovery group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request.GetRecoveryGroupReadinessSummaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response.GetRecoveryGroupReadinessSummaryResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group_readiness_summary

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group_readiness_summary.async_get_recovery_group_readiness_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request.GetRecoveryGroupReadinessSummaryRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["recovery_group_name"] = recovery_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_recovery_group_readiness_summary(
        self,
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.readiness_check_summary.ReadinessCheckSummary]":
        _token = next_token
        while True:
            _response = await self.get_recovery_group_readiness_summary(
                recovery_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resource_set(
        self,
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.get_resource_set_response.GetResourceSetResponse":
        """<p>Displays the details about a resource set, including a list of the resources in the set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.get_resource_set_request.GetResourceSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.get_resource_set_response.GetResourceSetResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_resource_set

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.get_resource_set.async_get_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.get_resource_set_request.GetResourceSetRequest = {}  # type: ignore[typeddict-item]
        input_["resource_set_name"] = resource_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_cells(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> (
        "aws_sdk_route53_recovery_readiness.types.list_cells_response.ListCellsResponse"
    ):
        """<p>Lists the cells for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_cells_request.ListCellsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_cells_response.ListCellsResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_cells

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_cells.async_list_cells(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_cells_request.ListCellsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_cells(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_route53_recovery_readiness.types.cell_output.CellOutput]"
    ):
        _token = next_token
        while True:
            _response = await self.list_cells(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cells",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cross_account_authorizations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_response.ListCrossAccountAuthorizationsResponse":
        """<p>Lists the cross-account readiness authorizations that are in place for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_request.ListCrossAccountAuthorizationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_response.ListCrossAccountAuthorizationsResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_cross_account_authorizations

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_cross_account_authorizations.async_list_cross_account_authorizations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_cross_account_authorizations_request.ListCrossAccountAuthorizationsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_cross_account_authorizations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization]":
        _token = next_token
        while True:
            _response = await self.list_cross_account_authorizations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cross_account_authorizations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_readiness_checks(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.list_readiness_checks_response.ListReadinessChecksResponse":
        """<p>Lists the readiness checks for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_readiness_checks_request.ListReadinessChecksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_readiness_checks_response.ListReadinessChecksResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_readiness_checks

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_readiness_checks.async_list_readiness_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_readiness_checks_request.ListReadinessChecksRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_readiness_checks(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.readiness_check_output.ReadinessCheckOutput]":
        _token = next_token
        while True:
            _response = await self.list_readiness_checks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recovery_groups(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.list_recovery_groups_response.ListRecoveryGroupsResponse":
        """<p>Lists the recovery groups in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_recovery_groups_request.ListRecoveryGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_recovery_groups_response.ListRecoveryGroupsResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_recovery_groups

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_recovery_groups.async_list_recovery_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_recovery_groups_request.ListRecoveryGroupsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_recovery_groups(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.recovery_group_output.RecoveryGroupOutput]":
        _token = next_token
        while True:
            _response = await self.list_recovery_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recovery_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_sets(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.list_resource_sets_response.ListResourceSetsResponse":
        """<p>Lists the resource sets in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_resource_sets_request.ListResourceSetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_resource_sets_response.ListResourceSetsResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_resource_sets

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_resource_sets.async_list_resource_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_resource_sets_request.ListResourceSetsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_resource_sets(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.resource_set_output.ResourceSetOutput]":
        _token = next_token
        while True:
            _response = await self.list_resource_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_rules(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_type: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> (
        "aws_sdk_route53_recovery_readiness.types.list_rules_response.ListRulesResponse"
    ):
        """<p>Lists all readiness rules, or lists the readiness rules for a specific resource type.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            resource_type: <p>The resource type that a readiness rule applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_rules_response.ListRulesResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_rules

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_rules_request.ListRulesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_type is not None:
            input_["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_rules(
        self,
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_type: Optional[
            "aws_sdk_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_route53_recovery_readiness.types.list_rules_output.ListRulesOutput]":
        _token = next_token
        while True:
            _response = await self.list_rules(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_type=resource_type,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resources(
        self,
        resource_arn: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_response.ListTagsForResourcesResponse":
        """<p>Lists the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_request.ListTagsForResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_response.ListTagsForResourcesResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_tags_for_resources

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.list_tags_for_resources.async_list_tags_for_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.list_tags_for_resources_request.ListTagsForResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        tags: "aws_sdk_route53_recovery_readiness.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>
            tags: <p></p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        tag_keys: "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>
            tag_keys: <p>The keys for tags you add to resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_cell(
        self,
        cell_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        cells: "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.update_cell_response.UpdateCellResponse":
        """<p>Updates a cell to replace the list of nested cells with a new list of nested cells.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
            cells: <p>A list of cell Amazon Resource Names (ARNs), which completely replaces the previous list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.update_cell_request.UpdateCellRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.update_cell_response.UpdateCellResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_cell

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_cell.async_update_cell(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.update_cell_request.UpdateCellRequest = {}  # type: ignore[typeddict-item]
        input_["cell_name"] = cell_name
        input_["cells"] = cells

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_readiness_check(
        self,
        readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.update_readiness_check_response.UpdateReadinessCheckResponse":
        """<p>Updates a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>
            resource_set_name: <p>The name of the resource set to be checked.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.update_readiness_check_request.UpdateReadinessCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.update_readiness_check_response.UpdateReadinessCheckResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_readiness_check

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_readiness_check.async_update_readiness_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.update_readiness_check_request.UpdateReadinessCheckRequest = {}  # type: ignore[typeddict-item]
        input_["readiness_check_name"] = readiness_check_name
        input_["resource_set_name"] = resource_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_recovery_group(
        self,
        cells: "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string",
        recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.update_recovery_group_response.UpdateRecoveryGroupResponse":
        """<p>Updates a recovery group.</p>

        Args:
            cells: <p>A list of cell Amazon Resource Names (ARNs). This list completely replaces the previous list.</p>
            recovery_group_name: <p>The name of a recovery group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.update_recovery_group_request.UpdateRecoveryGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.update_recovery_group_response.UpdateRecoveryGroupResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_recovery_group

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_recovery_group.async_update_recovery_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.update_recovery_group_request.UpdateRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
        input_["cells"] = cells
        input_["recovery_group_name"] = recovery_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_resource_set(
        self,
        resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string",
        resource_set_type: "aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09",
        resources: "aws_sdk_route53_recovery_readiness.types.__list_of_resource.__listOfResource",
        *,
        config_overrides: Optional[AsyncRoute53RecoveryReadinessClientConfig] = None,
    ) -> "aws_sdk_route53_recovery_readiness.types.update_resource_set_response.UpdateResourceSetResponse":
        """<p>Updates a resource set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>
            resource_set_type: <p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>
            resources: <p>A list of resource objects.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53_recovery_readiness.types.update_resource_set_request.UpdateResourceSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53_recovery_readiness.types.update_resource_set_response.UpdateResourceSetResponse"
        ]:
            import aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_resource_set

            (
                output,
                http_response,
            ) = await aws_sdk_route53_recovery_readiness._operations.route53_recovery_readiness.update_resource_set.async_update_resource_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_route53_recovery_readiness.types.update_resource_set_request.UpdateResourceSetRequest = {}  # type: ignore[typeddict-item]
        input_["resource_set_name"] = resource_set_name
        input_["resource_set_type"] = resource_set_type
        input_["resources"] = resources

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
