"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#GetSoftwareSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.software_set


class GetSoftwareSetResponse(TypedDict, closed=True):
    software_set: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set.SoftwareSet"
    ]
    """<p>Describes a software set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareSetResponse) -> dict:
    out: dict = {}
    if "software_set" in value:
        import aws_sdk_workspaces_thin_client.types.software_set

        out["softwareSet"] = (
            aws_sdk_workspaces_thin_client.types.software_set.serialize_json(
                value["software_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSoftwareSetResponse:
    out: GetSoftwareSetResponse = {}  # type: ignore[typeddict-item]
    if "softwareSet" in data:
        import aws_sdk_workspaces_thin_client.types.software_set

        out["software_set"] = (
            aws_sdk_workspaces_thin_client.types.software_set.deserialize_json(
                data["softwareSet"]
            )
        )
    return out
