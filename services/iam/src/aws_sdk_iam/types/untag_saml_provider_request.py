"""Generated from Smithy shape ``com.amazonaws.iam#UntagSAMLProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.tag_key_list_type


class UntagSAMLProviderRequest(TypedDict):
    saml_provider_arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The ARN of the SAML identity provider in IAM from which you want to remove tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "aws_sdk_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified SAML identity provider.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagSAMLProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))
    import aws_sdk_iam.types.tag_key_list_type

    aws_sdk_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{prefix}.TagKeys"
    )


def deserialize_query(el: Element) -> UntagSAMLProviderRequest:
    out: UntagSAMLProviderRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    else:
        raise DeserializationError(
            "UntagSAMLProviderRequest.saml_provider_arn required"
        )
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_iam.types.tag_key_list_type

        out["tag_keys"] = aws_sdk_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagSAMLProviderRequest.tag_keys required")
    return out
