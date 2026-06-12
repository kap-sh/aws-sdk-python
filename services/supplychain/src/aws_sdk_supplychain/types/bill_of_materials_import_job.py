"""Generated from Smithy shape ``com.amazonaws.supplychain#BillOfMaterialsImportJob``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_supplychain.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_supplychain.types.configuration_job_status
    import aws_sdk_supplychain.types.configuration_s3_uri
    import aws_sdk_supplychain.types.uuid

class BillOfMaterialsImportJob(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The BillOfMaterialsImportJob instanceId.</p>"""
    job_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The BillOfMaterialsImportJob jobId.</p>"""
    status: "aws_sdk_supplychain.types.configuration_job_status.ConfigurationJobStatus"
    """<p>The BillOfMaterialsImportJob ConfigurationJobStatus.</p>"""
    s3uri: "aws_sdk_supplychain.types.configuration_s3_uri.ConfigurationS3Uri"
    """<p>The S3 URI from which the CSV is read.</p>"""
    message: NotRequired["str"]
    """<p>When the BillOfMaterialsImportJob has reached a terminal state, there will be a message.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BillOfMaterialsImportJob) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["jobId"] = value["job_id"]
    import aws_sdk_supplychain.types.configuration_job_status
    out["status"] = aws_sdk_supplychain.types.configuration_job_status.serialize_json(value["status"])
    out["s3uri"] = value["s3uri"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BillOfMaterialsImportJob:
    out: BillOfMaterialsImportJob = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("BillOfMaterialsImportJob.instance_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BillOfMaterialsImportJob.job_id required")
    if "status" in data:
        import aws_sdk_supplychain.types.configuration_job_status
        out["status"] = aws_sdk_supplychain.types.configuration_job_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("BillOfMaterialsImportJob.status required")
    if "s3uri" in data:
        out["s3uri"] = data["s3uri"]
    else:
        raise DeserializationError("BillOfMaterialsImportJob.s3uri required")
    if "message" in data:
        out["message"] = data["message"]
    return out