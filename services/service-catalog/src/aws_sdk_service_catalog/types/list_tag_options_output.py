"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListTagOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.tag_option_details


class ListTagOptionsOutput(TypedDict):
    tag_option_details: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagOptionsOutput) -> dict:
    out: dict = {}
    if "tag_option_details" in value:
        import aws_sdk_service_catalog.types.tag_option_details

        out["TagOptionDetails"] = (
            aws_sdk_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_option_details"]
            )
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagOptionsOutput:
    out: ListTagOptionsOutput = {}  # type: ignore[typeddict-item]
    if "TagOptionDetails" in data:
        import aws_sdk_service_catalog.types.tag_option_details

        out["tag_option_details"] = (
            aws_sdk_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptionDetails"]
            )
        )
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
