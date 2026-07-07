"""Generated from Smithy shape ``com.amazonaws.mwaa#DeleteEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_name


class DeleteEnvironmentInput(TypedDict, closed=True):
    name: "aws_sdk_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentInput:
    out: DeleteEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
