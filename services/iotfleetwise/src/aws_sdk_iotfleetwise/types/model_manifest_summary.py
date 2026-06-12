"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ModelManifestSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.manifest_status
    import aws_sdk_iotfleetwise.types.string
    import aws_sdk_iotfleetwise.types.timestamp


class ModelManifestSummary(TypedDict):
    name: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>The name of the vehicle model.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the vehicle model.</p>"""
    signal_catalog_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the signal catalog associated with the vehicle model.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the vehicle model.</p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p>The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model.</p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle model was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelManifestSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_aws_json_1_0(data: dict) -> ModelManifestSummary:
    out: ModelManifestSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if "description" in data:
        out["description"] = data["description"]
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
        raise DeserializationError("ModelManifestSummary.creation_time required")
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ModelManifestSummary.last_modification_time required"
        )
    return out
