"""Generated from Smithy shape ``com.amazonaws.configservice#PutRemediationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.failed_remediation_batches


class PutRemediationConfigurationsResponse(TypedDict, closed=True):
    failed_batches: NotRequired[
        "capo_config_service.types.failed_remediation_batches.FailedRemediationBatches"
    ]
    """<p>Returns a list of failed remediation batch objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRemediationConfigurationsResponse) -> dict:
    out: dict = {}
    if "failed_batches" in value:
        import capo_config_service.types.failed_remediation_batches

        out["FailedBatches"] = (
            capo_config_service.types.failed_remediation_batches.serialize_aws_json_1_1(
                value["failed_batches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRemediationConfigurationsResponse:
    out: PutRemediationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "FailedBatches" in data:
        import capo_config_service.types.failed_remediation_batches

        out["failed_batches"] = (
            capo_config_service.types.failed_remediation_batches.deserialize_aws_json_1_1(
                data["FailedBatches"]
            )
        )
    return out
