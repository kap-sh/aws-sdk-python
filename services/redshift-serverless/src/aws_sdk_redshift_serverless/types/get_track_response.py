"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetTrackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.serverless_track


class GetTrackResponse(TypedDict, closed=True):
    track: NotRequired[
        "aws_sdk_redshift_serverless.types.serverless_track.ServerlessTrack"
    ]
    """<p>The version of the specified track.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrackResponse) -> dict:
    out: dict = {}
    if "track" in value:
        import aws_sdk_redshift_serverless.types.serverless_track

        out["track"] = (
            aws_sdk_redshift_serverless.types.serverless_track.serialize_aws_json_1_1(
                value["track"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrackResponse:
    out: GetTrackResponse = {}  # type: ignore[typeddict-item]
    if "track" in data:
        import aws_sdk_redshift_serverless.types.serverless_track

        out["track"] = (
            aws_sdk_redshift_serverless.types.serverless_track.deserialize_aws_json_1_1(
                data["track"]
            )
        )
    return out
