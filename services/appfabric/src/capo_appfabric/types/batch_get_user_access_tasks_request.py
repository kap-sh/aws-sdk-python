"""Generated from Smithy shape ``com.amazonaws.appfabric#BatchGetUserAccessTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.identifier
    import capo_appfabric.types.task_id_list


class BatchGetUserAccessTasksRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    task_id_list: "capo_appfabric.types.task_id_list.TaskIdList"
    """<p>The tasks IDs to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetUserAccessTasksRequest) -> dict:
    out: dict = {}
    out["appBundleIdentifier"] = value["app_bundle_identifier"]
    import capo_appfabric.types.task_id_list

    out["taskIdList"] = capo_appfabric.types.task_id_list.serialize_json(
        value["task_id_list"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetUserAccessTasksRequest:
    out: BatchGetUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
    if "appBundleIdentifier" in data:
        out["app_bundle_identifier"] = data["appBundleIdentifier"]
    else:
        raise DeserializationError(
            "BatchGetUserAccessTasksRequest.app_bundle_identifier required"
        )
    if "taskIdList" in data:
        import capo_appfabric.types.task_id_list

        out["task_id_list"] = capo_appfabric.types.task_id_list.deserialize_json(
            data["taskIdList"]
        )
    else:
        raise DeserializationError(
            "BatchGetUserAccessTasksRequest.task_id_list required"
        )
    return out
