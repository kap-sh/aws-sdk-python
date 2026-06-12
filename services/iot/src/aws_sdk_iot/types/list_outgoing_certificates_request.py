"""Generated from Smithy shape ``com.amazonaws.iot#ListOutgoingCertificatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size


class ListOutgoingCertificatesRequest(TypedDict):
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutgoingCertificatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOutgoingCertificatesRequest:
    out: ListOutgoingCertificatesRequest = {}  # type: ignore[typeddict-item]
    return out
