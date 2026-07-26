"""Generated from Smithy shape ``com.amazonaws.iam#StatementListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.statement

StatementListType: TypeAlias = list["capo_iam.types.statement.Statement"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StatementListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.statement

    for n, item in enumerate(value, 1):
        capo_iam.types.statement.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> StatementListType:
    import capo_iam.types.statement

    out: StatementListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.statement.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StatementListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.statement

    for n, item in enumerate(value, 1):
        capo_iam.types.statement.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> StatementListType:
    import capo_iam.types.statement

    out: StatementListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.statement.deserialize_query(child))
    return out
