"""Generated from Smithy shape ``com.amazonaws.neptune#DeleteDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DeleteDBSubnetGroupMessage(TypedDict):
    db_subnet_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the database subnet group to delete.</p> <note> <p>You can't delete the default subnet group.</p> </note> <p>Constraints:</p> <p>Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteDBSubnetGroupMessage:
    out: DeleteDBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    return out
