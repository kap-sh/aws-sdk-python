"""Generated from Smithy shape ``com.amazonaws.omics#ListConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.configuration_list
    import aws_sdk_omics.types.configuration_list_token


class ListConfigurationsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_omics.types.configuration_list.ConfigurationList"]
    """<p>List of configuration items.</p>"""
    next_token: NotRequired[
        "aws_sdk_omics.types.configuration_list_token.ConfigurationListToken"
    ]
    """<p>Token for retrieving next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.configuration_list

        out["items"] = aws_sdk_omics.types.configuration_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationsResponse:
    out: ListConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.configuration_list

        out["items"] = aws_sdk_omics.types.configuration_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
