"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceContributor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.long


class SpaceContributor(TypedDict, closed=True):
    user_name: NotRequired["str"]
    """<p>The user name of the contributor.</p>"""
    raw_file_size_bytes: "capo_quicksight.types.long.Long"
    """<p>The raw file size in bytes contributed by the user.</p>"""
    percentage: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The percentage of total contributions made by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceContributor) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    out["rawFileSizeBytes"] = value["raw_file_size_bytes"]
    if "percentage" in value:
        out["percentage"] = value["percentage"]
    return out


def deserialize_json(data: dict) -> SpaceContributor:
    out: SpaceContributor = {}  # type: ignore[typeddict-item]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "rawFileSizeBytes" in data:
        out["raw_file_size_bytes"] = data["rawFileSizeBytes"]
    else:
        raise DeserializationError("SpaceContributor.raw_file_size_bytes required")
    if "percentage" in data:
        out["percentage"] = data["percentage"]
    return out
