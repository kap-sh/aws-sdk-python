"""Generated from Smithy shape ``com.amazonaws.s3tables#ManagedTableInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.replication_information


class ManagedTableInformation(TypedDict):
    replication_information: NotRequired[
        "aws_sdk_s3tables.types.replication_information.ReplicationInformation"
    ]
    """<p>If this table is a replica, contains information about the source table from which it is replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedTableInformation) -> dict:
    out: dict = {}
    if "replication_information" in value:
        import aws_sdk_s3tables.types.replication_information

        out["replicationInformation"] = (
            aws_sdk_s3tables.types.replication_information.serialize_json(
                value["replication_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedTableInformation:
    out: ManagedTableInformation = {}  # type: ignore[typeddict-item]
    if "replicationInformation" in data:
        import aws_sdk_s3tables.types.replication_information

        out["replication_information"] = (
            aws_sdk_s3tables.types.replication_information.deserialize_json(
                data["replicationInformation"]
            )
        )
    return out
