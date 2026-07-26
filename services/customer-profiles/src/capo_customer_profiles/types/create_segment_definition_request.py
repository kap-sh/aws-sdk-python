"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.segment_group
    import capo_customer_profiles.types.segment_sort
    import capo_customer_profiles.types.sensitive_string1_to4000
    import capo_customer_profiles.types.sensitive_string1_to50000
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map


class CreateSegmentDefinitionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition.</p>"""
    display_name: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The display name of the segment definition.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to4000.sensitiveString1To4000"
    ]
    """<p>The description of the segment definition.</p>"""
    segment_groups: NotRequired[
        "capo_customer_profiles.types.segment_group.SegmentGroup"
    ]
    """<p>Specifies the base segments and dimensions for a segment definition along with their respective relationship.</p>"""
    segment_sql_query: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
    ]
    """<p>The segment SQL query.</p>"""
    segment_sort: NotRequired["capo_customer_profiles.types.segment_sort.SegmentSort"]
    """<p>The segment sort.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentDefinitionRequest) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_groups" in value:
        import capo_customer_profiles.types.segment_group

        out["SegmentGroups"] = (
            capo_customer_profiles.types.segment_group.serialize_json(
                value["segment_groups"]
            )
        )
    if "segment_sql_query" in value:
        out["SegmentSqlQuery"] = value["segment_sql_query"]
    if "segment_sort" in value:
        import capo_customer_profiles.types.segment_sort

        out["SegmentSort"] = capo_customer_profiles.types.segment_sort.serialize_json(
            value["segment_sort"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSegmentDefinitionRequest:
    out: CreateSegmentDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError(
            "CreateSegmentDefinitionRequest.display_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "SegmentGroups" in data:
        import capo_customer_profiles.types.segment_group

        out["segment_groups"] = (
            capo_customer_profiles.types.segment_group.deserialize_json(
                data["SegmentGroups"]
            )
        )
    if "SegmentSqlQuery" in data:
        out["segment_sql_query"] = data["SegmentSqlQuery"]
    if "SegmentSort" in data:
        import capo_customer_profiles.types.segment_sort

        out["segment_sort"] = (
            capo_customer_profiles.types.segment_sort.deserialize_json(
                data["SegmentSort"]
            )
        )
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
