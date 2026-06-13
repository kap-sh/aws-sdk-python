"""Generated from Smithy shape ``com.amazonaws.proton#SyncBlocker``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_proton.types.blocker_status
    import aws_sdk_proton.types.blocker_type
    import aws_sdk_proton.types.sync_blocker_contexts


class SyncBlocker(TypedDict):
    id: "str"
    """<p>The ID of the sync blocker.</p>"""
    type: "aws_sdk_proton.types.blocker_type.BlockerType"
    """<p>The type of the sync blocker.</p>"""
    status: "aws_sdk_proton.types.blocker_status.BlockerStatus"
    """<p>The status of the sync blocker.</p>"""
    created_reason: "str"
    """<p>The reason why the sync blocker was created.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the sync blocker was created.</p>"""
    contexts: NotRequired[
        "aws_sdk_proton.types.sync_blocker_contexts.SyncBlockerContexts"
    ]
    """<p>The contexts for the sync blocker.</p>"""
    resolved_reason: NotRequired["str"]
    """<p>The reason the sync blocker was resolved.</p>"""
    resolved_at: NotRequired["datetime.datetime"]
    """<p>The time the sync blocker was resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlocker) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    out["createdReason"] = value["created_reason"]
    import aws_sdk_proton.types._prelude.timestamp

    out["createdAt"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "contexts" in value:
        import aws_sdk_proton.types.sync_blocker_contexts

        out["contexts"] = (
            aws_sdk_proton.types.sync_blocker_contexts.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    if "resolved_reason" in value:
        out["resolvedReason"] = value["resolved_reason"]
    if "resolved_at" in value:
        import aws_sdk_proton.types._prelude.timestamp

        out["resolvedAt"] = (
            aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
                value["resolved_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlocker:
    out: SyncBlocker = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SyncBlocker.id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SyncBlocker.type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SyncBlocker.status required")
    if "createdReason" in data:
        out["created_reason"] = data["createdReason"]
    else:
        raise DeserializationError("SyncBlocker.created_reason required")
    if "createdAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SyncBlocker.created_at required")
    if "contexts" in data:
        import aws_sdk_proton.types.sync_blocker_contexts

        out["contexts"] = (
            aws_sdk_proton.types.sync_blocker_contexts.deserialize_aws_json_1_0(
                data["contexts"]
            )
        )
    if "resolvedReason" in data:
        out["resolved_reason"] = data["resolvedReason"]
    if "resolvedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["resolved_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["resolvedAt"]
            )
        )
    return out
