"""Generated from Smithy shape ``com.amazonaws.autoscaling#CpuManufacturers``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.cpu_manufacturer

CpuManufacturers: TypeAlias = list[
    "aws_sdk_auto_scaling.types.cpu_manufacturer.CpuManufacturer"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CpuManufacturers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.cpu_manufacturer

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.cpu_manufacturer.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CpuManufacturers:
    import aws_sdk_auto_scaling.types.cpu_manufacturer

    out: CpuManufacturers = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.cpu_manufacturer.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CpuManufacturers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.cpu_manufacturer

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.cpu_manufacturer.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CpuManufacturers:
    import aws_sdk_auto_scaling.types.cpu_manufacturer

    out: CpuManufacturers = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.cpu_manufacturer.deserialize_query(child))
    return out
