"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.boolean
    import aws_sdk_application_discovery_service.types.to_delete_identifier_list


class BatchDeleteImportDataRequest(TypedDict):
    import_task_ids: "aws_sdk_application_discovery_service.types.to_delete_identifier_list.ToDeleteIdentifierList"
    """<p>The IDs for the import tasks that you want to delete.</p>"""
    delete_history: "aws_sdk_application_discovery_service.types.boolean.Boolean"
    """<p> Set to <code>true</code> to remove the deleted import task from <a>DescribeImportTasks</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.to_delete_identifier_list

    out["importTaskIds"] = (
        aws_sdk_application_discovery_service.types.to_delete_identifier_list.serialize_aws_json_1_1(
            value["import_task_ids"]
        )
    )
    out["deleteHistory"] = value.get("delete_history", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImportDataRequest:
    out: BatchDeleteImportDataRequest = {}  # type: ignore[typeddict-item]
    if "importTaskIds" in data:
        import aws_sdk_application_discovery_service.types.to_delete_identifier_list

        out["import_task_ids"] = (
            aws_sdk_application_discovery_service.types.to_delete_identifier_list.deserialize_aws_json_1_1(
                data["importTaskIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteImportDataRequest.import_task_ids required"
        )
    if "deleteHistory" in data:
        out["delete_history"] = data["deleteHistory"]
    else:
        out["delete_history"] = False
    return out
