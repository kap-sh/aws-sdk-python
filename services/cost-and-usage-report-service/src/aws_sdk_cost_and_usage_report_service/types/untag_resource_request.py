"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.report_name
    import aws_sdk_cost_and_usage_report_service.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The report name of the report definition that tags are to be disassociated from.</p>"""
    tag_keys: "aws_sdk_cost_and_usage_report_service.types.tag_key_list.TagKeyList"
    """<p>The tags to be disassociated from the report definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import aws_sdk_cost_and_usage_report_service.types.tag_key_list

    out["TagKeys"] = (
        aws_sdk_cost_and_usage_report_service.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("UntagResourceRequest.report_name required")
    if "TagKeys" in data:
        import aws_sdk_cost_and_usage_report_service.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_cost_and_usage_report_service.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
