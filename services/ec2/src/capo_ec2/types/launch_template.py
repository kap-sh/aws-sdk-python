"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.launch_template_name
    import capo_ec2.types.long
    import capo_ec2.types.operator_response
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class LaunchTemplate(TypedDict, closed=True):
    launch_template_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired[
        "capo_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time launch template was created.</p>"""
    created_by: NotRequired["capo_ec2.types.string.String"]
    """<p>The principal that created the launch template. </p>"""
    default_version_number: NotRequired["capo_ec2.types.long.Long"]
    """<p>The version number of the default version of the launch template.</p>"""
    latest_version_number: NotRequired["capo_ec2.types.long.Long"]
    """<p>The version number of the latest version of the launch template.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the launch template.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "created_by" in value:
        pairs.append((f"{key_prefix}CreatedBy", str(value["created_by"])))
    if "default_version_number" in value:
        pairs.append(
            (f"{key_prefix}DefaultVersionNumber", str(value["default_version_number"]))
        )
    if "latest_version_number" in value:
        pairs.append(
            (f"{key_prefix}LatestVersionNumber", str(value["latest_version_number"]))
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplate:
    out: LaunchTemplate = {}  # type: ignore[typeddict-item]
    child_launch_template_id = el.find("launchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("launchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_created_by = el.find("createdBy")
    if child_created_by is not None:
        out["created_by"] = str(child_created_by.text or "")
    child_default_version_number = el.find("defaultVersionNumber")
    if child_default_version_number is not None:
        out["default_version_number"] = int(child_default_version_number.text or "")
    child_latest_version_number = el.find("latestVersionNumber")
    if child_latest_version_number is not None:
        out["latest_version_number"] = int(child_latest_version_number.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out
