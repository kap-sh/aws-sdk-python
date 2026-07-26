"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefreshes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_refresh

InstanceRefreshes: TypeAlias = list[
    "capo_auto_scaling.types.instance_refresh.InstanceRefresh"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRefreshes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.instance_refresh

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.instance_refresh.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceRefreshes:
    import capo_auto_scaling.types.instance_refresh

    out: InstanceRefreshes = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.instance_refresh.deserialize_query(child))
    return out


def serialize_query_flat(
    value: InstanceRefreshes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.instance_refresh

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.instance_refresh.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceRefreshes:
    import capo_auto_scaling.types.instance_refresh

    out: InstanceRefreshes = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.instance_refresh.deserialize_query(child))
    return out
