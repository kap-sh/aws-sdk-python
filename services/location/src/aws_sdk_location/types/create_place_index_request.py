"""Generated from Smithy shape ``com.amazonaws.location#CreatePlaceIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.data_source_configuration
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map


class CreatePlaceIndexRequest(TypedDict):
    index_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource. </p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique place index resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExamplePlaceIndex</code>.</p> </li> </ul>"""
    data_source: "str"
    """<p>Specifies the geospatial data provider for the new place index.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/esri.html\">Esri</a>'s coverage in your region of interest, see <a href=\"https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm\">Esri details on geocoding coverage</a>.</p> </li> <li> <p> <code>Grab</code> – Grab provides place index functionality for Southeast Asia. For additional information about <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/grab.html\">GrabMaps</a>' coverage, see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area\">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/HERE.html\">HERE Technologies</a>' coverage in your region of interest, see <a href=\"https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html\">HERE details on goecoding coverage</a>.</p> <important> <p>If you specify HERE Technologies (<code>Here</code>) as the data provider, you may not <a href=\"https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html\">store results</a> for locations in Japan. For more information, see the <a href=\"http://aws.amazon.com/service-terms/\">Amazon Web Services service terms</a> for Amazon Location Service.</p> </important> </li> </ul> <p>For additional information , see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html\">Data providers</a> on the <i>Amazon Location Service developer guide</i>.</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    description: NotRequired[
        "aws_sdk_location.types.resource_description.ResourceDescription"
    ]
    """<p>The optional description for the place index resource.</p>"""
    data_source_configuration: NotRequired[
        "aws_sdk_location.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Specifies the data storage option requesting Places.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>\"key\" : \"value\"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use \"aws:\" as a prefix for a key.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePlaceIndexRequest) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    out["DataSource"] = value["data_source"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_source_configuration" in value:
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


def deserialize_json(data: dict) -> CreatePlaceIndexRequest:
    out: CreatePlaceIndexRequest = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("CreatePlaceIndexRequest.index_name required")
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("CreatePlaceIndexRequest.data_source required")
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataSourceConfiguration" in data:
        import aws_sdk_location.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_location.types.data_source_configuration.deserialize_json(
                data["DataSourceConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    return out
