"""Generated from Smithy shape ``com.amazonaws.iam#ResourceSpecificResultListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.resource_specific_result

ResourceSpecificResultListType: TypeAlias = list[
    "aws_sdk_iam.types.resource_specific_result.ResourceSpecificResult"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceSpecificResultListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.resource_specific_result

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.resource_specific_result.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceSpecificResultListType:
    import aws_sdk_iam.types.resource_specific_result

    out: ResourceSpecificResultListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.resource_specific_result.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ResourceSpecificResultListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.resource_specific_result

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.resource_specific_result.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceSpecificResultListType:
    import aws_sdk_iam.types.resource_specific_result

    out: ResourceSpecificResultListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.resource_specific_result.deserialize_query(child))
    return out
