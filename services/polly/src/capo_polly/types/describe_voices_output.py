"""Generated from Smithy shape ``com.amazonaws.polly#DescribeVoicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.next_token
    import capo_polly.types.voice_list


class DescribeVoicesOutput(TypedDict, closed=True):
    voices: NotRequired["capo_polly.types.voice_list.VoiceList"]
    """<p>A list of voices with their properties.</p>"""
    next_token: NotRequired["capo_polly.types.next_token.NextToken"]
    """<p>The pagination token to use in the next request to continue the listing of voices. <code>NextToken</code> is returned only if the response is truncated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVoicesOutput) -> dict:
    out: dict = {}
    if "voices" in value:
        import capo_polly.types.voice_list

        out["Voices"] = capo_polly.types.voice_list.serialize_json(value["voices"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeVoicesOutput:
    out: DescribeVoicesOutput = {}  # type: ignore[typeddict-item]
    if "Voices" in data:
        import capo_polly.types.voice_list

        out["voices"] = capo_polly.types.voice_list.deserialize_json(data["Voices"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
