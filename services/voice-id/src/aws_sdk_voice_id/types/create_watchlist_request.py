"""Generated from Smithy shape ``com.amazonaws.voiceid#CreateWatchlistRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.client_token_string
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.watchlist_description
    import aws_sdk_voice_id.types.watchlist_name


class CreateWatchlistRequest(TypedDict):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    name: "aws_sdk_voice_id.types.watchlist_name.WatchlistName"
    """<p>The name of the watchlist.</p>"""
    description: NotRequired[
        "aws_sdk_voice_id.types.watchlist_description.WatchlistDescription"
    ]
    """<p>A brief description of this watchlist.</p>"""
    client_token: NotRequired[
        "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWatchlistRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWatchlistRequest:
    out: CreateWatchlistRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("CreateWatchlistRequest.domain_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateWatchlistRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
