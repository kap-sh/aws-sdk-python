"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListInvalidationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation_list


class ListInvalidationsResult(TypedDict):
    invalidation_list: NotRequired[
        "aws_sdk_cloudfront.types.invalidation_list.InvalidationList"
    ]
    """<p>Information about invalidation batches.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListInvalidationsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "invalidation_list" in value:
        import aws_sdk_cloudfront.types.invalidation_list

        aws_sdk_cloudfront.types.invalidation_list.serialize_xml(
            value["invalidation_list"], el, "InvalidationList"
        )


def deserialize_xml(el: Element) -> ListInvalidationsResult:
    out: ListInvalidationsResult = {}  # type: ignore[typeddict-item]
    child_invalidation_list = el.find("InvalidationList")
    if child_invalidation_list is not None:
        import aws_sdk_cloudfront.types.invalidation_list

        out["invalidation_list"] = (
            aws_sdk_cloudfront.types.invalidation_list.deserialize_xml(
                child_invalidation_list
            )
        )
    return out
