"""Generated from Smithy shape ``com.amazonaws.xray#CreateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.filter_expression
    import aws_sdk_xray.types.group_name
    import aws_sdk_xray.types.insights_configuration
    import aws_sdk_xray.types.tag_list


class CreateGroupRequest(TypedDict):
    group_name: "aws_sdk_xray.types.group_name.GroupName"
    """<p>The case-sensitive name of the new group. Default is a reserved name and names must be unique.</p>"""
    filter_expression: NotRequired[
        "aws_sdk_xray.types.filter_expression.FilterExpression"
    ]
    """<p>The filter expression defining criteria by which to group traces.</p>"""
    insights_configuration: NotRequired[
        "aws_sdk_xray.types.insights_configuration.InsightsConfiguration"
    ]
    """<p>The structure containing configurations related to insights.</p> <ul> <li> <p>The InsightsEnabled boolean can be set to true to enable insights for the new group or false to disable insights for the new group.</p> </li> <li> <p>The NotificationsEnabled boolean can be set to true to enable insights notifications for the new group. Notifications may only be enabled on a group with InsightsEnabled set to true.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_xray.types.tag_list.TagList"]
    r"""<p>A map that contains one or more tag keys and tag values to attach to an X-Ray group. For more information about ways to use tags, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>Maximum number of user-applied tags per resource: 50</p> </li> <li> <p>Maximum tag key length: 128 Unicode characters</p> </li> <li> <p>Maximum tag value length: 256 Unicode characters</p> </li> <li> <p>Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for keys; it's reserved for Amazon Web Services use.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "insights_configuration" in value:
        import aws_sdk_xray.types.insights_configuration

        out["InsightsConfiguration"] = (
            aws_sdk_xray.types.insights_configuration.serialize_json(
                value["insights_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_xray.types.tag_list

        out["Tags"] = aws_sdk_xray.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    else:
        raise DeserializationError("CreateGroupRequest.group_name required")
    if "FilterExpression" in data:
        out["filter_expression"] = data["FilterExpression"]
    if "InsightsConfiguration" in data:
        import aws_sdk_xray.types.insights_configuration

        out["insights_configuration"] = (
            aws_sdk_xray.types.insights_configuration.deserialize_json(
                data["InsightsConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_xray.types.tag_list

        out["tags"] = aws_sdk_xray.types.tag_list.deserialize_json(data["Tags"])
    return out
