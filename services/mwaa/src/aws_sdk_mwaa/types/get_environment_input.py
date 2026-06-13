"""Generated from Smithy shape ``com.amazonaws.mwaa#GetEnvironmentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_name


class GetEnvironmentInput(TypedDict):
    name: "aws_sdk_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentInput:
    out: GetEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
