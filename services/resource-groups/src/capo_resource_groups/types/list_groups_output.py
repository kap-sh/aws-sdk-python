"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_identifier_list
    import capo_resource_groups.types.group_list
    import capo_resource_groups.types.next_token


class ListGroupsOutput(TypedDict, closed=True):
    group_identifiers: NotRequired[
        "capo_resource_groups.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>A list of <a>GroupIdentifier</a> objects. Each identifier is an object that contains both the <code>Name</code> and the <code>GroupArn</code>.</p>"""
    groups: NotRequired["capo_resource_groups.types.group_list.GroupList"]
    """<important> <p> <i> <b>Deprecated - don't use this field. Use the <code>GroupIdentifiers</code> response field instead.</b> </i> </p> </important>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsOutput) -> dict:
    out: dict = {}
    if "group_identifiers" in value:
        import capo_resource_groups.types.group_identifier_list

        out["GroupIdentifiers"] = (
            capo_resource_groups.types.group_identifier_list.serialize_json(
                value["group_identifiers"]
            )
        )
    if "groups" in value:
        import capo_resource_groups.types.group_list

        out["Groups"] = capo_resource_groups.types.group_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupsOutput:
    out: ListGroupsOutput = {}  # type: ignore[typeddict-item]
    if "GroupIdentifiers" in data:
        import capo_resource_groups.types.group_identifier_list

        out["group_identifiers"] = (
            capo_resource_groups.types.group_identifier_list.deserialize_json(
                data["GroupIdentifiers"]
            )
        )
    if "Groups" in data:
        import capo_resource_groups.types.group_list

        out["groups"] = capo_resource_groups.types.group_list.deserialize_json(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
