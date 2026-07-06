"""Generated from Smithy shape ``com.amazonaws.athena#GetNamedQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query


class GetNamedQueryOutput(TypedDict, closed=True):
    named_query: NotRequired["aws_sdk_athena.types.named_query.NamedQuery"]
    """<p>Information about the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamedQueryOutput) -> dict:
    out: dict = {}
    if "named_query" in value:
        import aws_sdk_athena.types.named_query

        out["NamedQuery"] = aws_sdk_athena.types.named_query.serialize_aws_json_1_1(
            value["named_query"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamedQueryOutput:
    out: GetNamedQueryOutput = {}  # type: ignore[typeddict-item]
    if "NamedQuery" in data:
        import aws_sdk_athena.types.named_query

        out["named_query"] = aws_sdk_athena.types.named_query.deserialize_aws_json_1_1(
            data["NamedQuery"]
        )
    return out
