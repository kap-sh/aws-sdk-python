"""Generated from Smithy shape ``com.amazonaws.iot#GetRegistrationCodeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.registration_code


class GetRegistrationCodeResponse(TypedDict):
    registration_code: NotRequired[
        "aws_sdk_iot.types.registration_code.RegistrationCode"
    ]
    """<p>The CA certificate registration code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegistrationCodeResponse) -> dict:
    out: dict = {}
    if "registration_code" in value:
        out["registrationCode"] = value["registration_code"]
    return out


def deserialize_json(data: dict) -> GetRegistrationCodeResponse:
    out: GetRegistrationCodeResponse = {}  # type: ignore[typeddict-item]
    if "registrationCode" in data:
        out["registration_code"] = data["registrationCode"]
    return out
