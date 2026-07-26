"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.version_failure_reason_codes
    import capo_groundstation.types.version_id
    import capo_groundstation.types.version_status


class ContactVersion(TypedDict, closed=True):
    version_id: NotRequired["capo_groundstation.types.version_id.VersionId"]
    """<p>Version ID of a contact.</p>"""
    created: NotRequired["datetime.datetime"]
    """<p>Time the contact version was created in UTC.</p>"""
    activated: NotRequired["datetime.datetime"]
    """<p>Time the contact version was activated in UTC. A version is activated when it becomes the current active version of the contact.</p>"""
    superseded: NotRequired["datetime.datetime"]
    """<p>Time the contact version was superseded in UTC. A version is superseded when a newer version becomes active.</p>"""
    last_updated: NotRequired["datetime.datetime"]
    """<p>Time the contact version was last updated in UTC.</p>"""
    status: NotRequired["capo_groundstation.types.version_status.VersionStatus"]
    """<p>Status of the contact version.</p>"""
    failure_codes: NotRequired[
        "capo_groundstation.types.version_failure_reason_codes.VersionFailureReasonCodes"
    ]
    """<p>List of failure codes for the contact version.</p>"""
    failure_message: NotRequired["str"]
    """<p>Failure message for the contact version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactVersion) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    if "created" in value:
        import capo_groundstation.types._prelude.timestamp

        out["created"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["created"]
        )
    if "activated" in value:
        import capo_groundstation.types._prelude.timestamp

        out["activated"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["activated"]
        )
    if "superseded" in value:
        import capo_groundstation.types._prelude.timestamp

        out["superseded"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["superseded"]
        )
    if "last_updated" in value:
        import capo_groundstation.types._prelude.timestamp

        out["lastUpdated"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["last_updated"]
        )
    if "status" in value:
        import capo_groundstation.types.version_status

        out["status"] = capo_groundstation.types.version_status.serialize_json(
            value["status"]
        )
    if "failure_codes" in value:
        import capo_groundstation.types.version_failure_reason_codes

        out["failureCodes"] = (
            capo_groundstation.types.version_failure_reason_codes.serialize_json(
                value["failure_codes"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> ContactVersion:
    out: ContactVersion = {}  # type: ignore[typeddict-item]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "created" in data:
        import capo_groundstation.types._prelude.timestamp

        out["created"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["created"]
        )
    if "activated" in data:
        import capo_groundstation.types._prelude.timestamp

        out["activated"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["activated"]
        )
    if "superseded" in data:
        import capo_groundstation.types._prelude.timestamp

        out["superseded"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["superseded"]
            )
        )
    if "lastUpdated" in data:
        import capo_groundstation.types._prelude.timestamp

        out["last_updated"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["lastUpdated"]
            )
        )
    if "status" in data:
        import capo_groundstation.types.version_status

        out["status"] = capo_groundstation.types.version_status.deserialize_json(
            data["status"]
        )
    if "failureCodes" in data:
        import capo_groundstation.types.version_failure_reason_codes

        out["failure_codes"] = (
            capo_groundstation.types.version_failure_reason_codes.deserialize_json(
                data["failureCodes"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
