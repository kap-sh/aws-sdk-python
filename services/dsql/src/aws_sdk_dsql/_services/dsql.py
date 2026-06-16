"""Generated from Smithy shape ``com.amazonaws.dsql#DSQL``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_dsql._auth._signers
import aws_sdk_dsql._auth._sigv4
from aws_sdk_dsql._auth._identity import Credentials
from aws_sdk_dsql._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_dsql._auth._zapros_handler import AuthMiddleware
from aws_sdk_dsql._resources.dsql.cluster import Cluster
from aws_sdk_dsql._resources.dsql.stream import Stream
from aws_sdk_dsql._services._aws_config import aws_config
from aws_sdk_dsql._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_dsql.types.arn
    import aws_sdk_dsql.types.list_tags_for_resource_input
    import aws_sdk_dsql.types.list_tags_for_resource_output
    import aws_sdk_dsql.types.tag_key_list
    import aws_sdk_dsql.types.tag_map
    import aws_sdk_dsql.types.tag_resource_input
    import aws_sdk_dsql.types.untag_resource_input


class DSQLClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class DSQLClient:
    """A client for the ``DSQL`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = DSQLClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.cluster = Cluster(self)
        self.stream = Stream(self)

    def operation_options(
        self, config_overrides: Optional[DSQLClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DSQLClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to list the tags.</p>

        Examples:
            List Tags For Resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.list_tags_for_resource

            output, http_response = (
                aws_sdk_dsql._operations.dsql.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        tags: "aws_sdk_dsql.types.tag_map.TagMap",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> None:
        """<p>Tags a resource with a map of key and value pairs.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to tag.</p>
            tags: <p>A map of key and value pairs to use to tag your resource.</p>

        Examples:
            Tag Resource

            >>> client.tag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tags={'MyKey': 'MyValue'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_dsql._operations.dsql.tag_resource

            output, http_response = (
                aws_sdk_dsql._operations.dsql.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        tag_keys: "aws_sdk_dsql.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove tags.</p>
            tag_keys: <p>The array of keys of the tags that you want to remove.</p>

        Examples:
            Untag Resource

            >>> client.untag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tag_keys=['MyKeyA', 'MyKeyB'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dsql.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_dsql._operations.dsql.untag_resource

            output, http_response = (
                aws_sdk_dsql._operations.dsql.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
