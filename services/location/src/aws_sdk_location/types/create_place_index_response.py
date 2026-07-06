"""Generated from Smithy shape ``com.amazonaws.location#CreatePlaceIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class CreatePlaceIndexResponse(TypedDict, closed=True):
    index_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name for the place index resource.</p>"""
    index_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex</code> </p> </li> </ul>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the place index resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePlaceIndexResponse) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    out["IndexArn"] = value["index_arn"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreatePlaceIndexResponse:
    out: CreatePlaceIndexResponse = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("CreatePlaceIndexResponse.index_name required")
    if "IndexArn" in data:
        out["index_arn"] = data["IndexArn"]
    else:
        raise DeserializationError("CreatePlaceIndexResponse.index_arn required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreatePlaceIndexResponse.create_time required")
    return out
