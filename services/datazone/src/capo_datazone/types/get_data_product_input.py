"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_product_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision


class GetDataProductInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product lives.</p>"""
    identifier: "capo_datazone.types.data_product_id.DataProductId"
    """<p>The ID of the data product.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataProductInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataProductInput:
    out: GetDataProductInput = {}  # type: ignore[typeddict-item]
    return out
