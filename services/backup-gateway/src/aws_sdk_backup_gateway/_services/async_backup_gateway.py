"""Generated from Smithy shape ``com.amazonaws.backupgateway#BackupOnPremises_v20210101``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_backup_gateway._auth._signers
import aws_sdk_backup_gateway._auth._sigv4
from aws_sdk_backup_gateway._auth._identity import Credentials
from aws_sdk_backup_gateway._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_backup_gateway._auth._zapros_handler import AuthMiddleware
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.gateway_resource import (
    AsyncGatewayResource,
)
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.hypervisor_resource import (
    AsyncHypervisorResource,
)
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.virtual_machine_resource import (
    AsyncVirtualMachineResource,
)
from aws_sdk_backup_gateway._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.list_tags_for_resource_input
    import aws_sdk_backup_gateway.types.list_tags_for_resource_output
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.tag_keys
    import aws_sdk_backup_gateway.types.tag_resource_input
    import aws_sdk_backup_gateway.types.tag_resource_output
    import aws_sdk_backup_gateway.types.tags
    import aws_sdk_backup_gateway.types.untag_resource_input
    import aws_sdk_backup_gateway.types.untag_resource_output


class AsyncBackupGatewayClientConfig(TypedDict, total=False):
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


class AsyncBackupGatewayClient:
    """A client for the ``BackupGateway`` service.

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
        self._config = AsyncBackupGatewayClientConfig(
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
        self.gateway_resource = AsyncGatewayResource(self)
        self.hypervisor_resource = AsyncHypervisorResource(self)
        self.virtual_machine_resource = AsyncVirtualMachineResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBackupGatewayClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBackupGatewayClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags applied to the resource identified by its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource's tags to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        tags: "aws_sdk_backup_gateway.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.tag_resource_output.TagResourceOutput":
        """<p>Tag the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_backup_gateway.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>The list of tag keys specifying which tags to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
