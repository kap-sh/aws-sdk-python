"""Generated from Smithy shape ``com.amazonaws.rds#SourceRegion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.string


class SourceRegion(TypedDict):
    region_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the source Amazon Web Services Region.</p>"""
    endpoint: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The endpoint for the source Amazon Web Services Region endpoint.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the source Amazon Web Services Region.</p>"""
    supports_db_instance_automated_backups_replication: NotRequired[
        "aws_sdk_rds.types.boolean.Boolean"
    ]
    """<p>Indicates whether the source Amazon Web Services Region supports replicating automated backups to the current Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceRegion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "region_name" in value:
        pairs.append((f"{prefix}.RegionName", str(value["region_name"])))
    if "endpoint" in value:
        pairs.append((f"{prefix}.Endpoint", str(value["endpoint"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "supports_db_instance_automated_backups_replication" in value:
        pairs.append(
            (
                f"{prefix}.SupportsDBInstanceAutomatedBackupsReplication",
                "true"
                if value["supports_db_instance_automated_backups_replication"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> SourceRegion:
    out: SourceRegion = {}  # type: ignore[typeddict-item]
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_supports_db_instance_automated_backups_replication = el.find(
        "SupportsDBInstanceAutomatedBackupsReplication"
    )
    if child_supports_db_instance_automated_backups_replication is not None:
        out["supports_db_instance_automated_backups_replication"] = (
            child_supports_db_instance_automated_backups_replication.text or ""
        ).lower() == "true"
    return out
