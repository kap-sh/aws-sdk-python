"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateIntegrationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_inspector2.types.update_git_hub_integration_detail
    import capo_inspector2.types.update_git_lab_self_managed_integration_detail


class _UpdateIntegrationDetails_gitlabSelfManaged(TypedDict, closed=True):
    gitlabSelfManaged: "capo_inspector2.types.update_git_lab_self_managed_integration_detail.UpdateGitLabSelfManagedIntegrationDetail"


class _UpdateIntegrationDetails_github(TypedDict, closed=True):
    github: "capo_inspector2.types.update_git_hub_integration_detail.UpdateGitHubIntegrationDetail"


UpdateIntegrationDetails: TypeAlias = (
    _UpdateIntegrationDetails_gitlabSelfManaged | _UpdateIntegrationDetails_github
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationDetails) -> dict:
    if "gitlabSelfManaged" in value:
        import capo_inspector2.types.update_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.update_git_lab_self_managed_integration_detail.serialize_json(
                value["gitlabSelfManaged"]
            )
        }
    elif "github" in value:
        import capo_inspector2.types.update_git_hub_integration_detail

        return {
            "github": capo_inspector2.types.update_git_hub_integration_detail.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("UpdateIntegrationDetails: no variant present")


def deserialize_json(data: dict) -> UpdateIntegrationDetails:
    if "gitlabSelfManaged" in data:
        import capo_inspector2.types.update_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.update_git_lab_self_managed_integration_detail.deserialize_json(
                data["gitlabSelfManaged"]
            )
        }
    elif "github" in data:
        import capo_inspector2.types.update_git_hub_integration_detail

        return {
            "github": capo_inspector2.types.update_git_hub_integration_detail.deserialize_json(
                data["github"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateIntegrationDetails: no recognized variant key"
        )
