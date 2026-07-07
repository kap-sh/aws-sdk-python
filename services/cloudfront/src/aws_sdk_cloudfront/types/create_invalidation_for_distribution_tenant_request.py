"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateInvalidationForDistributionTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation_batch
    import aws_sdk_cloudfront.types.string


class CreateInvalidationForDistributionTenantRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    invalidation_batch: "aws_sdk_cloudfront.types.invalidation_batch.InvalidationBatch"


# --- restXml ser/de ---
def serialize_xml(
    value: CreateInvalidationForDistributionTenantRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.invalidation_batch

    aws_sdk_cloudfront.types.invalidation_batch.serialize_xml(
        value["invalidation_batch"], el, "InvalidationBatch"
    )


def deserialize_xml(el: Element) -> CreateInvalidationForDistributionTenantRequest:
    out: CreateInvalidationForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    child_invalidation_batch = el.find("InvalidationBatch")
    if child_invalidation_batch is not None:
        import aws_sdk_cloudfront.types.invalidation_batch

        out["invalidation_batch"] = (
            aws_sdk_cloudfront.types.invalidation_batch.deserialize_xml(
                child_invalidation_batch
            )
        )
    else:
        raise DeserializationError(
            "CreateInvalidationForDistributionTenantRequest.invalidation_batch required"
        )
    return out
