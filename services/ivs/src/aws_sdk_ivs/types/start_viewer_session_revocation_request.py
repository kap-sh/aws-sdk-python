"""Generated from Smithy shape ``com.amazonaws.ivs#StartViewerSessionRevocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.viewer_id
    import aws_sdk_ivs.types.viewer_session_version


class StartViewerSessionRevocationRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>The ARN of the channel associated with the viewer session to revoke.</p>"""
    viewer_id: "aws_sdk_ivs.types.viewer_id.ViewerId"
    """<p>The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.</p>"""
    viewer_session_versions_less_than_or_equal_to: (
        "aws_sdk_ivs.types.viewer_session_version.ViewerSessionVersion"
    )
    """<p>An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartViewerSessionRevocationRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["viewerId"] = value["viewer_id"]
    out["viewerSessionVersionsLessThanOrEqualTo"] = value.get(
        "viewer_session_versions_less_than_or_equal_to", 0
    )
    return out


def deserialize_json(data: dict) -> StartViewerSessionRevocationRequest:
    out: StartViewerSessionRevocationRequest = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError(
            "StartViewerSessionRevocationRequest.channel_arn required"
        )
    if "viewerId" in data:
        out["viewer_id"] = data["viewerId"]
    else:
        raise DeserializationError(
            "StartViewerSessionRevocationRequest.viewer_id required"
        )
    if "viewerSessionVersionsLessThanOrEqualTo" in data:
        out["viewer_session_versions_less_than_or_equal_to"] = data[
            "viewerSessionVersionsLessThanOrEqualTo"
        ]
    else:
        out["viewer_session_versions_less_than_or_equal_to"] = 0
    return out
