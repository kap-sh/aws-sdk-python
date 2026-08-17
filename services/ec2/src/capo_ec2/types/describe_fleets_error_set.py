"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_fleet_error

DescribeFleetsErrorSet: TypeAlias = list[
    "capo_ec2.types.describe_fleet_error.DescribeFleetError"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.describe_fleet_error

        capo_ec2.types.describe_fleet_error.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetsErrorSet:
    import capo_ec2.types.describe_fleet_error

    out: DescribeFleetsErrorSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.describe_fleet_error.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DescribeFleetsErrorSet:
    import capo_ec2.types.describe_fleet_error

    out: DescribeFleetsErrorSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.describe_fleet_error.deserialize_ec2_query(child))
    return out
