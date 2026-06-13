"""Generated from Smithy shape ``com.amazonaws.proton#UpdateTemplateSyncConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.subdirectory
    import aws_sdk_proton.types.template_type


class UpdateTemplateSyncConfigInput(TypedDict):
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The synced template name.</p>"""
    template_type: "aws_sdk_proton.types.template_type.TemplateType"
    """<p>The synced template type.</p>"""
    repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    repository_name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name (for example, <code>myrepos/myrepo</code>).</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch for your template.</p>"""
    subdirectory: NotRequired["aws_sdk_proton.types.subdirectory.Subdirectory"]
    """<p>A subdirectory path to your template bundle version. When included, limits the template bundle search to this repository directory.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTemplateSyncConfigInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    if "subdirectory" in value:
        out["subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTemplateSyncConfigInput:
    out: UpdateTemplateSyncConfigInput = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "UpdateTemplateSyncConfigInput.template_name required"
        )
    if "templateType" in data:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError(
            "UpdateTemplateSyncConfigInput.template_type required"
        )
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError(
            "UpdateTemplateSyncConfigInput.repository_provider required"
        )
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "UpdateTemplateSyncConfigInput.repository_name required"
        )
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("UpdateTemplateSyncConfigInput.branch required")
    if "subdirectory" in data:
        out["subdirectory"] = data["subdirectory"]
    return out
