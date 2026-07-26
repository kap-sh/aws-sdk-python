"""Generated from Smithy shape ``com.amazonaws.internetmonitor#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>"""
    tag_keys: "capo_internetmonitor.types.tag_keys.TagKeys"
    """<p>Tag keys that you remove from a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
