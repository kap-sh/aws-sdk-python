"""Generated from Smithy shape ``com.amazonaws.guardduty#CloudTrailConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.data_source_status


class CloudTrailConfigurationResult(TypedDict):
    status: NotRequired["aws_sdk_guardduty.types.data_source_status.DataSourceStatus"]
    """<p>Describes whether CloudTrail is enabled as a data source for the detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudTrailConfigurationResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CloudTrailConfigurationResult:
    out: CloudTrailConfigurationResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.deserialize_json(
            data["status"]
        )
    return out
