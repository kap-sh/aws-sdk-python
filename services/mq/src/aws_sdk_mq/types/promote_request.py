"""Generated from Smithy shape ``com.amazonaws.mq#PromoteRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.promote_mode


class PromoteRequest(TypedDict):
    broker_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    mode: NotRequired["aws_sdk_mq.types.promote_mode.PromoteMode"]
    """<p>The Promote mode requested. Note: Valid values for the parameter are SWITCHOVER, FAILOVER.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromoteRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_mq.types.promote_mode

        out["mode"] = aws_sdk_mq.types.promote_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> PromoteRequest:
    out: PromoteRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_mq.types.promote_mode

        out["mode"] = aws_sdk_mq.types.promote_mode.deserialize_json(data["mode"])
    return out
