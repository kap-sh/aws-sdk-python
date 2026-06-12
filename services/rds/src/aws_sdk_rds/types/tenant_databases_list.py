"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabasesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.tenant_database

TenantDatabasesList: TypeAlias = list[
    "aws_sdk_rds.types.tenant_database.TenantDatabase"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.tenant_database

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.tenant_database.serialize_query(
            item, pairs, f"{prefix}.TenantDatabase.{n}"
        )


def deserialize_query(el: Element) -> TenantDatabasesList:
    import aws_sdk_rds.types.tenant_database

    out: TenantDatabasesList = []
    for child in el.findall("TenantDatabase"):
        out.append(aws_sdk_rds.types.tenant_database.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.tenant_database

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.tenant_database.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TenantDatabasesList:
    import aws_sdk_rds.types.tenant_database

    out: TenantDatabasesList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.tenant_database.deserialize_query(child))
    return out
