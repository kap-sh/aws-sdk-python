"""Generated from Smithy shape ``com.amazonaws.athena#CreateNamedQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query_id


class CreateNamedQueryOutput(TypedDict, closed=True):
    named_query_id: NotRequired["aws_sdk_athena.types.named_query_id.NamedQueryId"]
    """<p>The unique ID of the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamedQueryOutput) -> dict:
    out: dict = {}
    if "named_query_id" in value:
        out["NamedQueryId"] = value["named_query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamedQueryOutput:
    out: CreateNamedQueryOutput = {}  # type: ignore[typeddict-item]
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    return out
