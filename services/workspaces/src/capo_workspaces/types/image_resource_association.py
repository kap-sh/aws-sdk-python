"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageResourceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.association_state
    import capo_workspaces.types.association_state_reason
    import capo_workspaces.types.image_associated_resource_type
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.workspace_image_id


class ImageResourceAssociation(TypedDict, closed=True):
    associated_resource_id: NotRequired[
        "capo_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the associated resource.</p>"""
    associated_resource_type: NotRequired[
        "capo_workspaces.types.image_associated_resource_type.ImageAssociatedResourceType"
    ]
    """<p>The resource type of the associated resources.</p>"""
    created: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association is created.</p>"""
    last_updated_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association status was last updated.</p>"""
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the image.</p>"""
    state: NotRequired["capo_workspaces.types.association_state.AssociationState"]
    """<p>The status of the image resource association.</p>"""
    state_reason: NotRequired[
        "capo_workspaces.types.association_state_reason.AssociationStateReason"
    ]
    """<p>The reason the association deployment failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageResourceAssociation) -> dict:
    out: dict = {}
    if "associated_resource_id" in value:
        out["AssociatedResourceId"] = value["associated_resource_id"]
    if "associated_resource_type" in value:
        import capo_workspaces.types.image_associated_resource_type

        out["AssociatedResourceType"] = (
            capo_workspaces.types.image_associated_resource_type.serialize_aws_json_1_1(
                value["associated_resource_type"]
            )
        )
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_updated_time" in value:
        import capo_workspaces.types.timestamp

        out["LastUpdatedTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "state" in value:
        import capo_workspaces.types.association_state

        out["State"] = capo_workspaces.types.association_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        import capo_workspaces.types.association_state_reason

        out["StateReason"] = (
            capo_workspaces.types.association_state_reason.serialize_aws_json_1_1(
                value["state_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageResourceAssociation:
    out: ImageResourceAssociation = {}  # type: ignore[typeddict-item]
    if "AssociatedResourceId" in data:
        out["associated_resource_id"] = data["AssociatedResourceId"]
    if "AssociatedResourceType" in data:
        import capo_workspaces.types.image_associated_resource_type

        out["associated_resource_type"] = (
            capo_workspaces.types.image_associated_resource_type.deserialize_aws_json_1_1(
                data["AssociatedResourceType"]
            )
        )
    if "Created" in data:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "LastUpdatedTime" in data:
        import capo_workspaces.types.timestamp

        out["last_updated_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "State" in data:
        import capo_workspaces.types.association_state

        out["state"] = capo_workspaces.types.association_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        import capo_workspaces.types.association_state_reason

        out["state_reason"] = (
            capo_workspaces.types.association_state_reason.deserialize_aws_json_1_1(
                data["StateReason"]
            )
        )
    return out
