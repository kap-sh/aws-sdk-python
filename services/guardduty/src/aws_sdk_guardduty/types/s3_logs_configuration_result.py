"""Generated from Smithy shape ``com.amazonaws.guardduty#S3LogsConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.data_source_status


class S3LogsConfigurationResult(TypedDict):
    status: NotRequired["aws_sdk_guardduty.types.data_source_status.DataSourceStatus"]
    """<p>A value that describes whether S3 data event logs are automatically enabled for new members of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogsConfigurationResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> S3LogsConfigurationResult:
    out: S3LogsConfigurationResult = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_guardduty.types.data_source_status

        out["status"] = aws_sdk_guardduty.types.data_source_status.deserialize_json(
            data["status"]
        )
    return out
