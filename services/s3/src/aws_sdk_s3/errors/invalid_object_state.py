"""Generated from Smithy shape ``com.amazonaws.s3#InvalidObjectState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3.types.intelligent_tiering_access_tier
    import aws_sdk_s3.types.storage_class


class InvalidObjectState_(TypedDict, closed=True):
    storage_class: NotRequired["aws_sdk_s3.types.storage_class.StorageClass"]
    access_tier: NotRequired[
        "aws_sdk_s3.types.intelligent_tiering_access_tier.IntelligentTieringAccessTier"
    ]


# --- restXml ser/de ---
def serialize_xml(value: InvalidObjectState_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "storage_class" in value:
        import aws_sdk_s3.types.storage_class

        aws_sdk_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "access_tier" in value:
        import aws_sdk_s3.types.intelligent_tiering_access_tier

        aws_sdk_s3.types.intelligent_tiering_access_tier.serialize_xml(
            value["access_tier"], el, "AccessTier"
        )


def deserialize_xml(el: Element) -> InvalidObjectState_:
    out: InvalidObjectState_ = {}  # type: ignore[typeddict-item]
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import aws_sdk_s3.types.storage_class

        out["storage_class"] = aws_sdk_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    child_access_tier = el.find("AccessTier")
    if child_access_tier is not None:
        import aws_sdk_s3.types.intelligent_tiering_access_tier

        out["access_tier"] = (
            aws_sdk_s3.types.intelligent_tiering_access_tier.deserialize_xml(
                child_access_tier
            )
        )
    return out


class InvalidObjectState(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidObjectState``."""

    code: str | None = "InvalidObjectState"

    def __init__(self, data: InvalidObjectState_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidObjectState",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidObjectState":
        return cls(deserialize_xml(el))
