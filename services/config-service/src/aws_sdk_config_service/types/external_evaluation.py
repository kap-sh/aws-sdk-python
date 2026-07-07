"""Generated from Smithy shape ``com.amazonaws.configservice#ExternalEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_resource_id
    import aws_sdk_config_service.types.compliance_type
    import aws_sdk_config_service.types.ordering_timestamp
    import aws_sdk_config_service.types.string_with_char_limit256


class ExternalEvaluation(TypedDict, closed=True):
    compliance_resource_type: (
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The evaluated compliance resource type. Config accepts <code>AWS::::Account</code> resource type.</p>"""
    compliance_resource_id: (
        "aws_sdk_config_service.types.base_resource_id.BaseResourceId"
    )
    """<p>The evaluated compliance resource ID. Config accepts only Amazon Web Services account ID.</p>"""
    compliance_type: "aws_sdk_config_service.types.compliance_type.ComplianceType"
    """<p>The compliance of the Amazon Web Services resource. The valid values are <code>COMPLIANT, NON_COMPLIANT, </code> and <code>NOT_APPLICABLE</code>.</p>"""
    annotation: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Supplementary information about the reason of compliance. For example, this task was completed on a specific date.</p>"""
    ordering_timestamp: (
        "aws_sdk_config_service.types.ordering_timestamp.OrderingTimestamp"
    )
    """<p>The time when the compliance was recorded. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalEvaluation) -> dict:
    out: dict = {}
    out["ComplianceResourceType"] = value["compliance_resource_type"]
    out["ComplianceResourceId"] = value["compliance_resource_id"]
    import aws_sdk_config_service.types.compliance_type

    out["ComplianceType"] = (
        aws_sdk_config_service.types.compliance_type.serialize_aws_json_1_1(
            value["compliance_type"]
        )
    )
    if "annotation" in value:
        out["Annotation"] = value["annotation"]
    import aws_sdk_config_service.types.ordering_timestamp

    out["OrderingTimestamp"] = (
        aws_sdk_config_service.types.ordering_timestamp.serialize_aws_json_1_1(
            value["ordering_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalEvaluation:
    out: ExternalEvaluation = {}  # type: ignore[typeddict-item]
    if "ComplianceResourceType" in data:
        out["compliance_resource_type"] = data["ComplianceResourceType"]
    else:
        raise DeserializationError(
            "ExternalEvaluation.compliance_resource_type required"
        )
    if "ComplianceResourceId" in data:
        out["compliance_resource_id"] = data["ComplianceResourceId"]
    else:
        raise DeserializationError("ExternalEvaluation.compliance_resource_id required")
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    else:
        raise DeserializationError("ExternalEvaluation.compliance_type required")
    if "Annotation" in data:
        out["annotation"] = data["Annotation"]
    if "OrderingTimestamp" in data:
        import aws_sdk_config_service.types.ordering_timestamp

        out["ordering_timestamp"] = (
            aws_sdk_config_service.types.ordering_timestamp.deserialize_aws_json_1_1(
                data["OrderingTimestamp"]
            )
        )
    else:
        raise DeserializationError("ExternalEvaluation.ordering_timestamp required")
    return out
