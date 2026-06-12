"""Generated from Smithy shape ``com.amazonaws.m2#ApplicationVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_version_lifecycle
    import aws_sdk_m2.types.timestamp
    import aws_sdk_m2.types.version


class ApplicationVersionSummary(TypedDict):
    application_version: "aws_sdk_m2.types.version.Version"
    """<p>The application version.</p>"""
    status: "aws_sdk_m2.types.application_version_lifecycle.ApplicationVersionLifecycle"
    """<p>The status of the application.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    creation_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the application version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationVersionSummary) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_m2.types.timestamp

    out["creationTime"] = aws_sdk_m2.types.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> ApplicationVersionSummary:
    out: ApplicationVersionSummary = {}  # type: ignore[typeddict-item]
    if "applicationVersion" in data:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError(
            "ApplicationVersionSummary.application_version required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ApplicationVersionSummary.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "creationTime" in data:
        import aws_sdk_m2.types.timestamp

        out["creation_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ApplicationVersionSummary.creation_time required")
    return out
