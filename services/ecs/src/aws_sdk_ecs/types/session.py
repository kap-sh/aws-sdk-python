"""Generated from Smithy shape ``com.amazonaws.ecs#Session``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.sensitive_string
    import aws_sdk_ecs.types.string


class Session(TypedDict):
    session_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the execute command session.</p>"""
    stream_url: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A URL to the managed agent on the container that the SSM Session Manager client uses to send commands and receive output from the container.</p>"""
    token_value: NotRequired["aws_sdk_ecs.types.sensitive_string.SensitiveString"]
    """<p>An encrypted token value containing session and caller information. It's used to authenticate the connection to the container.</p>"""
