"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordIamCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.iam_role_arn
    import capo_bedrock_agentcore_control.types.iam_signing_region
    import capo_bedrock_agentcore_control.types.iam_signing_service_name


class RegistryRecordIamCredentialProvider(TypedDict, closed=True):
    role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for SigV4 signing.</p>"""
    service: NotRequired[
        "capo_bedrock_agentcore_control.types.iam_signing_service_name.IamSigningServiceName"
    ]
    """<p>The SigV4 signing service name (for example, <code>execute-api</code> or <code>bedrock-agentcore</code>).</p>"""
    region: NotRequired[
        "capo_bedrock_agentcore_control.types.iam_signing_region.IamSigningRegion"
    ]
    """<p>The Amazon Web Services region for SigV4 signing (for example, <code>us-west-2</code>). If not specified, the region is extracted from the MCP server URL hostname, with fallback to the service's own region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordIamCredentialProvider) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "service" in value:
        out["service"] = value["service"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RegistryRecordIamCredentialProvider:
    out: RegistryRecordIamCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out
