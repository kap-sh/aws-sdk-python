"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetQueryResultsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.query_data
    import aws_sdk_internetmonitor.types.query_fields


class GetQueryResultsOutput(TypedDict):
    fields: "aws_sdk_internetmonitor.types.query_fields.QueryFields"
    """<p>The fields that the query returns data for. Fields are name-data type pairs, such as <code>availability_score</code>-<code>float</code>.</p>"""
    data: "aws_sdk_internetmonitor.types.query_data.QueryData"
    """<p>The data results that the query returns. Data is returned in arrays, aligned with the <code>Fields</code> for the query, which creates a repository of Amazon CloudWatch Internet Monitor information for your application. Then, you can filter the information in the repository by using <code>FilterParameters</code> that you define.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsOutput) -> dict:
    out: dict = {}
    import aws_sdk_internetmonitor.types.query_fields

    out["Fields"] = aws_sdk_internetmonitor.types.query_fields.serialize_json(
        value["fields"]
    )
    import aws_sdk_internetmonitor.types.query_data

    out["Data"] = aws_sdk_internetmonitor.types.query_data.serialize_json(value["data"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetQueryResultsOutput:
    out: GetQueryResultsOutput = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_internetmonitor.types.query_fields

        out["fields"] = aws_sdk_internetmonitor.types.query_fields.deserialize_json(
            data["Fields"]
        )
    else:
        raise DeserializationError("GetQueryResultsOutput.fields required")
    if "Data" in data:
        import aws_sdk_internetmonitor.types.query_data

        out["data"] = aws_sdk_internetmonitor.types.query_data.deserialize_json(
            data["Data"]
        )
    else:
        raise DeserializationError("GetQueryResultsOutput.data required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
