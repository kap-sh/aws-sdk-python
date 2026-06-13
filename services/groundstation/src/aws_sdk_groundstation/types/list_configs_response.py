"""Generated from Smithy shape ``com.amazonaws.groundstation#ListConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_list
    import aws_sdk_groundstation.types.pagination_token


class ListConfigsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the response of a previous <code>ListConfigs</code> call. Used to get the next page of results.</p>"""
    config_list: NotRequired["aws_sdk_groundstation.types.config_list.ConfigList"]
    """<p>List of <code>Config</code> items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "config_list" in value:
        import aws_sdk_groundstation.types.config_list

        out["configList"] = aws_sdk_groundstation.types.config_list.serialize_json(
            value["config_list"]
        )
    return out


def deserialize_json(data: dict) -> ListConfigsResponse:
    out: ListConfigsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "configList" in data:
        import aws_sdk_groundstation.types.config_list

        out["config_list"] = aws_sdk_groundstation.types.config_list.deserialize_json(
            data["configList"]
        )
    return out
