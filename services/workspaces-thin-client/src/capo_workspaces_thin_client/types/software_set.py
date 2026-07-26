"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.software_list
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_validation_status
    import capo_workspaces_thin_client.types.timestamp


class SoftwareSet(TypedDict, closed=True):
    id: NotRequired["capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"]
    """<p>The ID of the software set.</p>"""
    version: NotRequired["str"]
    """<p>The version of the software set.</p>"""
    released_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the software set was released.</p>"""
    supported_until: NotRequired[
        "capo_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the end of support for the software set.</p>"""
    validation_status: NotRequired[
        "capo_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus"
    ]
    """<p>An option to define if the software set has been validated.</p>"""
    software: NotRequired[
        "capo_workspaces_thin_client.types.software_list.SoftwareList"
    ]
    """<p>A list of the software components in the software set.</p>"""
    arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the software set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    if "released_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["releasedAt"] = capo_workspaces_thin_client.types.timestamp.serialize_json(
            value["released_at"]
        )
    if "supported_until" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["supportedUntil"] = (
            capo_workspaces_thin_client.types.timestamp.serialize_json(
                value["supported_until"]
            )
        )
    if "validation_status" in value:
        import capo_workspaces_thin_client.types.software_set_validation_status

        out["validationStatus"] = (
            capo_workspaces_thin_client.types.software_set_validation_status.serialize_json(
                value["validation_status"]
            )
        )
    if "software" in value:
        import capo_workspaces_thin_client.types.software_list

        out["software"] = (
            capo_workspaces_thin_client.types.software_list.serialize_json(
                value["software"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SoftwareSet:
    out: SoftwareSet = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "version" in data:
        out["version"] = data["version"]
    if "releasedAt" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["released_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["releasedAt"]
            )
        )
    if "supportedUntil" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["supported_until"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["supportedUntil"]
            )
        )
    if "validationStatus" in data:
        import capo_workspaces_thin_client.types.software_set_validation_status

        out["validation_status"] = (
            capo_workspaces_thin_client.types.software_set_validation_status.deserialize_json(
                data["validationStatus"]
            )
        )
    if "software" in data:
        import capo_workspaces_thin_client.types.software_list

        out["software"] = (
            capo_workspaces_thin_client.types.software_list.deserialize_json(
                data["software"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
