"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.destination
    import aws_sdk_ses.types.message_tag_list
    import aws_sdk_ses.types.template_data


class BulkEmailDestination(TypedDict):
    destination: "aws_sdk_ses.types.destination.Destination"
    replacement_tags: NotRequired["aws_sdk_ses.types.message_tag_list.MessageTagList"]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using <code>SendBulkTemplatedEmail</code>. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>"""
    replacement_template_data: NotRequired[
        "aws_sdk_ses.types.template_data.TemplateData"
    ]
    """<p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BulkEmailDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.destination

    aws_sdk_ses.types.destination.serialize_query(
        value["destination"], pairs, f"{prefix}.Destination"
    )
    if "replacement_tags" in value:
        import aws_sdk_ses.types.message_tag_list

        aws_sdk_ses.types.message_tag_list.serialize_query(
            value["replacement_tags"], pairs, f"{prefix}.ReplacementTags"
        )
    if "replacement_template_data" in value:
        pairs.append(
            (
                f"{prefix}.ReplacementTemplateData",
                str(value["replacement_template_data"]),
            )
        )


def deserialize_query(el: Element) -> BulkEmailDestination:
    out: BulkEmailDestination = {}  # type: ignore[typeddict-item]
    child_destination = el.find("Destination")
    if child_destination is not None:
        import aws_sdk_ses.types.destination

        out["destination"] = aws_sdk_ses.types.destination.deserialize_query(
            child_destination
        )
    else:
        raise DeserializationError("BulkEmailDestination.destination required")
    child_replacement_tags = el.find("ReplacementTags")
    if child_replacement_tags is not None:
        import aws_sdk_ses.types.message_tag_list

        out["replacement_tags"] = aws_sdk_ses.types.message_tag_list.deserialize_query(
            child_replacement_tags
        )
    child_replacement_template_data = el.find("ReplacementTemplateData")
    if child_replacement_template_data is not None:
        out["replacement_template_data"] = str(
            child_replacement_template_data.text or ""
        )
    return out
