"""Generated from Smithy shape ``com.amazonaws.location#DescribePlaceIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.data_source_configuration
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map
    import aws_sdk_location.types.timestamp


class DescribePlaceIndexResponse(TypedDict):
    index_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource being described.</p>"""
    index_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex</code> </p> </li> </ul>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    description: "aws_sdk_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the place index resource.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the place index resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the place index resource was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    data_source: "str"
    """<p>The data provider of geospatial data. Values can be one of the following:</p> <ul> <li> <p> <code>Esri</code> </p> </li> <li> <p> <code>Grab</code> </p> </li> <li> <p> <code>Here</code> </p> </li> </ul> <p>For more information about data providers, see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html\">Amazon Location Service data providers</a>.</p>"""
    data_source_configuration: (
        "aws_sdk_location.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The specified data storage option for requesting Places.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>Tags associated with place index resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePlaceIndexResponse) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    out["IndexArn"] = value["index_arn"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    out["Description"] = value["description"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    out["DataSource"] = value["data_source"]
    import aws_sdk_location.types.data_source_configuration

    out["DataSourceConfiguration"] = (
        aws_sdk_location.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    if "tags" in value:
        import aws_sdk_location.types.tag_map

        out["Tags"] = aws_sdk_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePlaceIndexResponse:
    out: DescribePlaceIndexResponse = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("DescribePlaceIndexResponse.index_name required")
    if "IndexArn" in data:
        out["index_arn"] = data["IndexArn"]
    else:
        raise DeserializationError("DescribePlaceIndexResponse.index_arn required")
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribePlaceIndexResponse.description required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("DescribePlaceIndexResponse.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("DescribePlaceIndexResponse.update_time required")
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("DescribePlaceIndexResponse.data_source required")
    if "DataSourceConfiguration" in data:
        import aws_sdk_location.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_location.types.data_source_configuration.deserialize_json(
                data["DataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePlaceIndexResponse.data_source_configuration required"
        )
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    return out
