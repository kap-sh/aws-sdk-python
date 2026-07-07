"""Generated from Smithy shape ``com.amazonaws.gamelift#ClaimFilterOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.filter_instance_statuses


class ClaimFilterOption(TypedDict, closed=True):
    instance_statuses: NotRequired[
        "aws_sdk_gamelift.types.filter_instance_statuses.FilterInstanceStatuses"
    ]
    """<p>List of instance statuses that game servers may be claimed on. If provided, the list must contain the <code>ACTIVE</code> status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClaimFilterOption) -> dict:
    out: dict = {}
    if "instance_statuses" in value:
        import aws_sdk_gamelift.types.filter_instance_statuses

        out["InstanceStatuses"] = (
            aws_sdk_gamelift.types.filter_instance_statuses.serialize_aws_json_1_1(
                value["instance_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClaimFilterOption:
    out: ClaimFilterOption = {}  # type: ignore[typeddict-item]
    if "InstanceStatuses" in data:
        import aws_sdk_gamelift.types.filter_instance_statuses

        out["instance_statuses"] = (
            aws_sdk_gamelift.types.filter_instance_statuses.deserialize_aws_json_1_1(
                data["InstanceStatuses"]
            )
        )
    return out
