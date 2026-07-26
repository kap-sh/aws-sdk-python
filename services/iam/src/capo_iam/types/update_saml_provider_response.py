"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSAMLProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type


class UpdateSAMLProviderResponse(TypedDict, closed=True):
    saml_provider_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the SAML provider that was updated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateSAMLProviderResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "saml_provider_arn" in value:
        pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))


def deserialize_query(el: Element) -> UpdateSAMLProviderResponse:
    out: UpdateSAMLProviderResponse = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    return out
