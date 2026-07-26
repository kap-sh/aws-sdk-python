"""Generated from Smithy shape ``com.amazonaws.iot#ManagedJobTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.environments
    import capo_iot.types.job_description
    import capo_iot.types.job_template_arn
    import capo_iot.types.managed_job_template_name
    import capo_iot.types.managed_template_version


class ManagedJobTemplateSummary(TypedDict, closed=True):
    template_arn: NotRequired["capo_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The Amazon Resource Name (ARN) for a managed template.</p>"""
    template_name: NotRequired[
        "capo_iot.types.managed_job_template_name.ManagedJobTemplateName"
    ]
    """<p>The unique Name for a managed template.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>The description for a managed template.</p>"""
    environments: NotRequired["capo_iot.types.environments.Environments"]
    """<p>A list of environments that are supported with the managed job template.</p>"""
    template_version: NotRequired[
        "capo_iot.types.managed_template_version.ManagedTemplateVersion"
    ]
    """<p>The version for a managed template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedJobTemplateSummary) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "environments" in value:
        import capo_iot.types.environments

        out["environments"] = capo_iot.types.environments.serialize_json(
            value["environments"]
        )
    if "template_version" in value:
        out["templateVersion"] = value["template_version"]
    return out


def deserialize_json(data: dict) -> ManagedJobTemplateSummary:
    out: ManagedJobTemplateSummary = {}  # type: ignore[typeddict-item]
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "description" in data:
        out["description"] = data["description"]
    if "environments" in data:
        import capo_iot.types.environments

        out["environments"] = capo_iot.types.environments.deserialize_json(
            data["environments"]
        )
    if "templateVersion" in data:
        out["template_version"] = data["templateVersion"]
    return out
