"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string2048


class AssociationInfo(TypedDict):
    source_arn: NotRequired["aws_sdk_sagemaker.types.string2048.String2048"]
    """<p> The Amazon Resource Name (ARN) of the <code>AssociationInfo</code> source. </p>"""
    destination_arn: NotRequired["aws_sdk_sagemaker.types.string2048.String2048"]
    """<p> The Amazon Resource Name (ARN) of the <code>AssociationInfo</code> destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationInfo) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationInfo:
    out: AssociationInfo = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    return out
