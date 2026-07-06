"""Generated from Smithy shape ``com.amazonaws.sesv2#GetConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name


class GetConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationSetRequest:
    out: GetConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    return out
