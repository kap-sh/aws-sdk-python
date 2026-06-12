"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabasePendingModifiedValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.sensitive_string
    import aws_sdk_rds.types.string


class TenantDatabasePendingModifiedValues(TypedDict):
    master_user_password: NotRequired[
        "aws_sdk_rds.types.sensitive_string.SensitiveString"
    ]
    """<p>The master password for the tenant database.</p>"""
    tenant_db_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the tenant database.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabasePendingModifiedValues,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "master_user_password" in value:
        pairs.append(
            (f"{prefix}.MasterUserPassword", str(value["master_user_password"]))
        )
    if "tenant_db_name" in value:
        pairs.append((f"{prefix}.TenantDBName", str(value["tenant_db_name"])))


def deserialize_query(el: Element) -> TenantDatabasePendingModifiedValues:
    out: TenantDatabasePendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    return out
