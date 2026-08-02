"""Generated from Smithy shape ``com.amazonaws.ec2#CpuPerformanceFactor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.performance_factor_reference_set


class CpuPerformanceFactor(TypedDict, closed=True):
    references: NotRequired[
        "capo_ec2.types.performance_factor_reference_set.PerformanceFactorReferenceSet"
    ]
    """<p>Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.</p> <note> <p>Currently, only one instance family can be specified in the list.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CpuPerformanceFactor, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "references" in value:
        import capo_ec2.types.performance_factor_reference_set

        capo_ec2.types.performance_factor_reference_set.serialize_ec2_query(
            value["references"], pairs, f"{key_prefix}ReferenceSet"
        )


def deserialize_ec2_query(el: Element) -> CpuPerformanceFactor:
    out: CpuPerformanceFactor = {}  # type: ignore[typeddict-item]
    if el.find("ReferenceSet") is not None:
        import capo_ec2.types.performance_factor_reference_set

        out["references"] = (
            capo_ec2.types.performance_factor_reference_set.deserialize_ec2_query(
                el, "ReferenceSet"
            )
        )
    return out
