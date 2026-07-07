"""Generated from Smithy shape ``com.amazonaws.iam#ListOpenIDConnectProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.open_id_connect_provider_list_type


class ListOpenIDConnectProvidersResponse(TypedDict, closed=True):
    open_id_connect_provider_list: NotRequired[
        "aws_sdk_iam.types.open_id_connect_provider_list_type.OpenIDConnectProviderListType"
    ]
    """<p>The list of IAM OIDC provider resource objects defined in the Amazon Web Services account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOpenIDConnectProvidersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "open_id_connect_provider_list" in value:
        import aws_sdk_iam.types.open_id_connect_provider_list_type

        aws_sdk_iam.types.open_id_connect_provider_list_type.serialize_query(
            value["open_id_connect_provider_list"],
            pairs,
            f"{prefix}.OpenIDConnectProviderList",
        )


def deserialize_query(el: Element) -> ListOpenIDConnectProvidersResponse:
    out: ListOpenIDConnectProvidersResponse = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_list = el.find("OpenIDConnectProviderList")
    if child_open_id_connect_provider_list is not None:
        import aws_sdk_iam.types.open_id_connect_provider_list_type

        out["open_id_connect_provider_list"] = (
            aws_sdk_iam.types.open_id_connect_provider_list_type.deserialize_query(
                child_open_id_connect_provider_list
            )
        )
    return out
