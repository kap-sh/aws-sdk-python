"""Generated from Smithy shape ``com.amazonaws.kendra#CreateThesaurusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.thesaurus_id


class CreateThesaurusResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.thesaurus_id.ThesaurusId"]
    """<p>The identifier of the thesaurus. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateThesaurusResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateThesaurusResponse:
    out: CreateThesaurusResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
