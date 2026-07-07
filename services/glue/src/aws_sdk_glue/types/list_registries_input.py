"""Generated from Smithy shape ``com.amazonaws.glue#ListRegistriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.max_results_number
    import aws_sdk_glue.types.schema_registry_token_string


class ListRegistriesInput(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_glue.types.max_results_number.MaxResultsNumber"]
    """<p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegistriesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegistriesInput:
    out: ListRegistriesInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
