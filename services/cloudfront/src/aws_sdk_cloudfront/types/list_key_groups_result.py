"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListKeyGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group_list


class ListKeyGroupsResult(TypedDict):
    key_group_list: NotRequired["aws_sdk_cloudfront.types.key_group_list.KeyGroupList"]
    """<p>A list of key groups.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListKeyGroupsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group_list" in value:
        import aws_sdk_cloudfront.types.key_group_list

        aws_sdk_cloudfront.types.key_group_list.serialize_xml(
            value["key_group_list"], el, "KeyGroupList"
        )


def deserialize_xml(el: Element) -> ListKeyGroupsResult:
    out: ListKeyGroupsResult = {}  # type: ignore[typeddict-item]
    child_key_group_list = el.find("KeyGroupList")
    if child_key_group_list is not None:
        import aws_sdk_cloudfront.types.key_group_list

        out["key_group_list"] = aws_sdk_cloudfront.types.key_group_list.deserialize_xml(
            child_key_group_list
        )
    return out
