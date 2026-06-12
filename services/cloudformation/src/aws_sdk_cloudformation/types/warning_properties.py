"""Generated from Smithy shape ``com.amazonaws.cloudformation#WarningProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.warning_property

WarningProperties: TypeAlias = list[
    "aws_sdk_cloudformation.types.warning_property.WarningProperty"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: WarningProperties, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.warning_property

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.warning_property.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> WarningProperties:
    import aws_sdk_cloudformation.types.warning_property

    out: WarningProperties = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.warning_property.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: WarningProperties, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.warning_property

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.warning_property.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> WarningProperties:
    import aws_sdk_cloudformation.types.warning_property

    out: WarningProperties = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.warning_property.deserialize_query(child)
        )
    return out
