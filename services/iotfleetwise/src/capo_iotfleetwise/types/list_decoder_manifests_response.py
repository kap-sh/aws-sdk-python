"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListDecoderManifestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.decoder_manifest_summaries
    import capo_iotfleetwise.types.next_token


class ListDecoderManifestsResponse(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_iotfleetwise.types.decoder_manifest_summaries.decoderManifestSummaries"
    ]
    """<p> A list of information about each decoder manifest. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDecoderManifestsResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_iotfleetwise.types.decoder_manifest_summaries

        out["summaries"] = (
            capo_iotfleetwise.types.decoder_manifest_summaries.serialize_aws_json_1_0(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDecoderManifestsResponse:
    out: ListDecoderManifestsResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import capo_iotfleetwise.types.decoder_manifest_summaries

        out["summaries"] = (
            capo_iotfleetwise.types.decoder_manifest_summaries.deserialize_aws_json_1_0(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
