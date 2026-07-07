"""Generated from Smithy shape ``com.amazonaws.rds#ModifyTenantDatabaseResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.tenant_database


class ModifyTenantDatabaseResult(TypedDict, closed=True):
    tenant_database: NotRequired["aws_sdk_rds.types.tenant_database.TenantDatabase"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTenantDatabaseResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tenant_database" in value:
        import aws_sdk_rds.types.tenant_database

        aws_sdk_rds.types.tenant_database.serialize_query(
            value["tenant_database"], pairs, f"{prefix}.TenantDatabase"
        )


def deserialize_query(el: Element) -> ModifyTenantDatabaseResult:
    out: ModifyTenantDatabaseResult = {}  # type: ignore[typeddict-item]
    child_tenant_database = el.find("TenantDatabase")
    if child_tenant_database is not None:
        import aws_sdk_rds.types.tenant_database

        out["tenant_database"] = aws_sdk_rds.types.tenant_database.deserialize_query(
            child_tenant_database
        )
    return out
