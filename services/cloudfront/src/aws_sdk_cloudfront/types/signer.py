"""Generated from Smithy shape ``com.amazonaws.cloudfront#Signer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_pair_ids
    import aws_sdk_cloudfront.types.string


class Signer(TypedDict):
    aws_account_number: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>An Amazon Web Services account number that contains active CloudFront key pairs that CloudFront can use to verify the signatures of signed URLs and signed cookies. If the Amazon Web Services account that owns the key pairs is the same account that owns the CloudFront distribution, the value of this field is <code>self</code>.</p>"""
    key_pair_ids: NotRequired["aws_sdk_cloudfront.types.key_pair_ids.KeyPairIds"]
    """<p>A list of CloudFront key pair identifiers.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Signer, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "aws_account_number" in value:
        SubElement(el, "AwsAccountNumber").text = str(value["aws_account_number"])
    if "key_pair_ids" in value:
        import aws_sdk_cloudfront.types.key_pair_ids

        aws_sdk_cloudfront.types.key_pair_ids.serialize_xml(
            value["key_pair_ids"], el, "KeyPairIds"
        )


def deserialize_xml(el: Element) -> Signer:
    out: Signer = {}  # type: ignore[typeddict-item]
    child_aws_account_number = el.find("AwsAccountNumber")
    if child_aws_account_number is not None:
        out["aws_account_number"] = str(child_aws_account_number.text or "")
    child_key_pair_ids = el.find("KeyPairIds")
    if child_key_pair_ids is not None:
        import aws_sdk_cloudfront.types.key_pair_ids

        out["key_pair_ids"] = aws_sdk_cloudfront.types.key_pair_ids.deserialize_xml(
            child_key_pair_ids
        )
    return out
