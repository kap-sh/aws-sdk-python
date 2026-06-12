"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeProblemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.problem_id


class DescribeProblemRequest(TypedDict):
    problem_id: "aws_sdk_application_insights.types.problem_id.ProblemId"
    """<p>The ID of the problem.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the resource group affected by the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProblemRequest) -> dict:
    out: dict = {}
    out["ProblemId"] = value["problem_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProblemRequest:
    out: DescribeProblemRequest = {}  # type: ignore[typeddict-item]
    if "ProblemId" in data:
        out["problem_id"] = data["ProblemId"]
    else:
        raise DeserializationError("DescribeProblemRequest.problem_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
