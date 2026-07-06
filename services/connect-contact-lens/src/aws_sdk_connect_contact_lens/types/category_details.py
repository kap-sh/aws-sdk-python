"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#CategoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.points_of_interest


class CategoryDetails(TypedDict, closed=True):
    points_of_interest: NotRequired[
        "aws_sdk_connect_contact_lens.types.points_of_interest.PointsOfInterest"
    ]
    """<p>The section of audio where the category rule was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryDetails) -> dict:
    out: dict = {}
    if "points_of_interest" in value:
        import aws_sdk_connect_contact_lens.types.points_of_interest

        out["PointsOfInterest"] = (
            aws_sdk_connect_contact_lens.types.points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryDetails:
    out: CategoryDetails = {}  # type: ignore[typeddict-item]
    if "PointsOfInterest" in data:
        import aws_sdk_connect_contact_lens.types.points_of_interest

        out["points_of_interest"] = (
            aws_sdk_connect_contact_lens.types.points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
