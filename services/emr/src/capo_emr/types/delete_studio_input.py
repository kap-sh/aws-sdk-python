"""Generated from Smithy shape ``com.amazonaws.emr#DeleteStudioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256


class DeleteStudioInput(TypedDict, closed=True):
    studio_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStudioInput) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStudioInput:
    out: DeleteStudioInput = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    return out
