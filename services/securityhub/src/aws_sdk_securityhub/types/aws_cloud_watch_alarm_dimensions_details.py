"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudWatchAlarmDimensionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsCloudWatchAlarmDimensionsDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of a dimension. </p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of a dimension. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudWatchAlarmDimensionsDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsCloudWatchAlarmDimensionsDetails:
    out: AwsCloudWatchAlarmDimensionsDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
