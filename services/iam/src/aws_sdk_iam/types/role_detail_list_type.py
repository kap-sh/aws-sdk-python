"""Generated from Smithy shape ``com.amazonaws.iam#roleDetailListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.role_detail

roleDetailListType: TypeAlias = list["aws_sdk_iam.types.role_detail.RoleDetail"]


# --- awsQuery ser/de ---
def serialize_query(
    value: roleDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.role_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> roleDetailListType:
    import aws_sdk_iam.types.role_detail

    out: roleDetailListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.role_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: roleDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.role_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.role_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> roleDetailListType:
    import aws_sdk_iam.types.role_detail

    out: roleDetailListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.role_detail.deserialize_query(child))
    return out
