"""Generated from Smithy shape ``com.amazonaws.m2#GetApplicationVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.application_version_lifecycle
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.string_free65000
    import capo_m2.types.timestamp
    import capo_m2.types.version


class GetApplicationVersionResponse(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The name of the application version.</p>"""
    application_version: "capo_m2.types.version.Version"
    """<p>The specific version of the application.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The application description.</p>"""
    definition_content: "capo_m2.types.string_free65000.StringFree65000"
    """<p>The content of the application definition. This is a JSON object that contains the resource configuration and definitions that identify an application.</p>"""
    status: "capo_m2.types.application_version_lifecycle.ApplicationVersionLifecycle"
    """<p>The status of the application version.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the application version was created.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationVersionResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["applicationVersion"] = value["application_version"]
    if "description" in value:
        out["description"] = value["description"]
    out["definitionContent"] = value["definition_content"]
    out["status"] = value["status"]
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> GetApplicationVersionResponse:
    out: GetApplicationVersionResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetApplicationVersionResponse.name required")
    if "applicationVersion" in data:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError(
            "GetApplicationVersionResponse.application_version required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "definitionContent" in data:
        out["definition_content"] = data["definitionContent"]
    else:
        raise DeserializationError(
            "GetApplicationVersionResponse.definition_content required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetApplicationVersionResponse.status required")
    if "creationTime" in data:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetApplicationVersionResponse.creation_time required"
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
