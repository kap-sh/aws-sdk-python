"""Generated from Smithy shape ``com.amazonaws.iam#entityDetailsListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.entity_details

entityDetailsListType: TypeAlias = list[
    "aws_sdk_iam.types.entity_details.EntityDetails"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: entityDetailsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.entity_details

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.entity_details.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> entityDetailsListType:
    import aws_sdk_iam.types.entity_details

    out: entityDetailsListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.entity_details.deserialize_query(child))
    return out


def serialize_query_flat(
    value: entityDetailsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.entity_details

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.entity_details.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> entityDetailsListType:
    import aws_sdk_iam.types.entity_details

    out: entityDetailsListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.entity_details.deserialize_query(child))
    return out
