"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#DynamodbTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.dynamodb_table_policy


class DynamodbTableConfiguration(TypedDict, closed=True):
    table_policy: NotRequired[
        "capo_accessanalyzer.types.dynamodb_table_policy.DynamodbTablePolicy"
    ]
    """<p>The proposed resource policy defining who can access or manage the DynamoDB table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamodbTableConfiguration) -> dict:
    out: dict = {}
    if "table_policy" in value:
        out["tablePolicy"] = value["table_policy"]
    return out


def deserialize_json(data: dict) -> DynamodbTableConfiguration:
    out: DynamodbTableConfiguration = {}  # type: ignore[typeddict-item]
    if "tablePolicy" in data:
        out["table_policy"] = data["tablePolicy"]
    return out
