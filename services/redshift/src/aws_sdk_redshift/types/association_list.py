"""Generated from Smithy shape ``com.amazonaws.redshift#AssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.association

AssociationList: TypeAlias = list["aws_sdk_redshift.types.association.Association"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.association.serialize_query(
            item, pairs, f"{prefix}.Association.{n}"
        )


def deserialize_query(el: Element) -> AssociationList:
    import aws_sdk_redshift.types.association

    out: AssociationList = []
    for child in el.findall("Association"):
        out.append(aws_sdk_redshift.types.association.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.association.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AssociationList:
    import aws_sdk_redshift.types.association

    out: AssociationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.association.deserialize_query(child))
    return out
