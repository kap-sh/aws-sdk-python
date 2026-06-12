"""Generated from Smithy shape ``com.amazonaws.cloudformation#WarningDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.warning_detail

WarningDetails: TypeAlias = list[
    "aws_sdk_cloudformation.types.warning_detail.WarningDetail"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: WarningDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.warning_detail

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.warning_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> WarningDetails:
    import aws_sdk_cloudformation.types.warning_detail

    out: WarningDetails = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.warning_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: WarningDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.warning_detail

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.warning_detail.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> WarningDetails:
    import aws_sdk_cloudformation.types.warning_detail

    out: WarningDetails = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.warning_detail.deserialize_query(child))
    return out
