"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupResourcesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.resource_identifier
    import capo_resource_groups.types.resource_status


class ListGroupResourcesItem(TypedDict, closed=True):
    identifier: NotRequired[
        "capo_resource_groups.types.resource_identifier.ResourceIdentifier"
    ]
    status: NotRequired["capo_resource_groups.types.resource_status.ResourceStatus"]
    """<p>A structure that contains the status of this resource's membership in the group.</p> <note> <p>This field is present in the response only if the group is of type <code>AWS::EC2::HostManagement</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupResourcesItem) -> dict:
    out: dict = {}
    if "identifier" in value:
        import capo_resource_groups.types.resource_identifier

        out["Identifier"] = (
            capo_resource_groups.types.resource_identifier.serialize_json(
                value["identifier"]
            )
        )
    if "status" in value:
        import capo_resource_groups.types.resource_status

        out["Status"] = capo_resource_groups.types.resource_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ListGroupResourcesItem:
    out: ListGroupResourcesItem = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        import capo_resource_groups.types.resource_identifier

        out["identifier"] = (
            capo_resource_groups.types.resource_identifier.deserialize_json(
                data["Identifier"]
            )
        )
    if "Status" in data:
        import capo_resource_groups.types.resource_status

        out["status"] = capo_resource_groups.types.resource_status.deserialize_json(
            data["Status"]
        )
    return out
