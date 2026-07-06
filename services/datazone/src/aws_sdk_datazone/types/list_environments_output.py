"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_summaries
    import aws_sdk_datazone.types.pagination_token


class ListEnvironmentsOutput(TypedDict, closed=True):
    items: "aws_sdk_datazone.types.environment_summaries.EnvironmentSummaries"
    """<p>The results of the <code>ListEnvironments</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of environments is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environments, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.environment_summaries

    out["items"] = aws_sdk_datazone.types.environment_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsOutput:
    out: ListEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.environment_summaries

        out["items"] = aws_sdk_datazone.types.environment_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListEnvironmentsOutput.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
