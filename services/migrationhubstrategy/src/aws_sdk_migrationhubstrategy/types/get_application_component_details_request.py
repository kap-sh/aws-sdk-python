"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetApplicationComponentDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_id


class GetApplicationComponentDetailsRequest(TypedDict):
    application_component_id: "aws_sdk_migrationhubstrategy.types.application_component_id.ApplicationComponentId"
    """<p> The ID of the application component. The ID is unique within an AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationComponentDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationComponentDetailsRequest:
    out: GetApplicationComponentDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
