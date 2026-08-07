"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupStickinessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_group_stickiness_duration_seconds
    import capo_elastic_load_balancing_v2.types.target_group_stickiness_enabled


class TargetGroupStickinessConfig(TypedDict, closed=True):
    enabled: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_group_stickiness_enabled.TargetGroupStickinessEnabled"
    ]
    """<p>Indicates whether target group stickiness is enabled.</p>"""
    duration_seconds: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_group_stickiness_duration_seconds.TargetGroupStickinessDurationSeconds"
    ]
    """<p>[Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days). You must specify this value when enabling target group stickiness.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroupStickinessConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))


def deserialize_query(el: Element) -> TargetGroupStickinessConfig:
    out: TargetGroupStickinessConfig = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    return out
