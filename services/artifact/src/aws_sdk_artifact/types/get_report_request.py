"""Generated from Smithy shape ``com.amazonaws.artifact#GetReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_artifact.types.report_id
    import aws_sdk_artifact.types.short_string_attribute
    import aws_sdk_artifact.types.version_attribute


class GetReportRequest(TypedDict):
    report_id: "aws_sdk_artifact.types.report_id.ReportId"
    """<p>Unique resource ID for the report resource.</p>"""
    report_version: NotRequired[
        "aws_sdk_artifact.types.version_attribute.VersionAttribute"
    ]
    """<p>Version for the report resource.</p>"""
    term_token: "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    """<p>Unique download token provided by GetTermForReport API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReportRequest:
    out: GetReportRequest = {}  # type: ignore[typeddict-item]
    return out
