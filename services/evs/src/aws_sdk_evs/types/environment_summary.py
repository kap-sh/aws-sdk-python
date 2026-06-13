"""Generated from Smithy shape ``com.amazonaws.evs#EnvironmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_evs.types.arn
    import aws_sdk_evs.types.check_result
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.environment_name
    import aws_sdk_evs.types.environment_state
    import aws_sdk_evs.types.vcf_version


class EnvironmentSummary(TypedDict):
    environment_id: NotRequired["aws_sdk_evs.types.environment_id.EnvironmentId"]
    """<p>A unique ID for the environment.</p>"""
    environment_name: NotRequired["aws_sdk_evs.types.environment_name.EnvironmentName"]
    """<p> The name of the environment.</p>"""
    vcf_version: NotRequired["aws_sdk_evs.types.vcf_version.VcfVersion"]
    """<p>The VCF version of the environment.</p>"""
    environment_status: NotRequired["aws_sdk_evs.types.check_result.CheckResult"]
    """<p>Reports impaired functionality that stems from issues internal to the environment, such as impaired reachability.</p>"""
    environment_state: NotRequired[
        "aws_sdk_evs.types.environment_state.EnvironmentState"
    ]
    """<p>The state of an environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the environment was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the environment was modified.</p>"""
    environment_arn: NotRequired["aws_sdk_evs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that is associated with the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentSummary) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "vcf_version" in value:
        import aws_sdk_evs.types.vcf_version

        out["vcfVersion"] = aws_sdk_evs.types.vcf_version.serialize_aws_json_1_0(
            value["vcf_version"]
        )
    if "environment_status" in value:
        import aws_sdk_evs.types.check_result

        out["environmentStatus"] = (
            aws_sdk_evs.types.check_result.serialize_aws_json_1_0(
                value["environment_status"]
            )
        )
    if "environment_state" in value:
        import aws_sdk_evs.types.environment_state

        out["environmentState"] = (
            aws_sdk_evs.types.environment_state.serialize_aws_json_1_0(
                value["environment_state"]
            )
        )
    if "created_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["createdAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["modifiedAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    if "vcfVersion" in data:
        import aws_sdk_evs.types.vcf_version

        out["vcf_version"] = aws_sdk_evs.types.vcf_version.deserialize_aws_json_1_0(
            data["vcfVersion"]
        )
    if "environmentStatus" in data:
        import aws_sdk_evs.types.check_result

        out["environment_status"] = (
            aws_sdk_evs.types.check_result.deserialize_aws_json_1_0(
                data["environmentStatus"]
            )
        )
    if "environmentState" in data:
        import aws_sdk_evs.types.environment_state

        out["environment_state"] = (
            aws_sdk_evs.types.environment_state.deserialize_aws_json_1_0(
                data["environmentState"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["modifiedAt"]
            )
        )
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    return out
