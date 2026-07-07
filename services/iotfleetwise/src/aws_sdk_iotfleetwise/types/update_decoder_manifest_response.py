"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateDecoderManifestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.resource_name


class UpdateDecoderManifestResponse(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the updated decoder manifest. </p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the updated decoder manifest. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDecoderManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDecoderManifestResponse:
    out: UpdateDecoderManifestResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateDecoderManifestResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateDecoderManifestResponse.arn required")
    return out
