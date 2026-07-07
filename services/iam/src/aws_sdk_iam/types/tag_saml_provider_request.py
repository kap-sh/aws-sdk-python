"""Generated from Smithy shape ``com.amazonaws.iam#TagSAMLProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.tag_list_type


class TagSAMLProviderRequest(TypedDict, closed=True):
    saml_provider_arn: "aws_sdk_iam.types.arn_type.arnType"
    r"""<p>The ARN of the SAML identity provider in IAM to which you want to add tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the SAML identity provider in IAM. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagSAMLProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagSAMLProviderRequest:
    out: TagSAMLProviderRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    else:
        raise DeserializationError("TagSAMLProviderRequest.saml_provider_arn required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagSAMLProviderRequest.tags required")
    return out
