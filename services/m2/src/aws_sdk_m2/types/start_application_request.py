"""Generated from Smithy shape ``com.amazonaws.m2#StartApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class StartApplicationRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartApplicationRequest:
    out: StartApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
