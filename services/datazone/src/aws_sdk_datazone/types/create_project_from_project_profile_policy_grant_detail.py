"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectFromProjectProfilePolicyGrantDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_profile_list


class CreateProjectFromProjectProfilePolicyGrantDetail(TypedDict):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to include child domain units when creating a project from project profile policy grant details</p>"""
    project_profiles: NotRequired[
        "aws_sdk_datazone.types.project_profile_list.ProjectProfileList"
    ]
    """<p>Specifies project profiles when creating a project from project profile policy grant details</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectFromProjectProfilePolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    if "project_profiles" in value:
        import aws_sdk_datazone.types.project_profile_list

        out["projectProfiles"] = (
            aws_sdk_datazone.types.project_profile_list.serialize_json(
                value["project_profiles"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProjectFromProjectProfilePolicyGrantDetail:
    out: CreateProjectFromProjectProfilePolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    if "projectProfiles" in data:
        import aws_sdk_datazone.types.project_profile_list

        out["project_profiles"] = (
            aws_sdk_datazone.types.project_profile_list.deserialize_json(
                data["projectProfiles"]
            )
        )
    return out
