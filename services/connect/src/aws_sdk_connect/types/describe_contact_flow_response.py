"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow


class DescribeContactFlowResponse(TypedDict):
    contact_flow: NotRequired["aws_sdk_connect.types.contact_flow.ContactFlow"]
    """<p>Information about the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowResponse) -> dict:
    out: dict = {}
    if "contact_flow" in value:
        import aws_sdk_connect.types.contact_flow

        out["ContactFlow"] = aws_sdk_connect.types.contact_flow.serialize_json(
            value["contact_flow"]
        )
    return out


def deserialize_json(data: dict) -> DescribeContactFlowResponse:
    out: DescribeContactFlowResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlow" in data:
        import aws_sdk_connect.types.contact_flow

        out["contact_flow"] = aws_sdk_connect.types.contact_flow.deserialize_json(
            data["ContactFlow"]
        )
    return out
