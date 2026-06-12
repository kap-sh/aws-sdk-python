"""Generated from Smithy shape ``com.amazonaws.rum#RUM``."""

from aws_sdk_rum._auth._signers import SigV4Signer
from aws_sdk_rum._auth._sigv4 import presign_sigv4
from collections.abc import Iterator
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, BaseHandler, Client
from aws_sdk_rum._auth._zapros_handler import AuthMiddleware
from aws_sdk_rum._services._pipeline import Interceptor, OperationOptions, OperationRequest, OperationResponse, execute_pipeline, retry
import time
from aws_sdk_rum.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
import aws_sdk_rum._auth._signers
import aws_sdk_rum._auth._sigv4
from aws_sdk_rum._auth._identity import Credentials
from aws_sdk_rum._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
if TYPE_CHECKING:
    import aws_sdk_rum.types.alias
    import aws_sdk_rum.types.app_monitor_details
    import aws_sdk_rum.types.app_monitor_id
    import aws_sdk_rum.types.arn
    import aws_sdk_rum.types.list_tags_for_resource_request
    import aws_sdk_rum.types.list_tags_for_resource_response
    import aws_sdk_rum.types.put_rum_events_request
    import aws_sdk_rum.types.put_rum_events_response
    import aws_sdk_rum.types.rum_event_list
    import aws_sdk_rum.types.tag_key_list
    import aws_sdk_rum.types.tag_map
    import aws_sdk_rum.types.tag_resource_request
    import aws_sdk_rum.types.tag_resource_response
    import aws_sdk_rum.types.untag_resource_request
    import aws_sdk_rum.types.untag_resource_response
    import aws_sdk_rum.types.user_details

class RUMClientConfig(TypedDict, total=False):
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

class RUMClient:
    """A client for the ``RUM`` service.

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
    def __init__(self, http_handler: BaseHandler | None = None, operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, region: str | None = None, use_dual_stack: bool | None = None, use_fips: bool | None = None, endpoint: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = Client(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = RUMClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "region": region, "use_dual_stack": use_dual_stack, "use_fips": use_fips, "endpoint": endpoint, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[RUMClientConfig] = None) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RUMClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), retry()]
        options_: OperationOptions = OperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), region=overrides.get("region", self.config.get("region")), use_dual_stack=overrides.get("use_dual_stack", self.config.get("use_dual_stack")), use_fips=overrides.get("use_fips", self.config.get("use_fips")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    def list_tags_for_resource(self, resource_arn: "aws_sdk_rum.types.arn.Arn", *, config_overrides: Optional[RUMClientConfig] = None) -> "aws_sdk_rum.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a CloudWatch RUM resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to see the tags of.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_rum.types.list_tags_for_resource_request.ListTagsForResourceRequest]') -> OperationResponse["aws_sdk_rum.types.list_tags_for_resource_response.ListTagsForResourceResponse"]:
            import aws_sdk_rum._operations.rum.list_tags_for_resource
            output, http_response = aws_sdk_rum._operations.rum.list_tags_for_resource.list_tags_for_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rum.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def put_rum_events(self, id: "aws_sdk_rum.types.app_monitor_id.AppMonitorId", batch_id: str, app_monitor_details: "aws_sdk_rum.types.app_monitor_details.AppMonitorDetails", user_details: "aws_sdk_rum.types.user_details.UserDetails", rum_events: "aws_sdk_rum.types.rum_event_list.RumEventList", *, config_overrides: Optional[RUMClientConfig] = None, alias: Optional["aws_sdk_rum.types.alias.Alias"] = None) -> "aws_sdk_rum.types.put_rum_events_response.PutRumEventsResponse":
        """<p>Sends telemetry events about your application performance and user behavior to CloudWatch RUM. The code snippet that RUM generates for you to add to your application includes <code>PutRumEvents</code> operations to send this data to RUM.</p> <p>Each <code>PutRumEvents</code> operation can send a batch of events from one user session.</p>

        Args:
            id: <p>The ID of the app monitor that is sending this data.</p>
            batch_id: <p>A unique identifier for this batch of RUM event data.</p>
            app_monitor_details: <p>A structure that contains information about the app monitor that collected this telemetry information.</p>
            user_details: <p>A structure that contains information about the user session that this batch of events was collected from.</p>
            rum_events: <p>An array of structures that contain the telemetry event data.</p>
            alias: <p>If the app monitor uses a resource-based policy that requires <code>PutRumEvents</code> requests to specify a certain alias, specify that alias here. This alias will be compared to the <code>rum:alias</code> context key in the resource-based policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html\">Using resource-based policies with CloudWatch RUM</a>.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_rum.types.put_rum_events_request.PutRumEventsRequest]') -> OperationResponse["aws_sdk_rum.types.put_rum_events_response.PutRumEventsResponse"]:
            import aws_sdk_rum._operations.rum.put_rum_events
            output, http_response = aws_sdk_rum._operations.rum.put_rum_events.put_rum_events(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rum.types.put_rum_events_request.PutRumEventsRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["batch_id"] = batch_id
        input["app_monitor_details"] = app_monitor_details
        input["user_details"] = user_details
        input["rum_events"] = rum_events
        if alias is not None:
            input["alias"] = alias

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def tag_resource(self, resource_arn: "aws_sdk_rum.types.arn.Arn", tags: "aws_sdk_rum.types.tag_map.TagMap", *, config_overrides: Optional[RUMClientConfig] = None) -> "aws_sdk_rum.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM resource. Currently, the only resources that can be tagged app monitors.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a>.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch RUM resource that you're adding tags to.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_rum.types.tag_resource_request.TagResourceRequest]') -> OperationResponse["aws_sdk_rum.types.tag_resource_response.TagResourceResponse"]:
            import aws_sdk_rum._operations.rum.tag_resource
            output, http_response = aws_sdk_rum._operations.rum.tag_resource.tag_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rum.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def untag_resource(self, resource_arn: "aws_sdk_rum.types.arn.Arn", tag_keys: "aws_sdk_rum.types.tag_key_list.TagKeyList", *, config_overrides: Optional[RUMClientConfig] = None) -> "aws_sdk_rum.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch RUM resource that you're removing tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_rum.types.untag_resource_request.UntagResourceRequest]') -> OperationResponse["aws_sdk_rum.types.untag_resource_response.UntagResourceResponse"]:
            import aws_sdk_rum._operations.rum.untag_resource
            output, http_response = aws_sdk_rum._operations.rum.untag_resource.untag_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rum.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def __enter__(self) -> Self:
        return self
    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()