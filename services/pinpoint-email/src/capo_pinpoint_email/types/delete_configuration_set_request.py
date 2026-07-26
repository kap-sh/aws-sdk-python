"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeleteConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name


class DeleteConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetRequest:
    out: DeleteConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    return out
