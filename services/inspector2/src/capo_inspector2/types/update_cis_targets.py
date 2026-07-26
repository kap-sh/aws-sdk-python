"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCisTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.target_account_list
    import capo_inspector2.types.target_resource_tags


class UpdateCisTargets(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_inspector2.types.target_account_list.TargetAccountList"
    ]
    """<p>The target account ids.</p>"""
    target_resource_tags: NotRequired[
        "capo_inspector2.types.target_resource_tags.TargetResourceTags"
    ]
    """<p>The target resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCisTargets) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_inspector2.types.target_account_list

        out["accountIds"] = capo_inspector2.types.target_account_list.serialize_json(
            value["account_ids"]
        )
    if "target_resource_tags" in value:
        import capo_inspector2.types.target_resource_tags

        out["targetResourceTags"] = (
            capo_inspector2.types.target_resource_tags.serialize_json(
                value["target_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCisTargets:
    out: UpdateCisTargets = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_inspector2.types.target_account_list

        out["account_ids"] = capo_inspector2.types.target_account_list.deserialize_json(
            data["accountIds"]
        )
    if "targetResourceTags" in data:
        import capo_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            capo_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    return out
