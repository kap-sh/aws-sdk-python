"""Generated from Smithy shape ``com.amazonaws.rds#AddRoleToDBClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class AddRoleToDBClusterMessage(TypedDict):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB cluster to associate the IAM role with.</p>"""
    role_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example <code>arn:aws:iam::123456789012:role/AuroraAccessRole</code>.</p>"""
    feature_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the feature for the DB cluster that the IAM role is to be associated with. For information about supported feature names, see <a>DBEngineVersion</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddRoleToDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "feature_name" in value:
        pairs.append((f"{prefix}.FeatureName", str(value["feature_name"])))


def deserialize_query(el: Element) -> AddRoleToDBClusterMessage:
    out: AddRoleToDBClusterMessage = {}  # type: ignore[typeddict-item]
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
