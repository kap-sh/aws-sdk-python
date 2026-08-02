"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DBInstanceRole(TypedDict, closed=True):
    role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that is associated with the DB instance.</p>"""
    feature_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the feature associated with the Amazon Web Services Identity and Access Management (IAM) role. For information about supported feature names, see <code>DBEngineVersion</code>.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>Information about the state of association between the IAM role and the DB instance. The Status property returns one of the following values:</p> <ul> <li> <p> <code>ACTIVE</code> - the IAM role ARN is associated with the DB instance and can be used to access other Amazon Web Services services on your behalf.</p> </li> <li> <p> <code>PENDING</code> - the IAM role ARN is being associated with the DB instance.</p> </li> <li> <p> <code>INVALID</code> - the IAM role ARN is associated with the DB instance, but the DB instance is unable to assume the IAM role in order to access other Amazon Web Services services on your behalf.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    if "feature_name" in value:
        pairs.append((f"{key_prefix}FeatureName", str(value["feature_name"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> DBInstanceRole:
    out: DBInstanceRole = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_feature_name = el.find("FeatureName")
    if child_feature_name is not None:
        out["feature_name"] = str(child_feature_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
