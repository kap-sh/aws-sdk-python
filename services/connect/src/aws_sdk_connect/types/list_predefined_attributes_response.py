"""Generated from Smithy shape ``com.amazonaws.connect#ListPredefinedAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.predefined_attribute_summary_list


class ListPredefinedAttributesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    predefined_attribute_summary_list: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_summary_list.PredefinedAttributeSummaryList"
    ]
    """<p>Summary of the predefined attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPredefinedAttributesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "predefined_attribute_summary_list" in value:
        import aws_sdk_connect.types.predefined_attribute_summary_list

        out["PredefinedAttributeSummaryList"] = (
            aws_sdk_connect.types.predefined_attribute_summary_list.serialize_json(
                value["predefined_attribute_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPredefinedAttributesResponse:
    out: ListPredefinedAttributesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PredefinedAttributeSummaryList" in data:
        import aws_sdk_connect.types.predefined_attribute_summary_list

        out["predefined_attribute_summary_list"] = (
            aws_sdk_connect.types.predefined_attribute_summary_list.deserialize_json(
                data["PredefinedAttributeSummaryList"]
            )
        )
    return out
