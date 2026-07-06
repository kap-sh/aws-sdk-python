"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterOptionGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DBClusterOptionGroupStatus(TypedDict, closed=True):
    db_cluster_option_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    status: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterOptionGroupStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_option_group_name" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterOptionGroupName",
                str(value["db_cluster_option_group_name"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> DBClusterOptionGroupStatus:
    out: DBClusterOptionGroupStatus = {}  # type: ignore[typeddict-item]
    child_db_cluster_option_group_name = el.find("DBClusterOptionGroupName")
    if child_db_cluster_option_group_name is not None:
        out["db_cluster_option_group_name"] = str(
            child_db_cluster_option_group_name.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
