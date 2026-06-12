"""Generated from Smithy shape ``com.amazonaws.rds#UserAuthConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.user_auth_config

UserAuthConfigList: TypeAlias = list[
    "aws_sdk_rds.types.user_auth_config.UserAuthConfig"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserAuthConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.user_auth_config

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.user_auth_config.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UserAuthConfigList:
    import aws_sdk_rds.types.user_auth_config

    out: UserAuthConfigList = []
    for child in el.findall("member"):
        out.append(aws_sdk_rds.types.user_auth_config.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UserAuthConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.user_auth_config

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.user_auth_config.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> UserAuthConfigList:
    import aws_sdk_rds.types.user_auth_config

    out: UserAuthConfigList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.user_auth_config.deserialize_query(child))
    return out
