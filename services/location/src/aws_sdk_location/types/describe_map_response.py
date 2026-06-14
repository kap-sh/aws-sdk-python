"""Generated from Smithy shape ``com.amazonaws.location#DescribeMapResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.map_configuration
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map
    import aws_sdk_location.types.timestamp


class DescribeMapResponse(TypedDict):
    map_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The map style selected from an available provider.</p>"""
    map_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:map/ExampleMap</code> </p> </li> </ul>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    data_source: "str"
    """<p>Specifies the data provider for the associated map tiles.</p>"""
    configuration: "aws_sdk_location.types.map_configuration.MapConfiguration"
    """<p>Specifies the map tile style selected from a partner data provider.</p>"""
    description: "aws_sdk_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the map resource.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>Tags associated with the map resource.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the map resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the map resource was last update in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMapResponse) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    out["MapArn"] = value["map_arn"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    out["DataSource"] = value["data_source"]
    import aws_sdk_location.types.map_configuration

    out["Configuration"] = aws_sdk_location.types.map_configuration.serialize_json(
        value["configuration"]
    )
    out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_location.types.tag_map

        out["Tags"] = aws_sdk_location.types.tag_map.serialize_json(value["tags"])
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> DescribeMapResponse:
    out: DescribeMapResponse = {}  # type: ignore[typeddict-item]
    if "MapName" in data:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("DescribeMapResponse.map_name required")
    if "MapArn" in data:
        out["map_arn"] = data["MapArn"]
    else:
        raise DeserializationError("DescribeMapResponse.map_arn required")
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("DescribeMapResponse.data_source required")
    if "Configuration" in data:
        import aws_sdk_location.types.map_configuration

        out["configuration"] = (
            aws_sdk_location.types.map_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("DescribeMapResponse.configuration required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribeMapResponse.description required")
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("DescribeMapResponse.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("DescribeMapResponse.update_time required")
    return out
