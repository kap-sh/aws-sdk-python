"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.service_update_status

ServiceUpdateStatusList: TypeAlias = list[
    "aws_sdk_elasticache.types.service_update_status.ServiceUpdateStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.service_update_status

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.service_update_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServiceUpdateStatusList:
    import aws_sdk_elasticache.types.service_update_status

    out: ServiceUpdateStatusList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elasticache.types.service_update_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ServiceUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.service_update_status

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.service_update_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServiceUpdateStatusList:
    import aws_sdk_elasticache.types.service_update_status

    out: ServiceUpdateStatusList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.service_update_status.deserialize_query(child)
        )
    return out
