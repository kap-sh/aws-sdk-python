"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.long
    import aws_sdk_appsync.types.string


class ApiKey(TypedDict, closed=True):
    id: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The API key ID.</p>"""
    description: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>A description of the purpose of the API key.</p>"""
    expires: "aws_sdk_appsync.types.long.Long"
    """<p>The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.</p>"""
    deletes: "aws_sdk_appsync.types.long.Long"
    """<p>The time after which the API key is deleted. The date is represented as seconds since the epoch, rounded down to the nearest hour.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKey) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    out["expires"] = value.get("expires", 0)
    out["deletes"] = value.get("deletes", 0)
    return out


def deserialize_json(data: dict) -> ApiKey:
    out: ApiKey = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "expires" in data:
        out["expires"] = data["expires"]
    else:
        out["expires"] = 0
    if "deletes" in data:
        out["deletes"] = data["deletes"]
    else:
        out["deletes"] = 0
    return out
