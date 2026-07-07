"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.list_group_resources_item_list
    import aws_sdk_resource_groups.types.next_token
    import aws_sdk_resource_groups.types.query_error_list
    import aws_sdk_resource_groups.types.resource_identifier_list


class ListGroupResourcesOutput(TypedDict, closed=True):
    resources: NotRequired[
        "aws_sdk_resource_groups.types.list_group_resources_item_list.ListGroupResourcesItemList"
    ]
    """<p>An array of resources from which you can determine each resource's identity, type, and group membership status.</p>"""
    resource_identifiers: NotRequired[
        "aws_sdk_resource_groups.types.resource_identifier_list.ResourceIdentifierList"
    ]
    """<important> <p> <b> <i>Deprecated - don't use this parameter. Use the <code>Resources</code> response field instead.</i> </b> </p> </important>"""
    next_token: NotRequired["aws_sdk_resource_groups.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    query_errors: NotRequired[
        "aws_sdk_resource_groups.types.query_error_list.QueryErrorList"
    ]
    """<p>A list of <code>QueryError</code> objects. Each error contains an <code>ErrorCode</code> and <code>Message</code>. Possible values for ErrorCode are <code>CLOUDFORMATION_STACK_INACTIVE</code>, <code>CLOUDFORMATION_STACK_NOT_EXISTING</code>, <code>CLOUDFORMATION_STACK_UNASSUMABLE_ROLE</code> and <code>RESOURCE_TYPE_NOT_SUPPORTED</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupResourcesOutput) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_resource_groups.types.list_group_resources_item_list

        out["Resources"] = (
            aws_sdk_resource_groups.types.list_group_resources_item_list.serialize_json(
                value["resources"]
            )
        )
    if "resource_identifiers" in value:
        import aws_sdk_resource_groups.types.resource_identifier_list

        out["ResourceIdentifiers"] = (
            aws_sdk_resource_groups.types.resource_identifier_list.serialize_json(
                value["resource_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "query_errors" in value:
        import aws_sdk_resource_groups.types.query_error_list

        out["QueryErrors"] = (
            aws_sdk_resource_groups.types.query_error_list.serialize_json(
                value["query_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListGroupResourcesOutput:
    out: ListGroupResourcesOutput = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_resource_groups.types.list_group_resources_item_list

        out["resources"] = (
            aws_sdk_resource_groups.types.list_group_resources_item_list.deserialize_json(
                data["Resources"]
            )
        )
    if "ResourceIdentifiers" in data:
        import aws_sdk_resource_groups.types.resource_identifier_list

        out["resource_identifiers"] = (
            aws_sdk_resource_groups.types.resource_identifier_list.deserialize_json(
                data["ResourceIdentifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "QueryErrors" in data:
        import aws_sdk_resource_groups.types.query_error_list

        out["query_errors"] = (
            aws_sdk_resource_groups.types.query_error_list.deserialize_json(
                data["QueryErrors"]
            )
        )
    return out
