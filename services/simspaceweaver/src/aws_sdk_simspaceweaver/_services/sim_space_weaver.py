"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimSpaceWeaver``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_simspaceweaver._auth._signers
import aws_sdk_simspaceweaver._auth._sigv4
from aws_sdk_simspaceweaver._auth._identity import Credentials
from aws_sdk_simspaceweaver._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_simspaceweaver._auth._zapros_handler import AuthMiddleware
from aws_sdk_simspaceweaver._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class SimSpaceWeaverClientConfig(TypedDict, total=False):
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


class SimSpaceWeaverClient:
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
        self.config = SimSpaceWeaverClientConfig(
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
        self, config_overrides: Optional[SimSpaceWeaverClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SimSpaceWeaverClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        *,
        config_overrides: Optional[SimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all tags on a SimSpace Weaver resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource

            output, http_response = (
                aws_sdk_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tags: "aws_sdk_simspaceweaver.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to a SimSpace Weaver resource. For more information about tags, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add tags to. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>A list of tags to apply to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_simspaceweaver.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_simspaceweaver.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.tag_resource

            output, http_response = (
                aws_sdk_simspaceweaver._operations.sim_space_weaver.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_simspaceweaver.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tag_keys: "aws_sdk_simspaceweaver.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SimSpaceWeaverClientConfig] = None,
    ) -> "aws_sdk_simspaceweaver.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a SimSpace Weaver resource. For more information about tags, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_simspaceweaver.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_simspaceweaver.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_simspaceweaver._operations.sim_space_weaver.untag_resource

            output, http_response = (
                aws_sdk_simspaceweaver._operations.sim_space_weaver.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_simspaceweaver.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
