"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDataProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_product_id
    import capo_datazone.types.domain_id


class DeleteDataProductInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data product is deleted.</p>"""
    identifier: "capo_datazone.types.data_product_id.DataProductId"
    """<p>The identifier of the data product that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataProductInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataProductInput:
    out: DeleteDataProductInput = {}  # type: ignore[typeddict-item]
    return out
