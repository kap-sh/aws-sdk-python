"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_object_type_template_list
    import aws_sdk_customer_profiles.types.token


class ListProfileObjectTypeTemplatesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.profile_object_type_template_list.ProfileObjectTypeTemplateList"
    ]
    """<p>The list of ListProfileObjectType template instances.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListObjectTypeTemplates API call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeTemplatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.profile_object_type_template_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.profile_object_type_template_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeTemplatesResponse:
    out: ListProfileObjectTypeTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.profile_object_type_template_list

        out["items"] = (
            aws_sdk_customer_profiles.types.profile_object_type_template_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
