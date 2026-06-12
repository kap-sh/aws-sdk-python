"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributeDefinitionItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.readiness_status
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class ListCalculatedAttributeDefinitionItem(TypedDict):
    calculated_attribute_name: NotRequired[
        "aws_sdk_customer_profiles.types.type_name.typeName"
    ]
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.display_name.displayName"
    ]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The threshold for the calculated attribute.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The threshold for the calculated attribute.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was most recently edited.</p>"""
    use_historical_data: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.readiness_status.ReadinessStatus"
    ]
    """<p>Status of the Calculated Attribute creation (whether all historical data has been indexed.)</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributeDefinitionItem) -> dict:
    out: dict = {}
    if "calculated_attribute_name" in value:
        out["CalculatedAttributeName"] = value["calculated_attribute_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "status" in value:
        import aws_sdk_customer_profiles.types.readiness_status

        out["Status"] = aws_sdk_customer_profiles.types.readiness_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributeDefinitionItem:
    out: ListCalculatedAttributeDefinitionItem = {}  # type: ignore[typeddict-item]
    if "CalculatedAttributeName" in data:
        out["calculated_attribute_name"] = data["CalculatedAttributeName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "UseHistoricalData" in data:
        out["use_historical_data"] = data["UseHistoricalData"]
    if "Status" in data:
        import aws_sdk_customer_profiles.types.readiness_status

        out["status"] = (
            aws_sdk_customer_profiles.types.readiness_status.deserialize_json(
                data["Status"]
            )
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
