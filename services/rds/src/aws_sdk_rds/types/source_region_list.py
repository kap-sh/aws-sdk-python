"""Generated from Smithy shape ``com.amazonaws.rds#SourceRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.source_region

SourceRegionList: TypeAlias = list["aws_sdk_rds.types.source_region.SourceRegion"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceRegionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.source_region

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.source_region.serialize_query(
            item, pairs, f"{prefix}.SourceRegion.{n}"
        )


def deserialize_query(el: Element) -> SourceRegionList:
    import aws_sdk_rds.types.source_region

    out: SourceRegionList = []
    for child in el.findall("SourceRegion"):
        out.append(aws_sdk_rds.types.source_region.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SourceRegionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.source_region

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.source_region.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SourceRegionList:
    import aws_sdk_rds.types.source_region

    out: SourceRegionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.source_region.deserialize_query(child))
    return out
