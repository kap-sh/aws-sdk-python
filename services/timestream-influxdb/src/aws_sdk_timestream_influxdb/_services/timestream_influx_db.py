"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#AmazonTimestreamInfluxDB``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_timestream_influxdb._auth._signers
import aws_sdk_timestream_influxdb._auth._sigv4
from aws_sdk_timestream_influxdb._auth._identity import Credentials
from aws_sdk_timestream_influxdb._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_timestream_influxdb._auth._zapros_handler import AuthMiddleware
from aws_sdk_timestream_influxdb._resources.amazon_timestream_influx_db.db_cluster_resource import (
    DbClusterResource,
)
from aws_sdk_timestream_influxdb._resources.amazon_timestream_influx_db.db_instance_resource import (
    DbInstanceResource,
)
from aws_sdk_timestream_influxdb._resources.amazon_timestream_influx_db.db_parameter_group_resource import (
    DbParameterGroupResource,
)
from aws_sdk_timestream_influxdb._services._aws_config import aws_config
from aws_sdk_timestream_influxdb._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.arn
    import aws_sdk_timestream_influxdb.types.list_tags_for_resource_request
    import aws_sdk_timestream_influxdb.types.list_tags_for_resource_response
    import aws_sdk_timestream_influxdb.types.request_tag_map
    import aws_sdk_timestream_influxdb.types.tag_keys
    import aws_sdk_timestream_influxdb.types.tag_resource_request
    import aws_sdk_timestream_influxdb.types.untag_resource_request


class TimestreamInfluxDBClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class TimestreamInfluxDBClient:
    """A client for the ``TimestreamInfluxDB`` service.

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
        self._config = TimestreamInfluxDBClientConfig(
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
        self.db_cluster_resource = DbClusterResource(self)
        self.db_instance_resource = DbInstanceResource(self)
        self.db_parameter_group_resource = DbParameterGroupResource(self)

    def operation_options(
        self, config_overrides: Optional[TimestreamInfluxDBClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: TimestreamInfluxDBClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_timestream_influxdb.types.arn.Arn",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> "aws_sdk_timestream_influxdb.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>A list of tags applied to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_timestream_influxdb.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_timestream_influxdb.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_tags_for_resource

            output, http_response = (
                aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_timestream_influxdb.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_timestream_influxdb.types.arn.Arn",
        tags: "aws_sdk_timestream_influxdb.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> None:
        """<p>Tags are composed of a Key/Value pairs. You can use tags to categorize and track your Timestream for InfluxDB resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>
            tags: <p>A list of tags used to categorize and track resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_timestream_influxdb.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.tag_resource

            output, http_response = (
                aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_timestream_influxdb.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_timestream_influxdb.types.arn.Arn",
        tag_keys: "aws_sdk_timestream_influxdb.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> None:
        """<p>Removes the tag from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>
            tag_keys: <p>The keys used to identify the tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_timestream_influxdb.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.untag_resource

            output, http_response = (
                aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_timestream_influxdb.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
