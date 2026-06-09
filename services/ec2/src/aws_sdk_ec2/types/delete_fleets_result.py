"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_error_set
    import aws_sdk_ec2.types.delete_fleet_success_set


class DeleteFleetsResult(TypedDict):
    successful_fleet_deletions: NotRequired[
        "aws_sdk_ec2.types.delete_fleet_success_set.DeleteFleetSuccessSet"
    ]
    """<p>Information about the EC2 Fleets that are successfully deleted.</p>"""
    unsuccessful_fleet_deletions: NotRequired[
        "aws_sdk_ec2.types.delete_fleet_error_set.DeleteFleetErrorSet"
    ]
    """<p>Information about the EC2 Fleets that are not successfully deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful_fleet_deletions" in value:
        import aws_sdk_ec2.types.delete_fleet_success_set

        aws_sdk_ec2.types.delete_fleet_success_set.serialize_ec2_query(
            value["successful_fleet_deletions"],
            pairs,
            f"{prefix}.SuccessfulFleetDeletionSet",
        )
    if "unsuccessful_fleet_deletions" in value:
        import aws_sdk_ec2.types.delete_fleet_error_set

        aws_sdk_ec2.types.delete_fleet_error_set.serialize_ec2_query(
            value["unsuccessful_fleet_deletions"],
            pairs,
            f"{prefix}.UnsuccessfulFleetDeletionSet",
        )


def deserialize_ec2_query(el: Element) -> DeleteFleetsResult:
    out: DeleteFleetsResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulFleetDeletionSet") is not None:
        import aws_sdk_ec2.types.delete_fleet_success_set

        out["successful_fleet_deletions"] = (
            aws_sdk_ec2.types.delete_fleet_success_set.deserialize_ec2_query(
                el, "SuccessfulFleetDeletionSet"
            )
        )
    if el.find("UnsuccessfulFleetDeletionSet") is not None:
        import aws_sdk_ec2.types.delete_fleet_error_set

        out["unsuccessful_fleet_deletions"] = (
            aws_sdk_ec2.types.delete_fleet_error_set.deserialize_ec2_query(
                el, "UnsuccessfulFleetDeletionSet"
            )
        )
    return out
