"""Generated from Smithy shape ``com.amazonaws.connect#ContactFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_states


class ContactFilter(TypedDict):
    contact_states: NotRequired["aws_sdk_connect.types.contact_states.ContactStates"]
    r"""<p>A list of up to 9 <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html\">contact states</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFilter) -> dict:
    out: dict = {}
    if "contact_states" in value:
        import aws_sdk_connect.types.contact_states

        out["ContactStates"] = aws_sdk_connect.types.contact_states.serialize_json(
            value["contact_states"]
        )
    return out


def deserialize_json(data: dict) -> ContactFilter:
    out: ContactFilter = {}  # type: ignore[typeddict-item]
    if "ContactStates" in data:
        import aws_sdk_connect.types.contact_states

        out["contact_states"] = aws_sdk_connect.types.contact_states.deserialize_json(
            data["ContactStates"]
        )
    return out
