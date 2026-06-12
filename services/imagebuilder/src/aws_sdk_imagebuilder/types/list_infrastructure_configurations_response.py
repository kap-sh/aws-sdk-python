"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListInfrastructureConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListInfrastructureConfigurationsResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    infrastructure_configuration_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list.InfrastructureConfigurationSummaryList"
    ]
    """<p>The list of infrastructure configurations.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInfrastructureConfigurationsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "infrastructure_configuration_summary_list" in value:
        import aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list

        out["infrastructureConfigurationSummaryList"] = (
            aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list.serialize_json(
                value["infrastructure_configuration_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInfrastructureConfigurationsResponse:
    out: ListInfrastructureConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "infrastructureConfigurationSummaryList" in data:
        import aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list

        out["infrastructure_configuration_summary_list"] = (
            aws_sdk_imagebuilder.types.infrastructure_configuration_summary_list.deserialize_json(
                data["infrastructureConfigurationSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
