"""Generated from Smithy shape ``com.amazonaws.m2#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.version


class UpdateApplicationResponse(TypedDict):
    application_version: "aws_sdk_m2.types.version.Version"
    """<p>The new version of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "applicationVersion" in data:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError(
            "UpdateApplicationResponse.application_version required"
        )
    return out
