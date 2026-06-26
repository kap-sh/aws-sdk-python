from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_ecs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_daemon_deployments_request
    import aws_sdk_ecs.types.describe_daemon_deployments_response
    import aws_sdk_ecs.types.string_list
    from aws_sdk_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from aws_sdk_ecs._services.ecs import ECSClient, ECSClientConfig


class DaemonDeploymentResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_daemon_deployments(
        self,
        daemon_deployment_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse":
        """<p>Describes one or more of your daemon deployments.</p> <p>A daemon deployment orchestrates the progressive rollout of daemon task updates across container instances managed by the daemon's capacity providers. Each deployment includes circuit breaker and alarm-based rollback capabilities.</p>

        Args:
            daemon_deployment_arns: <p>The ARN of the daemon deployments to describe. You can specify up to 20 ARNs.</p>

        Raises:
            aws_sdk_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            aws_sdk_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            aws_sdk_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html\">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            aws_sdk_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            aws_sdk_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            aws_sdk_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            aws_sdk_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe daemon deployments
            This example describes a daemon deployment for the my-monitoring-daemon daemon.

            >>> client.describe_daemon_deployments(daemon_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments.describe_daemon_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input_["daemon_deployment_arns"] = daemon_deployment_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDaemonDeploymentResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_daemon_deployments(
        self,
        daemon_deployment_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse":
        """<p>Describes one or more of your daemon deployments.</p> <p>A daemon deployment orchestrates the progressive rollout of daemon task updates across container instances managed by the daemon's capacity providers. Each deployment includes circuit breaker and alarm-based rollback capabilities.</p>

        Args:
            daemon_deployment_arns: <p>The ARN of the daemon deployments to describe. You can specify up to 20 ARNs.</p>

        Raises:
            aws_sdk_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            aws_sdk_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            aws_sdk_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html\">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            aws_sdk_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            aws_sdk_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            aws_sdk_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            aws_sdk_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe daemon deployments
            This example describes a daemon deployment for the my-monitoring-daemon daemon.

            >>> await client.describe_daemon_deployments(daemon_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments.async_describe_daemon_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input_["daemon_deployment_arns"] = daemon_deployment_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
