"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_status
    import aws_sdk_drs.types.participating_resource_id


class ParticipatingResource(TypedDict):
    participating_resource_id: NotRequired[
        "aws_sdk_drs.types.participating_resource_id.ParticipatingResourceID"
    ]
    """<p>The ID of a participating resource.</p>"""
    launch_status: NotRequired["aws_sdk_drs.types.launch_status.LaunchStatus"]
    """<p>The launch status of a participating resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingResource) -> dict:
    out: dict = {}
    if "participating_resource_id" in value:
        import aws_sdk_drs.types.participating_resource_id

        out["participatingResourceID"] = (
            aws_sdk_drs.types.participating_resource_id.serialize_json(
                value["participating_resource_id"]
            )
        )
    if "launch_status" in value:
        out["launchStatus"] = value["launch_status"]
    return out


def deserialize_json(data: dict) -> ParticipatingResource:
    out: ParticipatingResource = {}  # type: ignore[typeddict-item]
    if "participatingResourceID" in data:
        import aws_sdk_drs.types.participating_resource_id

        out["participating_resource_id"] = (
            aws_sdk_drs.types.participating_resource_id.deserialize_json(
                data["participatingResourceID"]
            )
        )
    if "launchStatus" in data:
        out["launch_status"] = data["launchStatus"]
    return out
