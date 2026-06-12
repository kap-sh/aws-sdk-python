"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowTypeCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_type


class ContactFlowTypeCondition(TypedDict):
    contact_flow_type: NotRequired[
        "aws_sdk_connect.types.contact_flow_type.ContactFlowType"
    ]
    """<p> Contact flow type of the contact flow type condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowTypeCondition) -> dict:
    out: dict = {}
    if "contact_flow_type" in value:
        import aws_sdk_connect.types.contact_flow_type

        out["ContactFlowType"] = aws_sdk_connect.types.contact_flow_type.serialize_json(
            value["contact_flow_type"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowTypeCondition:
    out: ContactFlowTypeCondition = {}  # type: ignore[typeddict-item]
    if "ContactFlowType" in data:
        import aws_sdk_connect.types.contact_flow_type

        out["contact_flow_type"] = (
            aws_sdk_connect.types.contact_flow_type.deserialize_json(
                data["ContactFlowType"]
            )
        )
    return out
