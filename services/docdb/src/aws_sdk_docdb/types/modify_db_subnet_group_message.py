"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.subnet_identifier_list


class ModifyDBSubnetGroupMessage(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name for the subnet group. This value is stored as a lowercase string. You can't modify the default subnet group. </p> <p>Constraints: Must match the name of an existing <code>DBSubnetGroup</code>. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    db_subnet_group_description: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The description for the subnet group.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_docdb.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The Amazon EC2 subnet IDs for the subnet group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{prefix}.DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_docdb.types.subnet_identifier_list

        aws_sdk_docdb.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )


def deserialize_query(el: Element) -> ModifyDBSubnetGroupMessage:
    out: ModifyDBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_db_subnet_group_description = el.find("DBSubnetGroupDescription")
    if child_db_subnet_group_description is not None:
        out["db_subnet_group_description"] = str(
            child_db_subnet_group_description.text or ""
        )
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import aws_sdk_docdb.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_docdb.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    return out
