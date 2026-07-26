"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAdditionalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.feature_status
    import capo_guardduty.types.org_feature_additional_configuration


class MemberAdditionalConfiguration(TypedDict, closed=True):
    name: NotRequired[
        "capo_guardduty.types.org_feature_additional_configuration.OrgFeatureAdditionalConfiguration"
    ]
    """<p>Name of the additional configuration.</p>"""
    status: NotRequired["capo_guardduty.types.feature_status.FeatureStatus"]
    """<p>Status of the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAdditionalConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            capo_guardduty.types.org_feature_additional_configuration.serialize_json(
                value["name"]
            )
        )
    if "status" in value:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> MemberAdditionalConfiguration:
    out: MemberAdditionalConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            capo_guardduty.types.org_feature_additional_configuration.deserialize_json(
                data["name"]
            )
        )
    if "status" in data:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.deserialize_json(
            data["status"]
        )
    return out
