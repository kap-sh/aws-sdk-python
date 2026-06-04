"""Generated from Smithy shape ``com.amazonaws.iam#userDetailListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.user_detail

userDetailListType: TypeAlias = list["aws_sdk_iam.types.user_detail.UserDetail"]


# --- awsQuery ser/de ---
def serialize_query(
    value: userDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.user_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.user_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> userDetailListType:
    import aws_sdk_iam.types.user_detail

    out: userDetailListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.user_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: userDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.user_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.user_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> userDetailListType:
    import aws_sdk_iam.types.user_detail

    out: userDetailListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.user_detail.deserialize_query(child))
    return out
