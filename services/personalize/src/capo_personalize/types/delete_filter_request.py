"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DeleteFilterRequest(TypedDict, closed=True):
    filter_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the filter to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFilterRequest) -> dict:
    out: dict = {}
    out["filterArn"] = value["filter_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFilterRequest:
    out: DeleteFilterRequest = {}  # type: ignore[typeddict-item]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    else:
        raise DeserializationError("DeleteFilterRequest.filter_arn required")
    return out
