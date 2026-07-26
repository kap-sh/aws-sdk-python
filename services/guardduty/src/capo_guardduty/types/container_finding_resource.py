"""Generated from Smithy shape ``com.amazonaws.guardduty#ContainerFindingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.container_image_uid
    import capo_guardduty.types.string


class ContainerFindingResource(TypedDict, closed=True):
    image: NotRequired["capo_guardduty.types.string.String"]
    """<p>The container image information, including the image name and tag used to run the container that was involved in the finding.</p>"""
    image_uid: NotRequired["capo_guardduty.types.container_image_uid.ContainerImageUid"]
    """<p>The unique ID associated with the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerFindingResource) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "image_uid" in value:
        out["imageUid"] = value["image_uid"]
    return out


def deserialize_json(data: dict) -> ContainerFindingResource:
    out: ContainerFindingResource = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "imageUid" in data:
        out["image_uid"] = data["imageUid"]
    return out
