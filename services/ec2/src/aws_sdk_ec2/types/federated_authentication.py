"""Generated from Smithy shape ``com.amazonaws.ec2#FederatedAuthentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class FederatedAuthentication(TypedDict):
    saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider.</p>"""
    self_service_saml_provider_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FederatedAuthentication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "saml_provider_arn" in value:
        pairs.append((f"{prefix}.SamlProviderArn", str(value["saml_provider_arn"])))
    if "self_service_saml_provider_arn" in value:
        pairs.append(
            (
                f"{prefix}.SelfServiceSamlProviderArn",
                str(value["self_service_saml_provider_arn"]),
            )
        )


def deserialize_ec2_query(el: Element) -> FederatedAuthentication:
    out: FederatedAuthentication = {}  # type: ignore[typeddict-item]
    child_saml_provider_arn = el.find("SamlProviderArn")
    if child_saml_provider_arn is not None:
        out["saml_provider_arn"] = str(child_saml_provider_arn.text or "")
    child_self_service_saml_provider_arn = el.find("SelfServiceSamlProviderArn")
    if child_self_service_saml_provider_arn is not None:
        out["self_service_saml_provider_arn"] = str(
            child_self_service_saml_provider_arn.text or ""
        )
    return out
