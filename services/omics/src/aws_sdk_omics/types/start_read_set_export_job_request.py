"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.export_read_set_list
    import aws_sdk_omics.types.role_arn
    import aws_sdk_omics.types.s3_destination
    import aws_sdk_omics.types.sequence_store_id


class StartReadSetExportJobRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    destination: "aws_sdk_omics.types.s3_destination.S3Destination"
    """<p>A location for exported files in Amazon S3.</p>"""
    role_arn: "aws_sdk_omics.types.role_arn.RoleArn"
    """<p>A service role for the job.</p>"""
    client_token: NotRequired["aws_sdk_omics.types.client_token.ClientToken"]
    """<p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>"""
    sources: "aws_sdk_omics.types.export_read_set_list.ExportReadSetList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetExportJobRequest) -> dict:
    out: dict = {}
    out["destination"] = value["destination"]
    out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_omics.types.export_read_set_list

    out["sources"] = aws_sdk_omics.types.export_read_set_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> StartReadSetExportJobRequest:
    out: StartReadSetExportJobRequest = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("StartReadSetExportJobRequest.destination required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartReadSetExportJobRequest.role_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "sources" in data:
        import aws_sdk_omics.types.export_read_set_list

        out["sources"] = aws_sdk_omics.types.export_read_set_list.deserialize_json(
            data["sources"]
        )
    else:
        raise DeserializationError("StartReadSetExportJobRequest.sources required")
    return out
