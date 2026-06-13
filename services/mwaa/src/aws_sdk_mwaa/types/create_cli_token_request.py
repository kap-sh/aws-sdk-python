"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateCliTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_name


class CreateCliTokenRequest(TypedDict):
    name: "aws_sdk_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCliTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateCliTokenRequest:
    out: CreateCliTokenRequest = {}  # type: ignore[typeddict-item]
    return out
