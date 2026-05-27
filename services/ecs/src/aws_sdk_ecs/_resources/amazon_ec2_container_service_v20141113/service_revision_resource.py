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
    from aws_sdk_ecs._services.amazon_ec2_container_service_v20141113 import (
        ECSClient,
        ECSClientConfig,
    )
    from aws_sdk_ecs._services.async_amazon_ec2_container_service_v20141113 import (
        AsyncECSClient,
        AsyncECSClientConfig,
    )
    import aws_sdk_ecs.types.describe_service_revisions_request
    import aws_sdk_ecs.types.describe_service_revisions_response
    import aws_sdk_ecs.types.string_list


class ServiceRevisionResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_service_revisions(
        self,
        service_revision_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse":
        """<p>Describes one or more service revisions.</p> <p>A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html\">Amazon ECS service revisions</a>.</p> <p>You can't describe a service revision that was created before October 25, 2024.</p>

        Args:
            service_revision_arns: <p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html\">ListServiceDeployments</a> to get the ARNs.</p>

        Examples:
            To describe a service revision
            This example describes a service revision with the specified ARN

            >>> client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions.describe_service_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest = {}  # type: ignore[typeddict-item]
        input["service_revision_arns"] = service_revision_arns

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServiceRevisionResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_service_revisions(
        self,
        service_revision_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse":
        """<p>Describes one or more service revisions.</p> <p>A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html\">Amazon ECS service revisions</a>.</p> <p>You can't describe a service revision that was created before October 25, 2024.</p>

        Args:
            service_revision_arns: <p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html\">ListServiceDeployments</a> to get the ARNs.</p>

        Examples:
            To describe a service revision
            This example describes a service revision with the specified ARN

            >>> await client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions.async_describe_service_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest = {}  # type: ignore[typeddict-item]
        input["service_revision_arns"] = service_revision_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
