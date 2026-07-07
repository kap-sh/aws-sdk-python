"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class QueryArgProfile(TypedDict, closed=True):
    query_arg: "aws_sdk_cloudfront.types.string.string"
    """<p>Query argument for field-level encryption query argument-profile mapping.</p>"""
    profile_id: "aws_sdk_cloudfront.types.string.string"
    """<p>ID of profile to use for field-level encryption query argument-profile mapping</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfile, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "QueryArg").text = str(value["query_arg"])
    SubElement(el, "ProfileId").text = str(value["profile_id"])


def deserialize_xml(el: Element) -> QueryArgProfile:
    out: QueryArgProfile = {}  # type: ignore[typeddict-item]
    child_query_arg = el.find("QueryArg")
    if child_query_arg is not None:
        out["query_arg"] = str(child_query_arg.text or "")
    else:
        raise DeserializationError("QueryArgProfile.query_arg required")
    child_profile_id = el.find("ProfileId")
    if child_profile_id is not None:
        out["profile_id"] = str(child_profile_id.text or "")
    else:
        raise DeserializationError("QueryArgProfile.profile_id required")
    return out
