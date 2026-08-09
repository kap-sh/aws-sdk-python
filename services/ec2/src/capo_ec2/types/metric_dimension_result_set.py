"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDimensionResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_dimension

MetricDimensionResultSet: TypeAlias = list[
    "capo_ec2.types.capacity_manager_dimension.CapacityManagerDimension"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricDimensionResultSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_manager_dimension

        capo_ec2.types.capacity_manager_dimension.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> MetricDimensionResultSet:
    import capo_ec2.types.capacity_manager_dimension

    out: MetricDimensionResultSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_manager_dimension.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> MetricDimensionResultSet:
    import capo_ec2.types.capacity_manager_dimension

    out: MetricDimensionResultSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_manager_dimension.deserialize_ec2_query(child)
        )
    return out
