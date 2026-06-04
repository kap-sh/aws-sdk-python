"""Generated from Smithy shape ``com.amazonaws.iam#roleListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role

roleListType: TypeAlias = list["aws_sdk_iam.types.role.Role"]


# --- awsQuery ser/de ---
def serialize_query(
    value: roleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.role.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> roleListType:
    import aws_sdk_iam.types.role

    out: roleListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: roleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.role.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> roleListType:
    import aws_sdk_iam.types.role

    out: roleListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.role.deserialize_query(child))
    return out
