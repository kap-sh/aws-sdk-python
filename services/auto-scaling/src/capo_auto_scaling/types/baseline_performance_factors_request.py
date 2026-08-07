"""Generated from Smithy shape ``com.amazonaws.autoscaling#BaselinePerformanceFactorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.cpu_performance_factor_request


class BaselinePerformanceFactorsRequest(TypedDict, closed=True):
    cpu: NotRequired[
        "capo_auto_scaling.types.cpu_performance_factor_request.CpuPerformanceFactorRequest"
    ]
    """<p> The CPU performance to consider, using an instance family as the baseline reference. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BaselinePerformanceFactorsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cpu" in value:
        import capo_auto_scaling.types.cpu_performance_factor_request

        capo_auto_scaling.types.cpu_performance_factor_request.serialize_query(
            value["cpu"], pairs, f"{key_prefix}Cpu"
        )


def deserialize_query(el: Element) -> BaselinePerformanceFactorsRequest:
    out: BaselinePerformanceFactorsRequest = {}  # type: ignore[typeddict-item]
    child_cpu = el.find("Cpu")
    if child_cpu is not None:
        import capo_auto_scaling.types.cpu_performance_factor_request

        out["cpu"] = (
            capo_auto_scaling.types.cpu_performance_factor_request.deserialize_query(
                child_cpu
            )
        )
    return out
