"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_object_list
    import aws_sdk_customer_profiles.types.token


class ListProfileObjectsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.profile_object_list.ProfileObjectList"
    ]
    """<p>The list of ListProfileObject instances.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListProfileObjects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.profile_object_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.profile_object_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileObjectsResponse:
    out: ListProfileObjectsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.profile_object_list

        out["items"] = (
            aws_sdk_customer_profiles.types.profile_object_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
