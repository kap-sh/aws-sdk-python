"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesDnsLogsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsGuardDutyDetectorDataSourcesDnsLogsDetails(TypedDict, closed=True):
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Describes whether DNS logs is enabled as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDataSourcesDnsLogsDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDataSourcesDnsLogsDetails:
    out: AwsGuardDutyDetectorDataSourcesDnsLogsDetails = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
