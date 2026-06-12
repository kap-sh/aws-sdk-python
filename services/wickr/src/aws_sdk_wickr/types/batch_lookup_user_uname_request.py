"""Generated from Smithy shape ``com.amazonaws.wickr#BatchLookupUserUnameRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.unames


class BatchLookupUserUnameRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the users will be looked up.</p>"""
    unames: "aws_sdk_wickr.types.unames.Unames"
    """<p>A list of username hashes (unames) to look up. Each uname is a unique identifier for a user's username. Maximum 50 unames per batch request.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchLookupUserUnameRequest) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.unames

    out["unames"] = aws_sdk_wickr.types.unames.serialize_json(value["unames"])
    return out


def deserialize_json(data: dict) -> BatchLookupUserUnameRequest:
    out: BatchLookupUserUnameRequest = {}  # type: ignore[typeddict-item]
    if "unames" in data:
        import aws_sdk_wickr.types.unames

        out["unames"] = aws_sdk_wickr.types.unames.deserialize_json(data["unames"])
    else:
        raise DeserializationError("BatchLookupUserUnameRequest.unames required")
    return out
