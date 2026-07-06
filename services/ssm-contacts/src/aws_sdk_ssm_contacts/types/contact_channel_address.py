"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactChannelAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.simple_address


class ContactChannelAddress(TypedDict, closed=True):
    simple_address: NotRequired[
        "aws_sdk_ssm_contacts.types.simple_address.SimpleAddress"
    ]
    """<p>The format is dependent on the type of the contact channel. The following are the expected formats:</p> <ul> <li> <p>SMS - '+' followed by the country code and phone number</p> </li> <li> <p>VOICE - '+' followed by the country code and phone number</p> </li> <li> <p>EMAIL - any standard email format</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactChannelAddress) -> dict:
    out: dict = {}
    if "simple_address" in value:
        out["SimpleAddress"] = value["simple_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactChannelAddress:
    out: ContactChannelAddress = {}  # type: ignore[typeddict-item]
    if "SimpleAddress" in data:
        out["simple_address"] = data["SimpleAddress"]
    return out
