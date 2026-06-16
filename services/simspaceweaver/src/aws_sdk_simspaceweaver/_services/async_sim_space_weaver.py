"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimSpaceWeaver``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_simspaceweaver._auth._signers
import aws_sdk_simspaceweaver._auth._sigv4
from aws_sdk_simspaceweaver._auth._identity import Credentials
from aws_sdk_simspaceweaver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_simspaceweaver._auth._zapros_handler import AuthMiddleware
from aws_sdk_simspaceweaver._resources.sim_space_weaver.simulation import (
    AsyncSimulation,
)
from aws_sdk_simspaceweaver._services._aws_config import aaws_config
from aws_sdk_simspaceweaver._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.list_tags_for_resource_input
    import aws_sdk_simspaceweaver.types.list_tags_for_resource_output
    import aws_sdk_simspaceweaver.types.sim_space_weaver_arn
    import aws_sdk_simspaceweaver.types.tag_key_list
    import aws_sdk_simspaceweaver.types.tag_map
    import aws_sdk_simspaceweaver.types.tag_resource_input
    import aws_sdk_simspaceweaver.types.tag_resource_output
    import aws_sdk_simspaceweaver.types.untag_resource_input
    import aws_sdk_simspaceweaver.types.untag_resource_output


class AsyncSimSpaceWeaverClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSimSpaceWeaverClient:
    """A client for the ``SimSpaceWeaver`` service.

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
        self._config = AsyncSimSpaceWeaverClientConfig(
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
        self.simulation = AsyncSimulation(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSimSpaceWeaverClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>Lists all tags on a SimSpace Weaver resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tags: "aws_sdk_simspaceweaver.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.tag_resource_output.TagResourceOutput":
        r"""<p>Adds tags to a SimSpace Weaver resource. For more information about tags, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add tags to. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>A list of tags to apply to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_simspaceweaver.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_simspaceweaver.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_simspaceweaver._operations.sim_space_weaver.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_simspaceweaver.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tag_keys: "aws_sdk_simspaceweaver.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Removes tags from a SimSpace Weaver resource. For more information about tags, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_simspaceweaver.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_simspaceweaver.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_simspaceweaver._operations.sim_space_weaver.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_simspaceweaver.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
