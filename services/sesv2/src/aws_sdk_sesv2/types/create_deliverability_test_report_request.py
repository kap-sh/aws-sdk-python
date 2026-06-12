"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateDeliverabilityTestReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.email_content
    import aws_sdk_sesv2.types.report_name
    import aws_sdk_sesv2.types.tag_list


class CreateDeliverabilityTestReportRequest(TypedDict):
    report_name: NotRequired["aws_sdk_sesv2.types.report_name.ReportName"]
    """<p>A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.</p>"""
    from_email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The email address that the predictive inbox placement test email was sent from.</p>"""
    content: "aws_sdk_sesv2.types.email_content.EmailContent"
    """<p>The HTML body of the message that you sent when you performed the predictive inbox placement test.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeliverabilityTestReportRequest) -> dict:
    out: dict = {}
    if "report_name" in value:
        out["ReportName"] = value["report_name"]
    out["FromEmailAddress"] = value["from_email_address"]
    import aws_sdk_sesv2.types.email_content

    out["Content"] = aws_sdk_sesv2.types.email_content.serialize_json(value["content"])
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDeliverabilityTestReportRequest:
    out: CreateDeliverabilityTestReportRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    if "FromEmailAddress" in data:
        out["from_email_address"] = data["FromEmailAddress"]
    else:
        raise DeserializationError(
            "CreateDeliverabilityTestReportRequest.from_email_address required"
        )
    if "Content" in data:
        import aws_sdk_sesv2.types.email_content

        out["content"] = aws_sdk_sesv2.types.email_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError(
            "CreateDeliverabilityTestReportRequest.content required"
        )
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
