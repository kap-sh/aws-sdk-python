"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributesForProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.calculated_attributes_for_profile_list
    import capo_customer_profiles.types.token


class ListCalculatedAttributesForProfileResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_customer_profiles.types.calculated_attributes_for_profile_list.CalculatedAttributesForProfileList"
    ]
    """<p>The list of calculated attributes.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListCalculatedAttributesForProfile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributesForProfileResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.calculated_attributes_for_profile_list

        out["Items"] = (
            capo_customer_profiles.types.calculated_attributes_for_profile_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributesForProfileResponse:
    out: ListCalculatedAttributesForProfileResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_customer_profiles.types.calculated_attributes_for_profile_list

        out["items"] = (
            capo_customer_profiles.types.calculated_attributes_for_profile_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
