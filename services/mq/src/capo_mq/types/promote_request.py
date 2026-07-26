"""Generated from Smithy shape ``com.amazonaws.mq#PromoteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string
    import capo_mq.types.promote_mode


class PromoteRequest(TypedDict, closed=True):
    broker_id: "capo_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    mode: NotRequired["capo_mq.types.promote_mode.PromoteMode"]
    """<p>The Promote mode requested. Note: Valid values for the parameter are SWITCHOVER, FAILOVER.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromoteRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_mq.types.promote_mode

        out["mode"] = capo_mq.types.promote_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> PromoteRequest:
    out: PromoteRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import capo_mq.types.promote_mode

        out["mode"] = capo_mq.types.promote_mode.deserialize_json(data["mode"])
    return out
