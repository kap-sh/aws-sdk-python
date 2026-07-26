"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelEndpointDataBlobMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model_endpoint_data_blob
    import capo_frauddetector.types.sage_maker_endpoint_identifier

ExternalModelEndpointDataBlobMap: TypeAlias = dict[
    "capo_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier",
    "capo_frauddetector.types.model_endpoint_data_blob.ModelEndpointDataBlob",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: ExternalModelEndpointDataBlobMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_frauddetector.types.model_endpoint_data_blob

        out[key] = (
            capo_frauddetector.types.model_endpoint_data_blob.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalModelEndpointDataBlobMap:
    out: ExternalModelEndpointDataBlobMap = {}
    for key, value in data.items():
        import capo_frauddetector.types.model_endpoint_data_blob

        out[key] = (
            capo_frauddetector.types.model_endpoint_data_blob.deserialize_aws_json_1_1(
                value
            )
        )
    return out
