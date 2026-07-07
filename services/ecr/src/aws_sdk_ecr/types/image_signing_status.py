"""Generated from Smithy shape ``com.amazonaws.ecr#ImageSigningStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_profile_arn
    import aws_sdk_ecr.types.signing_status
    import aws_sdk_ecr.types.signing_status_failure_code
    import aws_sdk_ecr.types.signing_status_failure_reason


class ImageSigningStatus(TypedDict, closed=True):
    signing_profile_arn: NotRequired[
        "aws_sdk_ecr.types.signing_profile_arn.SigningProfileArn"
    ]
    """<p>The ARN of the Amazon Web Services Signer signing profile used to sign the image.</p>"""
    failure_code: NotRequired[
        "aws_sdk_ecr.types.signing_status_failure_code.SigningStatusFailureCode"
    ]
    """<p>The failure code, which is only present if <code>status</code> is <code>FAILED</code>.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_ecr.types.signing_status_failure_reason.SigningStatusFailureReason"
    ]
    """<p>A description of why signing the image failed. This field is only present if <code>status</code> is <code>FAILED</code>.</p>"""
    status: NotRequired["aws_sdk_ecr.types.signing_status.SigningStatus"]
    """<p>The image's signing status. Possible values are:</p> <ul> <li> <p> <code>IN_PROGRESS</code> - Signing is currently in progress.</p> </li> <li> <p> <code>COMPLETE</code> - The signature was successfully generated.</p> </li> <li> <p> <code>FAILED</code> - Signing failed. See <code>failureCode</code> and <code>failureReason</code> for details.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSigningStatus) -> dict:
    out: dict = {}
    if "signing_profile_arn" in value:
        out["signingProfileArn"] = value["signing_profile_arn"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "status" in value:
        import aws_sdk_ecr.types.signing_status

        out["status"] = aws_sdk_ecr.types.signing_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageSigningStatus:
    out: ImageSigningStatus = {}  # type: ignore[typeddict-item]
    if "signingProfileArn" in data:
        out["signing_profile_arn"] = data["signingProfileArn"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "status" in data:
        import aws_sdk_ecr.types.signing_status

        out["status"] = aws_sdk_ecr.types.signing_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
