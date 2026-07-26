"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow


class DescribeContactFlowResponse(TypedDict, closed=True):
    contact_flow: NotRequired["capo_connect.types.contact_flow.ContactFlow"]
    """<p>Information about the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowResponse) -> dict:
    out: dict = {}
    if "contact_flow" in value:
        import capo_connect.types.contact_flow

        out["ContactFlow"] = capo_connect.types.contact_flow.serialize_json(
            value["contact_flow"]
        )
    return out


def deserialize_json(data: dict) -> DescribeContactFlowResponse:
    out: DescribeContactFlowResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlow" in data:
        import capo_connect.types.contact_flow

        out["contact_flow"] = capo_connect.types.contact_flow.deserialize_json(
            data["ContactFlow"]
        )
    return out
