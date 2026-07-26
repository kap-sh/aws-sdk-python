"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListContactChannelsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact_channel_list
    import capo_ssm_contacts.types.pagination_token


class ListContactChannelsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    contact_channels: "capo_ssm_contacts.types.contact_channel_list.ContactChannelList"
    """<p>A list of contact channels related to the specified contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContactChannelsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_ssm_contacts.types.contact_channel_list

    out["ContactChannels"] = (
        capo_ssm_contacts.types.contact_channel_list.serialize_aws_json_1_1(
            value["contact_channels"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContactChannelsResult:
    out: ListContactChannelsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ContactChannels" in data:
        import capo_ssm_contacts.types.contact_channel_list

        out["contact_channels"] = (
            capo_ssm_contacts.types.contact_channel_list.deserialize_aws_json_1_1(
                data["ContactChannels"]
            )
        )
    else:
        raise DeserializationError(
            "ListContactChannelsResult.contact_channels required"
        )
    return out
