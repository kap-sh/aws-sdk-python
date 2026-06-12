"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.data_share_association

DataShareAssociationList: TypeAlias = list[
    "aws_sdk_redshift.types.data_share_association.DataShareAssociation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DataShareAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.data_share_association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.data_share_association.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DataShareAssociationList:
    import aws_sdk_redshift.types.data_share_association

    out: DataShareAssociationList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_redshift.types.data_share_association.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DataShareAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.data_share_association

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.data_share_association.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DataShareAssociationList:
    import aws_sdk_redshift.types.data_share_association

    out: DataShareAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.data_share_association.deserialize_query(child)
        )
    return out
