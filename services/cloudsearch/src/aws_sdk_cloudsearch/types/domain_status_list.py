"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DomainStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_status

DomainStatusList: TypeAlias = list[
    "aws_sdk_cloudsearch.types.domain_status.DomainStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.domain_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudsearch.types.domain_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DomainStatusList:
    import aws_sdk_cloudsearch.types.domain_status

    out: DomainStatusList = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudsearch.types.domain_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DomainStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.domain_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudsearch.types.domain_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DomainStatusList:
    import aws_sdk_cloudsearch.types.domain_status

    out: DomainStatusList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudsearch.types.domain_status.deserialize_query(child))
    return out
