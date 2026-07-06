"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.execution_id
    import aws_sdk_transfer.types.execution_results
    import aws_sdk_transfer.types.execution_status
    import aws_sdk_transfer.types.file_location
    import aws_sdk_transfer.types.logging_configuration
    import aws_sdk_transfer.types.posix_profile
    import aws_sdk_transfer.types.role
    import aws_sdk_transfer.types.service_metadata


class DescribedExecution(TypedDict, closed=True):
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
    execution_role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>The IAM role associated with the execution.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_transfer.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The IAM logging role associated with the execution.</p>"""
    posix_profile: NotRequired["aws_sdk_transfer.types.posix_profile.PosixProfile"]
    status: NotRequired["aws_sdk_transfer.types.execution_status.ExecutionStatus"]
    """<p>The status is one of the execution. Can be in progress, completed, exception encountered, or handling the exception. </p>"""
    results: NotRequired["aws_sdk_transfer.types.execution_results.ExecutionResults"]
    """<p>A structure that describes the execution results. This includes a list of the steps along with the details of each step, error type and message (if any), and the <code>OnExceptionSteps</code> structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedExecution) -> dict:
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
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "logging_configuration" in value:
        import aws_sdk_transfer.types.logging_configuration

        out["LoggingConfiguration"] = (
            aws_sdk_transfer.types.logging_configuration.serialize_aws_json_1_1(
                value["logging_configuration"]
            )
        )
    if "posix_profile" in value:
        import aws_sdk_transfer.types.posix_profile

        out["PosixProfile"] = (
            aws_sdk_transfer.types.posix_profile.serialize_aws_json_1_1(
                value["posix_profile"]
            )
        )
    if "status" in value:
        import aws_sdk_transfer.types.execution_status

        out["Status"] = aws_sdk_transfer.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "results" in value:
        import aws_sdk_transfer.types.execution_results

        out["Results"] = (
            aws_sdk_transfer.types.execution_results.serialize_aws_json_1_1(
                value["results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedExecution:
    out: DescribedExecution = {}  # type: ignore[typeddict-item]
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
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "LoggingConfiguration" in data:
        import aws_sdk_transfer.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_transfer.types.logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    if "PosixProfile" in data:
        import aws_sdk_transfer.types.posix_profile

        out["posix_profile"] = (
            aws_sdk_transfer.types.posix_profile.deserialize_aws_json_1_1(
                data["PosixProfile"]
            )
        )
    if "Status" in data:
        import aws_sdk_transfer.types.execution_status

        out["status"] = (
            aws_sdk_transfer.types.execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Results" in data:
        import aws_sdk_transfer.types.execution_results

        out["results"] = (
            aws_sdk_transfer.types.execution_results.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    return out
