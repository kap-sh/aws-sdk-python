"""Generated from Smithy shape ``com.amazonaws.ivs#ListAdConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration_list
    import aws_sdk_ivs.types.pagination_token


class ListAdConfigurationsResponse(TypedDict):
    ad_configurations: "aws_sdk_ivs.types.ad_configuration_list.AdConfigurationList"
    """<p>List of the matching ad configurations.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more ad configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAdConfigurationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.ad_configuration_list

    out["adConfigurations"] = aws_sdk_ivs.types.ad_configuration_list.serialize_json(
        value["ad_configurations"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAdConfigurationsResponse:
    out: ListAdConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "adConfigurations" in data:
        import aws_sdk_ivs.types.ad_configuration_list

        out["ad_configurations"] = (
            aws_sdk_ivs.types.ad_configuration_list.deserialize_json(
                data["adConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListAdConfigurationsResponse.ad_configurations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
