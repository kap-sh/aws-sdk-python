"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.supported_operation

SupportedOperationList: TypeAlias = list[
    "capo_redshift.types.supported_operation.SupportedOperation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedOperationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.supported_operation

    for n, item in enumerate(value, 1):
        capo_redshift.types.supported_operation.serialize_query(
            item, pairs, f"{prefix}.SupportedOperation.{n}"
        )


def deserialize_query(el: Element) -> SupportedOperationList:
    import capo_redshift.types.supported_operation

    out: SupportedOperationList = []
    for child in el.findall("SupportedOperation"):
        out.append(capo_redshift.types.supported_operation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedOperationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.supported_operation

    for n, item in enumerate(value, 1):
        capo_redshift.types.supported_operation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SupportedOperationList:
    import capo_redshift.types.supported_operation

    out: SupportedOperationList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.supported_operation.deserialize_query(child))
    return out
