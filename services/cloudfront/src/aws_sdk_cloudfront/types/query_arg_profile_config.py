"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfileConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.query_arg_profiles


class QueryArgProfileConfig(TypedDict):
    forward_when_query_arg_profile_is_unknown: (
        "aws_sdk_cloudfront.types.boolean.boolean"
    )
    """<p>Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.</p>"""
    query_arg_profiles: NotRequired[
        "aws_sdk_cloudfront.types.query_arg_profiles.QueryArgProfiles"
    ]
    """<p>Profiles specified for query argument-profile mapping for field-level encryption.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfileConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ForwardWhenQueryArgProfileIsUnknown").text = (
        "true" if value["forward_when_query_arg_profile_is_unknown"] else "false"
    )
    if "query_arg_profiles" in value:
        import aws_sdk_cloudfront.types.query_arg_profiles

        aws_sdk_cloudfront.types.query_arg_profiles.serialize_xml(
            value["query_arg_profiles"], el, "QueryArgProfiles"
        )


def deserialize_xml(el: Element) -> QueryArgProfileConfig:
    out: QueryArgProfileConfig = {}  # type: ignore[typeddict-item]
    child_forward_when_query_arg_profile_is_unknown = el.find(
        "ForwardWhenQueryArgProfileIsUnknown"
    )
    if child_forward_when_query_arg_profile_is_unknown is not None:
        out["forward_when_query_arg_profile_is_unknown"] = (
            child_forward_when_query_arg_profile_is_unknown.text or ""
        ).lower() == "true"
    else:
        raise DeserializationError(
            "QueryArgProfileConfig.forward_when_query_arg_profile_is_unknown required"
        )
    child_query_arg_profiles = el.find("QueryArgProfiles")
    if child_query_arg_profiles is not None:
        import aws_sdk_cloudfront.types.query_arg_profiles

        out["query_arg_profiles"] = (
            aws_sdk_cloudfront.types.query_arg_profiles.deserialize_xml(
                child_query_arg_profiles
            )
        )
    return out
