"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_arn_model
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.ping_beacon


class LocationModel(TypedDict):
    location_name: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The location's name.</p>"""
    location_arn: NotRequired[
        "aws_sdk_gamelift.types.location_arn_model.LocationArnModel"
    ]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a custom location resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    ping_beacon: NotRequired["aws_sdk_gamelift.types.ping_beacon.PingBeacon"]
    """<p>Information about the UDP ping beacon for this location. Ping beacons are fixed endpoints that you can use to measure network latency between a player device and an Amazon GameLift Servers hosting location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationModel) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "ping_beacon" in value:
        import aws_sdk_gamelift.types.ping_beacon

        out["PingBeacon"] = aws_sdk_gamelift.types.ping_beacon.serialize_aws_json_1_1(
            value["ping_beacon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationModel:
    out: LocationModel = {}  # type: ignore[typeddict-item]
    if "LocationName" in data:
        out["location_name"] = data["LocationName"]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "PingBeacon" in data:
        import aws_sdk_gamelift.types.ping_beacon

        out["ping_beacon"] = (
            aws_sdk_gamelift.types.ping_beacon.deserialize_aws_json_1_1(
                data["PingBeacon"]
            )
        )
    return out
