"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class GetApplicationRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
