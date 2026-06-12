"""Generated from Smithy shape ``com.amazonaws.polly#DescribeVoicesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.next_token
    import aws_sdk_polly.types.voice_list


class DescribeVoicesOutput(TypedDict):
    voices: NotRequired["aws_sdk_polly.types.voice_list.VoiceList"]
    """<p>A list of voices with their properties.</p>"""
    next_token: NotRequired["aws_sdk_polly.types.next_token.NextToken"]
    """<p>The pagination token to use in the next request to continue the listing of voices. <code>NextToken</code> is returned only if the response is truncated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVoicesOutput) -> dict:
    out: dict = {}
    if "voices" in value:
        import aws_sdk_polly.types.voice_list

        out["Voices"] = aws_sdk_polly.types.voice_list.serialize_json(value["voices"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeVoicesOutput:
    out: DescribeVoicesOutput = {}  # type: ignore[typeddict-item]
    if "Voices" in data:
        import aws_sdk_polly.types.voice_list

        out["voices"] = aws_sdk_polly.types.voice_list.deserialize_json(data["Voices"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
