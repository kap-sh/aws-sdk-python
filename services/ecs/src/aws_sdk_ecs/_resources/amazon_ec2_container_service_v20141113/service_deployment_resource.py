from typing import Optional, TYPE_CHECKING
from aws_sdk_ecs._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)

if TYPE_CHECKING:
    from aws_sdk_ecs._services.ecs import ECSClient, ECSClientConfig
    from aws_sdk_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    import aws_sdk_ecs.types.describe_service_deployments_request
    import aws_sdk_ecs.types.describe_service_deployments_response
    import aws_sdk_ecs.types.string_list


class ServiceDeploymentResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_service_deployments(
        self,
        service_deployment_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse":
        """<p>Describes one or more of your service deployments.</p> <p>A service deployment happens when you release a software update for the service. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html\">View service history using Amazon ECS service deployments</a>.</p>

        Args:
            service_deployment_arns: <p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>

        Examples:
            To describe a service deployment
            This example describes a service deployment for the service sd-example in the example cluster.

            >>> client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5'])
            To describe a service deployment with a paused lifecycle hook
            This example describes a service deployment that is currently paused at a lifecycle hook. The lifecycleHookDetails field shows the status of the pause hook, including when it will expire and what action will be taken if the timeout is reached.

            >>> client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments.describe_service_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input["service_deployment_arns"] = service_deployment_arns

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServiceDeploymentResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_service_deployments(
        self,
        service_deployment_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse":
        """<p>Describes one or more of your service deployments.</p> <p>A service deployment happens when you release a software update for the service. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html\">View service history using Amazon ECS service deployments</a>.</p>

        Args:
            service_deployment_arns: <p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>

        Examples:
            To describe a service deployment
            This example describes a service deployment for the service sd-example in the example cluster.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5'])
            To describe a service deployment with a paused lifecycle hook
            This example describes a service deployment that is currently paused at a lifecycle hook. The lifecycleHookDetails field shows the status of the pause hook, including when it will expire and what action will be taken if the timeout is reached.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments.async_describe_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input["service_deployment_arns"] = service_deployment_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
