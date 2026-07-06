"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartCommitmentPurchaseAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration


class StartCommitmentPurchaseAnalysisRequest(TypedDict, closed=True):
    commitment_purchase_analysis_configuration: "aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration.CommitmentPurchaseAnalysisConfiguration"
    """<p>The configuration for the commitment purchase analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommitmentPurchaseAnalysisRequest) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration

    out["CommitmentPurchaseAnalysisConfiguration"] = (
        aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration.serialize_aws_json_1_1(
            value["commitment_purchase_analysis_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommitmentPurchaseAnalysisRequest:
    out: StartCommitmentPurchaseAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "CommitmentPurchaseAnalysisConfiguration" in data:
        import aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration

        out["commitment_purchase_analysis_configuration"] = (
            aws_sdk_cost_explorer.types.commitment_purchase_analysis_configuration.deserialize_aws_json_1_1(
                data["CommitmentPurchaseAnalysisConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartCommitmentPurchaseAnalysisRequest.commitment_purchase_analysis_configuration required"
        )
    return out
