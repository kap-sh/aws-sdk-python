"""Generated from Smithy shape ``com.amazonaws.iam#StatementListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.statement

StatementListType: TypeAlias = list["aws_sdk_iam.types.statement.Statement"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StatementListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.statement

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.statement.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> StatementListType:
    import aws_sdk_iam.types.statement

    out: StatementListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.statement.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StatementListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.statement

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.statement.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> StatementListType:
    import aws_sdk_iam.types.statement

    out: StatementListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.statement.deserialize_query(child))
    return out
