"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateSoftwareSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_thin_client.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.software_set_id
    import aws_sdk_workspaces_thin_client.types.software_set_validation_status


class UpdateSoftwareSetRequest(TypedDict, closed=True):
    id: "aws_sdk_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    """<p>The ID of the software set to update.</p>"""
    validation_status: "aws_sdk_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus"
    """<p>An option to define if the software set has been validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSoftwareSetRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_thin_client.types.software_set_validation_status

    out["validationStatus"] = (
        aws_sdk_workspaces_thin_client.types.software_set_validation_status.serialize_json(
            value["validation_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSoftwareSetRequest:
    out: UpdateSoftwareSetRequest = {}  # type: ignore[typeddict-item]
    if "validationStatus" in data:
        import aws_sdk_workspaces_thin_client.types.software_set_validation_status

        out["validation_status"] = (
            aws_sdk_workspaces_thin_client.types.software_set_validation_status.deserialize_json(
                data["validationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSoftwareSetRequest.validation_status required"
        )
    return out
