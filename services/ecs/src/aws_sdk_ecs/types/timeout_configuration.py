"""Generated from Smithy shape ``com.amazonaws.ecs#TimeoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.duration


class TimeoutConfiguration(TypedDict):
    idle_timeout_seconds: NotRequired["aws_sdk_ecs.types.duration.Duration"]
    """<p>The amount of time in seconds a connection will stay active while idle. A value of <code>0</code> can be set to disable <code>idleTimeout</code>.</p> <p>The <code>idleTimeout</code> default for <code>HTTP</code>/<code>HTTP2</code>/<code>GRPC</code> is 5 minutes.</p> <p>The <code>idleTimeout</code> default for <code>TCP</code> is 1 hour.</p>"""
    per_request_timeout_seconds: NotRequired["aws_sdk_ecs.types.duration.Duration"]
    """<p>The amount of time waiting for the upstream to respond with a complete response per request. A value of <code>0</code> can be set to disable <code>perRequestTimeout</code>. <code>perRequestTimeout</code> can only be set if Service Connect <code>appProtocol</code> isn't <code>TCP</code>. Only <code>idleTimeout</code> is allowed for <code>TCP</code> <code>appProtocol</code>.</p>"""
