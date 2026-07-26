"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteMeteredProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.metered_product_id


class DeleteMeteredProductRequest(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The ID of the license endpoint from which to remove the metered product.</p>"""
    product_id: "capo_deadline.types.metered_product_id.MeteredProductId"
    """<p>The product ID to remove from the license endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMeteredProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMeteredProductRequest:
    out: DeleteMeteredProductRequest = {}  # type: ignore[typeddict-item]
    return out
