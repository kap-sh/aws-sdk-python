"""Generated from Smithy shape ``com.amazonaws.iot#ListCACertificatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size
    import aws_sdk_iot.types.template_name


class ListCACertificatesRequest(TypedDict):
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Determines the order of the results.</p>"""
    template_name: NotRequired["aws_sdk_iot.types.template_name.TemplateName"]
    """<p>The name of the provisioning template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCACertificatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCACertificatesRequest:
    out: ListCACertificatesRequest = {}  # type: ignore[typeddict-item]
    return out
