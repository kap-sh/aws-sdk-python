"""Generated from Smithy shape ``com.amazonaws.omics#DeleteConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.configuration_name


class DeleteConfigurationRequest(TypedDict, closed=True):
    name: "capo_omics.types.configuration_name.ConfigurationName"
    """<p>Configuration name to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationRequest:
    out: DeleteConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
