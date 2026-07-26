"""Generated from Smithy shape ``com.amazonaws.rds#AddRoleToDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class AddRoleToDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB instance to associate the IAM role with.</p>"""
    role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the DB instance, for example <code>arn:aws:iam::123456789012:role/AccessRole</code>.</p>"""
    feature_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the feature for the DB instance that the IAM role is to be associated with. For information about supported feature names, see <a>DBEngineVersion</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddRoleToDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "feature_name" in value:
        pairs.append((f"{prefix}.FeatureName", str(value["feature_name"])))


def deserialize_query(el: Element) -> AddRoleToDBInstanceMessage:
    out: AddRoleToDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_feature_name = el.find("FeatureName")
    if child_feature_name is not None:
        out["feature_name"] = str(child_feature_name.text or "")
    return out
