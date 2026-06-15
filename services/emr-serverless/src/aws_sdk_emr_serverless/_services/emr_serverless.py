"""Generated from Smithy shape ``com.amazonaws.emrserverless#AwsToledoWebService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_emr_serverless._auth._signers
import aws_sdk_emr_serverless._auth._sigv4
from aws_sdk_emr_serverless._auth._identity import Credentials
from aws_sdk_emr_serverless._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_emr_serverless._auth._zapros_handler import AuthMiddleware
from aws_sdk_emr_serverless._resources.aws_toledo_web_service.application_resource import (
    ApplicationResource,
)
from aws_sdk_emr_serverless._resources.aws_toledo_web_service.job_run_resource import (
    JobRunResource,
)
from aws_sdk_emr_serverless._resources.aws_toledo_web_service.session_resource import (
    SessionResource,
)
from aws_sdk_emr_serverless._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.list_tags_for_resource_request
    import aws_sdk_emr_serverless.types.list_tags_for_resource_response
    import aws_sdk_emr_serverless.types.resource_arn
    import aws_sdk_emr_serverless.types.tag_key_list
    import aws_sdk_emr_serverless.types.tag_map
    import aws_sdk_emr_serverless.types.tag_resource_request
    import aws_sdk_emr_serverless.types.tag_resource_response
    import aws_sdk_emr_serverless.types.untag_resource_request
    import aws_sdk_emr_serverless.types.untag_resource_response


class EMRServerlessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class EMRServerlessClient:
    """A client for the ``EMRServerless`` service.

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
        self._config = EMRServerlessClientConfig(
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
        self.application_resource = ApplicationResource(self)
        self.job_run_resource = JobRunResource(self)
        self.session_resource = SessionResource(self)

    def operation_options(
        self, config_overrides: Optional[EMRServerlessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EMRServerlessClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_emr_serverless.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "aws_sdk_emr_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to the resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_emr_serverless._operations.aws_toledo_web_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_emr_serverless._operations.aws_toledo_web_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_emr_serverless.types.resource_arn.ResourceArn",
        tags: "aws_sdk_emr_serverless.types.tag_map.TagMap",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "aws_sdk_emr_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns tags to resources. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize your Amazon Web Services resources by attributes such as purpose, owner, or environment. When you have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned to it. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_emr_serverless._operations.aws_toledo_web_service.tag_resource

            output, http_response = (
                aws_sdk_emr_serverless._operations.aws_toledo_web_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_serverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_emr_serverless.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_emr_serverless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "aws_sdk_emr_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_emr_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_emr_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_emr_serverless._operations.aws_toledo_web_service.untag_resource

            output, http_response = (
                aws_sdk_emr_serverless._operations.aws_toledo_web_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_emr_serverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
