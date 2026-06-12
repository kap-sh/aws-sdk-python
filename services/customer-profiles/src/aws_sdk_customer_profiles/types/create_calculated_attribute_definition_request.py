"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateCalculatedAttributeDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_details
    import aws_sdk_customer_profiles.types.conditions
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.filter
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.statistic
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.type_name


class CreateCalculatedAttributeDefinitionRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    calculated_attribute_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.display_name.displayName"
    ]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the calculated attribute.</p>"""
    attribute_details: (
        "aws_sdk_customer_profiles.types.attribute_details.AttributeDetails"
    )
    """<p>Mathematical expression and a list of attribute items specified in that expression.</p>"""
    conditions: NotRequired["aws_sdk_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""
    filter: NotRequired["aws_sdk_customer_profiles.types.filter.Filter"]
    """<p>Defines how to filter incoming objects to include part of the Calculated Attribute.</p>"""
    statistic: "aws_sdk_customer_profiles.types.statistic.Statistic"
    """<p>The aggregation operation to perform for the calculated attribute.</p>"""
    use_historical_data: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCalculatedAttributeDefinitionRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_customer_profiles.types.attribute_details

    out["AttributeDetails"] = (
        aws_sdk_customer_profiles.types.attribute_details.serialize_json(
            value["attribute_details"]
        )
    )
    if "conditions" in value:
        import aws_sdk_customer_profiles.types.conditions

        out["Conditions"] = aws_sdk_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    if "filter" in value:
        import aws_sdk_customer_profiles.types.filter

        out["Filter"] = aws_sdk_customer_profiles.types.filter.serialize_json(
            value["filter"]
        )
    import aws_sdk_customer_profiles.types.statistic

    out["Statistic"] = aws_sdk_customer_profiles.types.statistic.serialize_json(
        value["statistic"]
    )
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCalculatedAttributeDefinitionRequest:
    out: CreateCalculatedAttributeDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AttributeDetails" in data:
        import aws_sdk_customer_profiles.types.attribute_details

        out["attribute_details"] = (
            aws_sdk_customer_profiles.types.attribute_details.deserialize_json(
                data["AttributeDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCalculatedAttributeDefinitionRequest.attribute_details required"
        )
    if "Conditions" in data:
        import aws_sdk_customer_profiles.types.conditions

        out["conditions"] = aws_sdk_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    if "Filter" in data:
        import aws_sdk_customer_profiles.types.filter

        out["filter"] = aws_sdk_customer_profiles.types.filter.deserialize_json(
            data["Filter"]
        )
    if "Statistic" in data:
        import aws_sdk_customer_profiles.types.statistic

        out["statistic"] = aws_sdk_customer_profiles.types.statistic.deserialize_json(
            data["Statistic"]
        )
    else:
        raise DeserializationError(
            "CreateCalculatedAttributeDefinitionRequest.statistic required"
        )
    if "UseHistoricalData" in data:
        out["use_historical_data"] = data["UseHistoricalData"]
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
