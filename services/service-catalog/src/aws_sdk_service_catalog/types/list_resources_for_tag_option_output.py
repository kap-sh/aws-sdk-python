"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListResourcesForTagOptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.resource_details


class ListResourcesForTagOptionOutput(TypedDict, closed=True):
    resource_details: NotRequired[
        "aws_sdk_service_catalog.types.resource_details.ResourceDetails"
    ]
    """<p>Information about the resources.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForTagOptionOutput) -> dict:
    out: dict = {}
    if "resource_details" in value:
        import aws_sdk_service_catalog.types.resource_details

        out["ResourceDetails"] = (
            aws_sdk_service_catalog.types.resource_details.serialize_aws_json_1_1(
                value["resource_details"]
            )
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForTagOptionOutput:
    out: ListResourcesForTagOptionOutput = {}  # type: ignore[typeddict-item]
    if "ResourceDetails" in data:
        import aws_sdk_service_catalog.types.resource_details

        out["resource_details"] = (
            aws_sdk_service_catalog.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
