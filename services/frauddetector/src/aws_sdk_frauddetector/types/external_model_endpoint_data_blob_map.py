"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelEndpointDataBlobMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_endpoint_data_blob
    import aws_sdk_frauddetector.types.sage_maker_endpoint_identifier

ExternalModelEndpointDataBlobMap: TypeAlias = dict[
    "aws_sdk_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier",
    "aws_sdk_frauddetector.types.model_endpoint_data_blob.ModelEndpointDataBlob",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: ExternalModelEndpointDataBlobMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_frauddetector.types.model_endpoint_data_blob

        out[key] = (
            aws_sdk_frauddetector.types.model_endpoint_data_blob.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalModelEndpointDataBlobMap:
    out: ExternalModelEndpointDataBlobMap = {}
    for key, value in data.items():
        import aws_sdk_frauddetector.types.model_endpoint_data_blob

        out[key] = (
            aws_sdk_frauddetector.types.model_endpoint_data_blob.deserialize_aws_json_1_1(
                value
            )
        )
    return out
