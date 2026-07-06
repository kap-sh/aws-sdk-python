"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class ClusterParameterGroup(TypedDict, closed=True):
    parameter_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group.</p>"""
    parameter_group_family: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group family that this cluster parameter group is compatible with.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the parameter group.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the cluster parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "parameter_group_family" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupFamily", str(value["parameter_group_family"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> ClusterParameterGroup:
    out: ClusterParameterGroup = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_parameter_group_family = el.find("ParameterGroupFamily")
    if child_parameter_group_family is not None:
        out["parameter_group_family"] = str(child_parameter_group_family.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
