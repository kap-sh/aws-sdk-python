"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#CloudTrailDataService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cloudtrail_data._auth._signers
import aws_sdk_cloudtrail_data._auth._sigv4
from aws_sdk_cloudtrail_data._auth._identity import Credentials
from aws_sdk_cloudtrail_data._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudtrail_data._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudtrail_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.audit_events
    import aws_sdk_cloudtrail_data.types.channel_arn
    import aws_sdk_cloudtrail_data.types.external_id
    import aws_sdk_cloudtrail_data.types.put_audit_events_request
    import aws_sdk_cloudtrail_data.types.put_audit_events_response


class CloudTrailDataClientConfig(TypedDict, total=False):
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


class CloudTrailDataClient:
    """A client for the ``CloudTrailData`` service.

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
        self.config = CloudTrailDataClientConfig(
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
        self, config_overrides: Optional[CloudTrailDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudTrailDataClientConfig = config_overrides or {}
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

    def put_audit_events(
        self,
        audit_events: "aws_sdk_cloudtrail_data.types.audit_events.AuditEvents",
        channel_arn: "aws_sdk_cloudtrail_data.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[CloudTrailDataClientConfig] = None,
        external_id: Optional[
            "aws_sdk_cloudtrail_data.types.external_id.ExternalId"
        ] = None,
    ) -> (
        "aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse"
    ):
        """<p>Ingests your application events into CloudTrail Lake. A required parameter, <code>auditEvents</code>, accepts the JSON records (also called <i>payload</i>) of events that you want CloudTrail to ingest. You can add up to 100 of these events (or up to 1 MB) per <code>PutAuditEvents</code> request.</p>

        Args:
            audit_events: <p>The JSON payload of events that you want to ingest. You can also point to the JSON event payload in a file.</p>
            channel_arn: <p>The ARN or ID (the ARN suffix) of a channel.</p>
            external_id: <p>A unique identifier that is conditionally required when the channel's resource policy includes an external ID. This value can be any string, such as a passphrase or account number.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail_data.types.put_audit_events_request.PutAuditEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse"
        ]:
            import aws_sdk_cloudtrail_data._operations.cloud_trail_data_service.put_audit_events

            output, http_response = (
                aws_sdk_cloudtrail_data._operations.cloud_trail_data_service.put_audit_events.put_audit_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail_data.types.put_audit_events_request.PutAuditEventsRequest = {}  # type: ignore[typeddict-item]
        input_["audit_events"] = audit_events
        input_["channel_arn"] = channel_arn
        if external_id is not None:
            input_["external_id"] = external_id

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
