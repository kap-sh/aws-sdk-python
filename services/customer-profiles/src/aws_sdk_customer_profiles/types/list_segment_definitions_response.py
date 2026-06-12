"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListSegmentDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.segment_definitions_list
    import aws_sdk_customer_profiles.types.token


class ListSegmentDefinitionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call.</p>"""
    items: NotRequired[
        "aws_sdk_customer_profiles.types.segment_definitions_list.SegmentDefinitionsList"
    ]
    """<p>List of segment definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSegmentDefinitionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_customer_profiles.types.segment_definitions_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.segment_definitions_list.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSegmentDefinitionsResponse:
    out: ListSegmentDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.segment_definitions_list

        out["items"] = (
            aws_sdk_customer_profiles.types.segment_definitions_list.deserialize_json(
                data["Items"]
            )
        )
    return out
