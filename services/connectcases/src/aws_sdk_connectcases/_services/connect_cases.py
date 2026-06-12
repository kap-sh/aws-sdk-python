"""Generated from Smithy shape ``com.amazonaws.connectcases#AmazonConnectCases``."""

from aws_sdk_connectcases._auth._signers import SigV4Signer
from aws_sdk_connectcases._auth._sigv4 import presign_sigv4
from collections.abc import Iterator
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, BaseHandler, Client
from aws_sdk_connectcases._auth._zapros_handler import AuthMiddleware
from aws_sdk_connectcases._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
import time
from aws_sdk_connectcases.errors import (
    ServiceError,
    WaiterFailedError,
    WaiterTimeoutError,
)
import warnings
import aws_sdk_connectcases._auth._signers
import aws_sdk_connectcases._auth._sigv4
from aws_sdk_connectcases._auth._identity import Credentials
from aws_sdk_connectcases._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.arn
    import aws_sdk_connectcases.types.list_tags_for_resource_request
    import aws_sdk_connectcases.types.list_tags_for_resource_response
    import aws_sdk_connectcases.types.tag_key_list
    import aws_sdk_connectcases.types.tag_resource_request
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.untag_resource_request


class ConnectCasesClientConfig(TypedDict, total=False):
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


class ConnectCasesClient:
    """A client for the ``ConnectCases`` service.

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
        self.config = ConnectCasesClientConfig(
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
        self, config_overrides: Optional[ConnectCasesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectCasesClientConfig = config_overrides or {}
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
        arn: "aws_sdk_connectcases.types.arn.Arn",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_tags_for_resource

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_connectcases.types.arn.Arn",
        tags: "aws_sdk_connectcases.types.tags.Tags",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> None:
        """<p>Adds tags to a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.tag_resource

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_connectcases.types.arn.Arn",
        tag_keys: "aws_sdk_connectcases.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> None:
        """<p>Untags a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>
            tag_keys: <p>List of tag keys.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.untag_resource

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
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
