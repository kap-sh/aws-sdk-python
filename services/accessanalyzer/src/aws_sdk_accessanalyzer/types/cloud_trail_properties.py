"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CloudTrailProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.timestamp
    import aws_sdk_accessanalyzer.types.trail_properties_list


class CloudTrailProperties(TypedDict, closed=True):
    trail_properties: (
        "aws_sdk_accessanalyzer.types.trail_properties_list.TrailPropertiesList"
    )
    """<p>A <code>TrailProperties</code> object that contains settings for trail properties.</p>"""
    start_time: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.</p>"""
    end_time: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudTrailProperties) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.trail_properties_list

    out["trailProperties"] = (
        aws_sdk_accessanalyzer.types.trail_properties_list.serialize_json(
            value["trail_properties"]
        )
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["startTime"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["endTime"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> CloudTrailProperties:
    out: CloudTrailProperties = {}  # type: ignore[typeddict-item]
    if "trailProperties" in data:
        import aws_sdk_accessanalyzer.types.trail_properties_list

        out["trail_properties"] = (
            aws_sdk_accessanalyzer.types.trail_properties_list.deserialize_json(
                data["trailProperties"]
            )
        )
    else:
        raise DeserializationError("CloudTrailProperties.trail_properties required")
    if "startTime" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["start_time"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("CloudTrailProperties.start_time required")
    if "endTime" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["end_time"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("CloudTrailProperties.end_time required")
    return out
