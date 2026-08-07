"""Generated from Smithy shape ``com.amazonaws.elasticache#ScaleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integer_optional


class ScaleConfig(TypedDict, closed=True):
    scale_percentage: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The percentage by which to scale the Memcached cluster, either horizontally by adding nodes or vertically by increasing resources.</p>"""
    scale_interval_minutes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The time interval in seconds between scaling operations when performing gradual scaling for a Memcached cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScaleConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scale_percentage" in value:
        pairs.append((f"{key_prefix}ScalePercentage", str(value["scale_percentage"])))
    if "scale_interval_minutes" in value:
        pairs.append(
            (f"{key_prefix}ScaleIntervalMinutes", str(value["scale_interval_minutes"]))
        )


def deserialize_query(el: Element) -> ScaleConfig:
    out: ScaleConfig = {}  # type: ignore[typeddict-item]
    child_scale_percentage = el.find("ScalePercentage")
    if child_scale_percentage is not None:
        out["scale_percentage"] = int(child_scale_percentage.text or "")
    child_scale_interval_minutes = el.find("ScaleIntervalMinutes")
    if child_scale_interval_minutes is not None:
        out["scale_interval_minutes"] = int(child_scale_interval_minutes.text or "")
    return out
