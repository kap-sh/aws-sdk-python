"""Generated from Smithy shape ``com.amazonaws.guardduty#DestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class DestinationProperties(TypedDict, closed=True):
    destination_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ARN of the resource to publish to.</p> <p>To specify an S3 bucket folder use the following format: <code>arn:aws:s3:::DOC-EXAMPLE-BUCKET/myFolder/</code> </p>"""
    kms_key_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ARN of the KMS key to use for encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationProperties) -> dict:
    out: dict = {}
    if "destination_arn" in value:
        out["destinationArn"] = value["destination_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> DestinationProperties:
    out: DestinationProperties = {}  # type: ignore[typeddict-item]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
