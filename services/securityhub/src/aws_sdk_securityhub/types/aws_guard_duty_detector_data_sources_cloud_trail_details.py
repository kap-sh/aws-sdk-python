"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDataSourcesCloudTrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsGuardDutyDetectorDataSourcesCloudTrailDetails(TypedDict, closed=True):
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Specifies whether CloudTrail is activated as a data source for the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDataSourcesCloudTrailDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDataSourcesCloudTrailDetails:
    out: AwsGuardDutyDetectorDataSourcesCloudTrailDetails = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
