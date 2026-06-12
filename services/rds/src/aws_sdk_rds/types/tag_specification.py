"""Generated from Smithy shape ``com.amazonaws.rds#TagSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.tag_list


class TagSpecification(TypedDict):
    resource_type: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The type of resource to tag on creation.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> <li> <p> <code>cluster-auto-backup</code> - The DB cluster's automated backup.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "tags" in value:
        import aws_sdk_rds.types.tag_list

        aws_sdk_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> TagSpecification:
    out: TagSpecification = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_rds.types.tag_list

        out["tags"] = aws_sdk_rds.types.tag_list.deserialize_query(child_tags)
    return out
