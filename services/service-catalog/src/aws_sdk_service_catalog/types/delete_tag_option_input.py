"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteTagOptionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_id


class DeleteTagOptionInput(TypedDict):
    id: "aws_sdk_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagOptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagOptionInput:
    out: DeleteTagOptionInput = {}  # type: ignore[typeddict-item]
    return out
