"""Generated from Smithy shape ``com.amazonaws.sns#NumberCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.number_capability

NumberCapabilityList: TypeAlias = list[
    "aws_sdk_sns.types.number_capability.NumberCapability"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NumberCapabilityList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.number_capability

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.number_capability.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> NumberCapabilityList:
    import aws_sdk_sns.types.number_capability

    out: NumberCapabilityList = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.number_capability.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NumberCapabilityList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.number_capability

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.number_capability.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NumberCapabilityList:
    import aws_sdk_sns.types.number_capability

    out: NumberCapabilityList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.number_capability.deserialize_query(child))
    return out
