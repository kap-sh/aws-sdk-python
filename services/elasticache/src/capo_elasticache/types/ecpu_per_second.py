"""Generated from Smithy shape ``com.amazonaws.elasticache#ECPUPerSecond``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integer_optional


class ECPUPerSecond(TypedDict, closed=True):
    maximum: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The configuration for the maximum number of ECPUs the cache can consume per second.</p>"""
    minimum: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The configuration for the minimum number of ECPUs the cache should be able consume per second.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ECPUPerSecond, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum" in value:
        pairs.append((f"{prefix}.Maximum", str(value["maximum"])))
    if "minimum" in value:
        pairs.append((f"{prefix}.Minimum", str(value["minimum"])))


def deserialize_query(el: Element) -> ECPUPerSecond:
    out: ECPUPerSecond = {}  # type: ignore[typeddict-item]
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = int(child_maximum.text or "")
    child_minimum = el.find("Minimum")
    if child_minimum is not None:
        out["minimum"] = int(child_minimum.text or "")
    return out
