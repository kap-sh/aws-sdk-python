"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetComponentInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.component_id


class GetComponentInput(TypedDict):
    application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    component_id: "aws_sdk_ssm_sap.types.component_id.ComponentId"
    """<p>The ID of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    out["ComponentId"] = value["component_id"]
    return out


def deserialize_json(data: dict) -> GetComponentInput:
    out: GetComponentInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError("GetComponentInput.application_id required")
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    else:
        raise DeserializationError("GetComponentInput.component_id required")
    return out
