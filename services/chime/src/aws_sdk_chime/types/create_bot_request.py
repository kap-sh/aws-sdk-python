"""Generated from Smithy shape ``com.amazonaws.chime#CreateBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.sensitive_string


class CreateBotRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    display_name: "aws_sdk_chime.types.sensitive_string.SensitiveString"
    """<p>The bot display name.</p>"""
    domain: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The domain of the Amazon Chime Enterprise account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotRequest) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> CreateBotRequest:
    out: CreateBotRequest = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("CreateBotRequest.display_name required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    return out
