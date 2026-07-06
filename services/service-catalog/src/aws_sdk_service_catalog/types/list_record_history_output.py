"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListRecordHistoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.record_details


class ListRecordHistoryOutput(TypedDict, closed=True):
    record_details: NotRequired[
        "aws_sdk_service_catalog.types.record_details.RecordDetails"
    ]
    """<p>The records, in reverse chronological order.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecordHistoryOutput) -> dict:
    out: dict = {}
    if "record_details" in value:
        import aws_sdk_service_catalog.types.record_details

        out["RecordDetails"] = (
            aws_sdk_service_catalog.types.record_details.serialize_aws_json_1_1(
                value["record_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecordHistoryOutput:
    out: ListRecordHistoryOutput = {}  # type: ignore[typeddict-item]
    if "RecordDetails" in data:
        import aws_sdk_service_catalog.types.record_details

        out["record_details"] = (
            aws_sdk_service_catalog.types.record_details.deserialize_aws_json_1_1(
                data["RecordDetails"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
