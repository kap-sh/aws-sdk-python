"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateWebLoginTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_name

class CreateWebLoginTokenRequest(TypedDict):
    name: "aws_sdk_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateWebLoginTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateWebLoginTokenRequest:
    out: CreateWebLoginTokenRequest = {}  # type: ignore[typeddict-item]
    return out