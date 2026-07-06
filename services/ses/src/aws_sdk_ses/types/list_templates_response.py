"""Generated from Smithy shape ``com.amazonaws.ses#ListTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.next_token
    import aws_sdk_ses.types.template_metadata_list


class ListTemplatesResponse(TypedDict, closed=True):
    templates_metadata: NotRequired[
        "aws_sdk_ses.types.template_metadata_list.TemplateMetadataList"
    ]
    """<p>An array the contains the name and creation time stamp for each template in your Amazon SES account.</p>"""
    next_token: NotRequired["aws_sdk_ses.types.next_token.NextToken"]
    """<p>A token indicating that there are additional email templates available to be listed. Pass this token to a subsequent call to <code>ListTemplates</code> to retrieve the next set of email templates within your page size.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTemplatesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "templates_metadata" in value:
        import aws_sdk_ses.types.template_metadata_list

        aws_sdk_ses.types.template_metadata_list.serialize_query(
            value["templates_metadata"], pairs, f"{prefix}.TemplatesMetadata"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    child_templates_metadata = el.find("TemplatesMetadata")
    if child_templates_metadata is not None:
        import aws_sdk_ses.types.template_metadata_list

        out["templates_metadata"] = (
            aws_sdk_ses.types.template_metadata_list.deserialize_query(
                child_templates_metadata
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
