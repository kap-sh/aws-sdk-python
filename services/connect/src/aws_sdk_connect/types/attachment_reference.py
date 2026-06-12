"""Generated from Smithy shape ``com.amazonaws.connect#AttachmentReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_arn
    import aws_sdk_connect.types.reference_key
    import aws_sdk_connect.types.reference_status
    import aws_sdk_connect.types.reference_value


class AttachmentReference(TypedDict):
    name: NotRequired["aws_sdk_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the attachment reference.</p>"""
    value: NotRequired["aws_sdk_connect.types.reference_value.ReferenceValue"]
    """<p>The location path of the attachment reference.</p>"""
    status: NotRequired["aws_sdk_connect.types.reference_status.ReferenceStatus"]
    """<p>Status of the attachment reference type.</p>"""
    arn: NotRequired["aws_sdk_connect.types.reference_arn.ReferenceArn"]
    """<p>The Amazon Resource Name (ARN) of the attachment reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "status" in value:
        import aws_sdk_connect.types.reference_status

        out["Status"] = aws_sdk_connect.types.reference_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AttachmentReference:
    out: AttachmentReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Status" in data:
        import aws_sdk_connect.types.reference_status

        out["status"] = aws_sdk_connect.types.reference_status.deserialize_json(
            data["Status"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
