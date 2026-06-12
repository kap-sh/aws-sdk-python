"""Generated from Smithy shape ``com.amazonaws.macie2#ReplicationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__list_of__string


class ReplicationDetails(TypedDict):
    replicated: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the bucket is configured to replicate one or more objects to any destination.</p>"""
    replicated_externally: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the bucket is configured to replicate one or more objects to a bucket for an Amazon Web Services account that isn't part of your Amazon Macie organization. An <i>Amazon Macie organization</i> is a set of Macie accounts that are centrally managed as a group of related accounts through Organizations or by Macie invitation.</p>"""
    replication_accounts: NotRequired[
        "aws_sdk_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of Amazon Web Services account IDs, one for each Amazon Web Services account that owns a bucket that the bucket is configured to replicate one or more objects to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDetails) -> dict:
    out: dict = {}
    if "replicated" in value:
        out["replicated"] = value["replicated"]
    if "replicated_externally" in value:
        out["replicatedExternally"] = value["replicated_externally"]
    if "replication_accounts" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["replicationAccounts"] = (
            aws_sdk_macie2.types.__list_of__string.serialize_json(
                value["replication_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplicationDetails:
    out: ReplicationDetails = {}  # type: ignore[typeddict-item]
    if "replicated" in data:
        out["replicated"] = data["replicated"]
    if "replicatedExternally" in data:
        out["replicated_externally"] = data["replicatedExternally"]
    if "replicationAccounts" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["replication_accounts"] = (
            aws_sdk_macie2.types.__list_of__string.deserialize_json(
                data["replicationAccounts"]
            )
        )
    return out
