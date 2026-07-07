"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceGraphResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.service_list
    import aws_sdk_xray.types.string


class GetTraceGraphResult(TypedDict, closed=True):
    services: NotRequired["aws_sdk_xray.types.service_list.ServiceList"]
    """<p>The services that have processed one of the specified requests.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceGraphResult) -> dict:
    out: dict = {}
    if "services" in value:
        import aws_sdk_xray.types.service_list

        out["Services"] = aws_sdk_xray.types.service_list.serialize_json(
            value["services"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTraceGraphResult:
    out: GetTraceGraphResult = {}  # type: ignore[typeddict-item]
    if "Services" in data:
        import aws_sdk_xray.types.service_list

        out["services"] = aws_sdk_xray.types.service_list.deserialize_json(
            data["Services"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
