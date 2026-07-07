"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CloudTrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.role_arn
    import aws_sdk_accessanalyzer.types.timestamp
    import aws_sdk_accessanalyzer.types.trail_list


class CloudTrailDetails(TypedDict, closed=True):
    trails: "aws_sdk_accessanalyzer.types.trail_list.TrailList"
    """<p>A <code>Trail</code> object that contains settings for a trail.</p>"""
    access_role: "aws_sdk_accessanalyzer.types.role_arn.RoleArn"
    """<p>The ARN of the service role that IAM Access Analyzer uses to access your CloudTrail trail and service last accessed information.</p>"""
    start_time: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.</p>"""
    end_time: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudTrailDetails) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.trail_list

    out["trails"] = aws_sdk_accessanalyzer.types.trail_list.serialize_json(
        value["trails"]
    )
    out["accessRole"] = value["access_role"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["startTime"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["endTime"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> CloudTrailDetails:
    out: CloudTrailDetails = {}  # type: ignore[typeddict-item]
    if "trails" in data:
        import aws_sdk_accessanalyzer.types.trail_list

        out["trails"] = aws_sdk_accessanalyzer.types.trail_list.deserialize_json(
            data["trails"]
        )
    else:
        raise DeserializationError("CloudTrailDetails.trails required")
    if "accessRole" in data:
        out["access_role"] = data["accessRole"]
    else:
        raise DeserializationError("CloudTrailDetails.access_role required")
    if "startTime" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["start_time"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("CloudTrailDetails.start_time required")
    if "endTime" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["end_time"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["endTime"]
        )
    return out
