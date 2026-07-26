"""Generated from Smithy shape ``com.amazonaws.sagemaker#DisableSagemakerServicecatalogPortfolioInput``."""

from typing_extensions import TypedDict


class DisableSagemakerServicecatalogPortfolioInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableSagemakerServicecatalogPortfolioInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisableSagemakerServicecatalogPortfolioInput:
    out: DisableSagemakerServicecatalogPortfolioInput = {}  # type: ignore[typeddict-item]
    return out
