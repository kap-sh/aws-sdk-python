"""Generated from Smithy shape ``com.amazonaws.scheduler#AWSChronosService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_scheduler._auth._signers
import aws_sdk_scheduler._auth._sigv4
from aws_sdk_scheduler._auth._identity import Credentials
from aws_sdk_scheduler._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_scheduler._auth._zapros_handler import AuthMiddleware
from aws_sdk_scheduler._resources.aws_chronos_service.schedule import AsyncSchedule
from aws_sdk_scheduler._resources.aws_chronos_service.schedule_group import (
    AsyncScheduleGroup,
)
from aws_sdk_scheduler._services._aws_config import aaws_config
from aws_sdk_scheduler._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.list_tags_for_resource_input
    import aws_sdk_scheduler.types.list_tags_for_resource_output
    import aws_sdk_scheduler.types.tag_key_list
    import aws_sdk_scheduler.types.tag_list
    import aws_sdk_scheduler.types.tag_resource_arn
    import aws_sdk_scheduler.types.tag_resource_input
    import aws_sdk_scheduler.types.tag_resource_output
    import aws_sdk_scheduler.types.untag_resource_input
    import aws_sdk_scheduler.types.untag_resource_output


class AsyncSchedulerClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSchedulerClient:
    """A client for the ``Scheduler`` service.

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
        self._config = AsyncSchedulerClientConfig(
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
        self.schedule = AsyncSchedule(self)
        self.schedule_group = AsyncScheduleGroup(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSchedulerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSchedulerClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_scheduler.types.tag_resource_arn.TagResourceArn",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
    ) -> "aws_sdk_scheduler.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with the Scheduler resource.</p>

        Args:
            resource_arn: <p>The ARN of the EventBridge Scheduler resource for which you want to view tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_scheduler.types.tag_resource_arn.TagResourceArn",
        tags: "aws_sdk_scheduler.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
    ) -> "aws_sdk_scheduler.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified EventBridge Scheduler resource. You can only assign tags to schedule groups.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the schedule group that you are adding tags to.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_scheduler.types.tag_resource_arn.TagResourceArn",
        tag_keys: "aws_sdk_scheduler.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
    ) -> "aws_sdk_scheduler.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified EventBridge Scheduler schedule group.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the schedule group from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
