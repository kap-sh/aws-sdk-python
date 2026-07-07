"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetCalculatedAttributeDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_details
    import aws_sdk_customer_profiles.types.conditions
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.filter
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.readiness
    import aws_sdk_customer_profiles.types.readiness_status
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.statistic
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class GetCalculatedAttributeDefinitionResponse(TypedDict, closed=True):
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
    """<p>The description of the calculated attribute.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was most recently edited.</p>"""
    statistic: NotRequired["aws_sdk_customer_profiles.types.statistic.Statistic"]
    """<p>The aggregation operation to perform for the calculated attribute.</p>"""
    filter: NotRequired["aws_sdk_customer_profiles.types.filter.Filter"]
    """<p>The filter assigned to this calculated attribute definition.</p>"""
    conditions: NotRequired["aws_sdk_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""
    attribute_details: NotRequired[
        "aws_sdk_customer_profiles.types.attribute_details.AttributeDetails"
    ]
    """<p>Mathematical expression and a list of attribute items specified in that expression.</p>"""
    use_historical_data: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.readiness_status.ReadinessStatus"
    ]
    """<p>Status of the Calculated Attribute creation (whether all historical data has been indexed).</p>"""
    readiness: NotRequired["aws_sdk_customer_profiles.types.readiness.Readiness"]
    """<p>Information indicating if the Calculated Attribute is ready for use by confirming all historical data has been processed and reflected.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCalculatedAttributeDefinitionResponse) -> dict:
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
    if "statistic" in value:
        import aws_sdk_customer_profiles.types.statistic

        out["Statistic"] = aws_sdk_customer_profiles.types.statistic.serialize_json(
            value["statistic"]
        )
    if "filter" in value:
        import aws_sdk_customer_profiles.types.filter

        out["Filter"] = aws_sdk_customer_profiles.types.filter.serialize_json(
            value["filter"]
        )
    if "conditions" in value:
        import aws_sdk_customer_profiles.types.conditions

        out["Conditions"] = aws_sdk_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    if "attribute_details" in value:
        import aws_sdk_customer_profiles.types.attribute_details

        out["AttributeDetails"] = (
            aws_sdk_customer_profiles.types.attribute_details.serialize_json(
                value["attribute_details"]
            )
        )
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "status" in value:
        import aws_sdk_customer_profiles.types.readiness_status

        out["Status"] = aws_sdk_customer_profiles.types.readiness_status.serialize_json(
            value["status"]
        )
    if "readiness" in value:
        import aws_sdk_customer_profiles.types.readiness

        out["Readiness"] = aws_sdk_customer_profiles.types.readiness.serialize_json(
            value["readiness"]
        )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetCalculatedAttributeDefinitionResponse:
    out: GetCalculatedAttributeDefinitionResponse = {}  # type: ignore[typeddict-item]
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
    if "Statistic" in data:
        import aws_sdk_customer_profiles.types.statistic

        out["statistic"] = aws_sdk_customer_profiles.types.statistic.deserialize_json(
            data["Statistic"]
        )
    if "Filter" in data:
        import aws_sdk_customer_profiles.types.filter

        out["filter"] = aws_sdk_customer_profiles.types.filter.deserialize_json(
            data["Filter"]
        )
    if "Conditions" in data:
        import aws_sdk_customer_profiles.types.conditions

        out["conditions"] = aws_sdk_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    if "AttributeDetails" in data:
        import aws_sdk_customer_profiles.types.attribute_details

        out["attribute_details"] = (
            aws_sdk_customer_profiles.types.attribute_details.deserialize_json(
                data["AttributeDetails"]
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
    if "Readiness" in data:
        import aws_sdk_customer_profiles.types.readiness

        out["readiness"] = aws_sdk_customer_profiles.types.readiness.deserialize_json(
            data["Readiness"]
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
