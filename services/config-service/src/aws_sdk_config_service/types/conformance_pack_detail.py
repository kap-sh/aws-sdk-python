"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_arn
    import aws_sdk_config_service.types.conformance_pack_id
    import aws_sdk_config_service.types.conformance_pack_input_parameters
    import aws_sdk_config_service.types.conformance_pack_name
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.delivery_s3_bucket
    import aws_sdk_config_service.types.delivery_s3_key_prefix
    import aws_sdk_config_service.types.string_with_char_limit256
    import aws_sdk_config_service.types.template_ssm_document_details


class ConformancePackDetail(TypedDict):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_arn: (
        "aws_sdk_config_service.types.conformance_pack_arn.ConformancePackArn"
    )
    """<p>Amazon Resource Name (ARN) of the conformance pack.</p>"""
    conformance_pack_id: (
        "aws_sdk_config_service.types.conformance_pack_id.ConformancePackId"
    )
    """<p>ID of the conformance pack.</p>"""
    delivery_s3_bucket: NotRequired[
        "aws_sdk_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
    ]
    """<p>The name of the Amazon S3 bucket where Config stores conformance pack templates. </p> <note> <p>This field is optional.</p> </note>"""
    delivery_s3_key_prefix: NotRequired[
        "aws_sdk_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
    ]
    """<p>The prefix for the Amazon S3 bucket.</p> <note> <p>This field is optional.</p> </note>"""
    conformance_pack_input_parameters: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
    ]
    """<p>A list of <code>ConformancePackInputParameter</code> objects.</p>"""
    last_update_requested_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The last time a conformation pack update was requested. </p>"""
    created_by: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The Amazon Web Services service that created the conformance pack.</p>"""
    template_ssm_document_details: NotRequired[
        "aws_sdk_config_service.types.template_ssm_document_details.TemplateSSMDocumentDetails"
    ]
    """<p>An object that contains the name or Amazon Resource Name (ARN) of the Amazon Web Services Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackDetail) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    out["ConformancePackArn"] = value["conformance_pack_arn"]
    out["ConformancePackId"] = value["conformance_pack_id"]
    if "delivery_s3_bucket" in value:
        out["DeliveryS3Bucket"] = value["delivery_s3_bucket"]
    if "delivery_s3_key_prefix" in value:
        out["DeliveryS3KeyPrefix"] = value["delivery_s3_key_prefix"]
    if "conformance_pack_input_parameters" in value:
        import aws_sdk_config_service.types.conformance_pack_input_parameters

        out["ConformancePackInputParameters"] = (
            aws_sdk_config_service.types.conformance_pack_input_parameters.serialize_aws_json_1_1(
                value["conformance_pack_input_parameters"]
            )
        )
    if "last_update_requested_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdateRequestedTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_requested_time"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "template_ssm_document_details" in value:
        import aws_sdk_config_service.types.template_ssm_document_details

        out["TemplateSSMDocumentDetails"] = (
            aws_sdk_config_service.types.template_ssm_document_details.serialize_aws_json_1_1(
                value["template_ssm_document_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackDetail:
    out: ConformancePackDetail = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "ConformancePackDetail.conformance_pack_name required"
        )
    if "ConformancePackArn" in data:
        out["conformance_pack_arn"] = data["ConformancePackArn"]
    else:
        raise DeserializationError(
            "ConformancePackDetail.conformance_pack_arn required"
        )
    if "ConformancePackId" in data:
        out["conformance_pack_id"] = data["ConformancePackId"]
    else:
        raise DeserializationError("ConformancePackDetail.conformance_pack_id required")
    if "DeliveryS3Bucket" in data:
        out["delivery_s3_bucket"] = data["DeliveryS3Bucket"]
    if "DeliveryS3KeyPrefix" in data:
        out["delivery_s3_key_prefix"] = data["DeliveryS3KeyPrefix"]
    if "ConformancePackInputParameters" in data:
        import aws_sdk_config_service.types.conformance_pack_input_parameters

        out["conformance_pack_input_parameters"] = (
            aws_sdk_config_service.types.conformance_pack_input_parameters.deserialize_aws_json_1_1(
                data["ConformancePackInputParameters"]
            )
        )
    if "LastUpdateRequestedTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_requested_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateRequestedTime"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "TemplateSSMDocumentDetails" in data:
        import aws_sdk_config_service.types.template_ssm_document_details

        out["template_ssm_document_details"] = (
            aws_sdk_config_service.types.template_ssm_document_details.deserialize_aws_json_1_1(
                data["TemplateSSMDocumentDetails"]
            )
        )
    return out
