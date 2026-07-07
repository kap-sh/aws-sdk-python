"""Generated from Smithy shape ``com.amazonaws.ssmsap#DeregisterApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id


class DeregisterApplicationInput(TypedDict, closed=True):
    application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterApplicationInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> DeregisterApplicationInput:
    out: DeregisterApplicationInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError("DeregisterApplicationInput.application_id required")
    return out
