"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers
    import aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response


class BatchGetRecordRequest(TypedDict, closed=True):
    identifiers: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers.BatchGetRecordIdentifiers"
    ]
    """<p>A list containing the name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code>, the list of names of <code>Feature</code>s to be retrieved, and the corresponding <code>RecordIdentifier</code> values as strings.</p>"""
    expiration_time_response: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
    ]
    """<p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>BatchGetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>BatchGetRecord</code> will return null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordRequest) -> dict:
    out: dict = {}
    if "identifiers" in value:
        import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers

        out["Identifiers"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers.serialize_json(
                value["identifiers"]
            )
        )
    if "expiration_time_response" in value:
        import aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response

        out["ExpirationTimeResponse"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response.serialize_json(
                value["expiration_time_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetRecordRequest:
    out: BatchGetRecordRequest = {}  # type: ignore[typeddict-item]
    if "Identifiers" in data:
        import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers

        out["identifiers"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers.deserialize_json(
                data["Identifiers"]
            )
        )
    if "ExpirationTimeResponse" in data:
        import aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response

        out["expiration_time_response"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response.deserialize_json(
                data["ExpirationTimeResponse"]
            )
        )
    return out
