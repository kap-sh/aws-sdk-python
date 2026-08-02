"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DeleteDBSubnetGroupMessage(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database subnet group to delete.</p> <note> <p>You can't delete the default subnet group.</p> </note> <p>Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.</p> <p>Example: <code>mydbsubnetgroup</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteDBSubnetGroupMessage:
    out: DeleteDBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    return out
