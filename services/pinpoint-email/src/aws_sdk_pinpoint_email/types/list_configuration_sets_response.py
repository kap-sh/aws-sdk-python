"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListConfigurationSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name_list
    import aws_sdk_pinpoint_email.types.next_token


class ListConfigurationSetsResponse(TypedDict, closed=True):
    configuration_sets: NotRequired[
        "aws_sdk_pinpoint_email.types.configuration_set_name_list.ConfigurationSetNameList"
    ]
    """<p>An array that contains all of the configuration sets in your Amazon Pinpoint account in the current AWS Region.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional configuration sets to list. To view additional configuration sets, issue another request to <code>ListConfigurationSets</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationSetsResponse) -> dict:
    out: dict = {}
    if "configuration_sets" in value:
        import aws_sdk_pinpoint_email.types.configuration_set_name_list

        out["ConfigurationSets"] = (
            aws_sdk_pinpoint_email.types.configuration_set_name_list.serialize_json(
                value["configuration_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationSetsResponse:
    out: ListConfigurationSetsResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationSets" in data:
        import aws_sdk_pinpoint_email.types.configuration_set_name_list

        out["configuration_sets"] = (
            aws_sdk_pinpoint_email.types.configuration_set_name_list.deserialize_json(
                data["ConfigurationSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
