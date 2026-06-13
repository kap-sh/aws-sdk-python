"""Generated from Smithy shape ``com.amazonaws.omics#GetConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.configuration_name


class GetConfigurationRequest(TypedDict):
    name: "aws_sdk_omics.types.configuration_name.ConfigurationName"
    """<p>Configuration name to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationRequest:
    out: GetConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
