"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_repository_integration_arn
    import aws_sdk_inspector2.types.code_repository_project_name
    import aws_sdk_inspector2.types.code_repository_provider_type


class CodeRepositoryDetails(TypedDict, closed=True):
    project_name: NotRequired[
        "aws_sdk_inspector2.types.code_repository_project_name.CodeRepositoryProjectName"
    ]
    """<p>The name of the project in the code repository.</p>"""
    integration_arn: NotRequired[
        "aws_sdk_inspector2.types.code_repository_integration_arn.CodeRepositoryIntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the code security integration associated with the repository.</p>"""
    provider_type: NotRequired[
        "aws_sdk_inspector2.types.code_repository_provider_type.CodeRepositoryProviderType"
    ]
    """<p>The type of repository provider (such as GitHub, GitLab, etc.).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryDetails) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "integration_arn" in value:
        out["integrationArn"] = value["integration_arn"]
    if "provider_type" in value:
        out["providerType"] = value["provider_type"]
    return out


def deserialize_json(data: dict) -> CodeRepositoryDetails:
    out: CodeRepositoryDetails = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    if "providerType" in data:
        out["provider_type"] = data["providerType"]
    return out
