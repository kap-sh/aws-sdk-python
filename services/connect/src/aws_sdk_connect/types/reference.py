"""Generated from Smithy shape ``com.amazonaws.connect#Reference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_arn
    import aws_sdk_connect.types.reference_status
    import aws_sdk_connect.types.reference_status_reason
    import aws_sdk_connect.types.reference_type
    import aws_sdk_connect.types.reference_value


class Reference(TypedDict):
    value: "aws_sdk_connect.types.reference_value.ReferenceValue"
    """<p>A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).</p>"""
    type: "aws_sdk_connect.types.reference_type.ReferenceType"
    """<p>The type of the reference. <code>DATE</code> must be of type Epoch timestamp. </p>"""
    status: NotRequired["aws_sdk_connect.types.reference_status.ReferenceStatus"]
    """<p>Status of the attachment reference type.</p>"""
    arn: NotRequired["aws_sdk_connect.types.reference_arn.ReferenceArn"]
    """<p>The Amazon Resource Name (ARN) of the reference</p>"""
    status_reason: NotRequired[
        "aws_sdk_connect.types.reference_status_reason.ReferenceStatusReason"
    ]
    """<p>Relevant details why the reference was not successfully created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Reference) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", "")
    import aws_sdk_connect.types.reference_type

    out["Type"] = aws_sdk_connect.types.reference_type.serialize_json(value["type"])
    if "status" in value:
        import aws_sdk_connect.types.reference_status

        out["Status"] = aws_sdk_connect.types.reference_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> Reference:
    out: Reference = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if "Type" in data:
        import aws_sdk_connect.types.reference_type

        out["type"] = aws_sdk_connect.types.reference_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("Reference.type required")
    if "Status" in data:
        import aws_sdk_connect.types.reference_status

        out["status"] = aws_sdk_connect.types.reference_status.deserialize_json(
            data["Status"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    return out
