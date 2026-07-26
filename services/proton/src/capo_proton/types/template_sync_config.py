"""Generated from Smithy shape ``com.amazonaws.proton#TemplateSyncConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.resource_name
    import capo_proton.types.subdirectory
    import capo_proton.types.template_type


class TemplateSyncConfig(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The template name.</p>"""
    template_type: "capo_proton.types.template_type.TemplateType"
    """<p>The template type.</p>"""
    repository_provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    repository_name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name (for example, <code>myrepos/myrepo</code>).</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""
    subdirectory: NotRequired["capo_proton.types.subdirectory.Subdirectory"]
    """<p>A subdirectory path to your template bundle version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TemplateSyncConfig) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    if "subdirectory" in value:
        out["subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TemplateSyncConfig:
    out: TemplateSyncConfig = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("TemplateSyncConfig.template_name required")
    if "templateType" in data:
        out["template_type"] = data["templateType"]
    else:
        raise DeserializationError("TemplateSyncConfig.template_type required")
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError("TemplateSyncConfig.repository_provider required")
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("TemplateSyncConfig.repository_name required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("TemplateSyncConfig.branch required")
    if "subdirectory" in data:
        out["subdirectory"] = data["subdirectory"]
    return out
