"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetTrackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.track_name


class GetTrackRequest(TypedDict, closed=True):
    track_name: "aws_sdk_redshift_serverless.types.track_name.TrackName"
    """<p>The name of the track of which its version is fetched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrackRequest) -> dict:
    out: dict = {}
    out["trackName"] = value["track_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrackRequest:
    out: GetTrackRequest = {}  # type: ignore[typeddict-item]
    if "trackName" in data:
        out["track_name"] = data["trackName"]
    else:
        raise DeserializationError("GetTrackRequest.track_name required")
    return out
