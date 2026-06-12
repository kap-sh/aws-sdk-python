"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectContactData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.quick_connect_id
    import aws_sdk_connect.types.quick_connect_name
    import aws_sdk_connect.types.quick_connect_type
    import aws_sdk_connect.types.timestamp


class QuickConnectContactData(TypedDict):
    contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p> The contact ID for quick connect contact data. </p>"""
    initiation_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p> Timestamp when the quick connect contact was initiated. </p>"""
    quick_connect_id: NotRequired[
        "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
    ]
    """<p> The quick connect ID. </p>"""
    quick_connect_name: NotRequired[
        "aws_sdk_connect.types.quick_connect_name.QuickConnectName"
    ]
    """<p> The name of the quick connect. </p>"""
    quick_connect_type: NotRequired[
        "aws_sdk_connect.types.quick_connect_type.QuickConnectType"
    ]
    """<p> The type of the quick connect. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectContactData) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "initiation_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["InitiationTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["initiation_timestamp"]
        )
    if "quick_connect_id" in value:
        out["QuickConnectId"] = value["quick_connect_id"]
    if "quick_connect_name" in value:
        out["QuickConnectName"] = value["quick_connect_name"]
    if "quick_connect_type" in value:
        import aws_sdk_connect.types.quick_connect_type

        out["QuickConnectType"] = (
            aws_sdk_connect.types.quick_connect_type.serialize_json(
                value["quick_connect_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuickConnectContactData:
    out: QuickConnectContactData = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "InitiationTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["initiation_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["InitiationTimestamp"]
        )
    if "QuickConnectId" in data:
        out["quick_connect_id"] = data["QuickConnectId"]
    if "QuickConnectName" in data:
        out["quick_connect_name"] = data["QuickConnectName"]
    if "QuickConnectType" in data:
        import aws_sdk_connect.types.quick_connect_type

        out["quick_connect_type"] = (
            aws_sdk_connect.types.quick_connect_type.deserialize_json(
                data["QuickConnectType"]
            )
        )
    return out
