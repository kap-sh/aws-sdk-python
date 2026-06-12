"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetModelManifestResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.manifest_status
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.timestamp


class GetModelManifestResponse(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the vehicle model. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    signal_catalog_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of the signal catalog associated with the vehicle model. </p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. You can edit the vehicle model if the status is marked <code>DRAFT</code>.</p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p>The last time the vehicle model was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetModelManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "status" in value:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    import aws_sdk_iotfleetwise.types.timestamp

    out["creationTime"] = aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import aws_sdk_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetModelManifestResponse:
    out: GetModelManifestResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetModelManifestResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetModelManifestResponse.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if "status" in data:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("GetModelManifestResponse.creation_time required")
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelManifestResponse.last_modification_time required"
        )
    return out
