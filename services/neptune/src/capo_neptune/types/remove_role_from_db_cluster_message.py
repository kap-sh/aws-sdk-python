"""Generated from Smithy shape ``com.amazonaws.neptune#RemoveRoleFromDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class RemoveRoleFromDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB cluster to disassociate the IAM role from.</p>"""
    role_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example <code>arn:aws:iam::123456789012:role/NeptuneAccessRole</code>.</p>"""
    feature_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the feature for the DB cluster that the IAM role is to be disassociated from. For the list of supported feature names, see <a>DescribeDBEngineVersions</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveRoleFromDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    if "feature_name" in value:
        pairs.append((f"{key_prefix}FeatureName", str(value["feature_name"])))


def deserialize_query(el: Element) -> RemoveRoleFromDBClusterMessage:
    out: RemoveRoleFromDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_feature_name = el.find("FeatureName")
    if child_feature_name is not None:
        out["feature_name"] = str(child_feature_name.text or "")
    return out
