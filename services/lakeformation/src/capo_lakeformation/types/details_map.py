"""Generated from Smithy shape ``com.amazonaws.lakeformation#DetailsMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_share_list


class DetailsMap(TypedDict, closed=True):
    resource_share: NotRequired[
        "capo_lakeformation.types.resource_share_list.ResourceShareList"
    ]
    """<p>A resource share ARN for a catalog resource shared through RAM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailsMap) -> dict:
    out: dict = {}
    if "resource_share" in value:
        import capo_lakeformation.types.resource_share_list

        out["ResourceShare"] = (
            capo_lakeformation.types.resource_share_list.serialize_json(
                value["resource_share"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetailsMap:
    out: DetailsMap = {}  # type: ignore[typeddict-item]
    if "ResourceShare" in data:
        import capo_lakeformation.types.resource_share_list

        out["resource_share"] = (
            capo_lakeformation.types.resource_share_list.deserialize_json(
                data["ResourceShare"]
            )
        )
    return out
