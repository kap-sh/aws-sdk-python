"""Generated from Smithy shape ``com.amazonaws.transfer#ListedExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.execution_id
    import aws_sdk_transfer.types.execution_status
    import aws_sdk_transfer.types.file_location
    import aws_sdk_transfer.types.service_metadata


class ListedExecution(TypedDict, closed=True):
    execution_id: NotRequired["aws_sdk_transfer.types.execution_id.ExecutionId"]
    """<p>A unique identifier for the execution of a workflow.</p>"""
    initial_file_location: NotRequired[
        "aws_sdk_transfer.types.file_location.FileLocation"
    ]
    """<p>A structure that describes the Amazon S3 or EFS file location. This is the file location when the execution begins: if the file is being copied, this is the initial (as opposed to destination) file location.</p>"""
    service_metadata: NotRequired[
        "aws_sdk_transfer.types.service_metadata.ServiceMetadata"
    ]
    """<p>A container object for the session details that are associated with a workflow.</p>"""
    status: NotRequired["aws_sdk_transfer.types.execution_status.ExecutionStatus"]
    """<p>The status is one of the execution. Can be in progress, completed, exception encountered, or handling the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedExecution) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "initial_file_location" in value:
        import aws_sdk_transfer.types.file_location

        out["InitialFileLocation"] = (
            aws_sdk_transfer.types.file_location.serialize_aws_json_1_1(
                value["initial_file_location"]
            )
        )
    if "service_metadata" in value:
        import aws_sdk_transfer.types.service_metadata

        out["ServiceMetadata"] = (
            aws_sdk_transfer.types.service_metadata.serialize_aws_json_1_1(
                value["service_metadata"]
            )
        )
    if "status" in value:
        import aws_sdk_transfer.types.execution_status

        out["Status"] = aws_sdk_transfer.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedExecution:
    out: ListedExecution = {}  # type: ignore[typeddict-item]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "InitialFileLocation" in data:
        import aws_sdk_transfer.types.file_location

        out["initial_file_location"] = (
            aws_sdk_transfer.types.file_location.deserialize_aws_json_1_1(
                data["InitialFileLocation"]
            )
        )
    if "ServiceMetadata" in data:
        import aws_sdk_transfer.types.service_metadata

        out["service_metadata"] = (
            aws_sdk_transfer.types.service_metadata.deserialize_aws_json_1_1(
                data["ServiceMetadata"]
            )
        )
    if "Status" in data:
        import aws_sdk_transfer.types.execution_status

        out["status"] = (
            aws_sdk_transfer.types.execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
