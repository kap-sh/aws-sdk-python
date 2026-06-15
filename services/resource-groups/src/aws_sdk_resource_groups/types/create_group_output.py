"""Generated from Smithy shape ``com.amazonaws.resourcegroups#CreateGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group
    import aws_sdk_resource_groups.types.group_configuration
    import aws_sdk_resource_groups.types.resource_query
    import aws_sdk_resource_groups.types.tags


class CreateGroupOutput(TypedDict):
    group: NotRequired["aws_sdk_resource_groups.types.group.Group"]
    """<p>The description of the resource group.</p>"""
    resource_query: NotRequired[
        "aws_sdk_resource_groups.types.resource_query.ResourceQuery"
    ]
    r"""<p>The resource query associated with the group. For more information about resource queries, see <a href=\"https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag\">Create a tag-based group in Resource Groups</a>. </p>"""
    tags: NotRequired["aws_sdk_resource_groups.types.tags.Tags"]
    """<p>The tags associated with the group.</p>"""
    group_configuration: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration.GroupConfiguration"
    ]
    r"""<p>The service configuration associated with the resource group. For details about the syntax of a service configuration, see <a href=\"https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\">Service configurations for Resource Groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_resource_groups.types.group

        out["Group"] = aws_sdk_resource_groups.types.group.serialize_json(
            value["group"]
        )
    if "resource_query" in value:
        import aws_sdk_resource_groups.types.resource_query

        out["ResourceQuery"] = (
            aws_sdk_resource_groups.types.resource_query.serialize_json(
                value["resource_query"]
            )
        )
    if "tags" in value:
        import aws_sdk_resource_groups.types.tags

        out["Tags"] = aws_sdk_resource_groups.types.tags.serialize_json(value["tags"])
    if "group_configuration" in value:
        import aws_sdk_resource_groups.types.group_configuration

        out["GroupConfiguration"] = (
            aws_sdk_resource_groups.types.group_configuration.serialize_json(
                value["group_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGroupOutput:
    out: CreateGroupOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_resource_groups.types.group

        out["group"] = aws_sdk_resource_groups.types.group.deserialize_json(
            data["Group"]
        )
    if "ResourceQuery" in data:
        import aws_sdk_resource_groups.types.resource_query

        out["resource_query"] = (
            aws_sdk_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if "Tags" in data:
        import aws_sdk_resource_groups.types.tags

        out["tags"] = aws_sdk_resource_groups.types.tags.deserialize_json(data["Tags"])
    if "GroupConfiguration" in data:
        import aws_sdk_resource_groups.types.group_configuration

        out["group_configuration"] = (
            aws_sdk_resource_groups.types.group_configuration.deserialize_json(
                data["GroupConfiguration"]
            )
        )
    return out
