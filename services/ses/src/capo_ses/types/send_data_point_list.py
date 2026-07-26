"""Generated from Smithy shape ``com.amazonaws.ses#SendDataPointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.send_data_point

SendDataPointList: TypeAlias = list["capo_ses.types.send_data_point.SendDataPoint"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SendDataPointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.send_data_point

    for n, item in enumerate(value, 1):
        capo_ses.types.send_data_point.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SendDataPointList:
    import capo_ses.types.send_data_point

    out: SendDataPointList = []
    for child in el.findall("member"):
        out.append(capo_ses.types.send_data_point.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SendDataPointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.send_data_point

    for n, item in enumerate(value, 1):
        capo_ses.types.send_data_point.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SendDataPointList:
    import capo_ses.types.send_data_point

    out: SendDataPointList = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.send_data_point.deserialize_query(child))
    return out
