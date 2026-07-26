"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.token


class ListApplicationGrantsRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application whose grants you want to list.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationGrantsRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationGrantsRequest:
    out: ListApplicationGrantsRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "ListApplicationGrantsRequest.application_arn required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
