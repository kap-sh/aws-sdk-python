"""Generated from Smithy shape ``com.amazonaws.autoscaling#CpuPerformanceFactorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.performance_factor_reference_set_request


class CpuPerformanceFactorRequest(TypedDict, closed=True):
    references: NotRequired[
        "capo_auto_scaling.types.performance_factor_reference_set_request.PerformanceFactorReferenceSetRequest"
    ]
    """<p> Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences. </p> <note> <p>Currently only one instance family can be specified in the list.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CpuPerformanceFactorRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "references" in value:
        import capo_auto_scaling.types.performance_factor_reference_set_request

        capo_auto_scaling.types.performance_factor_reference_set_request.serialize_query(
            value["references"], pairs, f"{key_prefix}Reference"
        )


def deserialize_query(el: Element) -> CpuPerformanceFactorRequest:
    out: CpuPerformanceFactorRequest = {}  # type: ignore[typeddict-item]
    child_references = el.find("Reference")
    if child_references is not None:
        import capo_auto_scaling.types.performance_factor_reference_set_request

        out["references"] = (
            capo_auto_scaling.types.performance_factor_reference_set_request.deserialize_query(
                child_references
            )
        )
    return out
