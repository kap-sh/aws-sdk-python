"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListDistributionConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.distribution_configuration_summary_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListDistributionConfigurationsResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    distribution_configuration_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.distribution_configuration_summary_list.DistributionConfigurationSummaryList"
    ]
    """<p>The list of distributions.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDistributionConfigurationsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "distribution_configuration_summary_list" in value:
        import aws_sdk_imagebuilder.types.distribution_configuration_summary_list

        out["distributionConfigurationSummaryList"] = (
            aws_sdk_imagebuilder.types.distribution_configuration_summary_list.serialize_json(
                value["distribution_configuration_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDistributionConfigurationsResponse:
    out: ListDistributionConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "distributionConfigurationSummaryList" in data:
        import aws_sdk_imagebuilder.types.distribution_configuration_summary_list

        out["distribution_configuration_summary_list"] = (
            aws_sdk_imagebuilder.types.distribution_configuration_summary_list.deserialize_json(
                data["distributionConfigurationSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
