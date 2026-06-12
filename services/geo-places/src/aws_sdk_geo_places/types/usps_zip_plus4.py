"""Generated from Smithy shape ``com.amazonaws.geoplaces#UspsZipPlus4``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.record_type_code


class UspsZipPlus4(TypedDict):
    record_type_code: NotRequired[
        "aws_sdk_geo_places.types.record_type_code.RecordTypeCode"
    ]
    """<p>The USPS ZIP+4 Record Type Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UspsZipPlus4) -> dict:
    out: dict = {}
    if "record_type_code" in value:
        out["RecordTypeCode"] = value["record_type_code"]
    return out


def deserialize_json(data: dict) -> UspsZipPlus4:
    out: UspsZipPlus4 = {}  # type: ignore[typeddict-item]
    if "RecordTypeCode" in data:
        out["record_type_code"] = data["RecordTypeCode"]
    return out
