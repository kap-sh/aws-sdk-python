"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.accelerator_type

AcceleratorTypes: TypeAlias = list[
    "aws_sdk_auto_scaling.types.accelerator_type.AcceleratorType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceleratorTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.accelerator_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.accelerator_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AcceleratorTypes:
    import aws_sdk_auto_scaling.types.accelerator_type

    out: AcceleratorTypes = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.accelerator_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AcceleratorTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.accelerator_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.accelerator_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AcceleratorTypes:
    import aws_sdk_auto_scaling.types.accelerator_type

    out: AcceleratorTypes = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.accelerator_type.deserialize_query(child))
    return out
