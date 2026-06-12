"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DBParameterGroup(TypedDict):
    db_parameter_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB parameter group.</p>"""
    db_parameter_group_family: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB parameter group family that this DB parameter group is compatible with.</p>"""
    description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Provides the customer-specified description for this DB parameter group.</p>"""
    db_parameter_group_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "db_parameter_group_arn" in value:
        pairs.append(
            (f"{prefix}.DBParameterGroupArn", str(value["db_parameter_group_arn"]))
        )


def deserialize_query(el: Element) -> DBParameterGroup:
    out: DBParameterGroup = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_db_parameter_group_arn = el.find("DBParameterGroupArn")
    if child_db_parameter_group_arn is not None:
        out["db_parameter_group_arn"] = str(child_db_parameter_group_arn.text or "")
    return out
