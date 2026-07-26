"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateInvalidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.invalidation_batch
    import capo_cloudfront.types.string


class CreateInvalidationRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The distribution's id.</p>"""
    invalidation_batch: "capo_cloudfront.types.invalidation_batch.InvalidationBatch"
    """<p>The batch information for the invalidation.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateInvalidationRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.invalidation_batch

    capo_cloudfront.types.invalidation_batch.serialize_xml(
        value["invalidation_batch"], el, "InvalidationBatch"
    )


def deserialize_xml(el: Element) -> CreateInvalidationRequest:
    out: CreateInvalidationRequest = {}  # type: ignore[typeddict-item]
    child_invalidation_batch = el.find("InvalidationBatch")
    if child_invalidation_batch is not None:
        import capo_cloudfront.types.invalidation_batch

        out["invalidation_batch"] = (
            capo_cloudfront.types.invalidation_batch.deserialize_xml(
                child_invalidation_batch
            )
        )
    else:
        raise DeserializationError(
            "CreateInvalidationRequest.invalidation_batch required"
        )
    return out
