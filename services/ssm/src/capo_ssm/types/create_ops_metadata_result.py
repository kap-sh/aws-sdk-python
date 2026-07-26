"""Generated from Smithy shape ``com.amazonaws.ssm#CreateOpsMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata_arn


class CreateOpsMetadataResult(TypedDict, closed=True):
    ops_metadata_arn: NotRequired["capo_ssm.types.ops_metadata_arn.OpsMetadataArn"]
    """<p>The Amazon Resource Name (ARN) of the OpsMetadata Object or blob created by the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpsMetadataResult) -> dict:
    out: dict = {}
    if "ops_metadata_arn" in value:
        out["OpsMetadataArn"] = value["ops_metadata_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpsMetadataResult:
    out: CreateOpsMetadataResult = {}  # type: ignore[typeddict-item]
    if "OpsMetadataArn" in data:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    return out
