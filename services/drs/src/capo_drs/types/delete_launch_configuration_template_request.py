"""Generated from Smithy shape ``com.amazonaws.drs#DeleteLaunchConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.launch_configuration_template_id


class DeleteLaunchConfigurationTemplateRequest(TypedDict, closed=True):
    launch_configuration_template_id: (
        "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    )
    """<p>The ID of the Launch Configuration Template to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLaunchConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    return out


def deserialize_json(data: dict) -> DeleteLaunchConfigurationTemplateRequest:
    out: DeleteLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateID" in data:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        raise DeserializationError(
            "DeleteLaunchConfigurationTemplateRequest.launch_configuration_template_id required"
        )
    return out
