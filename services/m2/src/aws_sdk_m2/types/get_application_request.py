"""Generated from Smithy shape ``com.amazonaws.m2#GetApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class GetApplicationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
