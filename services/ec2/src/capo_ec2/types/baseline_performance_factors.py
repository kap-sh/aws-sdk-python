"""Generated from Smithy shape ``com.amazonaws.ec2#BaselinePerformanceFactors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cpu_performance_factor


class BaselinePerformanceFactors(TypedDict, closed=True):
    cpu: NotRequired["capo_ec2.types.cpu_performance_factor.CpuPerformanceFactor"]
    """<p>The CPU performance to consider, using an instance family as the baseline reference.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BaselinePerformanceFactors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cpu" in value:
        import capo_ec2.types.cpu_performance_factor

        capo_ec2.types.cpu_performance_factor.serialize_ec2_query(
            value["cpu"], pairs, f"{key_prefix}Cpu"
        )


def deserialize_ec2_query(el: Element) -> BaselinePerformanceFactors:
    out: BaselinePerformanceFactors = {}  # type: ignore[typeddict-item]
    child_cpu = el.find("cpu")
    if child_cpu is not None:
        import capo_ec2.types.cpu_performance_factor

        out["cpu"] = capo_ec2.types.cpu_performance_factor.deserialize_ec2_query(
            child_cpu
        )
    return out
