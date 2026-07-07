"""Generated from Smithy shape ``com.amazonaws.voiceid#Watchlist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.boolean
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.timestamp
    import aws_sdk_voice_id.types.watchlist_description
    import aws_sdk_voice_id.types.watchlist_id
    import aws_sdk_voice_id.types.watchlist_name


class Watchlist(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: NotRequired["aws_sdk_voice_id.types.watchlist_id.WatchlistId"]
    """<p>The identifier of the watchlist.</p>"""
    name: NotRequired["aws_sdk_voice_id.types.watchlist_name.WatchlistName"]
    """<p>The name for the watchlist.</p>"""
    description: NotRequired[
        "aws_sdk_voice_id.types.watchlist_description.WatchlistDescription"
    ]
    """<p>The description of the watchlist.</p>"""
    default_watchlist: "aws_sdk_voice_id.types.boolean.Boolean"
    """<p>Whether the specified watchlist is the default watchlist of a domain.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the watchlist was created.</p>"""
    updated_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the watchlist was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Watchlist) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "watchlist_id" in value:
        out["WatchlistId"] = value["watchlist_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["DefaultWatchlist"] = value.get("default_watchlist", False)
    if "created_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["CreatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["UpdatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Watchlist:
    out: Watchlist = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultWatchlist" in data:
        out["default_watchlist"] = data["DefaultWatchlist"]
    else:
        out["default_watchlist"] = False
    if "CreatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["created_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["updated_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    return out
