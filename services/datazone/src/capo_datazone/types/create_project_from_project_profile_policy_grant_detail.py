"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectFromProjectProfilePolicyGrantDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.project_profile_list


class CreateProjectFromProjectProfilePolicyGrantDetail(TypedDict, closed=True):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to include child domain units when creating a project from project profile policy grant details</p>"""
    project_profiles: NotRequired[
        "capo_datazone.types.project_profile_list.ProjectProfileList"
    ]
    """<p>Specifies project profiles when creating a project from project profile policy grant details</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectFromProjectProfilePolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    if "project_profiles" in value:
        import capo_datazone.types.project_profile_list

        out["projectProfiles"] = (
            capo_datazone.types.project_profile_list.serialize_json(
                value["project_profiles"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProjectFromProjectProfilePolicyGrantDetail:
    out: CreateProjectFromProjectProfilePolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    if "projectProfiles" in data:
        import capo_datazone.types.project_profile_list

        out["project_profiles"] = (
            capo_datazone.types.project_profile_list.deserialize_json(
                data["projectProfiles"]
            )
        )
    return out
