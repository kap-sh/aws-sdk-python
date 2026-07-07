"""Generated from Smithy shape ``com.amazonaws.ec2#FederatedAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class FederatedAuthenticationRequest(TypedDict, closed=True):
    saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider.</p>"""
    self_service_saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FederatedAuthenticationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "saml_provider_arn" in value:
        pairs.append((f"{prefix}.SAMLProviderArn", str(value["saml_provider_arn"])))
    if "self_service_saml_provider_arn" in value:
        pairs.append(
            (
                f"{prefix}.SelfServiceSAMLProviderArn",
                str(value["self_service_saml_provider_arn"]),
            )
        )


def deserialize_ec2_query(el: Element) -> FederatedAuthenticationRequest:
    out: FederatedAuthenticationRequest = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SAMLProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    child_self_service_saml_provider_arn = el.find("SelfServiceSAMLProviderArn")
    if child_self_service_saml_provider_arn is not None:
        out["self_service_saml_provider_arn"] = str(
            child_self_service_saml_provider_arn.text or ""
        )
    return out
