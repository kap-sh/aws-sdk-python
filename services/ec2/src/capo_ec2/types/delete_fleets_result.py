"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_fleet_error_set
    import capo_ec2.types.delete_fleet_success_set


class DeleteFleetsResult(TypedDict, closed=True):
    successful_fleet_deletions: NotRequired[
        "capo_ec2.types.delete_fleet_success_set.DeleteFleetSuccessSet"
    ]
    """<p>Information about the EC2 Fleets that are successfully deleted.</p>"""
    unsuccessful_fleet_deletions: NotRequired[
        "capo_ec2.types.delete_fleet_error_set.DeleteFleetErrorSet"
    ]
    """<p>Information about the EC2 Fleets that are not successfully deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful_fleet_deletions" in value:
        import capo_ec2.types.delete_fleet_success_set

        capo_ec2.types.delete_fleet_success_set.serialize_ec2_query(
            value["successful_fleet_deletions"],
            pairs,
            f"{key_prefix}SuccessfulFleetDeletionSet",
        )
    if "unsuccessful_fleet_deletions" in value:
        import capo_ec2.types.delete_fleet_error_set

        capo_ec2.types.delete_fleet_error_set.serialize_ec2_query(
            value["unsuccessful_fleet_deletions"],
            pairs,
            f"{key_prefix}UnsuccessfulFleetDeletionSet",
        )


def deserialize_ec2_query(el: Element) -> DeleteFleetsResult:
    out: DeleteFleetsResult = {}  # type: ignore[typeddict-item]
    if el.find("successfulFleetDeletionSet") is not None:
        import capo_ec2.types.delete_fleet_success_set

        out["successful_fleet_deletions"] = (
            capo_ec2.types.delete_fleet_success_set.deserialize_ec2_query(
                el, "successfulFleetDeletionSet"
            )
        )
    if el.find("unsuccessfulFleetDeletionSet") is not None:
        import capo_ec2.types.delete_fleet_error_set

        out["unsuccessful_fleet_deletions"] = (
            capo_ec2.types.delete_fleet_error_set.deserialize_ec2_query(
                el, "unsuccessfulFleetDeletionSet"
            )
        )
    return out
