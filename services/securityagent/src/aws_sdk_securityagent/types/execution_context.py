"""Generated from Smithy shape ``com.amazonaws.securityagent#ExecutionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.context_type


class ExecutionContext(TypedDict, closed=True):
    context_type: NotRequired["aws_sdk_securityagent.types.context_type.ContextType"]
    """<p>The type of context. Valid values include ERROR, CLIENT_ERROR, WARNING, and INFO.</p>"""
    context: NotRequired["str"]
    """<p>The context message.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time the context was recorded, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionContext) -> dict:
    out: dict = {}
    if "context_type" in value:
        import aws_sdk_securityagent.types.context_type

        out["contextType"] = aws_sdk_securityagent.types.context_type.serialize_json(
            value["context_type"]
        )
    if "context" in value:
        out["context"] = value["context"]
    if "timestamp" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionContext:
    out: ExecutionContext = {}  # type: ignore[typeddict-item]
    if "contextType" in data:
        import aws_sdk_securityagent.types.context_type

        out["context_type"] = aws_sdk_securityagent.types.context_type.deserialize_json(
            data["contextType"]
        )
    if "context" in data:
        out["context"] = data["context"]
    if "timestamp" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    return out
