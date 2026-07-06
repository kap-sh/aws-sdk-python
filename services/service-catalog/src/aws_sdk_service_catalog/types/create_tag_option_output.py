"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateTagOptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_detail


class CreateTagOptionOutput(TypedDict, closed=True):
    tag_option_detail: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_detail.TagOptionDetail"
    ]
    """<p>Information about the TagOption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTagOptionOutput) -> dict:
    out: dict = {}
    if "tag_option_detail" in value:
        import aws_sdk_service_catalog.types.tag_option_detail

        out["TagOptionDetail"] = (
            aws_sdk_service_catalog.types.tag_option_detail.serialize_aws_json_1_1(
                value["tag_option_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTagOptionOutput:
    out: CreateTagOptionOutput = {}  # type: ignore[typeddict-item]
    if "TagOptionDetail" in data:
        import aws_sdk_service_catalog.types.tag_option_detail

        out["tag_option_detail"] = (
            aws_sdk_service_catalog.types.tag_option_detail.deserialize_aws_json_1_1(
                data["TagOptionDetail"]
            )
        )
    return out
