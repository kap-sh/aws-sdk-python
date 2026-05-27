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
    import aws_sdk_ecs.types.describe_daemon_revisions_request
    import aws_sdk_ecs.types.describe_daemon_revisions_response
    import aws_sdk_ecs.types.string_list


class DaemonRevisionResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_daemon_revisions(
        self,
        daemon_revision_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse":
        """<p>Describes one or more of your daemon revisions.</p> <p>A daemon revision is a snapshot of a daemon's configuration at the time a deployment was initiated. It captures the daemon task definition, container images, tag propagation, and execute command settings. Daemon revisions are immutable.</p>

        Args:
            daemon_revision_arns: <p>The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.</p>

        Examples:
            To describe daemon revisions
            This example describes a daemon revision for the my-monitoring-daemon daemon.

            >>> client.describe_daemon_revisions(daemon_revision_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions.describe_daemon_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest = {}  # type: ignore[typeddict-item]
        input["daemon_revision_arns"] = daemon_revision_arns

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDaemonRevisionResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_daemon_revisions(
        self,
        daemon_revision_arns: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse":
        """<p>Describes one or more of your daemon revisions.</p> <p>A daemon revision is a snapshot of a daemon's configuration at the time a deployment was initiated. It captures the daemon task definition, container images, tag propagation, and execute command settings. Daemon revisions are immutable.</p>

        Args:
            daemon_revision_arns: <p>The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.</p>

        Examples:
            To describe daemon revisions
            This example describes a daemon revision for the my-monitoring-daemon daemon.

            >>> await client.describe_daemon_revisions(daemon_revision_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions.async_describe_daemon_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest = {}  # type: ignore[typeddict-item]
        input["daemon_revision_arns"] = daemon_revision_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
