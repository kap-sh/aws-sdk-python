"""Generated from Smithy shape ``com.amazonaws.location#CreateMapResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class CreateMapResponse(TypedDict, closed=True):
    map_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the map resource.</p>"""
    map_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:map/ExampleMap</code> </p> </li> </ul>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the map resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMapResponse) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    out["MapArn"] = value["map_arn"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateMapResponse:
    out: CreateMapResponse = {}  # type: ignore[typeddict-item]
    if "MapName" in data:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("CreateMapResponse.map_name required")
    if "MapArn" in data:
        out["map_arn"] = data["MapArn"]
    else:
        raise DeserializationError("CreateMapResponse.map_arn required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreateMapResponse.create_time required")
    return out
