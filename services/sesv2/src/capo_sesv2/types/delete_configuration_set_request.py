"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name


class DeleteConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetRequest:
    out: DeleteConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    return out
