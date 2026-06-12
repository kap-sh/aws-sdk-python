"""Generated from Smithy shape ``com.amazonaws.wickr#CallingSettings``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CallingSettings(TypedDict):
    can_start11_call: NotRequired["bool"]
    """<p>Specifies whether users can start one-to-one calls.</p>"""
    can_video_call: NotRequired["bool"]
    """<p>Specifies whether users can make video calls (as opposed to audio-only calls). Valid only when audio call(canStart11Call) is enabled.</p>"""
    force_tcp_call: NotRequired["bool"]
    """<p>When enabled, forces all calls to use TCP protocol instead of UDP for network traversal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallingSettings) -> dict:
    out: dict = {}
    if "can_start11_call" in value:
        out["canStart11Call"] = value["can_start11_call"]
    if "can_video_call" in value:
        out["canVideoCall"] = value["can_video_call"]
    if "force_tcp_call" in value:
        out["forceTcpCall"] = value["force_tcp_call"]
    return out


def deserialize_json(data: dict) -> CallingSettings:
    out: CallingSettings = {}  # type: ignore[typeddict-item]
    if "canStart11Call" in data:
        out["can_start11_call"] = data["canStart11Call"]
    if "canVideoCall" in data:
        out["can_video_call"] = data["canVideoCall"]
    if "forceTcpCall" in data:
        out["force_tcp_call"] = data["forceTcpCall"]
    return out
