"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TrackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.serverless_track

TrackList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.serverless_track.ServerlessTrack"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrackList) -> list:
    import aws_sdk_redshift_serverless.types.serverless_track

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.serverless_track.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrackList:
    import aws_sdk_redshift_serverless.types.serverless_track

    out: TrackList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.serverless_track.deserialize_aws_json_1_1(
                item
            )
        )
    return out
