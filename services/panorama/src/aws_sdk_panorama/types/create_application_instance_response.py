"""Generated from Smithy shape ``com.amazonaws.panorama#CreateApplicationInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id


class CreateApplicationInstanceResponse(TypedDict):
    application_instance_id: (
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>The application instance's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationInstanceResponse) -> dict:
    out: dict = {}
    out["ApplicationInstanceId"] = value["application_instance_id"]
    return out


def deserialize_json(data: dict) -> CreateApplicationInstanceResponse:
    out: CreateApplicationInstanceResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationInstanceId" in data:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    else:
        raise DeserializationError(
            "CreateApplicationInstanceResponse.application_instance_id required"
        )
    return out
