"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.segment_group_structure
    import aws_sdk_customer_profiles.types.sensitive_string1_to50000


class CreateSegmentEstimateRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_query: NotRequired[
        "aws_sdk_customer_profiles.types.segment_group_structure.SegmentGroupStructure"
    ]
    """<p>The segment query for calculating a segment estimate.</p>"""
    segment_sql_query: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
    ]
    """<p>The segment SQL query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentEstimateRequest) -> dict:
    out: dict = {}
    if "segment_query" in value:
        import aws_sdk_customer_profiles.types.segment_group_structure

        out["SegmentQuery"] = (
            aws_sdk_customer_profiles.types.segment_group_structure.serialize_json(
                value["segment_query"]
            )
        )
    if "segment_sql_query" in value:
        out["SegmentSqlQuery"] = value["segment_sql_query"]
    return out


def deserialize_json(data: dict) -> CreateSegmentEstimateRequest:
    out: CreateSegmentEstimateRequest = {}  # type: ignore[typeddict-item]
    if "SegmentQuery" in data:
        import aws_sdk_customer_profiles.types.segment_group_structure

        out["segment_query"] = (
            aws_sdk_customer_profiles.types.segment_group_structure.deserialize_json(
                data["SegmentQuery"]
            )
        )
    if "SegmentSqlQuery" in data:
        out["segment_sql_query"] = data["SegmentSqlQuery"]
    return out
