"""Generated from Smithy shape ``com.amazonaws.sesv2#ListEmailTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_metadata_list
    import aws_sdk_sesv2.types.next_token


class ListEmailTemplatesResponse(TypedDict):
    templates_metadata: NotRequired[
        "aws_sdk_sesv2.types.email_template_metadata_list.EmailTemplateMetadataList"
    ]
    """<p>An array the contains the name and creation time stamp for each template in your Amazon SES account.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token indicating that there are additional email templates available to be listed. Pass this token to a subsequent <code>ListEmailTemplates</code> call to retrieve the next 10 email templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailTemplatesResponse) -> dict:
    out: dict = {}
    if "templates_metadata" in value:
        import aws_sdk_sesv2.types.email_template_metadata_list

        out["TemplatesMetadata"] = (
            aws_sdk_sesv2.types.email_template_metadata_list.serialize_json(
                value["templates_metadata"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEmailTemplatesResponse:
    out: ListEmailTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "TemplatesMetadata" in data:
        import aws_sdk_sesv2.types.email_template_metadata_list

        out["templates_metadata"] = (
            aws_sdk_sesv2.types.email_template_metadata_list.deserialize_json(
                data["TemplatesMetadata"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
