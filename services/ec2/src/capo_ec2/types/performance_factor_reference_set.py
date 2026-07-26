"""Generated from Smithy shape ``com.amazonaws.ec2#PerformanceFactorReferenceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.performance_factor_reference

PerformanceFactorReferenceSet: TypeAlias = list[
    "capo_ec2.types.performance_factor_reference.PerformanceFactorReference"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PerformanceFactorReferenceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.performance_factor_reference

        capo_ec2.types.performance_factor_reference.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PerformanceFactorReferenceSet:
    import capo_ec2.types.performance_factor_reference

    out: PerformanceFactorReferenceSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.performance_factor_reference.deserialize_ec2_query(child)
        )
    return out
