"""Generated from Smithy shape ``com.amazonaws.iot#ListThingRegistrationTaskReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.report_type
    import capo_iot.types.s3_file_url_list


class ListThingRegistrationTaskReportsResponse(TypedDict, closed=True):
    resource_links: NotRequired["capo_iot.types.s3_file_url_list.S3FileUrlList"]
    """<p>Links to the task resources.</p>"""
    report_type: NotRequired["capo_iot.types.report_type.ReportType"]
    """<p>The type of task report.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingRegistrationTaskReportsResponse) -> dict:
    out: dict = {}
    if "resource_links" in value:
        import capo_iot.types.s3_file_url_list

        out["resourceLinks"] = capo_iot.types.s3_file_url_list.serialize_json(
            value["resource_links"]
        )
    if "report_type" in value:
        import capo_iot.types.report_type

        out["reportType"] = capo_iot.types.report_type.serialize_json(
            value["report_type"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingRegistrationTaskReportsResponse:
    out: ListThingRegistrationTaskReportsResponse = {}  # type: ignore[typeddict-item]
    if "resourceLinks" in data:
        import capo_iot.types.s3_file_url_list

        out["resource_links"] = capo_iot.types.s3_file_url_list.deserialize_json(
            data["resourceLinks"]
        )
    if "reportType" in data:
        import capo_iot.types.report_type

        out["report_type"] = capo_iot.types.report_type.deserialize_json(
            data["reportType"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
