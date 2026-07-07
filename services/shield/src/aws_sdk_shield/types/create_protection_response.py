"""Generated from Smithy shape ``com.amazonaws.shield#CreateProtectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_id


class CreateProtectionResponse(TypedDict, closed=True):
    protection_id: NotRequired["aws_sdk_shield.types.protection_id.ProtectionId"]
    """<p>The unique identifier (ID) for the <a>Protection</a> object that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProtectionResponse) -> dict:
    out: dict = {}
    if "protection_id" in value:
        out["ProtectionId"] = value["protection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProtectionResponse:
    out: CreateProtectionResponse = {}  # type: ignore[typeddict-item]
    if "ProtectionId" in data:
        out["protection_id"] = data["ProtectionId"]
    return out
