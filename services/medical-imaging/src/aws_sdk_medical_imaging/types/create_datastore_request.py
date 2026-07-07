"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CreateDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.client_token
    import aws_sdk_medical_imaging.types.datastore_name
    import aws_sdk_medical_imaging.types.kms_key_arn
    import aws_sdk_medical_imaging.types.lambda_arn
    import aws_sdk_medical_imaging.types.lossless_storage_format
    import aws_sdk_medical_imaging.types.tag_map


class CreateDatastoreRequest(TypedDict, closed=True):
    datastore_name: NotRequired[
        "aws_sdk_medical_imaging.types.datastore_name.DatastoreName"
    ]
    """<p>The data store name.</p>"""
    client_token: "aws_sdk_medical_imaging.types.client_token.ClientToken"
    """<p>A unique identifier for API idempotency.</p>"""
    tags: NotRequired["aws_sdk_medical_imaging.types.tag_map.TagMap"]
    """<p>The tags provided when creating a data store.</p>"""
    kms_key_arn: NotRequired["aws_sdk_medical_imaging.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>"""
    lambda_authorizer_arn: NotRequired[
        "aws_sdk_medical_imaging.types.lambda_arn.LambdaArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    lossless_storage_format: NotRequired[
        "aws_sdk_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
    ]
    """<p>The lossless storage format for the datastore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatastoreRequest) -> dict:
    out: dict = {}
    if "datastore_name" in value:
        out["datastoreName"] = value["datastore_name"]
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_medical_imaging.types.tag_map

        out["tags"] = aws_sdk_medical_imaging.types.tag_map.serialize_json(
            value["tags"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "lambda_authorizer_arn" in value:
        out["lambdaAuthorizerArn"] = value["lambda_authorizer_arn"]
    if "lossless_storage_format" in value:
        import aws_sdk_medical_imaging.types.lossless_storage_format

        out["losslessStorageFormat"] = (
            aws_sdk_medical_imaging.types.lossless_storage_format.serialize_json(
                value["lossless_storage_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDatastoreRequest:
    out: CreateDatastoreRequest = {}  # type: ignore[typeddict-item]
    if "datastoreName" in data:
        out["datastore_name"] = data["datastoreName"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateDatastoreRequest.client_token required")
    if "tags" in data:
        import aws_sdk_medical_imaging.types.tag_map

        out["tags"] = aws_sdk_medical_imaging.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "lambdaAuthorizerArn" in data:
        out["lambda_authorizer_arn"] = data["lambdaAuthorizerArn"]
    if "losslessStorageFormat" in data:
        import aws_sdk_medical_imaging.types.lossless_storage_format

        out["lossless_storage_format"] = (
            aws_sdk_medical_imaging.types.lossless_storage_format.deserialize_json(
                data["losslessStorageFormat"]
            )
        )
    return out
