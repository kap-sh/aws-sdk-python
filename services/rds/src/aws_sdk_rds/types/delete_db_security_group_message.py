"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DeleteDBSecurityGroupMessage(TypedDict, closed=True):
    db_security_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    r"""<p>The name of the DB security group to delete.</p> <note> <p>You can't delete the default DB security group.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> <li> <p>Must not be \"Default\"</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_security_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSecurityGroupName", str(value["db_security_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteDBSecurityGroupMessage:
    out: DeleteDBSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_security_group_name = el.find("DBSecurityGroupName")
    if child_db_security_group_name is not None:
        out["db_security_group_name"] = str(child_db_security_group_name.text or "")
    return out
