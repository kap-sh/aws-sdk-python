"""Generated from Smithy shape ``com.amazonaws.batch#Ulimit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string


class Ulimit(TypedDict):
    hard_limit: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The hard limit for the <code>ulimit</code> type. </p>"""
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>type</code> of the <code>ulimit</code>. Valid values are: <code>core</code> | <code>cpu</code> | <code>data</code> | <code>fsize</code> | <code>locks</code> | <code>memlock</code> | <code>msgqueue</code> | <code>nice</code> | <code>nofile</code> | <code>nproc</code> | <code>rss</code> | <code>rtprio</code> | <code>rttime</code> | <code>sigpending</code> | <code>stack</code>.</p>"""
    soft_limit: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The soft limit for the <code>ulimit</code> type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ulimit) -> dict:
    out: dict = {}
    if "hard_limit" in value:
        out["hardLimit"] = value["hard_limit"]
    if "name" in value:
        out["name"] = value["name"]
    if "soft_limit" in value:
        out["softLimit"] = value["soft_limit"]
    return out


def deserialize_json(data: dict) -> Ulimit:
    out: Ulimit = {}  # type: ignore[typeddict-item]
    if "hardLimit" in data:
        out["hard_limit"] = data["hardLimit"]
    if "name" in data:
        out["name"] = data["name"]
    if "softLimit" in data:
        out["soft_limit"] = data["softLimit"]
    return out
