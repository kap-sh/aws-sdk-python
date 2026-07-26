"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.fleet_id
    import capo_iotfleetwise.types.timestamp


class GetFleetResponse(TypedDict, closed=True):
    id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the fleet.</p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the fleet. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the fleet. </p>"""
    signal_catalog_arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The ARN of a signal catalog associated with the fleet. </p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the fleet was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the fleet was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFleetResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    import capo_iotfleetwise.types.timestamp

    out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import capo_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFleetResponse:
    out: GetFleetResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetFleetResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetFleetResponse.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError("GetFleetResponse.signal_catalog_arn required")
    if "creationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("GetFleetResponse.creation_time required")
    if "lastModificationTime" in data:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError("GetFleetResponse.last_modification_time required")
    return out
