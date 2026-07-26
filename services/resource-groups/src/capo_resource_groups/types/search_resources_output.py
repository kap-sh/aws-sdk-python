"""Generated from Smithy shape ``com.amazonaws.resourcegroups#SearchResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.next_token
    import capo_resource_groups.types.query_error_list
    import capo_resource_groups.types.resource_identifier_list


class SearchResourcesOutput(TypedDict, closed=True):
    resource_identifiers: NotRequired[
        "capo_resource_groups.types.resource_identifier_list.ResourceIdentifierList"
    ]
    """<p>The ARNs and resource types of resources that are members of the group that you specified.</p>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    query_errors: NotRequired[
        "capo_resource_groups.types.query_error_list.QueryErrorList"
    ]
    """<p>A list of <code>QueryError</code> objects. Each error contains an <code>ErrorCode</code> and <code>Message</code>.</p> <p>Possible values for <code>ErrorCode</code>:</p> <ul> <li> <p> <code>CLOUDFORMATION_STACK_INACTIVE</code> </p> </li> <li> <p> <code>CLOUDFORMATION_STACK_NOT_EXISTING</code> </p> </li> <li> <p> <code>CLOUDFORMATION_STACK_UNASSUMABLE_ROLE </code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesOutput) -> dict:
    out: dict = {}
    if "resource_identifiers" in value:
        import capo_resource_groups.types.resource_identifier_list

        out["ResourceIdentifiers"] = (
            capo_resource_groups.types.resource_identifier_list.serialize_json(
                value["resource_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "query_errors" in value:
        import capo_resource_groups.types.query_error_list

        out["QueryErrors"] = capo_resource_groups.types.query_error_list.serialize_json(
            value["query_errors"]
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesOutput:
    out: SearchResourcesOutput = {}  # type: ignore[typeddict-item]
    if "ResourceIdentifiers" in data:
        import capo_resource_groups.types.resource_identifier_list

        out["resource_identifiers"] = (
            capo_resource_groups.types.resource_identifier_list.deserialize_json(
                data["ResourceIdentifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "QueryErrors" in data:
        import capo_resource_groups.types.query_error_list

        out["query_errors"] = (
            capo_resource_groups.types.query_error_list.deserialize_json(
                data["QueryErrors"]
            )
        )
    return out
