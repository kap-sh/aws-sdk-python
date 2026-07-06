"""Generated from Smithy shape ``com.amazonaws.apigateway#DomainNameAccessAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_domain_name_access_association
    import aws_sdk_api_gateway.types.string


class DomainNameAccessAssociations(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_api_gateway.types.list_of_domain_name_access_association.ListOfDomainNameAccessAssociation"
    ]
    """<p> The current page of elements from this collection. </p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameAccessAssociations) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_domain_name_access_association

        out["item"] = (
            aws_sdk_api_gateway.types.list_of_domain_name_access_association.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainNameAccessAssociations:
    out: DomainNameAccessAssociations = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_domain_name_access_association

        out["items"] = (
            aws_sdk_api_gateway.types.list_of_domain_name_access_association.deserialize_json(
                data["item"]
            )
        )
    return out
