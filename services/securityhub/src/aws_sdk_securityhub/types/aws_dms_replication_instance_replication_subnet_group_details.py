"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationInstanceReplicationSubnetGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsDmsReplicationInstanceReplicationSubnetGroupDetails(TypedDict, closed=True):
    replication_subnet_group_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The identifier of the replication subnet group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsDmsReplicationInstanceReplicationSubnetGroupDetails,
) -> dict:
    out: dict = {}
    if "replication_subnet_group_identifier" in value:
        out["ReplicationSubnetGroupIdentifier"] = value[
            "replication_subnet_group_identifier"
        ]
    return out


def deserialize_json(
    data: dict,
) -> AwsDmsReplicationInstanceReplicationSubnetGroupDetails:
    out: AwsDmsReplicationInstanceReplicationSubnetGroupDetails = {}  # type: ignore[typeddict-item]
    if "ReplicationSubnetGroupIdentifier" in data:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    return out
