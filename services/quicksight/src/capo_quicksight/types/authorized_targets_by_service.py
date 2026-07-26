"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizedTargetsByService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authorized_targets_list
    import capo_quicksight.types.service_type


class AuthorizedTargetsByService(TypedDict, closed=True):
    service: NotRequired["capo_quicksight.types.service_type.ServiceType"]
    """<p>The name of the Amazon Web Services service.</p>"""
    authorized_targets: NotRequired[
        "capo_quicksight.types.authorized_targets_list.AuthorizedTargetsList"
    ]
    """<p>Aist of authorized targets that are represented by IAM Identity Center application ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedTargetsByService) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_quicksight.types.service_type

        out["Service"] = capo_quicksight.types.service_type.serialize_json(
            value["service"]
        )
    if "authorized_targets" in value:
        import capo_quicksight.types.authorized_targets_list

        out["AuthorizedTargets"] = (
            capo_quicksight.types.authorized_targets_list.serialize_json(
                value["authorized_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthorizedTargetsByService:
    out: AuthorizedTargetsByService = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import capo_quicksight.types.service_type

        out["service"] = capo_quicksight.types.service_type.deserialize_json(
            data["Service"]
        )
    if "AuthorizedTargets" in data:
        import capo_quicksight.types.authorized_targets_list

        out["authorized_targets"] = (
            capo_quicksight.types.authorized_targets_list.deserialize_json(
                data["AuthorizedTargets"]
            )
        )
    return out
