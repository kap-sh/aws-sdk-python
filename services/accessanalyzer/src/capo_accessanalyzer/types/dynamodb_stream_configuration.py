"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#DynamodbStreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.dynamodb_stream_policy


class DynamodbStreamConfiguration(TypedDict, closed=True):
    stream_policy: NotRequired[
        "capo_accessanalyzer.types.dynamodb_stream_policy.DynamodbStreamPolicy"
    ]
    """<p>The proposed resource policy defining who can access or manage the DynamoDB stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamodbStreamConfiguration) -> dict:
    out: dict = {}
    if "stream_policy" in value:
        out["streamPolicy"] = value["stream_policy"]
    return out


def deserialize_json(data: dict) -> DynamodbStreamConfiguration:
    out: DynamodbStreamConfiguration = {}  # type: ignore[typeddict-item]
    if "streamPolicy" in data:
        out["stream_policy"] = data["streamPolicy"]
    return out
