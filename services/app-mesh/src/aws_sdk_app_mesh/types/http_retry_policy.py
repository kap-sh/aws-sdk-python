"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRetryPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.duration
    import aws_sdk_app_mesh.types.http_retry_policy_events
    import aws_sdk_app_mesh.types.max_retries
    import aws_sdk_app_mesh.types.tcp_retry_policy_events


class HttpRetryPolicy(TypedDict, closed=True):
    per_retry_timeout: "aws_sdk_app_mesh.types.duration.Duration"
    """<p>The timeout for each retry attempt.</p>"""
    max_retries: "aws_sdk_app_mesh.types.max_retries.MaxRetries"
    """<p>The maximum number of retry attempts.</p>"""
    http_retry_events: NotRequired[
        "aws_sdk_app_mesh.types.http_retry_policy_events.HttpRetryPolicyEvents"
    ]
    """<p>Specify at least one of the following values.</p> <ul> <li> <p> <b>server-error</b> – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511</p> </li> <li> <p> <b>gateway-error</b> – HTTP status codes 502, 503, and 504</p> </li> <li> <p> <b>client-error</b> – HTTP status code 409</p> </li> <li> <p> <b>stream-error</b> – Retry on refused stream</p> </li> </ul>"""
    tcp_retry_events: NotRequired[
        "aws_sdk_app_mesh.types.tcp_retry_policy_events.TcpRetryPolicyEvents"
    ]
    """<p>Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRetryPolicy) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.duration

    out["perRetryTimeout"] = aws_sdk_app_mesh.types.duration.serialize_json(
        value["per_retry_timeout"]
    )
    out["maxRetries"] = value["max_retries"]
    if "http_retry_events" in value:
        import aws_sdk_app_mesh.types.http_retry_policy_events

        out["httpRetryEvents"] = (
            aws_sdk_app_mesh.types.http_retry_policy_events.serialize_json(
                value["http_retry_events"]
            )
        )
    if "tcp_retry_events" in value:
        import aws_sdk_app_mesh.types.tcp_retry_policy_events

        out["tcpRetryEvents"] = (
            aws_sdk_app_mesh.types.tcp_retry_policy_events.serialize_json(
                value["tcp_retry_events"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpRetryPolicy:
    out: HttpRetryPolicy = {}  # type: ignore[typeddict-item]
    if "perRetryTimeout" in data:
        import aws_sdk_app_mesh.types.duration

        out["per_retry_timeout"] = aws_sdk_app_mesh.types.duration.deserialize_json(
            data["perRetryTimeout"]
        )
    else:
        raise DeserializationError("HttpRetryPolicy.per_retry_timeout required")
    if "maxRetries" in data:
        out["max_retries"] = data["maxRetries"]
    else:
        raise DeserializationError("HttpRetryPolicy.max_retries required")
    if "httpRetryEvents" in data:
        import aws_sdk_app_mesh.types.http_retry_policy_events

        out["http_retry_events"] = (
            aws_sdk_app_mesh.types.http_retry_policy_events.deserialize_json(
                data["httpRetryEvents"]
            )
        )
    if "tcpRetryEvents" in data:
        import aws_sdk_app_mesh.types.tcp_retry_policy_events

        out["tcp_retry_events"] = (
            aws_sdk_app_mesh.types.tcp_retry_policy_events.deserialize_json(
                data["tcpRetryEvents"]
            )
        )
    return out
