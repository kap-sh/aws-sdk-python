"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.aliases
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.price_class
    import aws_sdk_cloudfront.types.s3_origin
    import aws_sdk_cloudfront.types.streaming_logging_config
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.trusted_signers


class StreamingDistributionConfig(TypedDict, closed=True):
    caller_reference: "aws_sdk_cloudfront.types.string.string"
    """<p>A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.</p> <p>If the value of <code>CallerReference</code> is new (regardless of the content of the <code>StreamingDistributionConfig</code> object), CloudFront creates a new distribution.</p> <p>If <code>CallerReference</code> is a value that you already sent in a previous request to create a distribution, CloudFront returns a <code>DistributionAlreadyExists</code> error.</p>"""
    s3_origin: "aws_sdk_cloudfront.types.s3_origin.S3Origin"
    """<p>A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.</p>"""
    aliases: NotRequired["aws_sdk_cloudfront.types.aliases.Aliases"]
    """<p>A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.</p>"""
    comment: "aws_sdk_cloudfront.types.string.string"
    """<p>Any comments you want to include about the streaming distribution.</p>"""
    logging: NotRequired[
        "aws_sdk_cloudfront.types.streaming_logging_config.StreamingLoggingConfig"
    ]
    """<p>A complex type that controls whether access logs are written for the streaming distribution.</p>"""
    trusted_signers: "aws_sdk_cloudfront.types.trusted_signers.TrustedSigners"
    r"""<p>A complex type that specifies any Amazon Web Services accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    price_class: NotRequired["aws_sdk_cloudfront.types.price_class.PriceClass"]
    """<p>A complex type that contains information about price class for this streaming distribution.</p>"""
    enabled: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>Whether the streaming distribution is enabled to accept user requests for content.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    import aws_sdk_cloudfront.types.s3_origin

    aws_sdk_cloudfront.types.s3_origin.serialize_xml(value["s3_origin"], el, "S3Origin")
    if "aliases" in value:
        import aws_sdk_cloudfront.types.aliases

        aws_sdk_cloudfront.types.aliases.serialize_xml(value["aliases"], el, "Aliases")
    SubElement(el, "Comment").text = str(value["comment"])
    if "logging" in value:
        import aws_sdk_cloudfront.types.streaming_logging_config

        aws_sdk_cloudfront.types.streaming_logging_config.serialize_xml(
            value["logging"], el, "Logging"
        )
    import aws_sdk_cloudfront.types.trusted_signers

    aws_sdk_cloudfront.types.trusted_signers.serialize_xml(
        value["trusted_signers"], el, "TrustedSigners"
    )
    if "price_class" in value:
        import aws_sdk_cloudfront.types.price_class

        aws_sdk_cloudfront.types.price_class.serialize_xml(
            value["price_class"], el, "PriceClass"
        )
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> StreamingDistributionConfig:
    out: StreamingDistributionConfig = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError(
            "StreamingDistributionConfig.caller_reference required"
        )
    child_s3_origin = el.find("S3Origin")
    if child_s3_origin is not None:
        import aws_sdk_cloudfront.types.s3_origin

        out["s3_origin"] = aws_sdk_cloudfront.types.s3_origin.deserialize_xml(
            child_s3_origin
        )
    else:
        raise DeserializationError("StreamingDistributionConfig.s3_origin required")
    child_aliases = el.find("Aliases")
    if child_aliases is not None:
        import aws_sdk_cloudfront.types.aliases

        out["aliases"] = aws_sdk_cloudfront.types.aliases.deserialize_xml(child_aliases)
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("StreamingDistributionConfig.comment required")
    child_logging = el.find("Logging")
    if child_logging is not None:
        import aws_sdk_cloudfront.types.streaming_logging_config

        out["logging"] = (
            aws_sdk_cloudfront.types.streaming_logging_config.deserialize_xml(
                child_logging
            )
        )
    child_trusted_signers = el.find("TrustedSigners")
    if child_trusted_signers is not None:
        import aws_sdk_cloudfront.types.trusted_signers

        out["trusted_signers"] = (
            aws_sdk_cloudfront.types.trusted_signers.deserialize_xml(
                child_trusted_signers
            )
        )
    else:
        raise DeserializationError(
            "StreamingDistributionConfig.trusted_signers required"
        )
    child_price_class = el.find("PriceClass")
    if child_price_class is not None:
        import aws_sdk_cloudfront.types.price_class

        out["price_class"] = aws_sdk_cloudfront.types.price_class.deserialize_xml(
            child_price_class
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("StreamingDistributionConfig.enabled required")
    return out
