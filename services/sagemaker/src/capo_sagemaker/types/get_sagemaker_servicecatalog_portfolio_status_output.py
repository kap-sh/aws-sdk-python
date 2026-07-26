"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetSagemakerServicecatalogPortfolioStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.sagemaker_servicecatalog_status


class GetSagemakerServicecatalogPortfolioStatusOutput(TypedDict, closed=True):
    status: NotRequired[
        "capo_sagemaker.types.sagemaker_servicecatalog_status.SagemakerServicecatalogStatus"
    ]
    """<p>Whether Service Catalog is enabled or disabled in SageMaker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSagemakerServicecatalogPortfolioStatusOutput,
) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sagemaker.types.sagemaker_servicecatalog_status

        out["Status"] = (
            capo_sagemaker.types.sagemaker_servicecatalog_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSagemakerServicecatalogPortfolioStatusOutput:
    out: GetSagemakerServicecatalogPortfolioStatusOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_sagemaker.types.sagemaker_servicecatalog_status

        out["status"] = (
            capo_sagemaker.types.sagemaker_servicecatalog_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
