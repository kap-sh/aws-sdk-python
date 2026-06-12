"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.report_name
    import aws_sdk_cost_and_usage_report_service.types.tag_list


class TagResourceRequest(TypedDict):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The report name of the report definition that tags are to be associated with.</p>"""
    tags: "aws_sdk_cost_and_usage_report_service.types.tag_list.TagList"
    """<p>The tags to be assigned to the report definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import aws_sdk_cost_and_usage_report_service.types.tag_list

    out["Tags"] = (
        aws_sdk_cost_and_usage_report_service.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("TagResourceRequest.report_name required")
    if "Tags" in data:
        import aws_sdk_cost_and_usage_report_service.types.tag_list

        out["tags"] = (
            aws_sdk_cost_and_usage_report_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
