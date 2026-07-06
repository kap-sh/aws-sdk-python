"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainObjectTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.domain_object_types_list
    import aws_sdk_customer_profiles.types.token


class ListDomainObjectTypesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.domain_object_types_list.DomainObjectTypesList"
    ]
    """<p>The list of domain object types.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListDomainObjectTypes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainObjectTypesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.domain_object_types_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.domain_object_types_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainObjectTypesResponse:
    out: ListDomainObjectTypesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.domain_object_types_list

        out["items"] = (
            aws_sdk_customer_profiles.types.domain_object_types_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
