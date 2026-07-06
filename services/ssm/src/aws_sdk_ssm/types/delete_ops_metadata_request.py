"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteOpsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_metadata_arn


class DeleteOpsMetadataRequest(TypedDict, closed=True):
    ops_metadata_arn: "aws_sdk_ssm.types.ops_metadata_arn.OpsMetadataArn"
    """<p>The Amazon Resource Name (ARN) of an OpsMetadata Object to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOpsMetadataRequest) -> dict:
    out: dict = {}
    out["OpsMetadataArn"] = value["ops_metadata_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOpsMetadataRequest:
    out: DeleteOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if "OpsMetadataArn" in data:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    else:
        raise DeserializationError("DeleteOpsMetadataRequest.ops_metadata_arn required")
    return out
