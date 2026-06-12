"""Generated from Smithy shape ``com.amazonaws.personalize#CreateFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateFilterResponse(TypedDict):
    filter_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the new filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFilterResponse) -> dict:
    out: dict = {}
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFilterResponse:
    out: CreateFilterResponse = {}  # type: ignore[typeddict-item]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    return out
