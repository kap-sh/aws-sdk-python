"""Generated from Smithy shape ``com.amazonaws.dataexchange#LakeFormationDataPermissionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.lf_tag_policy_details


class LakeFormationDataPermissionDetails(TypedDict, closed=True):
    lf_tag_policy: NotRequired[
        "capo_dataexchange.types.lf_tag_policy_details.LFTagPolicyDetails"
    ]
    """<p>Details about the LF-tag policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationDataPermissionDetails) -> dict:
    out: dict = {}
    if "lf_tag_policy" in value:
        import capo_dataexchange.types.lf_tag_policy_details

        out["LFTagPolicy"] = (
            capo_dataexchange.types.lf_tag_policy_details.serialize_json(
                value["lf_tag_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> LakeFormationDataPermissionDetails:
    out: LakeFormationDataPermissionDetails = {}  # type: ignore[typeddict-item]
    if "LFTagPolicy" in data:
        import capo_dataexchange.types.lf_tag_policy_details

        out["lf_tag_policy"] = (
            capo_dataexchange.types.lf_tag_policy_details.deserialize_json(
                data["LFTagPolicy"]
            )
        )
    return out
