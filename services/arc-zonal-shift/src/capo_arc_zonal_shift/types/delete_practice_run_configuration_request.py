"""Generated from Smithy shape ``com.amazonaws.arczonalshift#DeletePracticeRunConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.resource_identifier


class DeletePracticeRunConfigurationRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you want to delete the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePracticeRunConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePracticeRunConfigurationRequest:
    out: DeletePracticeRunConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
