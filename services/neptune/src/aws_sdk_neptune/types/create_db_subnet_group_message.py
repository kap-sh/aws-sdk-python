"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.subnet_identifier_list
    import aws_sdk_neptune.types.tag_list


class CreateDBSubnetGroupMessage(TypedDict):
    db_subnet_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name for the DB subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>"""
    db_subnet_group_description: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The description for the DB subnet group.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_neptune.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The EC2 Subnet IDs for the DB subnet group.</p>"""
    tags: NotRequired["aws_sdk_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the new DB subnet group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
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
        import aws_sdk_neptune.types.subnet_identifier_list

        aws_sdk_neptune.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "tags" in value:
        import aws_sdk_neptune.types.tag_list

        aws_sdk_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateDBSubnetGroupMessage:
    out: CreateDBSubnetGroupMessage = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_neptune.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_neptune.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_neptune.types.tag_list

        out["tags"] = aws_sdk_neptune.types.tag_list.deserialize_query(child_tags)
    return out
