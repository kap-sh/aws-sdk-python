"""Generated from Smithy shape ``com.amazonaws.ssm#GetParameterHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.ps_parameter_name


class GetParameterHistoryRequest(TypedDict):
    name: "aws_sdk_ssm.types.ps_parameter_name.PSParameterName"
    """<p>The name or Amazon Resource Name (ARN) of the parameter for which you want to review history. For parameters shared with you from another account, you must use the full ARN.</p>"""
    with_decryption: NotRequired["aws_sdk_ssm.types.boolean.Boolean"]
    """<p>Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParameterHistoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "with_decryption" in value:
        out["WithDecryption"] = value["with_decryption"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParameterHistoryRequest:
    out: GetParameterHistoryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetParameterHistoryRequest.name required")
    if "WithDecryption" in data:
        out["with_decryption"] = data["WithDecryption"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
