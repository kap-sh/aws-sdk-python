"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled
    import capo_sesv2.types.last_fresh_start


class ReputationOptions(TypedDict, closed=True):
    reputation_metrics_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>If <code>true</code>, tracking of reputation metrics is enabled for the configuration set. If <code>false</code>, tracking of reputation metrics is disabled for the configuration set.</p>"""
    last_fresh_start: NotRequired["capo_sesv2.types.last_fresh_start.LastFreshStart"]
    """<p>The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReputationOptions) -> dict:
    out: dict = {}
    out["ReputationMetricsEnabled"] = value.get("reputation_metrics_enabled", False)
    if "last_fresh_start" in value:
        import capo_sesv2.types.last_fresh_start

        out["LastFreshStart"] = capo_sesv2.types.last_fresh_start.serialize_json(
            value["last_fresh_start"]
        )
    return out


def deserialize_json(data: dict) -> ReputationOptions:
    out: ReputationOptions = {}  # type: ignore[typeddict-item]
    if "ReputationMetricsEnabled" in data:
        out["reputation_metrics_enabled"] = data["ReputationMetricsEnabled"]
    else:
        out["reputation_metrics_enabled"] = False
    if "LastFreshStart" in data:
        import capo_sesv2.types.last_fresh_start

        out["last_fresh_start"] = capo_sesv2.types.last_fresh_start.deserialize_json(
            data["LastFreshStart"]
        )
    return out
