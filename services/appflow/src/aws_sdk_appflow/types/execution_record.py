"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.date
    import aws_sdk_appflow.types.execution_id
    import aws_sdk_appflow.types.execution_result
    import aws_sdk_appflow.types.execution_status
    import aws_sdk_appflow.types.metadata_catalog_details


class ExecutionRecord(TypedDict, closed=True):
    execution_id: NotRequired["aws_sdk_appflow.types.execution_id.ExecutionId"]
    """<p> Specifies the identifier of the given flow run. </p>"""
    execution_status: NotRequired[
        "aws_sdk_appflow.types.execution_status.ExecutionStatus"
    ]
    """<p> Specifies the flow run status and whether it is in progress, has completed successfully, or has failed. </p>"""
    execution_result: NotRequired[
        "aws_sdk_appflow.types.execution_result.ExecutionResult"
    ]
    """<p> Describes the result of the given flow run. </p>"""
    started_at: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> Specifies the start time of the flow run. </p>"""
    last_updated_at: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> Specifies the time of the most recent update. </p>"""
    data_pull_start_time: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> The timestamp that determines the first new or updated record to be transferred in the flow run. </p>"""
    data_pull_end_time: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p> The timestamp that indicates the last new or updated record to be transferred in the flow run. </p>"""
    metadata_catalog_details: NotRequired[
        "aws_sdk_appflow.types.metadata_catalog_details.MetadataCatalogDetails"
    ]
    """<p>Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionRecord) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "execution_status" in value:
        import aws_sdk_appflow.types.execution_status

        out["executionStatus"] = aws_sdk_appflow.types.execution_status.serialize_json(
            value["execution_status"]
        )
    if "execution_result" in value:
        import aws_sdk_appflow.types.execution_result

        out["executionResult"] = aws_sdk_appflow.types.execution_result.serialize_json(
            value["execution_result"]
        )
    if "started_at" in value:
        import aws_sdk_appflow.types.date

        out["startedAt"] = aws_sdk_appflow.types.date.serialize_json(
            value["started_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_appflow.types.date

        out["lastUpdatedAt"] = aws_sdk_appflow.types.date.serialize_json(
            value["last_updated_at"]
        )
    if "data_pull_start_time" in value:
        import aws_sdk_appflow.types.date

        out["dataPullStartTime"] = aws_sdk_appflow.types.date.serialize_json(
            value["data_pull_start_time"]
        )
    if "data_pull_end_time" in value:
        import aws_sdk_appflow.types.date

        out["dataPullEndTime"] = aws_sdk_appflow.types.date.serialize_json(
            value["data_pull_end_time"]
        )
    if "metadata_catalog_details" in value:
        import aws_sdk_appflow.types.metadata_catalog_details

        out["metadataCatalogDetails"] = (
            aws_sdk_appflow.types.metadata_catalog_details.serialize_json(
                value["metadata_catalog_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionRecord:
    out: ExecutionRecord = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "executionStatus" in data:
        import aws_sdk_appflow.types.execution_status

        out["execution_status"] = (
            aws_sdk_appflow.types.execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    if "executionResult" in data:
        import aws_sdk_appflow.types.execution_result

        out["execution_result"] = (
            aws_sdk_appflow.types.execution_result.deserialize_json(
                data["executionResult"]
            )
        )
    if "startedAt" in data:
        import aws_sdk_appflow.types.date

        out["started_at"] = aws_sdk_appflow.types.date.deserialize_json(
            data["startedAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_appflow.types.date

        out["last_updated_at"] = aws_sdk_appflow.types.date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "dataPullStartTime" in data:
        import aws_sdk_appflow.types.date

        out["data_pull_start_time"] = aws_sdk_appflow.types.date.deserialize_json(
            data["dataPullStartTime"]
        )
    if "dataPullEndTime" in data:
        import aws_sdk_appflow.types.date

        out["data_pull_end_time"] = aws_sdk_appflow.types.date.deserialize_json(
            data["dataPullEndTime"]
        )
    if "metadataCatalogDetails" in data:
        import aws_sdk_appflow.types.metadata_catalog_details

        out["metadata_catalog_details"] = (
            aws_sdk_appflow.types.metadata_catalog_details.deserialize_json(
                data["metadataCatalogDetails"]
            )
        )
    return out
