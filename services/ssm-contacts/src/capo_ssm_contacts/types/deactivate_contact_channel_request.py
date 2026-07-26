"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DeactivateContactChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class DeactivateContactChannelRequest(TypedDict, closed=True):
    contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel you're deactivating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeactivateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeactivateContactChannelRequest:
    out: DeactivateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if "ContactChannelId" in data:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        raise DeserializationError(
            "DeactivateContactChannelRequest.contact_channel_id required"
        )
    return out
