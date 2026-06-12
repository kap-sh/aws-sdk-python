"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.content_type_profile_config
    import aws_sdk_cloudfront.types.query_arg_profile_config
    import aws_sdk_cloudfront.types.string


class FieldLevelEncryptionConfig(TypedDict):
    caller_reference: "aws_sdk_cloudfront.types.string.string"
    """<p>A unique number that ensures the request can't be replayed.</p>"""
    comment: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>An optional comment about the configuration. The comment cannot be longer than 128 characters.</p>"""
    query_arg_profile_config: NotRequired[
        "aws_sdk_cloudfront.types.query_arg_profile_config.QueryArgProfileConfig"
    ]
    """<p>A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.</p>"""
    content_type_profile_config: NotRequired[
        "aws_sdk_cloudfront.types.content_type_profile_config.ContentTypeProfileConfig"
    ]
    """<p>A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FieldLevelEncryptionConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    if "query_arg_profile_config" in value:
        import aws_sdk_cloudfront.types.query_arg_profile_config

        aws_sdk_cloudfront.types.query_arg_profile_config.serialize_xml(
            value["query_arg_profile_config"], el, "QueryArgProfileConfig"
        )
    if "content_type_profile_config" in value:
        import aws_sdk_cloudfront.types.content_type_profile_config

        aws_sdk_cloudfront.types.content_type_profile_config.serialize_xml(
            value["content_type_profile_config"], el, "ContentTypeProfileConfig"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionConfig:
    out: FieldLevelEncryptionConfig = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError(
            "FieldLevelEncryptionConfig.caller_reference required"
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_query_arg_profile_config = el.find("QueryArgProfileConfig")
    if child_query_arg_profile_config is not None:
        import aws_sdk_cloudfront.types.query_arg_profile_config

        out["query_arg_profile_config"] = (
            aws_sdk_cloudfront.types.query_arg_profile_config.deserialize_xml(
                child_query_arg_profile_config
            )
        )
    child_content_type_profile_config = el.find("ContentTypeProfileConfig")
    if child_content_type_profile_config is not None:
        import aws_sdk_cloudfront.types.content_type_profile_config

        out["content_type_profile_config"] = (
            aws_sdk_cloudfront.types.content_type_profile_config.deserialize_xml(
                child_content_type_profile_config
            )
        )
    return out
