"""Generated from Smithy shape ``com.amazonaws.pcs#AWSParallelComputingService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_pcs._auth._signers
import aws_sdk_pcs._auth._sigv4
from aws_sdk_pcs._auth._identity import Credentials
from aws_sdk_pcs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_pcs._auth._zapros_handler import AuthMiddleware
from aws_sdk_pcs._resources.aws_parallel_computing_service.cluster_resource import (
    ClusterResource,
)
from aws_sdk_pcs._services._aws_config import aws_config
from aws_sdk_pcs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_pcs.types.arn
    import aws_sdk_pcs.types.list_tags_for_resource_request
    import aws_sdk_pcs.types.list_tags_for_resource_response
    import aws_sdk_pcs.types.request_tag_map
    import aws_sdk_pcs.types.tag_keys
    import aws_sdk_pcs.types.tag_resource_request
    import aws_sdk_pcs.types.tag_resource_response
    import aws_sdk_pcs.types.untag_resource_request
    import aws_sdk_pcs.types.untag_resource_response


class PCSClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PCSClient:
    """A client for the ``PCS`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = PCSClientConfig(
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
        self.cluster_resource = ClusterResource(self)

    def operation_options(
        self, config_overrides: Optional[PCSClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PCSClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_pcs.types.arn.Arn",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> (
        "aws_sdk_pcs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Returns a list of all tags on an PCS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_pcs.types.arn.Arn",
        tags: "aws_sdk_pcs.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or edits tags on an PCS resource. Each tag consists of a tag key and a tag value. The tag key and tag value are case-sensitive strings. The tag value can be an empty (null) string. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.tag_resource

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_pcs.types.arn.Arn",
        tag_keys: "aws_sdk_pcs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags from an PCS resource. To delete a tag, specify the tag key and the Amazon Resource Name (ARN) of the PCS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>1 or more tag keys to remove from the resource. Specify only tag keys and not tag values.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.untag_resource

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
