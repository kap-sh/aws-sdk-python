"""Generated from Smithy shape ``com.amazonaws.securityhub#CodeRepositoryDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class CodeRepositoryDetails(TypedDict):
    provider_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of repository provider. </p>"""
    project_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the project in the code repository. </p>"""
    code_security_integration_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the code security integration associated with the repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryDetails) -> dict:
    out: dict = {}
    if "provider_type" in value:
        out["ProviderType"] = value["provider_type"]
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "code_security_integration_arn" in value:
        out["CodeSecurityIntegrationArn"] = value["code_security_integration_arn"]
    return out


def deserialize_json(data: dict) -> CodeRepositoryDetails:
    out: CodeRepositoryDetails = {}  # type: ignore[typeddict-item]
    if "ProviderType" in data:
        out["provider_type"] = data["ProviderType"]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "CodeSecurityIntegrationArn" in data:
        out["code_security_integration_arn"] = data["CodeSecurityIntegrationArn"]
    return out
