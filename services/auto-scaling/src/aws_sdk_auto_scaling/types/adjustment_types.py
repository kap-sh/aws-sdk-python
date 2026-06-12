"""Generated from Smithy shape ``com.amazonaws.autoscaling#AdjustmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.adjustment_type

AdjustmentTypes: TypeAlias = list[
    "aws_sdk_auto_scaling.types.adjustment_type.AdjustmentType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AdjustmentTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.adjustment_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.adjustment_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AdjustmentTypes:
    import aws_sdk_auto_scaling.types.adjustment_type

    out: AdjustmentTypes = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.adjustment_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AdjustmentTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.adjustment_type

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.adjustment_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AdjustmentTypes:
    import aws_sdk_auto_scaling.types.adjustment_type

    out: AdjustmentTypes = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.adjustment_type.deserialize_query(child))
    return out
