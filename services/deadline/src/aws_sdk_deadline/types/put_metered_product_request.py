"""Generated from Smithy shape ``com.amazonaws.deadline#PutMeteredProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id
    import aws_sdk_deadline.types.metered_product_id


class PutMeteredProductRequest(TypedDict, closed=True):
    license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID to add to the metered product.</p>"""
    product_id: "aws_sdk_deadline.types.metered_product_id.MeteredProductId"
    """<p>The product ID to add to the metered product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMeteredProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutMeteredProductRequest:
    out: PutMeteredProductRequest = {}  # type: ignore[typeddict-item]
    return out
