"""Generated from Smithy shape ``com.amazonaws.translate#ListTerminologiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_translate.types.next_token
    import aws_sdk_translate.types.terminology_properties_list


class ListTerminologiesResponse(TypedDict, closed=True):
    terminology_properties_list: NotRequired[
        "aws_sdk_translate.types.terminology_properties_list.TerminologyPropertiesList"
    ]
    """<p>The properties list of the custom terminologies returned on the list request.</p>"""
    next_token: NotRequired["aws_sdk_translate.types.next_token.NextToken"]
    """<p> If the response to the ListTerminologies was truncated, the NextToken fetches the next group of custom terminologies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTerminologiesResponse) -> dict:
    out: dict = {}
    if "terminology_properties_list" in value:
        import aws_sdk_translate.types.terminology_properties_list

        out["TerminologyPropertiesList"] = (
            aws_sdk_translate.types.terminology_properties_list.serialize_aws_json_1_1(
                value["terminology_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTerminologiesResponse:
    out: ListTerminologiesResponse = {}  # type: ignore[typeddict-item]
    if "TerminologyPropertiesList" in data:
        import aws_sdk_translate.types.terminology_properties_list

        out["terminology_properties_list"] = (
            aws_sdk_translate.types.terminology_properties_list.deserialize_aws_json_1_1(
                data["TerminologyPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
