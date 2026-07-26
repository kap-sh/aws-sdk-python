"""Generated from Smithy shape ``com.amazonaws.appconfig#Environments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.environment_list
    import capo_appconfig.types.next_token


class Environments(TypedDict, closed=True):
    items: NotRequired["capo_appconfig.types.environment_list.EnvironmentList"]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environments) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_appconfig.types.environment_list

        out["Items"] = capo_appconfig.types.environment_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> Environments:
    out: Environments = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_appconfig.types.environment_list

        out["items"] = capo_appconfig.types.environment_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
