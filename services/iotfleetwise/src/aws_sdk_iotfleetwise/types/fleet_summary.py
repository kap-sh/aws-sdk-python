"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#FleetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.fleet_id
    import aws_sdk_iotfleetwise.types.timestamp


class FleetSummary(TypedDict, closed=True):
    id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId"
    """<p>The unique ID of the fleet.</p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the fleet.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the fleet.</p>"""
    signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The ARN of the signal catalog associated with the fleet.</p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the fleet was created, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: NotRequired[
        "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    ]
    """<p>The time the fleet was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FleetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    import aws_sdk_iotfleetwise.types.timestamp

    out["creationTime"] = aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    if "last_modification_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FleetSummary:
    out: FleetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FleetSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("FleetSummary.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError("FleetSummary.signal_catalog_arn required")
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("FleetSummary.creation_time required")
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    return out
