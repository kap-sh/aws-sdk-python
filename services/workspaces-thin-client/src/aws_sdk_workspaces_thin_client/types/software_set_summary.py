"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.arn
    import aws_sdk_workspaces_thin_client.types.software_set_id
    import aws_sdk_workspaces_thin_client.types.software_set_validation_status
    import aws_sdk_workspaces_thin_client.types.timestamp


class SoftwareSetSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set.</p>"""
    version: NotRequired["str"]
    """<p>The version of the software set.</p>"""
    released_at: NotRequired["aws_sdk_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the software set was released.</p>"""
    supported_until: NotRequired[
        "aws_sdk_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the end of support for the software set.</p>"""
    validation_status: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus"
    ]
    """<p>An option to define if the software set has been validated.</p>"""
    arn: NotRequired["aws_sdk_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the software set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    if "released_at" in value:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["releasedAt"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.serialize_json(
                value["released_at"]
            )
        )
    if "supported_until" in value:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["supportedUntil"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.serialize_json(
                value["supported_until"]
            )
        )
    if "validation_status" in value:
        import aws_sdk_workspaces_thin_client.types.software_set_validation_status

        out["validationStatus"] = (
            aws_sdk_workspaces_thin_client.types.software_set_validation_status.serialize_json(
                value["validation_status"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SoftwareSetSummary:
    out: SoftwareSetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "version" in data:
        out["version"] = data["version"]
    if "releasedAt" in data:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["released_at"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.deserialize_json(
                data["releasedAt"]
            )
        )
    if "supportedUntil" in data:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["supported_until"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.deserialize_json(
                data["supportedUntil"]
            )
        )
    if "validationStatus" in data:
        import aws_sdk_workspaces_thin_client.types.software_set_validation_status

        out["validation_status"] = (
            aws_sdk_workspaces_thin_client.types.software_set_validation_status.deserialize_json(
                data["validationStatus"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
