"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleResourceAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.association_state
    import aws_sdk_workspaces.types.association_state_reason
    import aws_sdk_workspaces.types.bundle_associated_resource_type
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.non_empty_string
    import aws_sdk_workspaces.types.timestamp


class BundleResourceAssociation(TypedDict):
    associated_resource_id: NotRequired[
        "aws_sdk_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the associated resource.</p>"""
    associated_resource_type: NotRequired[
        "aws_sdk_workspaces.types.bundle_associated_resource_type.BundleAssociatedResourceType"
    ]
    """<p>The resource type of the associated resources.</p>"""
    bundle_id: NotRequired["aws_sdk_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    created: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association is created.</p>"""
    last_updated_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association status was last updated.</p>"""
    state: NotRequired["aws_sdk_workspaces.types.association_state.AssociationState"]
    """<p>The status of the bundle resource association.</p>"""
    state_reason: NotRequired[
        "aws_sdk_workspaces.types.association_state_reason.AssociationStateReason"
    ]
    """<p>The reason the association deployment failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleResourceAssociation) -> dict:
    out: dict = {}
    if "associated_resource_id" in value:
        out["AssociatedResourceId"] = value["associated_resource_id"]
    if "associated_resource_type" in value:
        import aws_sdk_workspaces.types.bundle_associated_resource_type

        out["AssociatedResourceType"] = (
            aws_sdk_workspaces.types.bundle_associated_resource_type.serialize_aws_json_1_1(
                value["associated_resource_type"]
            )
        )
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "created" in value:
        import aws_sdk_workspaces.types.timestamp

        out["Created"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_updated_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    if "state" in value:
        import aws_sdk_workspaces.types.association_state

        out["State"] = (
            aws_sdk_workspaces.types.association_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        import aws_sdk_workspaces.types.association_state_reason

        out["StateReason"] = (
            aws_sdk_workspaces.types.association_state_reason.serialize_aws_json_1_1(
                value["state_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BundleResourceAssociation:
    out: BundleResourceAssociation = {}  # type: ignore[typeddict-item]
    if "AssociatedResourceId" in data:
        out["associated_resource_id"] = data["AssociatedResourceId"]
    if "AssociatedResourceType" in data:
        import aws_sdk_workspaces.types.bundle_associated_resource_type

        out["associated_resource_type"] = (
            aws_sdk_workspaces.types.bundle_associated_resource_type.deserialize_aws_json_1_1(
                data["AssociatedResourceType"]
            )
        )
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "Created" in data:
        import aws_sdk_workspaces.types.timestamp

        out["created"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "State" in data:
        import aws_sdk_workspaces.types.association_state

        out["state"] = (
            aws_sdk_workspaces.types.association_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        import aws_sdk_workspaces.types.association_state_reason

        out["state_reason"] = (
            aws_sdk_workspaces.types.association_state_reason.deserialize_aws_json_1_1(
                data["StateReason"]
            )
        )
    return out
