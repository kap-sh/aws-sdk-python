"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetSagemakerServicecatalogPortfolioStatusInput``."""

from typing import TypedDict


class GetSagemakerServicecatalogPortfolioStatusInput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSagemakerServicecatalogPortfolioStatusInput,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSagemakerServicecatalogPortfolioStatusInput:
    out: GetSagemakerServicecatalogPortfolioStatusInput = {}  # type: ignore[typeddict-item]
    return out
