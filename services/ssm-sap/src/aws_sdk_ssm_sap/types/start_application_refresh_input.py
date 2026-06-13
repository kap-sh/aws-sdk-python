"""Generated from Smithy shape ``com.amazonaws.ssmsap#StartApplicationRefreshInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id


class StartApplicationRefreshInput(TypedDict):
    application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApplicationRefreshInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> StartApplicationRefreshInput:
    out: StartApplicationRefreshInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "StartApplicationRefreshInput.application_id required"
        )
    return out
