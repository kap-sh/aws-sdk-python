"""Generated from Smithy shape ``com.amazonaws.m2#DeleteApplicationFromEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class DeleteApplicationFromEnvironmentRequest(TypedDict, closed=True):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to delete.</p>"""
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment where the application was previously deployed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationFromEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationFromEnvironmentRequest:
    out: DeleteApplicationFromEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
