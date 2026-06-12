"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetDecoderManifestResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.manifest_status
    import aws_sdk_iotfleetwise.types.message
    import aws_sdk_iotfleetwise.types.string
    import aws_sdk_iotfleetwise.types.timestamp


class GetDecoderManifestResponse(TypedDict):
    name: "aws_sdk_iotfleetwise.types.string.string"
    """<p> The name of the decoder manifest. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the decoder manifest. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the decoder manifest.</p>"""
    model_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The ARN of a vehicle model (model manifest) associated with the decoder manifest.</p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is marked <code>DRAFT</code>, you can edit the decoder manifest.</p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    message: NotRequired["aws_sdk_iotfleetwise.types.message.message"]
    """<p>The detailed message for the decoder manifest. When a decoder manifest is in an <code>INVALID</code> status, the message contains detailed reason and help information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDecoderManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "model_manifest_arn" in value:
        out["modelManifestArn"] = value["model_manifest_arn"]
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
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDecoderManifestResponse:
    out: GetDecoderManifestResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDecoderManifestResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDecoderManifestResponse.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "modelManifestArn" in data:
        out["model_manifest_arn"] = data["modelManifestArn"]
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
        raise DeserializationError("GetDecoderManifestResponse.creation_time required")
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetDecoderManifestResponse.last_modification_time required"
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
