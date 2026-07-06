"""Generated from Smithy shape ``com.amazonaws.m2#GetApplicationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.version


class GetApplicationVersionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    application_version: "aws_sdk_m2.types.version.Version"
    """<p>The specific version of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationVersionRequest:
    out: GetApplicationVersionRequest = {}  # type: ignore[typeddict-item]
    return out
