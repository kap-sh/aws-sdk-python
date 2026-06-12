"""Generated from Smithy shape ``com.amazonaws.m2#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.definition
    import aws_sdk_m2.types.entity_description
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.version


class UpdateApplicationRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to update.</p>"""
    description: NotRequired["aws_sdk_m2.types.entity_description.EntityDescription"]
    """<p>The description of the application to update.</p>"""
    current_application_version: "aws_sdk_m2.types.version.Version"
    """<p>The current version of the application to update.</p>"""
    definition: NotRequired["aws_sdk_m2.types.definition.Definition"]
    """<p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["currentApplicationVersion"] = value["current_application_version"]
    if "definition" in value:
        import aws_sdk_m2.types.definition

        out["definition"] = aws_sdk_m2.types.definition.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "currentApplicationVersion" in data:
        out["current_application_version"] = data["currentApplicationVersion"]
    else:
        raise DeserializationError(
            "UpdateApplicationRequest.current_application_version required"
        )
    if "definition" in data:
        import aws_sdk_m2.types.definition

        out["definition"] = aws_sdk_m2.types.definition.deserialize_json(
            data["definition"]
        )
    return out
