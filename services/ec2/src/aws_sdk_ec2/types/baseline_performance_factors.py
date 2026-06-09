"""Generated from Smithy shape ``com.amazonaws.ec2#BaselinePerformanceFactors``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cpu_performance_factor


class BaselinePerformanceFactors(TypedDict):
    cpu: NotRequired["aws_sdk_ec2.types.cpu_performance_factor.CpuPerformanceFactor"]
    """<p>The CPU performance to consider, using an instance family as the baseline reference.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BaselinePerformanceFactors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cpu" in value:
        import aws_sdk_ec2.types.cpu_performance_factor

        aws_sdk_ec2.types.cpu_performance_factor.serialize_ec2_query(
            value["cpu"], pairs, f"{prefix}.Cpu"
        )


def deserialize_ec2_query(el: Element) -> BaselinePerformanceFactors:
    out: BaselinePerformanceFactors = {}  # type: ignore[typeddict-item]
    child_cpu = el.find("Cpu")
    if child_cpu is not None:
        import aws_sdk_ec2.types.cpu_performance_factor

        out["cpu"] = aws_sdk_ec2.types.cpu_performance_factor.deserialize_ec2_query(
            child_cpu
        )
    return out
