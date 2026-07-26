"""Generated from Smithy shape ``com.amazonaws.lightsail#GetKeyPairsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.key_pair_list
    import capo_lightsail.types.string


class GetKeyPairsResult(TypedDict, closed=True):
    key_pairs: NotRequired["capo_lightsail.types.key_pair_list.KeyPairList"]
    """<p>An array of key-value pairs containing information about the key pairs.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetKeyPairs</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPairsResult) -> dict:
    out: dict = {}
    if "key_pairs" in value:
        import capo_lightsail.types.key_pair_list

        out["keyPairs"] = capo_lightsail.types.key_pair_list.serialize_aws_json_1_1(
            value["key_pairs"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPairsResult:
    out: GetKeyPairsResult = {}  # type: ignore[typeddict-item]
    if "keyPairs" in data:
        import capo_lightsail.types.key_pair_list

        out["key_pairs"] = capo_lightsail.types.key_pair_list.deserialize_aws_json_1_1(
            data["keyPairs"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
