"""Generated from Smithy shape ``com.amazonaws.connect#EmailMessageReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_arn
    import aws_sdk_connect.types.reference_key


class EmailMessageReference(TypedDict, closed=True):
    name: NotRequired["aws_sdk_connect.types.reference_key.ReferenceKey"]
    """<p>The name of the email message reference</p>"""
    arn: NotRequired["aws_sdk_connect.types.reference_arn.ReferenceArn"]
    """<p>The Amazon Resource Name (ARN) of the email message reference</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailMessageReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EmailMessageReference:
    out: EmailMessageReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
