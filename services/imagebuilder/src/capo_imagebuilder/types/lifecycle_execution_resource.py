"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.lifecycle_execution_resource_action
    import capo_imagebuilder.types.lifecycle_execution_resource_state
    import capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.string_list


class LifecycleExecutionResource(TypedDict, closed=True):
    account_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The account that owns the impacted resource.</p>"""
    resource_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Identifies the impacted resource. The resource ID depends on the type of resource, as follows.</p> <ul> <li> <p>Image Builder image resources: Amazon Resource Name (ARN)</p> </li> <li> <p>Distributed AMIs: AMI ID</p> </li> <li> <p>Container images distributed to an ECR repository: image URI or SHA Digest</p> </li> </ul>"""
    state: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_resource_state.LifecycleExecutionResourceState"
    ]
    """<p>The runtime state for the lifecycle execution.</p>"""
    action: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_resource_action.LifecycleExecutionResourceAction"
    ]
    """<p>The action to take for the identified resource.</p>"""
    region: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region where the lifecycle execution resource is stored.</p>"""
    snapshots: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list.LifecycleExecutionSnapshotResourceList"
    ]
    """<p>A list of associated resource snapshots for the impacted resource if it’s an AMI.</p>"""
    image_uris: NotRequired["capo_imagebuilder.types.string_list.StringList"]
    """<p>For an impacted container image, this identifies a list of URIs for associated container images distributed to ECR repositories.</p>"""
    start_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The starting timestamp from the lifecycle action that was applied to the resource.</p>"""
    end_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The ending timestamp from the lifecycle action that was applied to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResource) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "state" in value:
        import capo_imagebuilder.types.lifecycle_execution_resource_state

        out["state"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_state.serialize_json(
                value["state"]
            )
        )
    if "action" in value:
        import capo_imagebuilder.types.lifecycle_execution_resource_action

        out["action"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_action.serialize_json(
                value["action"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "snapshots" in value:
        import capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list

        out["snapshots"] = (
            capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list.serialize_json(
                value["snapshots"]
            )
        )
    if "image_uris" in value:
        import capo_imagebuilder.types.string_list

        out["imageUris"] = capo_imagebuilder.types.string_list.serialize_json(
            value["image_uris"]
        )
    if "start_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["startTime"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["endTime"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> LifecycleExecutionResource:
    out: LifecycleExecutionResource = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "state" in data:
        import capo_imagebuilder.types.lifecycle_execution_resource_state

        out["state"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_state.deserialize_json(
                data["state"]
            )
        )
    if "action" in data:
        import capo_imagebuilder.types.lifecycle_execution_resource_action

        out["action"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_action.deserialize_json(
                data["action"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "snapshots" in data:
        import capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list

        out["snapshots"] = (
            capo_imagebuilder.types.lifecycle_execution_snapshot_resource_list.deserialize_json(
                data["snapshots"]
            )
        )
    if "imageUris" in data:
        import capo_imagebuilder.types.string_list

        out["image_uris"] = capo_imagebuilder.types.string_list.deserialize_json(
            data["imageUris"]
        )
    if "startTime" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["start_time"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["end_time"] = capo_imagebuilder.types.date_time_timestamp.deserialize_json(
            data["endTime"]
        )
    return out
