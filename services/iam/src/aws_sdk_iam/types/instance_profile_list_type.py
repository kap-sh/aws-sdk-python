"""Generated from Smithy shape ``com.amazonaws.iam#instanceProfileListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile

instanceProfileListType: TypeAlias = list[
    "aws_sdk_iam.types.instance_profile.InstanceProfile"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: instanceProfileListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.instance_profile

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.instance_profile.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> instanceProfileListType:
    import aws_sdk_iam.types.instance_profile

    out: instanceProfileListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.instance_profile.deserialize_query(child))
    return out


def serialize_query_flat(
    value: instanceProfileListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.instance_profile

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.instance_profile.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> instanceProfileListType:
    import aws_sdk_iam.types.instance_profile

    out: instanceProfileListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.instance_profile.deserialize_query(child))
    return out
