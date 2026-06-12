"""Generated from Smithy shape ``com.amazonaws.finspacedata#Credentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_value_length1to2552
    import aws_sdk_finspace_data.types.string_value_max_length1000


class Credentials(TypedDict):
    access_key_id: NotRequired[
        "aws_sdk_finspace_data.types.string_value_length1to2552.StringValueLength1to2552"
    ]
    """<p>The access key identifier.</p>"""
    secret_access_key: NotRequired[
        "aws_sdk_finspace_data.types.string_value_max_length1000.stringValueMaxLength1000"
    ]
    """<p>The access key.</p>"""
    session_token: NotRequired[
        "aws_sdk_finspace_data.types.string_value_max_length1000.stringValueMaxLength1000"
    ]
    """<p>The session token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    return out
