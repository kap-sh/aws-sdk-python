"""Generated from Smithy shape ``com.amazonaws.evs#AmazonElasticVMwareService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_evs._auth._identity import Credentials
from aws_sdk_evs._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_evs._auth._zapros_handler import AuthMiddleware
from aws_sdk_evs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_evs.types.arn
    import aws_sdk_evs.types.get_versions_request
    import aws_sdk_evs.types.get_versions_response
    import aws_sdk_evs.types.list_tags_for_resource_request
    import aws_sdk_evs.types.list_tags_for_resource_response
    import aws_sdk_evs.types.request_tag_map
    import aws_sdk_evs.types.tag_keys
    import aws_sdk_evs.types.tag_resource_request
    import aws_sdk_evs.types.tag_resource_response
    import aws_sdk_evs.types.untag_resource_request
    import aws_sdk_evs.types.untag_resource_response


class evsClientConfig(TypedDict, total=False):
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


class evsClient:
    """A client for the ``evs`` service.

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
        self.config = evsClientConfig(
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
        self, config_overrides: Optional[evsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: evsClientConfig = config_overrides or {}
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

    def get_versions(
        self, *, config_overrides: Optional[evsClientConfig] = None
    ) -> "aws_sdk_evs.types.get_versions_response.GetVersionsResponse":
        """<p>Returns information about VCF versions, ESX versions and EC2 instance types provided by Amazon EVS. For each VCF version, the response also includes the default ESX version and provided EC2 instance types.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.get_versions_request.GetVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.get_versions_response.GetVersionsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_versions

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_versions.get_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_evs.types.get_versions_request.GetVersionsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        *,
        config_overrides: Optional[evsClientConfig] = None,
    ) -> (
        "aws_sdk_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists the tags for an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list tags for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        tags: "aws_sdk_evs.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[evsClientConfig] = None,
    ) -> "aws_sdk_evs.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to an Amazon EVS resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted. Tags that you create for Amazon EVS resources don't propagate to any other resources associated with the environment. For example, if you tag an environment with this operation, that tag doesn't automatically propagate to the VLAN subnets and hosts associated with the environment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other environment or Amazon Web Services resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.tag_resource

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_evs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        tag_keys: "aws_sdk_evs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[evsClientConfig] = None,
    ) -> "aws_sdk_evs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_evs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_evs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.untag_resource

            output, http_response = (
                aws_sdk_evs._operations.amazon_elastic_v_mware_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_evs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
