"""Generated from Smithy shape ``com.amazonaws.braket#Braket``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_braket._auth._signers
import aws_sdk_braket._auth._sigv4
from aws_sdk_braket._auth._identity import Credentials
from aws_sdk_braket._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_braket._auth._zapros_handler import AuthMiddleware
from aws_sdk_braket._resources.braket.device_resource import DeviceResource
from aws_sdk_braket._resources.braket.job_resource import JobResource
from aws_sdk_braket._resources.braket.quantum_task_resource import QuantumTaskResource
from aws_sdk_braket._resources.braket.spending_limit_resource import (
    SpendingLimitResource,
)
from aws_sdk_braket._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_braket.types.list_tags_for_resource_request
    import aws_sdk_braket.types.list_tags_for_resource_response
    import aws_sdk_braket.types.tag_keys
    import aws_sdk_braket.types.tag_resource_request
    import aws_sdk_braket.types.tag_resource_response
    import aws_sdk_braket.types.tags_map
    import aws_sdk_braket.types.untag_resource_request
    import aws_sdk_braket.types.untag_resource_response


class BraketClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class BraketClient:
    """A client for the ``Braket`` service.

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
        self._config = BraketClientConfig(
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
        self.device_resource = DeviceResource(self)
        self.job_resource = JobResource(self)
        self.quantum_task_resource = QuantumTaskResource(self)
        self.spending_limit_resource = SpendingLimitResource(self)

    def operation_options(
        self, config_overrides: Optional[BraketClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BraketClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Shows the tags associated with this resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource whose tags to display.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_braket._operations.braket.list_tags_for_resource

            output, http_response = (
                aws_sdk_braket._operations.braket.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_braket.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.tag_resource_response.TagResourceResponse":
        """<p>Add a tag to the specified resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> of the resource to which a tag will be added.</p>
            tags: <p>Specify the tags to add to the resource. Tags can be specified as a key-value map.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_braket._operations.braket.tag_resource

            output, http_response = (
                aws_sdk_braket._operations.braket.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_braket.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "aws_sdk_braket.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource from which to remove the tags.</p>
            tag_keys: <p>Specify the keys for the tags to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_braket._operations.braket.untag_resource

            output, http_response = (
                aws_sdk_braket._operations.braket.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_braket.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
