"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListOutgoingTypedLinksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.consistency_level
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.typed_link_attribute_range_list
    import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name


class ListOutgoingTypedLinksRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory where you want to list the typed links.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference that identifies the object whose attributes will be listed.</p>"""
    filter_attribute_ranges: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_attribute_range_list.TypedLinkAttributeRangeList"
    ]
    """<p>Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.</p>"""
    filter_typed_link: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName"
    ]
    """<p>Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_clouddirectory.types.number_results.NumberResults"
    ]
    """<p>The maximum number of results to retrieve.</p>"""
    consistency_level: NotRequired[
        "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level to execute the request at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutgoingTypedLinksRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    if "filter_attribute_ranges" in value:
        import aws_sdk_clouddirectory.types.typed_link_attribute_range_list

        out["FilterAttributeRanges"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_range_list.serialize_json(
                value["filter_attribute_ranges"]
            )
        )
    if "filter_typed_link" in value:
        import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name

        out["FilterTypedLink"] = (
            aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.serialize_json(
                value["filter_typed_link"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "consistency_level" in value:
        import aws_sdk_clouddirectory.types.consistency_level

        out["ConsistencyLevel"] = (
            aws_sdk_clouddirectory.types.consistency_level.serialize_json(
                value["consistency_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListOutgoingTypedLinksRequest:
    out: ListOutgoingTypedLinksRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "ListOutgoingTypedLinksRequest.object_reference required"
        )
    if "FilterAttributeRanges" in data:
        import aws_sdk_clouddirectory.types.typed_link_attribute_range_list

        out["filter_attribute_ranges"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_range_list.deserialize_json(
                data["FilterAttributeRanges"]
            )
        )
    if "FilterTypedLink" in data:
        import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name

        out["filter_typed_link"] = (
            aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.deserialize_json(
                data["FilterTypedLink"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ConsistencyLevel" in data:
        import aws_sdk_clouddirectory.types.consistency_level

        out["consistency_level"] = (
            aws_sdk_clouddirectory.types.consistency_level.deserialize_json(
                data["ConsistencyLevel"]
            )
        )
    return out
