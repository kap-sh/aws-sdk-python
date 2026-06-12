"""Generated from Smithy shape ``com.amazonaws.appfabric#BatchGetUserAccessTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier
    import aws_sdk_appfabric.types.task_id_list


class BatchGetUserAccessTasksRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    task_id_list: "aws_sdk_appfabric.types.task_id_list.TaskIdList"
    """<p>The tasks IDs to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetUserAccessTasksRequest) -> dict:
    out: dict = {}
    out["appBundleIdentifier"] = value["app_bundle_identifier"]
    import aws_sdk_appfabric.types.task_id_list

    out["taskIdList"] = aws_sdk_appfabric.types.task_id_list.serialize_json(
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
        import aws_sdk_appfabric.types.task_id_list

        out["task_id_list"] = aws_sdk_appfabric.types.task_id_list.deserialize_json(
            data["taskIdList"]
        )
    else:
        raise DeserializationError(
            "BatchGetUserAccessTasksRequest.task_id_list required"
        )
    return out
