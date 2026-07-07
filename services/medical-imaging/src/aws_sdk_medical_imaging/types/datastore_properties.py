"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.datastore_name
    import aws_sdk_medical_imaging.types.datastore_status
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.kms_key_arn
    import aws_sdk_medical_imaging.types.lambda_arn
    import aws_sdk_medical_imaging.types.lossless_storage_format


class DatastoreProperties(TypedDict, closed=True):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_name: "aws_sdk_medical_imaging.types.datastore_name.DatastoreName"
    """<p>The data store name.</p>"""
    datastore_status: "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    kms_key_arn: NotRequired["aws_sdk_medical_imaging.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>"""
    lambda_authorizer_arn: NotRequired[
        "aws_sdk_medical_imaging.types.lambda_arn.LambdaArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    lossless_storage_format: NotRequired[
        "aws_sdk_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
    ]
    """<p>The datastore's lossless storage format.</p>"""
    datastore_arn: NotRequired["aws_sdk_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the data store.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreProperties) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["datastoreName"] = value["datastore_name"]
    import aws_sdk_medical_imaging.types.datastore_status

    out["datastoreStatus"] = (
        aws_sdk_medical_imaging.types.datastore_status.serialize_json(
            value["datastore_status"]
        )
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
    if "datastore_arn" in value:
        out["datastoreArn"] = value["datastore_arn"]
    if "created_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["createdAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["updatedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DatastoreProperties:
    out: DatastoreProperties = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DatastoreProperties.datastore_id required")
    if "datastoreName" in data:
        out["datastore_name"] = data["datastoreName"]
    else:
        raise DeserializationError("DatastoreProperties.datastore_name required")
    if "datastoreStatus" in data:
        import aws_sdk_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        raise DeserializationError("DatastoreProperties.datastore_status required")
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
    if "datastoreArn" in data:
        out["datastore_arn"] = data["datastoreArn"]
    if "createdAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["created_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["updated_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    return out
