"""Generated from Smithy shape ``com.amazonaws.rds#UserAuthConfigInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.user_auth_config_info

UserAuthConfigInfoList: TypeAlias = list[
    "capo_rds.types.user_auth_config_info.UserAuthConfigInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserAuthConfigInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.user_auth_config_info

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.user_auth_config_info.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UserAuthConfigInfoList:
    import capo_rds.types.user_auth_config_info

    out: UserAuthConfigInfoList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.user_auth_config_info.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UserAuthConfigInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.user_auth_config_info

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.user_auth_config_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UserAuthConfigInfoList:
    import capo_rds.types.user_auth_config_info

    out: UserAuthConfigInfoList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.user_auth_config_info.deserialize_query(child))
    return out
