"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterRole``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DBClusterRole(TypedDict):
    role_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:</p> <ul> <li> <p> <code>ACTIVE</code> - the IAM role ARN is associated with the DB cluster and can be used to access other Amazon Web Services on your behalf.</p> </li> <li> <p> <code>PENDING</code> - the IAM role ARN is being associated with the DB cluster.</p> </li> <li> <p> <code>INVALID</code> - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other Amazon Web Services on your behalf.</p> </li> </ul>"""
    feature_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the feature associated with the Amazon Web Services Identity and Access Management (IAM) role. For information about supported feature names, see <a>DBEngineVersion</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "feature_name" in value:
        pairs.append((f"{prefix}.FeatureName", str(value["feature_name"])))


def deserialize_query(el: Element) -> DBClusterRole:
    out: DBClusterRole = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_feature_name = el.find("FeatureName")
    if child_feature_name is not None:
        out["feature_name"] = str(child_feature_name.text or "")
    return out
