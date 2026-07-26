"""Generated from Smithy shape ``com.amazonaws.rds#MetricReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.metric_reference

MetricReferenceList: TypeAlias = list["capo_rds.types.metric_reference.MetricReference"]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricReferenceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.metric_reference

    for n, item in enumerate(value, 1):
        capo_rds.types.metric_reference.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricReferenceList:
    import capo_rds.types.metric_reference

    out: MetricReferenceList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.metric_reference.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricReferenceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.metric_reference

    for n, item in enumerate(value, 1):
        capo_rds.types.metric_reference.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> MetricReferenceList:
    import capo_rds.types.metric_reference

    out: MetricReferenceList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.metric_reference.deserialize_query(child))
    return out
