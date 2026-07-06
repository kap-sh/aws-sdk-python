"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseParametersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_parameter_list
    import aws_sdk_lightsail.types.string


class GetRelationalDatabaseParametersResult(TypedDict, closed=True):
    parameters: NotRequired[
        "aws_sdk_lightsail.types.relational_database_parameter_list.RelationalDatabaseParameterList"
    ]
    """<p>An object describing the result of your get relational database parameters request.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabaseParameters</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseParametersResult) -> dict:
    out: dict = {}
    if "parameters" in value:
        import aws_sdk_lightsail.types.relational_database_parameter_list

        out["parameters"] = (
            aws_sdk_lightsail.types.relational_database_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseParametersResult:
    out: GetRelationalDatabaseParametersResult = {}  # type: ignore[typeddict-item]
    if "parameters" in data:
        import aws_sdk_lightsail.types.relational_database_parameter_list

        out["parameters"] = (
            aws_sdk_lightsail.types.relational_database_parameter_list.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
