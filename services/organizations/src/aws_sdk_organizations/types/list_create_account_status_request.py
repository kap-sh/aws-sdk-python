"""Generated from Smithy shape ``com.amazonaws.organizations#ListCreateAccountStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.create_account_states
    import aws_sdk_organizations.types.max_results
    import aws_sdk_organizations.types.next_token


class ListCreateAccountStatusRequest(TypedDict, closed=True):
    states: NotRequired[
        "aws_sdk_organizations.types.create_account_states.CreateAccountStates"
    ]
    """<p>A list of one or more states that you want included in the response. If this parameter isn't present, all requests are included in the response.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["aws_sdk_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCreateAccountStatusRequest) -> dict:
    out: dict = {}
    if "states" in value:
        import aws_sdk_organizations.types.create_account_states

        out["States"] = (
            aws_sdk_organizations.types.create_account_states.serialize_aws_json_1_1(
                value["states"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCreateAccountStatusRequest:
    out: ListCreateAccountStatusRequest = {}  # type: ignore[typeddict-item]
    if "States" in data:
        import aws_sdk_organizations.types.create_account_states

        out["states"] = (
            aws_sdk_organizations.types.create_account_states.deserialize_aws_json_1_1(
                data["States"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
