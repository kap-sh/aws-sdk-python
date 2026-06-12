"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceByConformancePack``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aggregate_conformance_pack_compliance
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.conformance_pack_name


class AggregateComplianceByConformancePack(TypedDict):
    conformance_pack_name: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    ]
    """<p>The name of the conformance pack.</p>"""
    compliance: NotRequired[
        "aws_sdk_config_service.types.aggregate_conformance_pack_compliance.AggregateConformancePackCompliance"
    ]
    """<p>The compliance status of the conformance pack.</p>"""
    account_id: NotRequired["aws_sdk_config_service.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID of the source account.</p>"""
    aws_region: NotRequired["aws_sdk_config_service.types.aws_region.AwsRegion"]
    """<p>The source Amazon Web Services Region from where the data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceByConformancePack) -> dict:
    out: dict = {}
    if "conformance_pack_name" in value:
        out["ConformancePackName"] = value["conformance_pack_name"]
    if "compliance" in value:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance

        out["Compliance"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance.serialize_aws_json_1_1(
                value["compliance"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateComplianceByConformancePack:
    out: AggregateComplianceByConformancePack = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    if "Compliance" in data:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance

        out["compliance"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
