"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningPolicies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_policy


class CodeSigningPolicies(TypedDict):
    untrusted_artifact_on_deployment: NotRequired[
        "aws_sdk_lambda.types.code_signing_policy.CodeSigningPolicy"
    ]
    """<p>Code signing configuration policy for deployment validation failure. If you set the policy to <code>Enforce</code>, Lambda blocks the deployment request if signature validation checks fail. If you set the policy to <code>Warn</code>, Lambda allows the deployment and issues a new Amazon CloudWatch metric (<code>SignatureValidationErrors</code>) and also stores the warning in the CloudTrail log.</p> <p>Default value: <code>Warn</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningPolicies) -> dict:
    out: dict = {}
    if "untrusted_artifact_on_deployment" in value:
        import aws_sdk_lambda.types.code_signing_policy

        out["UntrustedArtifactOnDeployment"] = (
            aws_sdk_lambda.types.code_signing_policy.serialize_json(
                value["untrusted_artifact_on_deployment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeSigningPolicies:
    out: CodeSigningPolicies = {}  # type: ignore[typeddict-item]
    if "UntrustedArtifactOnDeployment" in data:
        import aws_sdk_lambda.types.code_signing_policy

        out["untrusted_artifact_on_deployment"] = (
            aws_sdk_lambda.types.code_signing_policy.deserialize_json(
                data["UntrustedArtifactOnDeployment"]
            )
        )
    return out
