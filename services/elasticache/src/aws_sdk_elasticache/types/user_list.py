"""Generated from Smithy shape ``com.amazonaws.elasticache#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user

UserList: TypeAlias = list["aws_sdk_elasticache.types.user.User"]


# --- awsQuery ser/de ---
def serialize_query(value: UserList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_elasticache.types.user

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.user.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UserList:
    import aws_sdk_elasticache.types.user

    out: UserList = []
    for child in el.findall("member"):
        out.append(aws_sdk_elasticache.types.user.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UserList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.user

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.user.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> UserList:
    import aws_sdk_elasticache.types.user

    out: UserList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.user.deserialize_query(child))
    return out
