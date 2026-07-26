"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowOutputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.kms_arn
    import capo_entityresolution.types.s3_path


class IdMappingWorkflowOutputSource(TypedDict, closed=True):
    kms_arn: NotRequired["capo_entityresolution.types.kms_arn.KMSArn"]
    """<p>Customer KMS ARN for encryption at rest. If not provided, system will use an Entity Resolution managed KMS key.</p>"""
    output_s3_path: "capo_entityresolution.types.s3_path.S3Path"
    """<p>The S3 path to which Entity Resolution will write the output table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowOutputSource) -> dict:
    out: dict = {}
    if "kms_arn" in value:
        out["KMSArn"] = value["kms_arn"]
    out["outputS3Path"] = value["output_s3_path"]
    return out


def deserialize_json(data: dict) -> IdMappingWorkflowOutputSource:
    out: IdMappingWorkflowOutputSource = {}  # type: ignore[typeddict-item]
    if "KMSArn" in data:
        out["kms_arn"] = data["KMSArn"]
    if "outputS3Path" in data:
        out["output_s3_path"] = data["outputS3Path"]
    else:
        raise DeserializationError(
            "IdMappingWorkflowOutputSource.output_s3_path required"
        )
    return out
