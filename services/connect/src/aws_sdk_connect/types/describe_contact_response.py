"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact


class DescribeContactResponse(TypedDict):
    contact: NotRequired["aws_sdk_connect.types.contact.Contact"]
    """<p>Information about the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactResponse) -> dict:
    out: dict = {}
    if "contact" in value:
        import aws_sdk_connect.types.contact

        out["Contact"] = aws_sdk_connect.types.contact.serialize_json(value["contact"])
    return out


def deserialize_json(data: dict) -> DescribeContactResponse:
    out: DescribeContactResponse = {}  # type: ignore[typeddict-item]
    if "Contact" in data:
        import aws_sdk_connect.types.contact

        out["contact"] = aws_sdk_connect.types.contact.deserialize_json(data["Contact"])
    return out
