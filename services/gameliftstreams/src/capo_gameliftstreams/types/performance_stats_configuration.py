"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#PerformanceStatsConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class PerformanceStatsConfiguration(TypedDict, closed=True):
    shared_with_client: NotRequired["bool"]
    """<p>Performance stats for the session are streamed to the client when set to <code>true</code>. Defaults to <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceStatsConfiguration) -> dict:
    out: dict = {}
    if "shared_with_client" in value:
        out["SharedWithClient"] = value["shared_with_client"]
    return out


def deserialize_json(data: dict) -> PerformanceStatsConfiguration:
    out: PerformanceStatsConfiguration = {}  # type: ignore[typeddict-item]
    if "SharedWithClient" in data:
        out["shared_with_client"] = data["SharedWithClient"]
    return out
