"""Generated from Smithy shape ``com.amazonaws.artifact#ReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.acceptance_type
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.published_state
    import capo_artifact.types.report_id
    import capo_artifact.types.short_string_attribute
    import capo_artifact.types.status_message
    import capo_artifact.types.timestamp_attribute
    import capo_artifact.types.upload_state
    import capo_artifact.types.version_attribute


class ReportSummary(TypedDict, closed=True):
    id: NotRequired["capo_artifact.types.report_id.ReportId"]
    """<p>Unique resource ID for the report resource.</p>"""
    name: NotRequired["capo_artifact.types.short_string_attribute.ShortStringAttribute"]
    """<p>Name for the report resource.</p>"""
    state: NotRequired["capo_artifact.types.published_state.PublishedState"]
    """<p>Current state of the report resource.</p>"""
    arn: NotRequired["capo_artifact.types.long_string_attribute.LongStringAttribute"]
    """<p>ARN for the report resource.</p>"""
    version: NotRequired["capo_artifact.types.version_attribute.VersionAttribute"]
    """<p>Version for the report resource.</p>"""
    upload_state: NotRequired["capo_artifact.types.upload_state.UploadState"]
    """<p>The current state of the document upload.</p>"""
    description: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Description for the report resource.</p>"""
    period_start: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective start.</p>"""
    period_end: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective end.</p>"""
    series: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Series for the report resource.</p>"""
    category: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Category for the report resource.</p>"""
    company_name: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated company name for the report resource.</p>"""
    product_name: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated product name for the report resource.</p>"""
    status_message: NotRequired["capo_artifact.types.status_message.StatusMessage"]
    """<p>The message associated with the current upload state.</p>"""
    acceptance_type: NotRequired["capo_artifact.types.acceptance_type.AcceptanceType"]
    """<p>Acceptance type for report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "state" in value:
        import capo_artifact.types.published_state

        out["state"] = capo_artifact.types.published_state.serialize_json(
            value["state"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "upload_state" in value:
        import capo_artifact.types.upload_state

        out["uploadState"] = capo_artifact.types.upload_state.serialize_json(
            value["upload_state"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "period_start" in value:
        import capo_artifact.types.timestamp_attribute

        out["periodStart"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["period_start"]
        )
    if "period_end" in value:
        import capo_artifact.types.timestamp_attribute

        out["periodEnd"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["period_end"]
        )
    if "series" in value:
        out["series"] = value["series"]
    if "category" in value:
        out["category"] = value["category"]
    if "company_name" in value:
        out["companyName"] = value["company_name"]
    if "product_name" in value:
        out["productName"] = value["product_name"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "acceptance_type" in value:
        import capo_artifact.types.acceptance_type

        out["acceptanceType"] = capo_artifact.types.acceptance_type.serialize_json(
            value["acceptance_type"]
        )
    return out


def deserialize_json(data: dict) -> ReportSummary:
    out: ReportSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        import capo_artifact.types.published_state

        out["state"] = capo_artifact.types.published_state.deserialize_json(
            data["state"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "version" in data:
        out["version"] = data["version"]
    if "uploadState" in data:
        import capo_artifact.types.upload_state

        out["upload_state"] = capo_artifact.types.upload_state.deserialize_json(
            data["uploadState"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "periodStart" in data:
        import capo_artifact.types.timestamp_attribute

        out["period_start"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["periodStart"]
        )
    if "periodEnd" in data:
        import capo_artifact.types.timestamp_attribute

        out["period_end"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["periodEnd"]
        )
    if "series" in data:
        out["series"] = data["series"]
    if "category" in data:
        out["category"] = data["category"]
    if "companyName" in data:
        out["company_name"] = data["companyName"]
    if "productName" in data:
        out["product_name"] = data["productName"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "acceptanceType" in data:
        import capo_artifact.types.acceptance_type

        out["acceptance_type"] = capo_artifact.types.acceptance_type.deserialize_json(
            data["acceptanceType"]
        )
    return out
