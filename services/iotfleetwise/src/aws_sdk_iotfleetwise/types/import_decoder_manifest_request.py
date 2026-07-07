"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ImportDecoderManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.network_file_definitions
    import aws_sdk_iotfleetwise.types.resource_name


class ImportDecoderManifestRequest(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the decoder manifest to import. </p>"""
    network_file_definitions: (
        "aws_sdk_iotfleetwise.types.network_file_definitions.NetworkFileDefinitions"
    )
    """<p> The file to load into an Amazon Web Services account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDecoderManifestRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.network_file_definitions

    out["networkFileDefinitions"] = (
        aws_sdk_iotfleetwise.types.network_file_definitions.serialize_aws_json_1_0(
            value["network_file_definitions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDecoderManifestRequest:
    out: ImportDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if "networkFileDefinitions" in data:
        import aws_sdk_iotfleetwise.types.network_file_definitions

        out["network_file_definitions"] = (
            aws_sdk_iotfleetwise.types.network_file_definitions.deserialize_aws_json_1_0(
                data["networkFileDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "ImportDecoderManifestRequest.network_file_definitions required"
        )
    return out
