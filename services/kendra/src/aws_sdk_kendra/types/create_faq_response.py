"""Generated from Smithy shape ``com.amazonaws.kendra#CreateFaqResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_id


class CreateFaqResponse(TypedDict):
    id: NotRequired["aws_sdk_kendra.types.faq_id.FaqId"]
    """<p>The identifier of the FAQ.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFaqResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFaqResponse:
    out: CreateFaqResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
