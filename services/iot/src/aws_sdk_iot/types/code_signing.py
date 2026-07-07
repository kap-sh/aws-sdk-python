"""Generated from Smithy shape ``com.amazonaws.iot#CodeSigning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.custom_code_signing
    import aws_sdk_iot.types.signing_job_id
    import aws_sdk_iot.types.start_signing_job_parameter


class CodeSigning(TypedDict, closed=True):
    aws_signer_job_id: NotRequired["aws_sdk_iot.types.signing_job_id.SigningJobId"]
    """<p>The ID of the <code>AWSSignerJob</code> which was created to sign the file.</p>"""
    start_signing_job_parameter: NotRequired[
        "aws_sdk_iot.types.start_signing_job_parameter.StartSigningJobParameter"
    ]
    """<p>Describes the code-signing job.</p>"""
    custom_code_signing: NotRequired[
        "aws_sdk_iot.types.custom_code_signing.CustomCodeSigning"
    ]
    """<p>A custom method for code signing a file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigning) -> dict:
    out: dict = {}
    if "aws_signer_job_id" in value:
        out["awsSignerJobId"] = value["aws_signer_job_id"]
    if "start_signing_job_parameter" in value:
        import aws_sdk_iot.types.start_signing_job_parameter

        out["startSigningJobParameter"] = (
            aws_sdk_iot.types.start_signing_job_parameter.serialize_json(
                value["start_signing_job_parameter"]
            )
        )
    if "custom_code_signing" in value:
        import aws_sdk_iot.types.custom_code_signing

        out["customCodeSigning"] = aws_sdk_iot.types.custom_code_signing.serialize_json(
            value["custom_code_signing"]
        )
    return out


def deserialize_json(data: dict) -> CodeSigning:
    out: CodeSigning = {}  # type: ignore[typeddict-item]
    if "awsSignerJobId" in data:
        out["aws_signer_job_id"] = data["awsSignerJobId"]
    if "startSigningJobParameter" in data:
        import aws_sdk_iot.types.start_signing_job_parameter

        out["start_signing_job_parameter"] = (
            aws_sdk_iot.types.start_signing_job_parameter.deserialize_json(
                data["startSigningJobParameter"]
            )
        )
    if "customCodeSigning" in data:
        import aws_sdk_iot.types.custom_code_signing

        out["custom_code_signing"] = (
            aws_sdk_iot.types.custom_code_signing.deserialize_json(
                data["customCodeSigning"]
            )
        )
    return out
