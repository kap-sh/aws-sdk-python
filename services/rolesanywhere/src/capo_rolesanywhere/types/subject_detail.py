"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.credential_summaries
    import capo_rolesanywhere.types.instance_properties
    import capo_rolesanywhere.types.uuid


class SubjectDetail(TypedDict, closed=True):
    subject_arn: NotRequired["str"]
    """<p>The ARN of the resource.</p>"""
    subject_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The id of the resource</p>"""
    enabled: NotRequired["bool"]
    """<p>The enabled status of the subject.</p>"""
    x509_subject: NotRequired["str"]
    """<p>The x509 principal identifier of the authenticating certificate.</p>"""
    last_seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp of the last time this subject requested temporary session credentials.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the subject was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the subject was last updated.</p>"""
    credentials: NotRequired[
        "capo_rolesanywhere.types.credential_summaries.CredentialSummaries"
    ]
    """<p>The temporary session credentials vended at the last authenticating call with this subject.</p>"""
    instance_properties: NotRequired[
        "capo_rolesanywhere.types.instance_properties.InstanceProperties"
    ]
    """<p>The specified instance properties associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectDetail) -> dict:
    out: dict = {}
    if "subject_arn" in value:
        out["subjectArn"] = value["subject_arn"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "x509_subject" in value:
        out["x509Subject"] = value["x509_subject"]
    if "last_seen_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["lastSeenAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["last_seen_at"]
        )
    if "created_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["createdAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updatedAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "credentials" in value:
        import capo_rolesanywhere.types.credential_summaries

        out["credentials"] = (
            capo_rolesanywhere.types.credential_summaries.serialize_json(
                value["credentials"]
            )
        )
    if "instance_properties" in value:
        import capo_rolesanywhere.types.instance_properties

        out["instanceProperties"] = (
            capo_rolesanywhere.types.instance_properties.serialize_json(
                value["instance_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubjectDetail:
    out: SubjectDetail = {}  # type: ignore[typeddict-item]
    if "subjectArn" in data:
        out["subject_arn"] = data["subjectArn"]
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "x509Subject" in data:
        out["x509_subject"] = data["x509Subject"]
    if "lastSeenAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["last_seen_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["lastSeenAt"]
            )
        )
    if "createdAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["created_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updated_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "credentials" in data:
        import capo_rolesanywhere.types.credential_summaries

        out["credentials"] = (
            capo_rolesanywhere.types.credential_summaries.deserialize_json(
                data["credentials"]
            )
        )
    if "instanceProperties" in data:
        import capo_rolesanywhere.types.instance_properties

        out["instance_properties"] = (
            capo_rolesanywhere.types.instance_properties.deserialize_json(
                data["instanceProperties"]
            )
        )
    return out
