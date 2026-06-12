"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.service_update

ServiceUpdateList: TypeAlias = list[
    "aws_sdk_elasticache.types.service_update.ServiceUpdate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.service_update

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.service_update.serialize_query(
            item, pairs, f"{prefix}.ServiceUpdate.{n}"
        )


def deserialize_query(el: Element) -> ServiceUpdateList:
    import aws_sdk_elasticache.types.service_update

    out: ServiceUpdateList = []
    for child in el.findall("ServiceUpdate"):
        out.append(aws_sdk_elasticache.types.service_update.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ServiceUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.service_update

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.service_update.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServiceUpdateList:
    import aws_sdk_elasticache.types.service_update

    out: ServiceUpdateList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.service_update.deserialize_query(child))
    return out
