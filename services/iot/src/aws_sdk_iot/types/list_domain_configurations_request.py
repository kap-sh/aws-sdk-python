"""Generated from Smithy shape ``com.amazonaws.iot#ListDomainConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size
    import aws_sdk_iot.types.service_type


class ListDomainConfigurationsRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    service_type: NotRequired["aws_sdk_iot.types.service_type.ServiceType"]
    """<p>The type of service delivered by the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainConfigurationsRequest:
    out: ListDomainConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
