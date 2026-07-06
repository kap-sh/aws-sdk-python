"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_id


class SecurityProfileItem(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.security_profile_id.SecurityProfileId"]
    """<p> Id of a security profile item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> SecurityProfileItem:
    out: SecurityProfileItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
