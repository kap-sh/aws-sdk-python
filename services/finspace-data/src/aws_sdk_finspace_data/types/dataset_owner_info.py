"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetOwnerInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.email
    import aws_sdk_finspace_data.types.owner_name
    import aws_sdk_finspace_data.types.phone_number


class DatasetOwnerInfo(TypedDict, closed=True):
    name: NotRequired["aws_sdk_finspace_data.types.owner_name.OwnerName"]
    """<p>The name of the Dataset owner.</p>"""
    phone_number: NotRequired["aws_sdk_finspace_data.types.phone_number.PhoneNumber"]
    """<p>Phone number for the Dataset owner.</p>"""
    email: NotRequired["aws_sdk_finspace_data.types.email.Email"]
    """<p>Email address for the Dataset owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetOwnerInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "phone_number" in value:
        out["phoneNumber"] = value["phone_number"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> DatasetOwnerInfo:
    out: DatasetOwnerInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    if "email" in data:
        out["email"] = data["email"]
    return out
