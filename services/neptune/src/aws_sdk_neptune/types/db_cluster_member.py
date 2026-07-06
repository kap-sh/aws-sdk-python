"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean
    import aws_sdk_neptune.types.integer_optional
    import aws_sdk_neptune.types.string


class DBClusterMember(TypedDict, closed=True):
    db_instance_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Specifies the instance identifier for this member of the DB cluster.</p>"""
    is_cluster_writer: NotRequired["aws_sdk_neptune.types.boolean.Boolean"]
    """<p>Value that is <code>true</code> if the cluster member is the primary instance for the DB cluster and <code>false</code> otherwise.</p>"""
    db_cluster_parameter_group_status: NotRequired[
        "aws_sdk_neptune.types.string.String"
    ]
    """<p>Specifies the status of the DB cluster parameter group for this member of the DB cluster.</p>"""
    promotion_tier: NotRequired[
        "aws_sdk_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "is_cluster_writer" in value:
        pairs.append(
            (
                f"{prefix}.IsClusterWriter",
                "true" if value["is_cluster_writer"] else "false",
            )
        )
    if "db_cluster_parameter_group_status" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterParameterGroupStatus",
                str(value["db_cluster_parameter_group_status"]),
            )
        )
    if "promotion_tier" in value:
        pairs.append((f"{prefix}.PromotionTier", str(value["promotion_tier"])))


def deserialize_query(el: Element) -> DBClusterMember:
    out: DBClusterMember = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_is_cluster_writer = el.find("IsClusterWriter")
    if child_is_cluster_writer is not None:
        out["is_cluster_writer"] = (
            child_is_cluster_writer.text or ""
        ).lower() == "true"
    child_db_cluster_parameter_group_status = el.find("DBClusterParameterGroupStatus")
    if child_db_cluster_parameter_group_status is not None:
        out["db_cluster_parameter_group_status"] = str(
            child_db_cluster_parameter_group_status.text or ""
        )
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    return out
