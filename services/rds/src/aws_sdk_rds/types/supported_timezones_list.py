"""Generated from Smithy shape ``com.amazonaws.rds#SupportedTimezonesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.timezone

SupportedTimezonesList: TypeAlias = list["aws_sdk_rds.types.timezone.Timezone"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedTimezonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.timezone

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.timezone.serialize_query(
            item, pairs, f"{prefix}.Timezone.{n}"
        )


def deserialize_query(el: Element) -> SupportedTimezonesList:
    import aws_sdk_rds.types.timezone

    out: SupportedTimezonesList = []
    for child in el.findall("Timezone"):
        out.append(aws_sdk_rds.types.timezone.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedTimezonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.timezone

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.timezone.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SupportedTimezonesList:
    import aws_sdk_rds.types.timezone

    out: SupportedTimezonesList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.timezone.deserialize_query(child))
    return out
