"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.dimension_list
    import aws_sdk_customer_profiles.types.include_options
    import aws_sdk_customer_profiles.types.source_segment_list


class Group(TypedDict, closed=True):
    dimensions: NotRequired[
        "aws_sdk_customer_profiles.types.dimension_list.DimensionList"
    ]
    """<p>Defines the attributes to segment on.</p>"""
    source_segments: NotRequired[
        "aws_sdk_customer_profiles.types.source_segment_list.SourceSegmentList"
    ]
    """<p>Defines the starting source of data.</p>"""
    source_type: "aws_sdk_customer_profiles.types.include_options.IncludeOptions"
    """<p>Defines how to interact with the source data.</p>"""
    type: "aws_sdk_customer_profiles.types.include_options.IncludeOptions"
    """<p>Defines how to interact with the profiles found in the current filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_customer_profiles.types.dimension_list

        out["Dimensions"] = (
            aws_sdk_customer_profiles.types.dimension_list.serialize_json(
                value["dimensions"]
            )
        )
    if "source_segments" in value:
        import aws_sdk_customer_profiles.types.source_segment_list

        out["SourceSegments"] = (
            aws_sdk_customer_profiles.types.source_segment_list.serialize_json(
                value["source_segments"]
            )
        )
    import aws_sdk_customer_profiles.types.include_options

    out["SourceType"] = aws_sdk_customer_profiles.types.include_options.serialize_json(
        value.get("source_type", "ALL")
    )
    import aws_sdk_customer_profiles.types.include_options

    out["Type"] = aws_sdk_customer_profiles.types.include_options.serialize_json(
        value.get("type", "ALL")
    )
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_customer_profiles.types.dimension_list

        out["dimensions"] = (
            aws_sdk_customer_profiles.types.dimension_list.deserialize_json(
                data["Dimensions"]
            )
        )
    if "SourceSegments" in data:
        import aws_sdk_customer_profiles.types.source_segment_list

        out["source_segments"] = (
            aws_sdk_customer_profiles.types.source_segment_list.deserialize_json(
                data["SourceSegments"]
            )
        )
    if "SourceType" in data:
        import aws_sdk_customer_profiles.types.include_options

        out["source_type"] = (
            aws_sdk_customer_profiles.types.include_options.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        out["source_type"] = "ALL"
    if "Type" in data:
        import aws_sdk_customer_profiles.types.include_options

        out["type"] = aws_sdk_customer_profiles.types.include_options.deserialize_json(
            data["Type"]
        )
    else:
        out["type"] = "ALL"
    return out
