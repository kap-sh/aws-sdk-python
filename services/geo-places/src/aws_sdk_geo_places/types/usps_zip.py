"""Generated from Smithy shape ``com.amazonaws.geoplaces#UspsZip``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.zip_classification_code


class UspsZip(TypedDict, closed=True):
    zip_classification_code: NotRequired[
        "aws_sdk_geo_places.types.zip_classification_code.ZipClassificationCode"
    ]
    """<p>The ZIP Classification Code, or in other words what type of postal code is it. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UspsZip) -> dict:
    out: dict = {}
    if "zip_classification_code" in value:
        out["ZipClassificationCode"] = value["zip_classification_code"]
    return out


def deserialize_json(data: dict) -> UspsZip:
    out: UspsZip = {}  # type: ignore[typeddict-item]
    if "ZipClassificationCode" in data:
        out["zip_classification_code"] = data["ZipClassificationCode"]
    return out
