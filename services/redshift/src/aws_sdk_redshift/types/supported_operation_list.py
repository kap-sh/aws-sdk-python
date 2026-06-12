"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.supported_operation

SupportedOperationList: TypeAlias = list[
    "aws_sdk_redshift.types.supported_operation.SupportedOperation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedOperationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.supported_operation

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.supported_operation.serialize_query(
            item, pairs, f"{prefix}.SupportedOperation.{n}"
        )


def deserialize_query(el: Element) -> SupportedOperationList:
    import aws_sdk_redshift.types.supported_operation

    out: SupportedOperationList = []
    for child in el.findall("SupportedOperation"):
        out.append(aws_sdk_redshift.types.supported_operation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedOperationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.supported_operation

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.supported_operation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SupportedOperationList:
    import aws_sdk_redshift.types.supported_operation

    out: SupportedOperationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.supported_operation.deserialize_query(child))
    return out
