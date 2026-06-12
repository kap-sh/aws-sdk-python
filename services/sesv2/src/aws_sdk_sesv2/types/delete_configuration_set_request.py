"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteConfigurationSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name


class DeleteConfigurationSetRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetRequest:
    out: DeleteConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    return out
