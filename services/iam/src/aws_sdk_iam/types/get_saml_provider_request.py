"""Generated from Smithy shape ``com.amazonaws.iam#GetSAMLProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type


class GetSAMLProviderRequest(TypedDict):
    saml_provider_arn: "aws_sdk_iam.types.arn_type.arnType"
    r"""<p>The Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about.</p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSAMLProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))


def deserialize_query(el: Element) -> GetSAMLProviderRequest:
    out: GetSAMLProviderRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    else:
        raise DeserializationError("GetSAMLProviderRequest.saml_provider_arn required")
    return out
