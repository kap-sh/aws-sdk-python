"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociatePrincipalFromPortfolioOutput``."""

from typing_extensions import TypedDict


class DisassociatePrincipalFromPortfolioOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociatePrincipalFromPortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociatePrincipalFromPortfolioOutput:
    out: DisassociatePrincipalFromPortfolioOutput = {}  # type: ignore[typeddict-item]
    return out
