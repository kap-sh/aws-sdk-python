"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListPublicKeysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.public_key_list


class ListPublicKeysResponse(TypedDict):
    public_keys: "aws_sdk_ivs_realtime.types.public_key_list.PublicKeyList"
    """<p>List of the matching public keys (summary information only).</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more public keys than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPublicKeysResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.public_key_list

    out["publicKeys"] = aws_sdk_ivs_realtime.types.public_key_list.serialize_json(
        value["public_keys"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPublicKeysResponse:
    out: ListPublicKeysResponse = {}  # type: ignore[typeddict-item]
    if "publicKeys" in data:
        import aws_sdk_ivs_realtime.types.public_key_list

        out["public_keys"] = (
            aws_sdk_ivs_realtime.types.public_key_list.deserialize_json(
                data["publicKeys"]
            )
        )
    else:
        raise DeserializationError("ListPublicKeysResponse.public_keys required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
