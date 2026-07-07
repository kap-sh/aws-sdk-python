"""Generated from Smithy shape ``com.amazonaws.forecast#ListExplainabilityExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.explainability_exports
    import aws_sdk_forecast.types.next_token


class ListExplainabilityExportsResponse(TypedDict, closed=True):
    explainability_exports: NotRequired[
        "aws_sdk_forecast.types.explainability_exports.ExplainabilityExports"
    ]
    """<p>An array of objects that summarize the properties of each Explainability export.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>Returns this token if the response is truncated. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExplainabilityExportsResponse) -> dict:
    out: dict = {}
    if "explainability_exports" in value:
        import aws_sdk_forecast.types.explainability_exports

        out["ExplainabilityExports"] = (
            aws_sdk_forecast.types.explainability_exports.serialize_aws_json_1_1(
                value["explainability_exports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExplainabilityExportsResponse:
    out: ListExplainabilityExportsResponse = {}  # type: ignore[typeddict-item]
    if "ExplainabilityExports" in data:
        import aws_sdk_forecast.types.explainability_exports

        out["explainability_exports"] = (
            aws_sdk_forecast.types.explainability_exports.deserialize_aws_json_1_1(
                data["ExplainabilityExports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
