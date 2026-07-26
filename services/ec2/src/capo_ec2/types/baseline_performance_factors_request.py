"""Generated from Smithy shape ``com.amazonaws.ec2#BaselinePerformanceFactorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cpu_performance_factor_request


class BaselinePerformanceFactorsRequest(TypedDict, closed=True):
    cpu: NotRequired[
        "capo_ec2.types.cpu_performance_factor_request.CpuPerformanceFactorRequest"
    ]
    """<p>The CPU performance to consider, using an instance family as the baseline reference.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BaselinePerformanceFactorsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cpu" in value:
        import capo_ec2.types.cpu_performance_factor_request

        capo_ec2.types.cpu_performance_factor_request.serialize_ec2_query(
            value["cpu"], pairs, f"{prefix}.Cpu"
        )


def deserialize_ec2_query(el: Element) -> BaselinePerformanceFactorsRequest:
    out: BaselinePerformanceFactorsRequest = {}  # type: ignore[typeddict-item]
    child_cpu = el.find("Cpu")
    if child_cpu is not None:
        import capo_ec2.types.cpu_performance_factor_request

        out["cpu"] = (
            capo_ec2.types.cpu_performance_factor_request.deserialize_ec2_query(
                child_cpu
            )
        )
    return out
