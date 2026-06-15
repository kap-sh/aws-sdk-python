"""Generated from Smithy shape ``com.amazonaws.m2#AwsSupernovaControlPlaneService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_m2._auth._signers
import aws_sdk_m2._auth._sigv4
from aws_sdk_m2._auth._identity import Credentials
from aws_sdk_m2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_m2._auth._zapros_handler import AuthMiddleware
from aws_sdk_m2._pagination import resolve_path as _resolve_path
from aws_sdk_m2._resources.aws_supernova_control_plane_service.application import (
    Application,
)
from aws_sdk_m2._resources.aws_supernova_control_plane_service.environment import (
    Environment,
)
from aws_sdk_m2._services._aws_config import aws_config
from aws_sdk_m2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_m2.types.arn
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.engine_versions_summary
    import aws_sdk_m2.types.get_signed_bluinsights_url_response
    import aws_sdk_m2.types.list_engine_versions_request
    import aws_sdk_m2.types.list_engine_versions_response
    import aws_sdk_m2.types.list_tags_for_resource_request
    import aws_sdk_m2.types.list_tags_for_resource_response
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token
    import aws_sdk_m2.types.tag_key_list
    import aws_sdk_m2.types.tag_map
    import aws_sdk_m2.types.tag_resource_request
    import aws_sdk_m2.types.tag_resource_response
    import aws_sdk_m2.types.untag_resource_request
    import aws_sdk_m2.types.untag_resource_response


class m2ClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class m2Client:
    """A client for the ``m2`` service.

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
        self._config = m2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.application = Application(self)
        self.environment = Environment(self)

    def operation_options(
        self, config_overrides: Optional[m2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: m2ClientConfig = config_overrides or {}
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

    def get_signed_bluinsights_url(
        self, *, config_overrides: Optional[m2ClientConfig] = None
    ) -> "aws_sdk_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse":
        """<p>Gets a single sign-on URL that can be used to connect to AWS Blu Insights.</p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url.get_signed_bluinsights_url(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_engine_versions(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_m2.types.list_engine_versions_response.ListEngineVersionsResponse":
        """<p>Lists the available engine versions.</p>

        Args:
            engine_type: <p>The type of target platform.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.list_engine_versions_request.ListEngineVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.list_engine_versions_response.ListEngineVersionsResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_engine_versions

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.list_engine_versions.list_engine_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_m2.types.list_engine_versions_request.ListEngineVersionsRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input_["engine_type"] = engine_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_engine_versions(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_m2.types.engine_versions_summary.EngineVersionsSummary]":
        _token = next_token
        while True:
            _response = self.list_engine_versions(
                config_overrides=config_overrides,
                engine_type=engine_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        tags: "aws_sdk_m2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.tag_resource

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_m2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        tag_keys: "aws_sdk_m2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The keys of the tags to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.untag_resource

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_m2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
