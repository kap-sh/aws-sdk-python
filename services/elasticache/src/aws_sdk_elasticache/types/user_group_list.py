"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user_group

UserGroupList: TypeAlias = list["aws_sdk_elasticache.types.user_group.UserGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.user_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.user_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UserGroupList:
    import aws_sdk_elasticache.types.user_group

    out: UserGroupList = []
    for child in el.findall("member"):
        out.append(aws_sdk_elasticache.types.user_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UserGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.user_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.user_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UserGroupList:
    import aws_sdk_elasticache.types.user_group

    out: UserGroupList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.user_group.deserialize_query(child))
    return out
