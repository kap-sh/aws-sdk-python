"""Generated from Smithy shape ``com.amazonaws.iam#DeleteSAMLProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type


class DeleteSAMLProviderRequest(TypedDict):
    saml_provider_arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the SAML provider to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSAMLProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))


def deserialize_query(el: Element) -> DeleteSAMLProviderRequest:
    out: DeleteSAMLProviderRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    else:
        raise DeserializationError(
            "DeleteSAMLProviderRequest.saml_provider_arn required"
        )
    return out
