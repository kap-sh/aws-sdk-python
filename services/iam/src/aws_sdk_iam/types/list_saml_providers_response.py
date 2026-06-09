"""Generated from Smithy shape ``com.amazonaws.iam#ListSAMLProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.saml_provider_list_type


class ListSAMLProvidersResponse(TypedDict):
    saml_provider_list: NotRequired[
        "aws_sdk_iam.types.saml_provider_list_type.SAMLProviderListType"
    ]
    """<p>The list of SAML provider resource objects defined in IAM for this Amazon Web Services account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSAMLProvidersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "saml_provider_list" in value:
        import aws_sdk_iam.types.saml_provider_list_type

        aws_sdk_iam.types.saml_provider_list_type.serialize_query(
            value["saml_provider_list"], pairs, f"{prefix}.SAMLProviderList"
        )


def deserialize_query(el: Element) -> ListSAMLProvidersResponse:
    out: ListSAMLProvidersResponse = {}  # type: ignore[typeddict-item]
    child_saml_provider_list = el.find("SAMLProviderList")
    if child_saml_provider_list is not None:
        import aws_sdk_iam.types.saml_provider_list_type

        out["saml_provider_list"] = (
            aws_sdk_iam.types.saml_provider_list_type.deserialize_query(
                child_saml_provider_list
            )
        )
    return out
