"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterOptionGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRdsDbClusterOptionGroupMembership(TypedDict, closed=True):
    db_cluster_option_group_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the DB cluster option group.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the DB cluster option group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterOptionGroupMembership) -> dict:
    out: dict = {}
    if "db_cluster_option_group_name" in value:
        out["DbClusterOptionGroupName"] = value["db_cluster_option_group_name"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterOptionGroupMembership:
    out: AwsRdsDbClusterOptionGroupMembership = {}  # type: ignore[typeddict-item]
    if "DbClusterOptionGroupName" in data:
        out["db_cluster_option_group_name"] = data["DbClusterOptionGroupName"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
