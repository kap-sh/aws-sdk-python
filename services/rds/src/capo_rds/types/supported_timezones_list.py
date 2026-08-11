"""Generated from Smithy shape ``com.amazonaws.rds#SupportedTimezonesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.timezone

SupportedTimezonesList: TypeAlias = list["capo_rds.types.timezone.Timezone"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedTimezonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.timezone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.timezone.serialize_query(item, pairs, f"{prefix}.Timezone.{n}")


def deserialize_query(el: Element) -> SupportedTimezonesList:
    import capo_rds.types.timezone

    out: SupportedTimezonesList = []
    for child in el.findall("Timezone"):
        out.append(capo_rds.types.timezone.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedTimezonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.timezone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.timezone.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SupportedTimezonesList:
    import capo_rds.types.timezone

    out: SupportedTimezonesList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.timezone.deserialize_query(child))
    return out
